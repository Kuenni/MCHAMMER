#ifndef __HOMUON__COMMONFUNCTIONS_H__
#define __HOMUON__COMMONFUNCTIONS_H__

/*
 * Common Functions Class
 * Author Andreas Kuensken
 * 17.06.2015
 */

#include "DataFormats/HcalRecHit/interface/HORecHit.h"
#include "DataFormats/HcalRecHit/interface/HcalRecHitCollections.h"

class CommonFunctionsHandler {  

public:
	CommonFunctionsHandler(const edm::ParameterSet& iConfig);
	const HORecHit* findHoRecHitById(DetId id);
	const HODataFrame* findHoDigiById(DetId id);
	void getEvent(const edm::Event& iEvent);

private:
	//Handles to access the collections
	edm::Handle<HORecHitCollection> hoRecoHits;
	edm::Handle<HODigiCollection> hoDigis;

	//Input tags for the collections
	edm::InputTag _horecoInput;
	edm::InputTag _hoDigiInput;

};

#endif
