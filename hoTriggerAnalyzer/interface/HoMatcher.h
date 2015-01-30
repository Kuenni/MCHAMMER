/*
 * HoMatcher.h
 *
 *  Created on: Sep 26, 2014
 *      Author: kuensken
 */

#ifndef HOMATCHER_H_
#define HOMATCHER_H_

#include "DataFormats/HcalRecHit/interface/HORecHit.h"
#include "DataFormats/HcalRecHit/interface/HcalRecHitCollections.h"
#include "Geometry/CaloGeometry/interface/CaloGeometry.h"

class HoMatcher {
public:
	HoMatcher(CaloGeometry cg):caloGeometry(cg){};
	virtual ~HoMatcher();

	/**
	 * Finds the HORecHit with the highest energy entry inside a delta R cone
	 * for a given eta and phi. Uses the calo geometry for calculating eta and phi
	 * of the rec hits
	 */
	const HORecHit* matchByEMaxDeltaR(double,double,double,HORecHitCollection);
	int getDeltaIeta(double eta, const HORecHit* recHit);
	int getDeltaIphi(double phi, const HORecHit* rechit);
	double getHoBinSize(){return 0.087;};
private:
	CaloGeometry caloGeometry;
};

#endif /* HOMATCHER_H_ */
