/*
 * HoMatcher.cc
 *
 *  Created on: Sep 26, 2014
 *      Author: kuensken
 */

#include "HoMuonTrigger/hoTriggerAnalyzer/interface/HoMatcher.h"
#include "HoMuonTrigger/hoTriggerAnalyzer/interface/FilterPlugin.h"

HoMatcher::~HoMatcher() {
}

/**
 * Gets the collections for the given event
 */
void HoMatcher::getEvent(const edm::Event& iEvent){
	iEvent.getByLabel( _horecoInput, hoRecoHits);
	iEvent.getByLabel( _hoDigiInput, hoDigis);
}

/**
 * Search in the rec hit collection for a hit with the given detId
 */
const HORecHit* HoMatcher::findHoRecHitById(DetId id){
	auto hoRecoIt = hoRecoHits->begin();
	for( ; hoRecoIt != hoRecoHits->end() ; hoRecoIt++){
		if(hoRecoIt->detid() == id){
			return &*hoRecoIt;
		}
	}
	return 0;
}

/**
 * Search in the digi collection for a hit with the given detId
 */
const HODataFrame* HoMatcher::findHoDigiById(DetId id){
	auto hoDigiIt = hoDigis->begin();
	for( ; hoDigiIt != hoDigis->end() ; hoDigiIt++){
		if(hoDigiIt->id() == id){
			return &*hoDigiIt;
		}
	}
	return 0;
}

const HORecHit* HoMatcher::matchByEMaxDeltaR(double eta,double phi){
	HORecHitCollection::const_iterator hoRecHitIt = hoRecoHits->begin();
	const HORecHit* matchedRecHit = 0;
	//Loop over all rec hits
	for( ; hoRecHitIt!=hoRecoHits->end(); hoRecHitIt++ ){
		double recHitEta = caloGeometry.getPosition(hoRecHitIt->detid()).eta();
		double recHitPhi = caloGeometry.getPosition(hoRecHitIt->detid()).phi();
		if(FilterPlugin::isInsideDeltaR(eta,recHitEta,phi,recHitPhi,deltaR_Max)){
			if(!matchedRecHit){
				matchedRecHit = &(*hoRecHitIt);
			} else {
				//Update if already found energy is lower than actual iterator energy
				if(matchedRecHit->energy() < hoRecHitIt->energy()){
					matchedRecHit = &(*hoRecHitIt);
				}
			}
		}
	}
	return matchedRecHit;
}

/**
 * Get delta in iEta between given eta and given HORecHit
 */
int HoMatcher::getDeltaIeta(double eta, const HORecHit* recHit){
	double hoEta = caloGeometry.getPosition(recHit->detid()).eta();
	double deltaEta = hoEta - eta;
	return (deltaEta >= 0) ? int(deltaEta/getHoBinSize() + getHoBinSize()/2.) : int(deltaEta/getHoBinSize() - getHoBinSize()/2.);
}

/**
 * Get delta in iPhi between given phi and given HORecHit
 */
int HoMatcher::getDeltaIphi(double phi, const HORecHit* recHit){
	double hoPhi = caloGeometry.getPosition(recHit->detid()).phi();
	double deltaPhi = FilterPlugin::wrapCheck(hoPhi,phi);
	return (deltaPhi >= 0) ? int(deltaPhi/getHoBinSize() + getHoBinSize()/2.) : int(deltaPhi/getHoBinSize() - getHoBinSize()/2.);
}

/**
 * Evaluate, whether a given eta and phi coordinate is in the chimney position in HO
 */
bool HoMatcher::isInChimney(double eta, double phi){
	if(fabs(eta) > etaLowerBound && fabs(eta) < etaUpperBound){
		if(eta > 0){
			if(phi > phiLowerBoundP && phi < phiUpperBoundP){
				return true;
			}
		}else{
			if(phi > phiLowerBoundM && phi < phiUpperBoundM){
				return true;
			}
		}
	}
	return false;
}
