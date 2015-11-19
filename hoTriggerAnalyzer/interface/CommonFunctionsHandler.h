#ifndef __HOMUON__COMMONFUNCTIONS_H__
#define __HOMUON__COMMONFUNCTIONS_H__

/*
 * Common Functions Class
 * Author Andreas Kuensken
 * 17.06.2015
 */
#include "DataFormats/Common/interface/Handle.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/Utilities/interface/InputTag.h"
#include <DataFormats/L1Trigger/interface/L1MuonParticle.h>
#include <DataFormats/L1Trigger/interface/L1MuonParticleFwd.h>

class CommonFunctionsHandler {  

public:
	CommonFunctionsHandler(const edm::ParameterSet& iConfig);
	const l1extra::L1MuonParticle* getBestL1MuonMatch(double eta, double phi);
	void getEvent(const edm::Event& iEvent);
	static std::string getGridString(int grid);
private:
	//Handles to access the collections
	edm::Handle<l1extra::L1MuonParticleCollection> l1Muons;

	//Input tags for the collections
	edm::InputTag _l1MuonInput;

	/**
	 * Maximum delta R to be used for matching
	 */
	float deltaR_Max;
};

#endif
