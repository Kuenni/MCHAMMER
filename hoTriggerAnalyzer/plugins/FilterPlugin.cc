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
