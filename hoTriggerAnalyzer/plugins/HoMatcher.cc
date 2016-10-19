/*
 * HoMatcher.cc
 *
 *  Created on: Sep 26, 2014
 *      Author: kuensken
 */

#include "HoMuonTrigger/hoTriggerAnalyzer/interface/HoMatcher.h"
#include "HoMuonTrigger/hoTriggerAnalyzer/interface/FilterPlugin.h"

//Bin size definitions
const double HoMatcher::HO_BIN = 3.1415926535897931/36.;
const double HoMatcher::HALF_HO_BIN = HO_BIN/2.;

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
 * Find the largest energy rec hit in a grid of given size
 */
const HORecHit* HoMatcher::matchByEMaxInGrid(double eta, double phi, int gridSize, bool ignoreThreshold){
	HORecHitCollection::const_iterator hoRecHitIt = hoRecoHits->begin();
		const HORecHit* matchedRecHit = 0;
		//Loop over all rec hits
		for( ; hoRecHitIt!=hoRecoHits->end(); hoRecHitIt++ ){
			//Only look for potential hits, except for explicit requests
			if(!(hoRecHitIt->energy() >= threshold || ignoreThreshold)){
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
 * Count how many HoRecHits are above Thr for a given grid
 */
int HoMatcher::countHoHitsAboveThr(double eta, double phi, int gridSize){
	HORecHitCollection::const_iterator hoRecHitIt = hoRecoHits->begin();
	int matches = 0;
	//Loop over all rec hits
	for( ; hoRecHitIt!=hoRecoHits->end(); hoRecHitIt++ ){
		//Only look for potential hits, except for explicit requests
		if(!(hoRecHitIt->energy() >= threshold)){
			continue;
		}
		double deltaIEta = getDeltaIeta(eta,&*hoRecHitIt);
		double deltaIPhi = getDeltaIphi(phi,&*hoRecHitIt);
		if (fabs(deltaIEta) <= gridSize && fabs(deltaIPhi) <= gridSize){
			matches++;
		}
	}
	return matches;
}

/**
 * Returns the eta value from a rec hits det id value
 */
double HoMatcher::getRecHitEta(const HORecHit* recHit){
	return getEtaFromDetId(recHit->detid());
}

/**
 * Returns the phi value from a rec hits det id value
 */
double HoMatcher::getRecHitPhi(const HORecHit* recHit){
	return getPhiFromDetId(recHit->detid());
}

double HoMatcher::getPhiFromDetId(DetId id){
	return caloGeometry->getPosition(id).phi();
}

double HoMatcher::getEtaFromDetId(DetId id){
	return caloGeometry->getPosition(id).eta();
}

/**
 * Get delta in iEta between given eta and given HORecHit
 */
int HoMatcher::getDeltaIeta(double eta, const HORecHit* recHit){
	double hoEta = caloGeometry->getPosition(recHit->detid()).eta();
	return HoMatcher::getDeltaIeta(eta,hoEta);
}

/**
 * Get delta in iPhi between given phi and given HORecHit
 */
int HoMatcher::getDeltaIphi(double phi, const HORecHit* recHit){
	double hoPhi = caloGeometry->getPosition(recHit->detid()).phi();
	return HoMatcher::getDeltaIphi(phi,hoPhi);
}

//Calculate delta i eta between two given eta coordinates
int HoMatcher::getDeltaIeta(double eta, double hoEta){
	double deltaEta = hoEta - eta;
	int deltaIEta = 0;
	if(deltaEta > HALF_HO_BIN){
		deltaIEta = 1 + int((deltaEta - HALF_HO_BIN)/HO_BIN);
	} else if(deltaEta < -HALF_HO_BIN){
		deltaIEta = -1 + int((deltaEta + HALF_HO_BIN)/HO_BIN);
	}
	return deltaIEta;
}

//Calculate delta i phi between two phi coordinates
int HoMatcher::getDeltaIphi(double phi, double hoPhi){
	double deltaPhi = FilterPlugin::wrapCheck(phi,hoPhi);
		int deltaIPhi = 0;
		/**
		 * Assume L1 direction as the center of a tile.
		 * This gives one half tile in each direction before
		 * the next tile starts
		 */
		if(deltaPhi > HALF_HO_BIN){
			deltaIPhi = 1 + int((deltaPhi - HALF_HO_BIN)/HO_BIN);
		} else if(deltaPhi < -HALF_HO_BIN){
			deltaIPhi = -1 + int((deltaPhi + HALF_HO_BIN)/HO_BIN);
		}
		return deltaIPhi;
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
bool HoMatcher::hasHoHitInGrid(double eta, double phi, int gridSize){
	if(gridSize < 0){
		return false;
	}

	//Find the corresponding DetId in the rec hits
	for(auto itRecHits = hoRecoHits->begin(); itRecHits != hoRecoHits->end(); itRecHits++){
		if(isRecHitInGrid(eta,phi,&*itRecHits,gridSize)){
			if(itRecHits->energy() > threshold)
				return true;
		}
	}
	return false;
}

/**
 * Look for the closest HO Rec Hit (in terms of grid distance) in a given direction, that passes
 * the Energy threshold
 */
const HORecHit* HoMatcher::getClosestRecHitInGrid(double eta, double phi, int gridSize){
	const HORecHit* match = 0;
	int bestAbsDeltaIEta = 999;
	int bestAbsDeltaIPhi = 999;

	for(auto itRecHits = hoRecoHits->begin(); itRecHits != hoRecoHits->end(); itRecHits++){
		//First filter out all rec hits that are either not in the matching grid or
		//do not pass the energy threshold
		if(isRecHitInGrid(eta,phi,&*itRecHits,gridSize)){
			if(itRecHits->energy() > threshold){
				int absDeltaIEta = abs(getDeltaIeta(eta,&*itRecHits));
				int absDeltaIPhi = abs(getDeltaIphi(phi,&*itRecHits));
				/**
				 * If one delta i X is better that before, check whether the other
				 * does not get worse. In that case update the match
				 */
				if(absDeltaIEta < bestAbsDeltaIEta || absDeltaIPhi < bestAbsDeltaIPhi){
					if(!(absDeltaIEta > bestAbsDeltaIEta || absDeltaIPhi > bestAbsDeltaIPhi)){
						bestAbsDeltaIEta = absDeltaIEta;
						bestAbsDeltaIPhi = absDeltaIPhi;
						match = &*itRecHits;
					}
				}
			}
		}
	}
	return match;
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

/**
 * Returns a pointer to the closest Ho Data frame
 */
const HODataFrame* HoMatcher::getBestHoDataFrameMatch(double eta, double phi){
	const HODataFrame* bestDataFrame = 0;
	float bestDR = 999.;
	auto dataFrameIterator = hoDigis->begin();
	for(; dataFrameIterator!=hoDigis->end(); ++dataFrameIterator) {
		float hoPhi = getPhiFromDetId(dataFrameIterator->id());
		float hoEta = getEtaFromDetId(dataFrameIterator->id());
		float dR = deltaR(eta,phi,hoEta,hoPhi);
		if (dR < deltaR_Max && dR < bestDR) {
			bestDR = dR;
			bestDataFrame = &(*dataFrameIterator);
		}
	}
	return bestDataFrame;
}
