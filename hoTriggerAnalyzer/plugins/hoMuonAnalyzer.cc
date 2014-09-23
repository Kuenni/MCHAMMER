// -*- C++ -*-
//
// Package:    caloInspector
// Class:      caloInspector
// 
/**\class caloInspector caloInspector.cc L1TriggerDPGUpgrade/caloInspector/plugins/caloInspector.cc

 Description: [one line class summary]

 Implementation:
     [Notes on implementation]
 */
//
// Original Author:  Christopher Anelli  
//         Created:  Fri, 16 May 2014 04:20:05 GMT
// $Id$
//
//

//hoMuonAnalyzer header file
#include "HoMuonTrigger/hoTriggerAnalyzer/interface/hoMuonAnalyzer.h"

// system include files
#include <memory>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDAnalyzer.h"
#include "FWCore/Framework/interface/ESHandle.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"

#include "FWCore/ServiceRegistry/interface/Service.h"
#include "CommonTools/UtilAlgos/interface/TFileService.h"

#include "L1Trigger/GlobalTriggerAnalyzer/interface/L1GtUtils.h"

#include "CondFormats/DataRecord/interface/L1GtTriggerMenuRcd.h"
#include "CondFormats/L1TObjects/interface/L1GtTriggerMenu.h"

#include "DataFormats/HepMCCandidate/interface/GenParticle.h"
#include "DataFormats/TrackReco/interface/TrackFwd.h"
#include "DataFormats/TrackReco/interface/Track.h"
#include "DataFormats/HcalRecHit/interface/HORecHit.h"
#include "DataFormats/HcalRecHit/interface/HcalRecHitCollections.h"
#include "DataFormats/Math/interface/deltaR.h"
#include "DataFormats/L1Trigger/interface/L1MuonParticleFwd.h"

#include "SimDataFormats/GeneratorProducts/interface/GenEventInfoProduct.h"

#include "DataFormats/L1GlobalTrigger/interface/L1GlobalTriggerReadoutRecord.h"

#include "Geometry/CaloGeometry/interface/CaloGeometry.h"
#include "Geometry/Records/interface/CaloGeometryRecord.h"
//#include "DataFormats/HcalDetId/interface/HcalDetId.h"

#include "DataFormats/Common/interface/Association.h"

#include "HoMuonTrigger/hoTriggerAnalyzer/interface/HistogramBuilder.h"
#include "HoMuonTrigger/hoTriggerAnalyzer/interface/CommonFunctions.h"
#include "HoMuonTrigger/hoTriggerAnalyzer/interface/FilterPlugin.h"

#include <vector>
#include <iostream>
#include "math.h"

using namespace::std;

hoMuonAnalyzer::hoMuonAnalyzer(const edm::ParameterSet& iConfig){

	//now do what ever initialization is needed

	//Get Input Tags from the Configuration

	_genInput = iConfig.getParameter<edm::InputTag>("genSrc");
	_l1MuonInput = iConfig.getParameter<edm::InputTag>("l1MuonSrc");
	_horecoInput = iConfig.getParameter<edm::InputTag>("horecoSrc");
	_l1MuonGenMatchInput = iConfig.getParameter<edm::InputTag>("l1MuonGenMatchSrc");
	_hltSumAODInput = iConfig.getParameter<edm::InputTag>("hltSumAODSrc");

	singleMu3TrigName = "L1_SingleMu3";
	doubleMu0TrigName = "L1_DoubleMu0";
	doubleMu5TrigName = "L1_DoubleMu5 ";

	defineTriggersOfInterest();
}


hoMuonAnalyzer::~hoMuonAnalyzer()
{

	// do anything here that needs to be done at desctruction time
	// (e.g. close files, deallocate resources etc.)

	//f->Close();

}


//
// member functions
//

// ------------ method called for each event  ------------
void
hoMuonAnalyzer::analyze(const edm::Event& iEvent, 
		const edm::EventSetup& iSetup)
{
	using namespace edm;

	/*
	 * Get Event Data and Event Setup
	 */
	iEvent.getByLabel(_genInput,truthParticles);

	Handle<l1extra::L1MuonParticleCollection> l1Muons;
	iEvent.getByLabel(_l1MuonInput, l1Muons);

	Handle<HORecHitCollection> hoRecoHits;
	iEvent.getByLabel(_horecoInput, hoRecoHits);

	ESHandle<CaloGeometry> caloGeo;
	iSetup.get<CaloGeometryRecord>().get(caloGeo);

	edm::Handle<edm::View<l1extra::L1MuonParticle> > l1MuonView;
	iEvent.getByLabel(_l1MuonInput,l1MuonView);

	Handle<reco::GenParticleMatch> l1MuonGenMatches;
	iEvent.getByLabel(_l1MuonGenMatchInput,l1MuonGenMatches);

	/*
	 * Set Up Level 1 Global Trigger Utility
	 */

	bool useL1EventSetup = true;
	bool useL1GtTriggerMenuLite = true;

	m_l1GtUtils.getL1GtRunCache(iEvent, iSetup, useL1EventSetup,
			useL1GtTriggerMenuLite);
	/*
	 *
	 *  Start of Analysis
	 *
	 */

	histogramBuilder.fillCountHistogram("Events");


	//Try getting the event info for weights
	Handle<GenEventInfoProduct> genEventInfo;
	iEvent.getByLabel(edm::InputTag("generator"), genEventInfo);


	/*
	 * Fill a trig rate histogramm for the muons of the gen particles
	 */
	std::string gen_key = "gen";
	int genMuonCounter = 0;
	for(reco::GenParticleCollection::const_iterator genIt = truthParticles->begin();
			genIt != truthParticles->end(); genIt++){
		//Check for muons in Full barrel only
		if( ( abs(genIt->pdgId()) == 13 ) && ( abs(genIt->eta()) <= 0.8 ) ){
			genMuonCounter++;
			histogramBuilder.fillPtHistogram(genIt->pt(),gen_key);
			for (int i = 0; i < 200; i+=2) {
				if(genIt->pt() >= i){
					histogramBuilder.fillTrigRateHistograms(i,gen_key);
					histogramBuilder.fillEtaPhiHistograms(genIt->eta(),genIt->phi(),gen_key);
				}
			}
		}
	}
	histogramBuilder.fillMultiplicityHistogram(genMuonCounter,gen_key);


	/*
	 * Level 1 Muons
	 */

	//Use this variable to store whether the event has L1Muons in acceptance
	//This can be used when inspecting the HO energy
	bool hasMuonsInAcceptance = false;

	string l1muon_key = "L1Muon";

	//Define iterators
	l1extra::L1MuonParticleCollection::const_iterator bl1Muon = l1Muons->begin();
	l1extra::L1MuonParticleCollection::const_iterator el1Muon = l1Muons->end();

	for( unsigned int i = 0 ; i < l1Muons->size(); i++  ) {
		histogramBuilder.fillCountHistogram(l1muon_key);
		const l1extra::L1MuonParticle* bl1Muon = &(l1Muons->at(i));
		//Filter on l1muon objects in Barrel region only
		if( abs(bl1Muon->eta()) <= 0.8 ){
			hasMuonsInAcceptance = true;
			histogramBuilder.fillPdgIdHistogram(bl1Muon->pdgId(),l1muon_key);
			histogramBuilder.fillVzHistogram(bl1Muon->vz(),l1muon_key);
			const reco::GenParticle* genMatch = getBestGenMatch(bl1Muon->eta(),bl1Muon->phi());
			if(genMatch){
				histogramBuilder.fillDeltaVzHistogam( (genMatch->vz() - bl1Muon->vz()) ,l1muon_key);
				histogramBuilder.fillPtCorrelationHistogram(genMatch->pt(),bl1Muon->pt(),l1muon_key);
			}
			/*
			 * Fill histogram for different pt thresholds
			 * CAREFUL!! THIS IS NOT A REAL RATE YET!!
			 */
			for (int j = 0; j < 200; j+=2) {
				if(bl1Muon->pt() >= j){
					histogramBuilder.fillTrigRateHistograms(j,l1muon_key);
				}
			}

			const reco::GenParticle* bestGenMatch = getBestGenMatch(bl1Muon->eta(),bl1Muon->phi());
			if(bestGenMatch){
				//first argument is the condition for a muon trigger object to pass
				//Second is the pt of the "real" particle
				histogramBuilder.fillEfficiency(bl1Muon->pt()>=20,bestGenMatch->pt(),std::string("L1MuonPt20"));
			}
			histogramBuilder.fillL1MuonPtHistograms(bl1Muon->pt(), l1muon_key);
			histogramBuilder.fillEtaPhiHistograms(bl1Muon->eta(), bl1Muon->phi(),
					l1muon_key);
			//For variable binning
			listL1MuonPt.push_back(bl1Muon->pt());
			edm::RefToBase<l1extra::L1MuonParticle> l1MuonCandiateRef(l1MuonView,i);
			reco::GenParticleRef ref = (*l1MuonGenMatches)[l1MuonCandiateRef];
			if(ref.isNonnull())
				histogramBuilder.fillPdgIdHistogram(ref->pdgId(),l1muon_key);
			else
				histogramBuilder.fillPdgIdHistogram(0,l1muon_key);
		}// eta <= 0.8
	}



	/*
	 * Multiplicities
	 */
	string horeco_key = "horeco";
	/**
	 * Fill the multiplicity histograms for HORecHits without cuts and
	 * for events that contain L1 muons in the acceptance region
	 */
	histogramBuilder.fillMultiplicityHistogram(hoRecoHits->size(),horeco_key);
	//Also fill multiplicity for HO Rec hits that have muons in their acceptance area
	if(hasMuonsInAcceptance){
		histogramBuilder.fillMultiplicityHistogram(hoRecoHits->size(),std::string("horecoMuInAcc"));
	}
	//get HO Rec Hits Above Threshold
	string horecoT_key ="horecoAboveThreshold";
	HORecHitCollection hoRecoHitsAboveThreshold = FilterPlugin::cleanHoRecHits(*hoRecoHits,threshold);
	histogramBuilder.fillMultiplicityHistogram(hoRecoHitsAboveThreshold.size(),horecoT_key);
	//Also fill multiplicity for HO Rec hits that have muons in their acceptance area
	if(hasMuonsInAcceptance){
		histogramBuilder.fillMultiplicityHistogram(hoRecoHitsAboveThreshold.size(),std::string("horecoAboveThresholdMuInAcc"));
	}


	/*
	 * L1 Trigger Decisions
	 */
	singleMu3Trig = processTriggerDecision(singleMu3TrigName,iEvent);
	doubleMu0Trig = processTriggerDecision(doubleMu0TrigName,iEvent);
	//	processTriggerDecision(doubleMu5TrigName,iEvent);

	auto bho_recoT = hoRecoHitsAboveThreshold.begin();
	auto eho_recoT = hoRecoHitsAboveThreshold.end();

	/*
	 * L1 Muons and matched HO information
	 */
	string l1MuonWithHoMatch_key = "L1MuonwithHoMatch";

	bl1Muon = l1Muons->begin();
	el1Muon = l1Muons->end();

	for( unsigned int i = 0 ; i < l1Muons->size(); i++ ){

		const l1extra::L1MuonParticle* bl1Muon = &(l1Muons->at(i));

		//first fill information for ho hits without energy threshold
		auto bho_reco = hoRecoHits->begin();
		auto eho_reco = hoRecoHits->end();
		for(; bho_reco != eho_reco; ++bho_reco){
			float ho_eta, ho_phi;
			ho_eta = caloGeo->getPosition(bho_reco->id()).eta();
			ho_phi = caloGeo->getPosition(bho_reco->id()).phi();
			float l1Muon_eta = bl1Muon->eta();
			float l1Muon_phi = bl1Muon->phi();
			//Filter for full barrel region only
			if( !( abs(bl1Muon->eta())>0.8 || abs(ho_eta)>0.8 ) ){
				continue;
			}
			if(FilterPlugin::isInsideRCut(l1Muon_eta, ho_eta, l1Muon_phi, ho_phi,deltaR_Max)){
				histogramBuilder.fillCountHistogram(horeco_key);
				histogramBuilder.fillEnergyHistograms(bho_reco->energy(), horeco_key);
				histogramBuilder.fillEtaPhiHistograms(ho_eta, ho_phi, horeco_key);
				histogramBuilder.fillDeltaEtaDeltaPhiHistograms(l1Muon_eta,ho_eta,l1Muon_phi, ho_phi,std::string("L1MuonwithHoMatch"));
				for (int i = 0; i < 200; i+=2) {
					if(bl1Muon->pt() >= i)
						histogramBuilder.fillTrigRateHistograms(i,std::string("L1MuonWithHoNoThr"));
				}
				break;//Leave hoReco loop if a match was found
			}
		}

		//Now fill information for hits above threshold and escape l1muon loop if a match was found
		bool mipMatch = false;
		for( ; bho_recoT != eho_recoT; ++bho_recoT){
			//Get the eta and phi information
			float l1Muon_eta, horeco_eta, l1Muon_phi, horeco_phi;
			l1Muon_eta = bl1Muon->eta();
			l1Muon_phi = bl1Muon->phi();
			horeco_eta = caloGeo->getPosition(bho_recoT->id()).eta();
			horeco_phi = caloGeo->getPosition(bho_recoT->id()).phi();

			//Filter for full barrel region only
			if( !( abs(bl1Muon->eta())>0.8 || abs(horeco_eta)>0.8 ) ){
				continue;
			}
			//If eta and phi information for both match, then go on
			if(FilterPlugin::isInsideRCut(l1Muon_eta, horeco_eta, l1Muon_phi, horeco_phi, deltaR_Max)){
				//There could be more than one match but we are only interested in one
				//Use this switch to kill the loop
				mipMatch=true;

				//Fill the HO information
				histogramBuilder.fillCountHistogram(l1MuonWithHoMatch_key);
				histogramBuilder.fillEnergyHistograms(bho_recoT->energy(),l1MuonWithHoMatch_key);
				histogramBuilder.fillEtaPhiHistograms(horeco_eta,horeco_phi,std::string("L1MuonwithHoMatch_HO"));
				histogramBuilder.fillDeltaEtaDeltaPhiHistograms(l1Muon_eta,horeco_eta,l1Muon_phi, horeco_phi,std::string("L1MuonwithHoMatchAboveThr"));

				//Make the pseudo trig rate plot
				for (int i = 0; i < 200; i+=2) {
					if(bl1Muon->pt() >= i)
						histogramBuilder.fillTrigRateHistograms(i,l1MuonWithHoMatch_key);
				}
				break;

				//Try to find a corresponding Gen Muon
				edm::RefToBase<l1extra::L1MuonParticle> l1MuonCandiateRef(l1MuonView,i);
				reco::GenParticleRef ref = (*l1MuonGenMatches)[l1MuonCandiateRef];

				if(ref.isNonnull()){
					string l1MuonAndHoRecoAndGenref_key = "L1MuonandHORecowithMipMatchAndGenMatch";
					//Make the pseudo trig rate plot
					for (int i = 0; i < 200; i+=2) {
						if(bl1Muon->pt() >= i)
							histogramBuilder.fillTrigRateHistograms(i,l1MuonAndHoRecoAndGenref_key);
					}
					histogramBuilder.fillPdgIdHistogram(ref->pdgId(),l1MuonWithHoMatch_key);
				} else{
					histogramBuilder.fillPdgIdHistogram(0,l1MuonWithHoMatch_key);
				}
			}
		}

		if(mipMatch){
			histogramBuilder.fillL1MuonPtHistograms(bl1Muon->pt(), l1MuonWithHoMatch_key);
			histogramBuilder.fillEtaPhiHistograms(bl1Muon->eta(), bl1Muon->phi(), std::string("L1MuonwithHoMatch_L1Mu"));
			std::stringstream singleMu3Key;
			singleMu3Key << singleMu3TrigName;
			singleMu3Key << "L1HOMatch";
			std::stringstream doubleMu0Key;
			doubleMu0Key << doubleMu0TrigName;
			doubleMu0Key << "L1HOMatch";
			if(singleMu3Trig)
				histogramBuilder.fillTrigHistograms(singleMu3Trig,singleMu3Key.str());
			if(doubleMu0Trig)
				histogramBuilder.fillTrigHistograms(doubleMu0Trig,doubleMu0Key.str());
			break;
		}
	}
}

/**
 * Small helper function to print the number of triggers for a certain algorithm name
 */
bool hoMuonAnalyzer::processTriggerDecision(std::string algorithmName,const edm::Event& iEvent){
	// Select on events that pass a specific L1Trigger Decision
	int iErrorCode = -1;
	bool trigDecision = m_l1GtUtils.decision(iEvent, algorithmName, iErrorCode);
	if(iErrorCode == 0){
		histogramBuilder.fillTrigHistograms(trigDecision,algorithmName);
		if(trigDecision){
			histogramBuilder.fillCountHistogram(algorithmName);
		}

	} else if (iErrorCode == 1) {
		cout<< "trigger " << algorithmName << " does not exist in the L1 menu" << endl;
	} else {
		// error - see error code
		cout << "Error Code " << iErrorCode;
	}
	return trigDecision;
}


// ------------ method called once each job just before starting event loop  ------------
void 
hoMuonAnalyzer::beginJob()
{
}

// ------------ method called once each job just after ending the event loop  ------------
void 
hoMuonAnalyzer::endJob() 
{
}

// ------------ method called when starting to processes a run  ------------

void 
hoMuonAnalyzer::beginRun(const edm::Run& iRun, 
		const edm::EventSetup& evSetup)
{

	bool useL1EventSetup = true;
	bool useL1GtTriggerMenuLite = true;
	cout << "getL1GtRunCache" << endl;
	cout << "UseL1EventSetup: " << useL1EventSetup << "UseL1GtTriggerMenuLite :"
			<< useL1GtTriggerMenuLite << endl;
	m_l1GtUtils.getL1GtRunCache(iRun, evSetup, useL1EventSetup, useL1GtTriggerMenuLite);

}


// ------------ method called when ending the processing of a run  ------------

void 
hoMuonAnalyzer::endRun(const edm::Run& iRun, const edm::EventSetup& evSetup)
{

	//Only interested in unique values
	listL1MuonPt.sort();
	listL1MuonPt.unique();  //NB it is called after sort
	cout <<"The list contains " << listL1MuonPt.size() << "unique entries:";
	std::list<float>::iterator it;
	for (it=listL1MuonPt.begin(); it!=listL1MuonPt.end(); ++it){
		cout << ' ' << *it;
	}
	cout << endl;
}


// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void
hoMuonAnalyzer::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
	//The following says we do not know what parameters are allowed so do no validation
	// Please change this to state exactly what you do use, even if it is no parameters
	edm::ParameterSetDescription desc;
	desc.setUnknown();
	descriptions.addDefault(desc);
}

/*############################
 * Helper Functions for Filter
 *############################
 */

const l1extra::L1MuonParticle* hoMuonAnalyzer::getMatchedL1Object(trigger::TriggerObject hltObject
		,edm::Handle<l1extra::L1MuonParticleCollection> l1muons){
	for(unsigned int i = 0; i < l1muons->size(); i++){
		const l1extra::L1MuonParticle* l1muon = &(l1muons->at(i));
		double hltPhi,hltEta;
		double l1Phi,l1Eta;
		hltEta = hltObject.eta();
		hltPhi = hltObject.phi();
		l1Eta = l1muon->eta();
		l1Phi = l1muon->phi();
		if(FilterPlugin::isInsideRCut(hltEta,l1Eta,hltPhi,l1Phi,deltaR_Max))
			return l1muon;
	}
	return NULL;
}

/**
 FilterPlugin::isInsideRCutue, if the trigger object has a delta R match to a l1muon object
 */
bool hoMuonAnalyzer::hasL1Match(trigger::TriggerObject hltObject,edm::Handle<l1extra::L1MuonParticleCollection> l1muons){
	for(unsigned int i = 0; i < l1muons->size(); i++){
		const l1extra::L1MuonParticle* l1muon = &(l1muons->at(i));
		double hltPhi,hltEta;
		double l1Phi,l1Eta;
		hltEta = hltObject.eta();
		hltPhi = hltObject.phi();
		l1Eta = l1muon->eta();
		l1Phi = l1muon->phi();
		if(FilterPlugin::isInsideRCut(hltEta,l1Eta,hltPhi,l1Phi,deltaR_Max))
			return true;
	}
	return false;
}

/**
 * Returns a pointer to the closest gen particle of all particles that are closer
 * than delta R < 1
 */
const reco::GenParticle* hoMuonAnalyzer::getBestGenMatch(float eta, float phi){
	const reco::GenParticle* bestGen = 0;
	float bestDR = 999.;
	reco::GenParticleCollection::const_iterator genIt = truthParticles->begin();
	reco::GenParticleCollection::const_iterator genEnd = truthParticles->end();
	for(; genIt!=genEnd; ++genIt) {
		if (abs(genIt->pdgId()) == 13 ) {
			float genPhi = genIt->phi();
			float genEta = genIt->eta();
			float dR = deltaR(eta,phi,genEta,genPhi);
			if (dR < 1. && dR < bestDR) { // CB get it from CFG
				bestDR = dR;
				bestGen = &(*genIt);
			}
		}
	}
	return bestGen;
}

void hoMuonAnalyzer::defineTriggersOfInterest(){

	/*
	 * HLT Triggers
	 */

	string hltIsoMu24_key = "hltIsoMu24";
	hltNamesOfInterest.insert(pair<string, string>(hltIsoMu24_key,"HLT_IsoMu24_v18"));
	hltFiltersOfInterest.insert(pair<string, edm::InputTag>(hltIsoMu24_key,
			edm::InputTag("hltL3crIsoL1sMu16L1f0L2f16QL3"
					"f24QL3crIsoRhoFiltered0p15",
					"","HLT")));

	string hltMu5_key = "hltMu5";
	hltNamesOfInterest.insert(pair<string, string>(hltMu5_key, "HLT_Mu5_v21"));
	hltFiltersOfInterest.insert(pair<string, edm::InputTag>(hltMu5_key,
			edm::InputTag("hltL3fL1sMu3L3Filtered5",
					"","HLT")));

	string l1SingleMuOpen_key = "hlt_l1SingleMuOpen";
	hltNamesOfInterest.insert(std::pair<std::string,std::string>(l1SingleMuOpen_key,"HLT_L1SingleMuOpen_v7"));
	hltFiltersOfInterest.insert(std::pair<std::string,edm::InputTag>(l1SingleMuOpen_key,edm::InputTag("hltL1MuOpenL1Filtered0","","HLT")));

}

//define this as a plug-in
DEFINE_FWK_MODULE(hoMuonAnalyzer);
