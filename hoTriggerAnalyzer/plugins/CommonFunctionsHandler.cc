#include "../interface/CommonFunctionsHandler.h"

#include <DataFormats/Math/interface/deltaR.h>
#include "math.h"

/**
 * Setup the parameters for getting the collections later on
 */
void CommonFunctionsHandler::CommonFunctionsHandler(const edm::ParameterSet& iConfig){
	_l1MuonInput = iConfig.getParameter<edm::InputTag>("l1MuonSrc");
	deltaR_Max = iConfig.getParameter<double>("maxDeltaR");
}

/**
 * Gets the collections for the given event
 */
void CommonFunctionsHandler::getEvent(const edm::Event& iEvent){
	iEvent.getByLabel( _l1MuonInput, l1Muons);
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
		float l1Phi = l1It->phi();
		float l1Eta = l1It->eta();
		float dR = deltaR(eta,phi,l1Eta,l1Phi);
		if (dR < deltaR_Max && dR < bestDR) { // CB get it from CFG
			bestDR = dR;
			bestL1 = &(*l1It);
		}
	}
	return bestL1;
}
