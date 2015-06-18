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
	HoMatcher(CaloGeometry cg,const edm::ParameterSet& iConfig):caloGeometry(cg){
		_horecoInput = iConfig.getParameter<edm::InputTag>("horecoSrc");
		_hoDigiInput = iConfig.getParameter<edm::InputTag>("hoDigiSrc");
		deltaR_Max = iConfig.getParameter<double>("maxDeltaR");
	};
	virtual ~HoMatcher();

	bool isInChimney(double eta, double phi);

	const HODataFrame* findHoDigiById(DetId id);
	const HORecHit* findHoRecHitById(DetId id);

	/**
	 * Finds the HORecHit with the highest energy entry inside a delta R cone
	 * for a given eta and phi. Uses the calo geometry for calculating eta and phi
	 * of the rec hits
	 */
	const HORecHit* matchByEMaxDeltaR(double eta,double phi);

	double getHoBinSize(){return 0.087;};

	int getDeltaIeta(double eta, const HORecHit* recHit);
	int getDeltaIphi(double phi, const HORecHit* rechit);

	/**
	 * Get the current event's collections
	 */
	void getEvent(const edm::Event& iEvent);

private:
	CaloGeometry caloGeometry;

	//Input tags for the collections
	edm::InputTag _horecoInput;
	edm::InputTag _hoDigiInput;

	//Handles to access the collections
	edm::Handle<HORecHitCollection> hoRecoHits;
	edm::Handle<HODigiCollection> hoDigis;

	double deltaR_Max;

	/**
	 * Boundaries for the position of the chimney of HO. Calculated from n times the iEta
	 * and iPhi coordinates given for the chimney
	 *
	 * ieta 5, iphi 18,19
	 *
	 * and
	 *
	 * ieta -5 11,12,13,14
	 *
	 */
	const double etaUpperBound = 0.435;
	const double etaLowerBound = 0.3425;
	const double phiUpperBoundP = 1.653;
	const double phiLowerBoundP = 1.479;
	const double phiUpperBoundM = 1.218;
	const double phiLowerBoundM = 0.87;
};

#endif /* HOMATCHER_H_ */
