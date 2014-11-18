/*
 * FilterPlugin.cc
 *
 *  Created on: Sep 23, 2014
 *      Author: kuensken
 */

#include "HoMuonTrigger/hoTriggerAnalyzer/interface/FilterPlugin.h"

#include <math.h>

std::vector<HORecHit> FilterPlugin::cleanHoRecHits(HORecHitCollection hoRecHits,double threshold){
	std::vector<HORecHit> returnCollection;
		HORecHitCollection::const_iterator hoRecHitIt = hoRecHits.begin();
		for ( ; hoRecHitIt != hoRecHits.end() ; hoRecHitIt++ ){
			HORecHit* newRecHit = new HORecHit(*hoRecHitIt);
			if(newRecHit->energy() >= threshold){
				std::cout << "rechit " << newRecHit->id() << " energy " << newRecHit->energy() << " Addr. " << newRecHit << std::endl;
				returnCollection.push_back(*newRecHit);
			}
		}
		std::cout << "Collection size " << returnCollection.size() << std::endl;
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

bool FilterPlugin::isInsideDeltaR(float eta1, float eta2, float phi1, float phi2, float deltaR_Max){

	float delta_eta, delta_phi;

	delta_eta = eta1 - eta2;
	delta_phi = wrapCheck(phi1,phi2); //Finds difference in phi

	if(pow(delta_eta,2)+pow(delta_phi,2) <= pow(deltaR_Max,2)) return true;
	return false;
}
