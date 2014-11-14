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

#include <DataFormats/CaloRecHit/interface/CaloRecHit.h>
#include <DataFormats/Candidate/interface/LeafCandidate.h>
#include <DataFormats/Common/interface/HandleBase.h>
#include <DataFormats/Common/interface/Ref.h>
#include <DataFormats/Common/interface/RefToBase.h>
#include <DataFormats/Common/interface/SortedCollection.h>
#include <DataFormats/Common/interface/View.h>
#include <DataFormats/DetId/interface/DetId.h>
#include <DataFormats/GeometryVector/interface/GlobalPoint.h>
#include <DataFormats/GeometryVector/interface/GlobalVector.h>
#include <DataFormats/GeometryVector/interface/Phi.h>
#include <DataFormats/GeometryVector/interface/PV3DBase.h>
#include <DataFormats/HcalDetId/interface/HcalDetId.h>
#include <DataFormats/HcalRecHit/interface/HcalRecHitCollections.h>
#include <DataFormats/HcalRecHit/interface/HORecHit.h>
#include <DataFormats/HepMCCandidate/interface/GenParticle.h>
#include <DataFormats/L1Trigger/interface/L1MuonParticle.h>
#include <DataFormats/Math/interface/deltaR.h>
#include <FWCore/Framework/interface/ESHandle.h>
#include <FWCore/Framework/interface/Event.h>
#include <FWCore/Framework/interface/EventSetup.h>
#include <FWCore/Framework/interface/EventSetupRecord.h>
#include "FWCore/Framework/interface/MakerMacros.h"
#include <FWCore/ParameterSet/interface/ParameterSet.h>
#include <FWCore/ParameterSet/interface/ParameterSetDescription.h>
#include <Geometry/CaloGeometry/interface/CaloGeometry.h>
#include <Geometry/Records/interface/CaloGeometryRecord.h>
#include <Math/GenVector/PositionVector3D.h>
#include <SimDataFormats/CaloHit/interface/PCaloHit.h>
#include <SimDataFormats/GeneratorProducts/interface/GenEventInfoProduct.h>
#include <TrackingTools/TrackAssociator/interface/TrackDetMatchInfo.h>
#include <cmath>
#include <cstdlib>
#include <iostream>
#include <iterator>
#include <sstream>
#include <utility>
#include <fstream>

#include "RecoMuon/MuonIdentification/interface/MuonHOAcceptance.h"
#include "TMultiGraph.h"
#include <iosfwd>

#include "HoMuonTrigger/hoTriggerAnalyzer/interface/FilterPlugin.h"
#include "HoMuonTrigger/hoTriggerAnalyzer/interface/HoMatcher.h"

using namespace::std;

hoMuonAnalyzer::hoMuonAnalyzer(const edm::ParameterSet& iConfig)/*:
				assocParams(iConfig.getParameter<edm::ParameterSet>("TrackAssociatorParameters"))*/
{

	//now do what ever initialization is needed

	//Get Input Tags from the Configuration

	_genInput = iConfig.getParameter<edm::InputTag>("genSrc");
	_l1MuonInput = iConfig.getParameter<edm::InputTag>("l1MuonSrc");
	_horecoInput = iConfig.getParameter<edm::InputTag>("horecoSrc");
	_l1MuonGenMatchInput = iConfig.getParameter<edm::InputTag>("l1MuonGenMatchSrc");
	_hltSumAODInput = iConfig.getParameter<edm::InputTag>("hltSumAODSrc");
	deltaR_Max = iConfig.getParameter<double>("maxDeltaR");
	threshold = iConfig.getParameter<double>("hoEnergyThreshold");

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

	if (!MuonHOAcceptance::Inited()) MuonHOAcceptance::initIds(iSetup);

	//	TFile* graphFile = TFile::Open("graphs.root","RECREATE");
	//	TMultiGraph* deadRegions = MuonHOAcceptance::graphDeadRegions();
	//	TMultiGraph* sipmRegions = MuonHOAcceptance::graphSiPMRegions();
	//	deadRegions->Write();
	//	sipmRegions->Write();
	//	graphFile->Write();
	//	graphFile->Close();
	//
	//	deadRegions = 0;
	//	sipmRegions = 0;

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

	Handle<vector<PCaloHit>> caloHits;
	iEvent.getByLabel(edm::InputTag("g4SimHits","HcalHits"),caloHits);

	if (!caloHits.isValid()) {
		std::cout << "no SimHits" << std::endl;
		return;
	}

	//Generate the energy correlation plot
	for(HORecHitCollection::const_iterator recHitIt = hoRecoHits->begin();
			recHitIt != hoRecoHits->end(); recHitIt++){
		for(std::vector<PCaloHit>::const_iterator caloHitIt = caloHits->begin();
				caloHitIt != caloHits->end(); caloHitIt++){
			HcalDetId tempId(caloHitIt->id());
			//		std::cout << tempId.ieta()  << std::endl;
			//		std::cout << tempId.iphi()  << std::endl;
			if(tempId.rawId() == recHitIt->id().rawId()){
				std::cout << HcalDetId(caloHitIt->id()) << std::endl;
				std::cout << recHitIt->id().rawId() << std::endl;
				std::cout << std::endl;
			}
			if(recHitIt->detid() == HcalDetId(caloHitIt->id())){
				histogramBuilder.fillEnergyCorrelationHistogram(caloHitIt->energy(),recHitIt->energy(),std::string("energyCorr"));
			}
		}
	}

	/**
	 * Get the track det match info running
	 */
	reco::GenParticleCollection::const_iterator genPart = truthParticles->begin();
	GlobalPoint genvertex(genPart->vx(), genPart->vy(), genPart->vz());
	GlobalVector genmomentum(genPart->px(), genPart->py(), genPart->pz());

	//	assoc.useDefaultPropagator();
	//
	//	TrackDetMatchInfo genMatch = assoc.associate(iEvent, iSetup, genmomentum,
	//			genvertex, genPart->charge(),
	//			assocParams);

	//	double genHoEta = genMatch.trkGlobPosAtHO.Eta();
	//	double genHoPhi = genMatch.trkGlobPosAtHO.Phi();
	//
	//	std::cout << "GenEta " << genHoEta << " GenPhi " << genHoPhi << std::endl;

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
	histogramBuilder.fillMultiplicityHistogram(l1Muons->size(),l1muon_key);


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

	/**
	 * Collect information of all HO Rec hits when there are
	 * l1 muons in the acceptance region
	 */
	auto hoRecoIt = hoRecoHits->begin();
	for( ; hoRecoIt != hoRecoHits->end() ; hoRecoIt++){
		if(hasMuonsInAcceptance){
			double ho_eta = caloGeo->getPosition(hoRecoIt->id()).eta();
			double ho_phi = caloGeo->getPosition(hoRecoIt->id()).phi();
			histogramBuilder.fillCountHistogram(horeco_key);
			histogramBuilder.fillEnergyHistograms(hoRecoIt->energy(),horeco_key);
			histogramBuilder.fillEtaPhiHistograms(ho_eta, ho_phi, horeco_key);
		}
	}

	ofstream myfile;
	myfile.open ("abThr.txt",std::ios::app);
	for (unsigned int i = 0; i < hoRecoHitsAboveThreshold.size(); ++i) {
		myfile << hoRecoHitsAboveThreshold[i].energy() << "\n";
	}
	myfile.close();

	/*
	 * L1 Trigger Decisions
	 */
	singleMu3Trig = processTriggerDecision(singleMu3TrigName,iEvent);
	doubleMu0Trig = processTriggerDecision(doubleMu0TrigName,iEvent);
	//	processTriggerDecision(doubleMu5TrigName,iEvent);


	/*
	 * L1 Muons and matched HO information
	 */
	string l1MuonWithHoMatch_key = "L1MuonWithHoMatch";
	bl1Muon = l1Muons->begin();
	el1Muon = l1Muons->end();

	for( unsigned int i = 0 ; i < l1Muons->size(); i++ ){

		const l1extra::L1MuonParticle* bl1Muon = &(l1Muons->at(i));

		//first fill information for ho hits without energy threshold
		//###########################################################
		float l1Muon_eta = bl1Muon->eta();
		float l1Muon_phi = bl1Muon->phi();
		//Filter for full barrel region only
		if( !( abs(bl1Muon->eta())<0.8 ) ){
			continue;
		}
		const HORecHit* matchedRecHit = HoMatcher::matchByEMaxDeltaR(l1Muon_eta,l1Muon_phi,deltaR_Max,*hoRecoHits,*caloGeo);
		if(matchedRecHit){
			double hoEta,hoPhi;
			histogramBuilder.fillTrigHistograms(caloGeo->present(matchedRecHit->id()),std::string("caloGeoPresent_L1MuonHoMatch"));
			hoEta = caloGeo->getPosition(matchedRecHit->detid()).eta();
			hoPhi = caloGeo->getPosition(matchedRecHit->detid()).phi();
			histogramBuilder.fillCountHistogram(l1MuonWithHoMatch_key);
			histogramBuilder.fillEnergyHistograms(matchedRecHit->energy(),l1MuonWithHoMatch_key);
			histogramBuilder.fillEtaPhiHistograms(hoEta, hoPhi,l1MuonWithHoMatch_key);
			histogramBuilder.fillDeltaEtaDeltaPhiHistograms(l1Muon_eta,hoEta,l1Muon_phi, hoPhi,l1MuonWithHoMatch_key);
			histogramBuilder.fillEnergyVsPosition(hoEta,hoPhi,matchedRecHit->energy(),l1MuonWithHoMatch_key);
			for (int i = 0; i < 200; i+=2) {
				if(bl1Muon->pt() >= i)
					histogramBuilder.fillTrigRateHistograms(i,std::string("L1MuonWithHoNoThr"));
			}
			const reco::GenParticle* bestGenMatch = getBestGenMatch(bl1Muon->eta(),bl1Muon->phi());
			if(bestGenMatch){
				//first argument is the condition for a muon trigger object to pass
				//Second is the pt of the "real" particle
				histogramBuilder.fillEfficiency(bl1Muon->pt()>=10,bestGenMatch->pt(),std::string("L1MuonPt10HoReco"));
				histogramBuilder.fillEfficiency(bl1Muon->pt()>=15,bestGenMatch->pt(),std::string("L1MuonPt15HoReco"));
				histogramBuilder.fillEfficiency(bl1Muon->pt()>=20,bestGenMatch->pt(),std::string("L1MuonPt20HoReco"));
				histogramBuilder.fillEfficiency(bl1Muon->pt()>=25,bestGenMatch->pt(),std::string("L1MuonPt25HoReco"));
			}
		}
		//###########################################################


		//Now fill information for hits above threshold
		//###########################################################
		matchedRecHit = 0;
		matchedRecHit = HoMatcher::matchByEMaxDeltaR(l1Muon_eta,l1Muon_phi,deltaR_Max,hoRecoHitsAboveThreshold,*caloGeo);
		//Fill some counting histograms. Can be used for cut flow in efficiency
		histogramBuilder.fillCountHistogram(std::string("AllL1Muons"));

		if (MuonHOAcceptance::inGeomAccept(l1Muon_eta,l1Muon_phi,deltaR_Max,deltaR_Max)){
			histogramBuilder.fillCountHistogram(std::string("AllL1MuonsInAcc"));

			if (MuonHOAcceptance::inNotDeadGeom(l1Muon_eta,l1Muon_phi,deltaR_Max,deltaR_Max)){
				histogramBuilder.fillCountHistogram(std::string("AllL1MuonsInAccNotDead"));

				//This one is filled for the sake of completeness. The SiPM regions are hardcoded in the class!!
				if (MuonHOAcceptance::inSiPMGeom(l1Muon_eta,l1Muon_phi,deltaR_Max,deltaR_Max)){
					histogramBuilder.fillCountHistogram(std::string("AllL1MuonsInAccNotDeadInSipm"));
				}
			}
		}

		if(matchedRecHit /*&& (matchedRecHit->energy() > 0)*/ ){
			double hoEta,hoPhi;

			std::cout << std::endl;
			std::cout << "########################" << std::endl;
			std::cout << "####"<< matchedRecHit->id() << "####" << std::endl;
			std::cout << "####"<< matchedRecHit->energy() << "####" << std::endl;
			std::cout << "########################" << std::endl;

			std::cout << "Get HO Eta" << std::endl;
			hoEta = caloGeo->getPosition(matchedRecHit->detid()).eta();
			std::cout << "Get HO Phi" << std::endl;
			hoPhi = caloGeo->getPosition(matchedRecHit->detid()).phi();
			std::cout << "Done" << std::endl;
			//Fill the HO information
			histogramBuilder.fillCountHistogram(std::string("L1MuonWithHoMatchAboveThr"));
			std::cout << "Get CaloGeo present matched Rec hit" << std::endl;
			histogramBuilder.fillTrigHistograms(caloGeo->present(matchedRecHit->id()),std::string("caloGeoPresent_L1MuonHoMatchAboveThr"));
			std::cout << "Done" << std::endl;
			//Fill the counters
			if (MuonHOAcceptance::inGeomAccept(l1Muon_eta,l1Muon_phi/*,deltaR_Max,deltaR_Max*/)){
				histogramBuilder.fillCountHistogram(std::string("AllL1MuonsAndHoInAcc"));
				if (MuonHOAcceptance::inNotDeadGeom(l1Muon_eta,l1Muon_phi/*,deltaR_Max,deltaR_Max*/)){
					histogramBuilder.fillCountHistogram(std::string("AllL1MuonsAndHoInAccNotDead"));
					std::cout << "Get CaloGeo present matched rec hit 2" << std::endl;
					histogramBuilder.fillTrigHistograms(caloGeo->present(matchedRecHit->id()),std::string("caloGeoPresent_L1MuonHoMatchAboveThrFilt"));
					std::cout << "Done" << std::endl;
					histogramBuilder.fillEnergyHistograms(matchedRecHit->energy(),std::string("L1MuonWithHoMatchAboveThrFilt"));

				//	ofstream myfile;
				//	myfile.open ("matchedRecHit.txt",std::ios::app);
				//	myfile << matchedRecHit2->energy() << "\n";
				//	myfile.close();

					histogramBuilder.fillEtaPhiHistograms(hoEta,hoPhi,std::string("L1MuonWithHoMatchAboveThrFilt_HO"));
					histogramBuilder.fillDeltaEtaDeltaPhiHistograms(l1Muon_eta,hoEta,l1Muon_phi, hoPhi,std::string("L1MuonWithHoMatchAboveThrFilt"));
					histogramBuilder.fillL1MuonPtHistograms(bl1Muon->pt(),std::string("L1MuonWithHoMatchAboveThrFilt"));
					histogramBuilder.fillEnergyVsPosition(hoEta,hoPhi,matchedRecHit->energy(),std::string("L1MuonWithHoMatchAboveThrFilt"));

					const reco::GenParticle* bestGenMatch = getBestGenMatch(bl1Muon->eta(),bl1Muon->phi());
					if(bestGenMatch){
						//first argument is the condition for a muon trigger object to pass
						//Second is the pt of the "real" particle
						histogramBuilder.fillEfficiency(bl1Muon->pt()>=10,bestGenMatch->pt(),std::string("L1MuonPt10HoRecoAboveThrFilt"));
						histogramBuilder.fillEfficiency(bl1Muon->pt()>=15,bestGenMatch->pt(),std::string("L1MuonPt15HoRecoAboveThrFilt"));
						histogramBuilder.fillEfficiency(bl1Muon->pt()>=20,bestGenMatch->pt(),std::string("L1MuonPt20HoRecoAboveThrFilt"));
						histogramBuilder.fillEfficiency(bl1Muon->pt()>=25,bestGenMatch->pt(),std::string("L1MuonPt25HoRecoAboveThrFilt"));
					}

					//This one is filled for the sake of completeness. The SiPM regions are hardcoded in the class!!
					if (MuonHOAcceptance::inSiPMGeom(l1Muon_eta,l1Muon_phi/*,deltaR_Max,deltaR_Max*/)){
						histogramBuilder.fillCountHistogram(std::string("AllL1MuonsAndHoInAccNotDeadInSipm"));
					}
				}
			}
			histogramBuilder.fillEnergyHistograms(matchedRecHit->energy(),std::string("L1MuonWithHoMatchAboveThr"));
			histogramBuilder.fillEtaPhiHistograms(hoEta,hoPhi,std::string("L1MuonWithHoMatchAboveThr_HO"));
			histogramBuilder.fillDeltaEtaDeltaPhiHistograms(l1Muon_eta,hoEta,l1Muon_phi, hoPhi,std::string("L1MuonWithHoMatchAboveThr"));
			histogramBuilder.fillL1MuonPtHistograms(bl1Muon->pt(),std::string("L1MuonWithHoMatchAboveThr"));
			histogramBuilder.fillEnergyVsPosition(hoEta,hoPhi,matchedRecHit->energy(),std::string("L1MuonWithHoMatchAboveThr"));
			//Make the pseudo trig rate plot
			for (int i = 0; i < 200; i+=2) {
				if(bl1Muon->pt() >= i)
					histogramBuilder.fillTrigRateHistograms(i,l1MuonWithHoMatch_key);
			}
			const reco::GenParticle* bestGenMatch = getBestGenMatch(bl1Muon->eta(),bl1Muon->phi());
			if(bestGenMatch){
				//first argument is the condition for a muon trigger object to pass
				//Second is the pt of the "real" particle
				histogramBuilder.fillEfficiency(bl1Muon->pt()>=10,bestGenMatch->pt(),std::string("L1MuonPt10HoRecoAboveThr"));
				histogramBuilder.fillEfficiency(bl1Muon->pt()>=15,bestGenMatch->pt(),std::string("L1MuonPt15HoRecoAboveThr"));
				histogramBuilder.fillEfficiency(bl1Muon->pt()>=20,bestGenMatch->pt(),std::string("L1MuonPt20HoRecoAboveThr"));
				histogramBuilder.fillEfficiency(bl1Muon->pt()>=25,bestGenMatch->pt(),std::string("L1MuonPt25HoRecoAboveThr"));
			}
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
			histogramBuilder.fillL1MuonPtHistograms(bl1Muon->pt(), l1MuonWithHoMatch_key);
			histogramBuilder.fillEtaPhiHistograms(bl1Muon->eta(), bl1Muon->phi(), std::string("L1MuonWithHoMatchAboveThr_L1Mu"));
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
		}//inside delta R
	}// For loop over all l1muons
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
		if(FilterPlugin::isInsideDeltaR(hltEta,l1Eta,hltPhi,l1Phi,deltaR_Max))
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
		if(FilterPlugin::isInsideDeltaR(hltEta,l1Eta,hltPhi,l1Phi,deltaR_Max))
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
