/*
 * FilterPlugin.cc
 *
 *  Created on: Sep 23, 2014
 *      Author: kuensken
 */

#include "HoMuonTrigger/hoTriggerAnalyzer/interface/FilterPlugin.h"

HORecHitCollection FilterPlugin::cleanHoRecHits(HORecHitCollection hoRecHits,double threshold){
	HORecHitCollection returnCollection;
		HORecHitCollection::const_iterator hoRecHitIt = hoRecHits.begin();
		for ( ; hoRecHitIt != hoRecHits.end() ; hoRecHitIt++ ){
			if(hoRecHitIt->energy() >= threshold){
				returnCollection.push_back(*hoRecHitIt);
			}
		}
		return returnCollection;
}

double FilterPlugin::wrapCheck(float phi1, float phi2){
  //double M_PI = (double) 3.14;
  float delta_phi = phi1 - phi2;
  if(delta_phi < -M_PI){
    return (2*M_PI + delta_phi);
  }
  if(delta_phi > M_PI){
    return (delta_phi - 2*M_PI);
  }
  return delta_phi;
};

bool FilterPlugin::isInsideRCut(float eta1, float eta2, float phi1, float phi2, float deltaR_Max){

	float delta_eta, delta_phi;

	delta_eta = eta1 - eta2;
	delta_phi = wrapCheck(phi1,phi2); //Finds difference in phi

	//The L1 Muon is compared with all HO Rec Hits above Threshold.
	if(pow(delta_eta,2)+pow(delta_phi,2) <= pow(deltaR_Max,2)) return true;
	return false;
}
