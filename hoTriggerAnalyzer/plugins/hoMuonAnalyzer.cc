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
#include "DataFormats/L1Trigger/interface/L1MuonParticle.h"
#include "DataFormats/L1Trigger/interface/L1MuonParticleFwd.h"
#include "DataFormats/TrackReco/interface/TrackFwd.h"
#include "DataFormats/TrackReco/interface/Track.h"
#include "DataFormats/HcalRecHit/interface/HORecHit.h"
#include "DataFormats/HcalRecHit/interface/HcalRecHitCollections.h"
#include "DataFormats/L1GlobalTrigger/interface/L1GlobalTriggerReadoutRecord.h"

#include "Geometry/CaloGeometry/interface/CaloGeometry.h"
#include "Geometry/Records/interface/CaloGeometryRecord.h"
//#include "DataFormats/HcalDetId/interface/HcalDetId.h"

#include "DataFormats/Common/interface/Association.h"

#include "HoMuonTrigger/hoTriggerAnalyzer/interface/HistogramBuilder.h"
#include "HoMuonTrigger/hoTriggerAnalyzer/interface/CommonFunctions.h"

#include <vector>
#include <iostream>
#include "math.h"

using namespace::std;

bool hoBelowThreshold(HORecHit horeco);
//bool isMipMatch(l1extra::L1MuonParticle l1muon, vector<HORecHit> & hoRecoHitsAboveThreshold);
bool isInsideRCut(float eta1, float eta2, float phi1, float phi2);
//float WrapCheck(float phi1, float phi2);

hoMuonAnalyzer::hoMuonAnalyzer(const edm::ParameterSet& iConfig){

	//now do what ever initialization is needed

	//Get Input Tags from the Configuration

	_genInput = iConfig.getParameter<edm::InputTag>("genSrc");
	_l1MuonInput = iConfig.getParameter<edm::InputTag>("l1MuonSrc");
	_horecoInput = iConfig.getParameter<edm::InputTag>("horecoSrc");
	_l1MuonGenMatchInput = iConfig.getParameter<edm::InputTag>("l1MuonGenMatchSrc");


	singleMu3TrigName = "L1_SingleMu3";
	doubleMu0TrigName = "L1_DoubleMu0";
	doubleMu5TrigName = "L1_DoubleMu5 ";


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

	Handle<reco::GenParticleCollection> truthParticles;
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



	/*
	 * Level 1 Muons
	 */

	string l1muon_key = "L1Muon";

	auto bl1Muon = l1Muons->cbegin();
	auto el1Muon = l1Muons->cend();

	for(  unsigned int i = 0 ; i < l1Muons->size(); i++  ) {
		histogramBuilder.fillCountHistogram(l1muon_key);
		const l1extra::L1MuonParticle* bl1Muon = &(l1Muons->at(i));

		/*
		 * Fill histogram for different pt thresholds
		 * CAREFUL!! THIS IS NOT A REAL RATE YET!!
		 */
		for (int i = 0; i < 200; i+=5) {
			if(bl1Muon->pt() >= i)
				histogramBuilder.fillTrigRateHistograms(i,l1muon_key);
		}

		histogramBuilder.fillL1MuonPtHistograms(bl1Muon->pt(), l1muon_key);
		histogramBuilder.fillEtaPhiHistograms(bl1Muon->eta(), bl1Muon->phi(),
				l1muon_key);
		//fillEtaPhiHistograms(bl1Muon->eta(), bl1Muon->phi(), l1muon_key);
		//For variable binning
		listL1MuonPt.push_back(bl1Muon->pt());
		edm::RefToBase<l1extra::L1MuonParticle> l1MuonCandiateRef(l1MuonView,i);
		reco::GenParticleRef ref = (*l1MuonGenMatches)[l1MuonCandiateRef];
		if(ref.isNonnull())
			histogramBuilder.fillPdgIdHistogram(ref->pdgId(),l1muon_key);
		else
			histogramBuilder.fillPdgIdHistogram(0,l1muon_key);
	}


	/*
	 * HO Reco Hits
	 */

	string horeco_key = "horeco";

	//cout << hoRecoHits.size() << endl;
	auto bho_reco = hoRecoHits->begin();
	auto eho_reco = hoRecoHits->end();
	for(; bho_reco != eho_reco; ++bho_reco){
		histogramBuilder.fillCountHistogram(horeco_key);
		histogramBuilder.fillEnergyHistograms(bho_reco->energy(), horeco_key);

		float ho_eta, ho_phi;
		ho_eta = caloGeo->getPosition(bho_reco->id()).eta();
		ho_phi = caloGeo->getPosition(bho_reco->id()).phi();
		histogramBuilder.fillEtaPhiHistograms(ho_eta, ho_phi, horeco_key);

		/*
		 * Fill histogram for different pt thresholds
		 * CAREFUL!! THIS IS NOT A REAL RATE YET!!
		 *
		 * Here we have to loop over the l1Muons again to find a MIP match.
		 * More than one found match could be possible. Matching is done using a
		 * Delta R matcher
		 *
		 */
		bl1Muon = l1Muons->cbegin();
		for( ; bl1Muon != el1Muon; ++bl1Muon ){
			float l1Muon_eta = bl1Muon->eta();
			float l1Muon_phi = bl1Muon->phi();
			if(isInsideRCut(l1Muon_eta, ho_eta, l1Muon_phi, ho_phi)){
				for (int i = 0; i < 200; i+=5) {
					if(bl1Muon->pt() >= i)
						histogramBuilder.fillTrigRateHistograms(i,horeco_key);
				}
				break;
			}
		}

	}


	/*
	 * L1 Trigger Decisions
	 */
	processTriggerDecision(singleMu3TrigName,iEvent);
	processTriggerDecision(doubleMu0TrigName,iEvent);
//	processTriggerDecision(doubleMu5TrigName,iEvent);



	/*
	 * HO Rec Hits Above Threshold
	 */

	string horecoT_key ="horecoAboveThreshold";

	//Filter out HO Rec Hits below Threshold.

	std::vector<HORecHit> hoRecoHitsAboveThreshold (hoRecoHits->size());

	auto it =std::remove_copy_if (hoRecoHits->begin(), hoRecoHits->end(),
			hoRecoHitsAboveThreshold.begin(),
			hoBelowThreshold);
	hoRecoHitsAboveThreshold.resize(std::distance(hoRecoHitsAboveThreshold.begin(),it));

	auto bho_recoT = hoRecoHitsAboveThreshold.begin();
	auto eho_recoT = hoRecoHitsAboveThreshold.end();

	for(; bho_recoT != eho_recoT; ++bho_recoT){
		histogramBuilder.fillCountHistogram(horecoT_key);
		histogramBuilder.fillEnergyHistograms(bho_recoT->energy(), horecoT_key);

		float hoT_eta, hoT_phi;
		hoT_eta = caloGeo->getPosition(bho_recoT->id()).eta();
		hoT_phi = caloGeo->getPosition(bho_recoT->id()).phi();
		histogramBuilder.fillEtaPhiHistograms(hoT_eta, hoT_phi, horecoT_key);

		/*
		 * Fill histogram for different pt thresholds
		 * CAREFUL!! THIS IS NOT A REAL RATE YET!!
		 *
		 * Here we have to loop over the l1Muons again to find a MIP match.
		 * More than one found match could be possible. Matching is done using a
		 * Delta R matcher
		 *
		 */
		bl1Muon = l1Muons->cbegin();
		for( ; bl1Muon != el1Muon; ++bl1Muon ){
			float l1Muon_eta = bl1Muon->eta();
			float l1Muon_phi = bl1Muon->phi();
			if(isInsideRCut(l1Muon_eta, hoT_eta, l1Muon_phi, hoT_phi)){
				for (int i = 0; i < 200; i+=5) {
					if(bl1Muon->pt() >= i)
						histogramBuilder.fillTrigRateHistograms(i,horecoT_key);
				}
				break;
			}
		}

	}

	/*
	 * L1 Muons Matched to a MIP
	 */

	string l1MuonMipMatch_key = "L1MuonwithMipMatch";

	bl1Muon = l1Muons->cbegin();
	el1Muon = l1Muons->cend();

	for( unsigned int i = 0 ; i < l1Muons->size(); i++ ){

		const l1extra::L1MuonParticle* bl1Muon = &(l1Muons->at(i));

		//bool isMipMatch=checkMipMatch();
		bho_recoT = hoRecoHitsAboveThreshold.begin();
		eho_recoT = hoRecoHitsAboveThreshold.end();

		bool mipMatch = false;
		for( ; bho_recoT != eho_recoT; ++bho_recoT){
			float l1Muon_eta, horeco_eta, l1Muon_phi, horeco_phi;
			l1Muon_eta = bl1Muon->eta();
			l1Muon_phi = bl1Muon->phi();
			horeco_eta = caloGeo->getPosition(bho_recoT->id()).eta();
			horeco_phi = caloGeo->getPosition(bho_recoT->id()).phi();

			string l1MuonhoReco_key = "L1MuonandHOReco";
			histogramBuilder.fillDeltaEtaDeltaPhiHistograms(l1Muon_eta, horeco_eta,
					l1Muon_phi, horeco_phi,
					l1MuonhoReco_key);
			if(isInsideRCut(l1Muon_eta, horeco_eta, l1Muon_phi, horeco_phi)){
				mipMatch=true; //Only need a single match
				//NB It is possible for there to be more than one matched Mip.
				string hoRecoMipMatch_key = "HORecowithMipMatch";
				histogramBuilder.fillCountHistogram(hoRecoMipMatch_key);
				histogramBuilder.fillEtaPhiHistograms(caloGeo->getPosition(bho_recoT->id()).eta(),
						caloGeo->getPosition(bho_recoT->id()).phi(),
						hoRecoMipMatch_key);
				histogramBuilder.fillEnergyHistograms(bho_recoT->energy(),hoRecoMipMatch_key);

				string l1MuonhoRecomipMatch_key = "L1MuonandHORecowithMipMatch";
				histogramBuilder.fillDeltaEtaDeltaPhiHistograms(l1Muon_eta,horeco_eta,
						l1Muon_phi, horeco_phi,
						l1MuonhoRecomipMatch_key);

				edm::RefToBase<l1extra::L1MuonParticle> l1MuonCandiateRef(l1MuonView,i);
				reco::GenParticleRef ref = (*l1MuonGenMatches)[l1MuonCandiateRef];

				if(ref.isNonnull())
					histogramBuilder.fillPdgIdHistogram(ref->pdgId(),hoRecoMipMatch_key);
				else
					histogramBuilder.fillPdgIdHistogram(0,hoRecoMipMatch_key);

				//Make the pseudo trig rate plot
				for (int i = 0; i < 200; i+=5) {
					if(bl1Muon->pt() >= i)
						histogramBuilder.fillTrigRateHistograms(i,hoRecoMipMatch_key);
				}
			}
		}

		if(mipMatch){
			histogramBuilder.fillCountHistogram(l1MuonMipMatch_key);
			histogramBuilder.fillL1MuonPtHistograms(bl1Muon->pt(), l1MuonMipMatch_key);
			histogramBuilder.fillEtaPhiHistograms(bl1Muon->eta(), bl1Muon->phi(), l1MuonMipMatch_key);
			break;
		}
	}
}

/**
 * Small helper function to print the number of triggers for a certain algorithm name
 */
void hoMuonAnalyzer::processTriggerDecision(std::string algorithmName,const edm::Event& iEvent){
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



/*
 * Helper Functions for Filter
 */

bool hoBelowThreshold(HORecHit horeco){
	if(horeco.energy() < threshold) return true;
	return false;
}


bool isInsideRCut(float eta1, float eta2, float phi1, float phi2){

	float delta_eta, delta_phi;
	CommonFunctions commonFunctions;

	delta_eta = eta1 - eta2;
	delta_phi = commonFunctions.WrapCheck(phi1,phi2); //Finds difference in phi

	//The L1 Muon is compared with all HO Rec Hits above Threshold.
	if(pow(delta_eta,2)+pow(delta_phi,2) <= pow(deltaR_Max,2)) return true;
	return false;
}

//define this as a plug-in
DEFINE_FWK_MODULE(hoMuonAnalyzer);
