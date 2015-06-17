#include "../interface/CommonFunctionsHandler.h"

#include "math.h"

/**
 * Setup the parameters for getting the collections later on
 */
void CommonFunctionsHandler::CommonFunctionsHandler(const edm::ParameterSet& iConfig){
	_horecoInput = iConfig.getParameter<edm::InputTag>("horecoSrc");
	_hoDigiInput = iConfig.getParameter<edm::InputTag>("hoDigiSrc");
}

/**
 * Gets the collections for the given event
 */
void CommonFunctionsHandler::getEvent(const edm::Event& iEvent){
	iEvent.getByLabel( _horecoInput, hoRecoHits);
	iEvent.getByLabel( _hoDigiInput, hoDigis);
}

/**
 * Search in the rec hit collection for a hit with the given detId
 */
const HORecHit* CommonFunctionsHandler::findHoRecHitById(DetId id){
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
const HODataFrame* CommonFunctionsHandler::findHoDigiById(DetId id){
	auto hoDigiIt = hoDigis->begin();
	for( ; hoDigiIt != hoDigis->end() ; hoDigiIt++){
		if(hoDigiIt->id() == id){
			return &*hoDigiIt;
		}
	}
	return 0;
}
