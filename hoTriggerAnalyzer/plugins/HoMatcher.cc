/*
 * HoMatcher.cc
 *
 *  Created on: Sep 26, 2014
 *      Author: kuensken
 */

#include "HoMuonTrigger/hoTriggerAnalyzer/interface/HoMatcher.h"
#include "HoMuonTrigger/hoTriggerAnalyzer/interface/FilterPlugin.h"

HoMatcher::HoMatcher() {
	// TODO Auto-generated constructor stub

}

HoMatcher::~HoMatcher() {
	// TODO Auto-generated destructor stub
}

const HORecHit* HoMatcher::matchByEMaxDeltaR(double eta,double phi,double maxDeltaR,std::vector<HORecHit> hoRecHits,CaloGeometry caloGeo){
	HORecHitCollection::const_iterator hoRecHitIt = hoRecHits.begin();
	const HORecHit* matchedRecHit = 0;
	//Loop over all rec hits
	for( ; hoRecHitIt!=hoRecHits.end(); hoRecHitIt++ ){
		double recHitEta = caloGeo.getPosition(hoRecHitIt->detid()).eta();
		double recHitPhi = caloGeo.getPosition(hoRecHitIt->detid()).phi();
		if(FilterPlugin::isInsideDeltaR(eta,recHitEta,phi,recHitPhi,maxDeltaR)){
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

const HORecHit* HoMatcher::matchByEMaxDeltaR(double eta,double phi,double maxDeltaR,HORecHitCollection hoRecHits,CaloGeometry caloGeo){
	HORecHitCollection::const_iterator hoRecHitIt = hoRecHits.begin();
	const HORecHit* matchedRecHit = 0;
	//Loop over all rec hits
	for( ; hoRecHitIt!=hoRecHits.end(); hoRecHitIt++ ){
		double recHitEta = caloGeo.getPosition(hoRecHitIt->detid()).eta();
		double recHitPhi = caloGeo.getPosition(hoRecHitIt->detid()).phi();
		if(FilterPlugin::isInsideDeltaR(eta,recHitEta,phi,recHitPhi,maxDeltaR)){
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
