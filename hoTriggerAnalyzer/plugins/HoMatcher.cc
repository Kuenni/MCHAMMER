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
void HoMatcher::getEvent(const edm::Event& iEvent,const edm::EventSetup& iSetup){
	iEvent.getByLabel( _horecoInput, hoRecoHits);
	iEvent.getByLabel( _hoDigiInput, hoDigis);
	iSetup.get<CaloGeometryRecord>().get(caloGeometry);
	iSetup.get<DetIdAssociatorRecord>().get("HODetIdAssociator", hoDetIdAssociator);
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
 * Count, how often a Digi with the same DetId is found per Event.
 * Should not be more often than once!
 */
int HoMatcher::countHoDigisByDetId(DetId id){
	int hoDigiCounter = 0;
	auto hoDigiIt = hoDigis->begin();
	for( ; hoDigiIt != hoDigis->end() ; hoDigiIt++){
		if(hoDigiIt->id() == id){
			hoDigiCounter++;
		}
	}
	return hoDigiCounter;
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

/**
 * Try to find the HO Rec hit with the largest energy entry in a given
 * Delta R cone
 */
const HORecHit* HoMatcher::matchByEMaxDeltaR(double eta,double phi){
	HORecHitCollection::const_iterator hoRecHitIt = hoRecoHits->begin();
	const HORecHit* matchedRecHit = 0;
	//Loop over all rec hits
	for( ; hoRecHitIt!=hoRecoHits->end(); hoRecHitIt++ ){
		double recHitEta = caloGeometry->getPosition(hoRecHitIt->detid()).eta();
		double recHitPhi = caloGeometry->getPosition(hoRecHitIt->detid()).phi();
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
 * Find the highest energy rec hit in a grid of given size
 */
const HORecHit* HoMatcher::findEMaxHitInGrid(double eta, double phi, int gridSize){
	HORecHitCollection::const_iterator hoRecHitIt = hoRecoHits->begin();
		const HORecHit* matchedRecHit = 0;
		//Loop over all rec hits
		for( ; hoRecHitIt!=hoRecoHits->end(); hoRecHitIt++ ){
			//Only look for potential hits
			if(hoRecHitIt->energy() < threshold){
				continue;
			}
			double deltaIEta = getDeltaIeta(eta,&*hoRecHitIt);
			double deltaIPhi = getDeltaIphi(phi,&*hoRecHitIt);
			if (abs(deltaIEta) <= gridSize && abs(deltaIPhi) <= gridSize){
				if(!matchedRecHit){
					matchedRecHit = &*hoRecHitIt;
				} else {
					if(matchedRecHit->energy() < hoRecHitIt->energy()){
						matchedRecHit = &*hoRecHitIt;
					}
				}
			}
		}
		return matchedRecHit;
}

/**
 * Returns the eta value from a rec hits det id value
 */
double HoMatcher::getRecHitEta(const HORecHit* recHit){
	return caloGeometry->getPosition(recHit->detid()).eta();
}

/**
 * Returns the phi value from a rec hits det id value
 */
double HoMatcher::getRecHitPhi(const HORecHit* recHit){
	return caloGeometry->getPosition(recHit->detid()).phi();
}

/**
 * Get delta in iEta between given eta and given HORecHit
 */
int HoMatcher::getDeltaIeta(double eta, const HORecHit* recHit){
	double hoEta = caloGeometry->getPosition(recHit->detid()).eta();
	double deltaEta = hoEta - eta;
	return (deltaEta >= 0) ? int(deltaEta/getHoBinSize() + getHoBinSize()/2.) : int(deltaEta/getHoBinSize() - getHoBinSize()/2.);
}

/**
 * Get delta in iPhi between given phi and given HORecHit
 */
int HoMatcher::getDeltaIphi(double phi, const HORecHit* recHit){
	double hoPhi = caloGeometry->getPosition(recHit->detid()).phi();
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

/**
 * Find out whether a given direction, represented by a point (Thank You, CMSSW)
 * points to an HORecHit with E > 0.2,
 * The Gridsize determines the search area, e.g.:
 *
 * 		Size: 0		Size: 1		Size: 2
 *
 * 								# # # # #
 * 					# # #		# # # # #
 * 			O		# O #		# # O # #
 * 					# # #		# # # # #
 * 								# # # # #
 */
bool HoMatcher::hasHoHitInGrid(GlobalPoint direction, int gridSize){
	if(gridSize < 0){
		return false;
	}

	//Find the corresponding DetId in the rec hits
	for(auto itRecHits = hoRecoHits->begin(); itRecHits != hoRecoHits->end(); itRecHits++){
		if(isRecHitInGrid(double(direction.eta()),double(direction.phi()),&*itRecHits,gridSize)){
			if(itRecHits->energy() > threshold)
				return true;
		}
	}
	return false;
}

/**
 * Check whether a given combination of eta, phi and HORecHit (its coordinates)
 * are within a given tile grid
 */
bool HoMatcher::isRecHitInGrid(double eta, double phi, const HORecHit* recHit, int gridSize){
	double deltaIEta = getDeltaIeta(eta,recHit);
	double deltaIPhi = getDeltaIphi(phi,recHit);
	if (abs(deltaIEta) <= gridSize && abs(deltaIPhi) <= gridSize){
		return true;
	}
	return false;
}

