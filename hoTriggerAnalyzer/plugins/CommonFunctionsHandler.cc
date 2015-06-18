#include "../interface/CommonFunctionsHandler.h"

#include <DataFormats/Math/interface/deltaR.h>
#include "math.h"

/**
 * Setup the parameters for getting the collections later on
 */
void CommonFunctionsHandler::CommonFunctionsHandler(const edm::ParameterSet& iConfig){
	_horecoInput = iConfig.getParameter<edm::InputTag>("horecoSrc");
	_hoDigiInput = iConfig.getParameter<edm::InputTag>("hoDigiSrc");
	_l1MuonInput = iConfig.getParameter<edm::InputTag>("l1MuonSrc");
	deltaR_Max = iConfig.getParameter<double>("maxDeltaR");
}

/**
 * Gets the collections for the given event
 */
void CommonFunctionsHandler::getEvent(const edm::Event& iEvent){
	iEvent.getByLabel( _horecoInput, hoRecoHits);
	iEvent.getByLabel( _hoDigiInput, hoDigis);
	iEvent.getByLabel( _l1MuonInput, l1Muons);
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

/**
 * Returns a pointer to the closest l1 muon particle of all particles that are closer
 * than delta R given by delta R max
 */
const l1extra::L1MuonParticle* CommonFunctionsHandler::getBestL1MuonMatch(double eta, double phi){
	const l1extra::L1MuonParticle* bestL1 = 0;
	float bestDR = 999.;
	l1extra::L1MuonParticleCollection::const_iterator l1It = l1Muons->begin();
	l1extra::L1MuonParticleCollection::const_iterator l1End = l1Muons->end();
	for(; l1It!=l1End; ++l1It) {
		float genPhi = l1It->phi();
		float genEta = l1It->eta();
		float dR = deltaR(eta,phi,genEta,genPhi);
		if (dR < deltaR_Max && dR < bestDR) { // CB get it from CFG
			bestDR = dR;
			bestL1 = &(*l1It);
		}
	}
	return bestL1;
}
