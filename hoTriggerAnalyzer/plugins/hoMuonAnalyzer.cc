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
#include "../interface/hoMuonAnalyzer.h"

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
#include "DataFormats/GeometryVector/interface/GlobalTag.h"
#include <DataFormats/GeometryVector/interface/Phi.h>
#include <DataFormats/GeometryVector/interface/PV3DBase.h>
#include <DataFormats/HcalDetId/interface/HcalDetId.h>
#include <DataFormats/HcalDetId/interface/HcalSubdetector.h>
#include <DataFormats/HcalRecHit/interface/HcalRecHitCollections.h>
#include <DataFormats/HcalRecHit/interface/HORecHit.h>
#include <DataFormats/HepMCCandidate/interface/GenParticle.h>
#include <DataFormats/L1Trigger/interface/L1MuonParticle.h>
#include <DataFormats/Math/interface/deltaR.h>
#include <DataFormats/Provenance/interface/EventID.h>
#include <DataFormats/TrajectorySeed/interface/PropagationDirection.h>
#include <FWCore/Common/interface/EventBase.h>
#include <FWCore/Framework/interface/ESHandle.h>
#include <FWCore/Framework/interface/Event.h>
#include <FWCore/Framework/interface/EventSetup.h>
#include <FWCore/Framework/interface/EventSetupRecord.h>
#include <FWCore/Framework/interface/MakerMacros.h>
#include <FWCore/Framework/src/Factory.h>
#include <FWCore/Framework/src/WorkerMaker.h>
#include <FWCore/ParameterSet/interface/ParameterSet.h>
#include <FWCore/ParameterSet/interface/ParameterSetDescription.h>
#include <FWCore/ParameterSet/interface/ParameterSetDescriptionFiller.h>
#include <FWCore/ParameterSet/interface/ParameterSetDescriptionFillerPluginFactory.h>
#include <FWCore/PluginManager/interface/PluginFactory.h>
#include <Geometry/CaloGeometry/interface/CaloGeometry.h>
#include <Geometry/Records/interface/CaloGeometryRecord.h>
#include <MagneticField/Records/interface/IdealMagneticFieldRecord.h>
#include <Math/GenVector/DisplacementVector3D.h>
#include <RecoMuon/MuonIdentification/interface/MuonHOAcceptance.h>
#include <SimDataFormats/CaloHit/interface/PCaloHit.h>
#include <SimDataFormats/GeneratorProducts/interface/GenEventInfoProduct.h>
#include <TrackingTools/TrackAssociator/interface/TrackAssociatorParameters.h>
#include <TrackingTools/TrackAssociator/interface/TrackDetMatchInfo.h>
#include <TrackingTools/TrajectoryState/interface/FreeTrajectoryState.h>
#include <TrackPropagation/SteppingHelixPropagator/interface/SteppingHelixPropagator.h>
#include <TROOT.h>
#include <TTree.h>
#include <cmath>
#include <cstdlib>
#include <fstream>
#include <iostream>
#include <iterator>
#include <utility>

#include "../interface/FilterPlugin.h"

#include "TMultiGraph.h"
#include "TCanvas.h"

using namespace::std;

hoMuonAnalyzer::hoMuonAnalyzer(const edm::ParameterSet& iConfig)/*:
				assocParams(iConfig.getParameter<edm::ParameterSet>("TrackAssociatorParameters"))*/
{
	coutPrefix = std::string("[hoMuonAnalyzer] ");
	//now do what ever initialization is needed

	//Get Input Tags from the Configuration

	_genInput = iConfig.getParameter<edm::InputTag>("genSrc");
	_l1MuonInput = iConfig.getParameter<edm::InputTag>("l1MuonSrc");
	_horecoInput = iConfig.getParameter<edm::InputTag>("horecoSrc");
	_l1MuonGenMatchInput = iConfig.getParameter<edm::InputTag>("l1MuonGenMatchSrc");
	_hltSumAODInput = iConfig.getParameter<edm::InputTag>("hltSumAODSrc");
	deltaR_Max = iConfig.getParameter<double>("maxDeltaR");
	threshold = iConfig.getParameter<double>("hoEnergyThreshold");
	debug = iConfig.getParameter<bool>("debug");
	deltaR_L1MuonMatching = iConfig.getParameter<double>("maxDeltaRL1MuonMatching");

	assoc.useDefaultPropagator();

	edm::ParameterSet parameters = iConfig.getParameter<edm::ParameterSet>("TrackAssociatorParameters");
	edm::ConsumesCollector iC = consumesCollector();
	assocParams.loadParameters( parameters, iC );

	singleMu3TrigName = "L1_SingleMu3";
	doubleMu0TrigName = "L1_DoubleMu0";
	doubleMu5TrigName = "L1_DoubleMu5 ";

	defineTriggersOfInterest();


	/**
	 * Create the root tree for tuple storage. After that tell root to process the loader
	 * script which will provide support for the vetors of structs in the tree
	 */
	dataTree = _fileService->make<TTree>("dataTree","Tree with L1, Gen, and HO data");

	gROOT->ProcessLine(".L ./loader.C+");

	l1MuonVector = new std::vector<L1MuonData>();
	genMuonVector = new std::vector<GenMuonData>();
	hoRecHitVector = new std::vector<HoRecHitData>();

	dataTree->Branch("l1MuonData","vector<L1MuonData>",l1MuonVector);
	dataTree->Branch("hoRecHitData","vector<HoRecHitData>",hoRecHitVector);
	dataTree->Branch("genMuonData","vector<GenMuonData>",genMuonVector);

}


hoMuonAnalyzer::~hoMuonAnalyzer()
{

	// do anything here that needs to be done at desctruction time
	// (e.g. close files, deallocate resources etc.)

	//f->Close();

}


//
// member functions#include "DataFormats/GeometryVector/interface/GlobalTag.h"

//

// ------------ method called for each event  ------------
void
hoMuonAnalyzer::analyze(const edm::Event& iEvent, 
		const edm::EventSetup& iSetup)
{
	/*
	 * Get Event Data and Event Setup
	 */

	iEvent.getByLabel(_genInput,truthParticles);

	iEvent.getByLabel(_l1MuonInput, l1Muons);

	iEvent.getByLabel(_horecoInput, hoRecoHits);

	edm::ESHandle<CaloGeometry> caloGeo;
	iSetup.get<CaloGeometryRecord>().get(caloGeo);

	edm::Handle<edm::View<l1extra::L1MuonParticle> > l1MuonView;
	iEvent.getByLabel(_l1MuonInput,l1MuonView);

	edm::Handle<reco::GenParticleMatch> l1MuonGenMatches;
	iEvent.getByLabel(_l1MuonGenMatchInput,l1MuonGenMatches);

	edm::Handle<vector<PCaloHit>> caloHits;
	iEvent.getByLabel(edm::InputTag("g4SimHits","HcalHits"),caloHits);

	edm::ESHandle<MagneticField> theMagField;
	iSetup.get<IdealMagneticFieldRecord>().get(theMagField );

	iSetup.get<DetIdAssociatorRecord>().get("HODetIdAssociator", hoDetIdAssociator_);
	if(!hoDetIdAssociator_.isValid()){
		std::cout << coutPrefix << "HODetIdAssociator is not Valid!" << std::endl;
	}


	hoMatcher = new HoMatcher(*caloGeo);

	//Try getting the event info for weights
	edm::Handle<GenEventInfoProduct> genEventInfo;
	iEvent.getByLabel(edm::InputTag("generator"), genEventInfo);

	if (!caloHits.isValid()) {
		std::cout << coutPrefix << "no SimHits" << std::endl;
		return;
	}

	if (!MuonHOAcceptance::Inited()) MuonHOAcceptance::initIds(iSetup);

//	MuonHOAcceptance* mhoa = new MuonHOAcceptance();
//	std::cout << "Is inited: " << mhoa->Inited() << std::endl;
//	mhoa->initIds(iSetup);
//	TFile* f = new TFile("deadRegions.root","RECREATE");
//	TCanvas* c  = new TCanvas();
//	TMultiGraph* deadRegions = mhoa->graphDeadRegions();
//	deadRegions->Draw("ap");
//	c->Write();
//	f->Write();
//	f->Close();

	/**
	 * Loop over the collections for gen muons, l1muons and hoRechits
	 * Fill the information in vectors of structs and write this data to
	 * the root tree
	 */
	genMuonVector->clear();
	for( reco::GenParticleCollection::const_iterator genPart = truthParticles->begin() ; genPart != truthParticles->end(); genPart++){
		genMuonVector->push_back(GenMuonData(
				genPart->eta(),
				genPart->phi(),
				genPart->pt(),
				genPart->pdgId(),
				MuonHOAcceptance::inGeomAccept(genPart->eta(),genPart->phi()),
				MuonHOAcceptance::inNotDeadGeom(genPart->eta(),genPart->phi()),
				MuonHOAcceptance::inSiPMGeom(genPart->eta(),genPart->phi())
		));

		TrackDetMatchInfo * muMatch = getTrackDetMatchInfo(*genPart,theMagField,iEvent,iSetup);
		double muMatchEta = muMatch->trkGlobPosAtHO.eta();
		double muMatchPhi = muMatch->trkGlobPosAtHO.phi();

		//The mu match position is inside HO acceptance
		if(MuonHOAcceptance::inGeomAccept(muMatchEta,muMatchPhi)
			&& MuonHOAcceptance::inNotDeadGeom(muMatchEta,muMatchPhi)
			&& !hoMatcher->isInChimney(muMatchEta,muMatchPhi)){

			histogramBuilder.fillCountHistogram(std::string("tdmiInGA"));
			histogramBuilder.fillEtaPhiGraph(muMatchEta,muMatchPhi,std::string("tdmiInGA"));

			const HORecHit* matchedRecHit = hoMatcher->matchByEMaxDeltaR(muMatch->trkGlobPosAtHO.eta()
					,muMatch->trkGlobPosAtHO.phi(),deltaR_Max,*hoRecoHits);
			//Found the Rec Hit with largest E
			if(matchedRecHit){
				double ho_eta = caloGeo->getPosition(matchedRecHit->id()).eta();
				double ho_phi = caloGeo->getPosition(matchedRecHit->id()).phi();
				histogramBuilder.fillDeltaEtaDeltaPhiHistograms(
						muMatch->trkGlobPosAtHO.eta(),
						ho_eta,
						muMatch->trkGlobPosAtHO.phi(),
						ho_phi,
						std::string("tdmiHoMatch")
				);
				//Energy is above threshold
				if(matchedRecHit->energy() > threshold){
					histogramBuilder.fillDeltaEtaDeltaPhiHistograms(
							muMatch->trkGlobPosAtHO.eta(),
							ho_eta,
							muMatch->trkGlobPosAtHO.phi(),
							ho_phi,
							std::string("tdmiHoAboveThr")
					);
					//TDMI has energy entry > 0
					if(muMatch->hoCrossedEnergy() > 0 ){
						histogramBuilder.fillDeltaEtaDeltaPhiHistograms(
								muMatch->trkGlobPosAtHO.eta(),
								ho_eta,
								muMatch->trkGlobPosAtHO.phi(),
								ho_phi,
								std::string("tdmiHoAboveThrGt0")
						);
					} else{
						/**
						 * In this case, the muMatch from TDMI has 0 energy
						 * but was found to be in the geom acceptance
						 */
						histogramBuilder.fillDeltaEtaDeltaPhiHistograms(
								muMatch->trkGlobPosAtHO.eta(),
								ho_eta,
								muMatch->trkGlobPosAtHO.phi(),
								ho_phi,
								std::string("tdmiHoAboveThrEq0")
						);
						histogramBuilder.fillEtaPhiGraph(
								muMatch->trkGlobPosAtHO.eta(),
								muMatch->trkGlobPosAtHO.phi(),
								std::string("tdmiHoAboveThrEq0")
						);
					}
				}
			} else{
				/**
				 * There could not be found a rec hit by delta R matching
				 */
				histogramBuilder.fillCountHistogram(std::string("tdmiMatchHoFail"));
				histogramBuilder.fillEtaPhiGraph(muMatchEta,muMatchPhi,std::string("tdmiMatchHoFail"));
			}
		}//<-- TDMI in GA
	}

	l1MuonVector->clear();
	for( l1extra::L1MuonParticleCollection::const_iterator it = l1Muons->begin();
			it != l1Muons->end() ; it++ ){
		l1MuonVector->push_back(
				L1MuonData(
						it->eta(),
						it->phi(),
						it->pt(),
						it->bx(),
						MuonHOAcceptance::inGeomAccept(it->eta(),it->phi()),
						MuonHOAcceptance::inNotDeadGeom(it->eta(),it->phi()),
						MuonHOAcceptance::inSiPMGeom(it->eta(),it->phi())
				)
		);
	}

	hoRecHitVector->clear();
	for( auto it = hoRecoHits->begin(); it != hoRecoHits->end(); it++ ){
		hoRecHitVector->push_back(
				HoRecHitData(
						caloGeo->getPosition(it->id()).eta(),
						caloGeo->getPosition(it->id()).phi(),
						it->energy(),
						it->time()
				)
		);
	}

	dataTree->Fill();

	/**
	 * ###########################
	 * Done with filling the data into the trees
	 * ###########################
	 */

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

	histogramBuilder.fillCountHistogram("ProcessedEvents");

	//###############################
	// BEGIN Loop over Gen Particles only
	//###############################
	//Use this variable to store whether the event has GenMuons in acceptance
	bool hasMuonsInAcceptance = false;
	std::string gen_key = "gen";
	int genMuonCounter = 0;
	for(reco::GenParticleCollection::const_iterator genIt = truthParticles->begin();
			genIt != truthParticles->end(); genIt++){
		//Check for muons in Full barrel only
		if( ( abs(genIt->pdgId()) == 13 ) && ( abs(genIt->eta()) <= 0.8 ) ){
			hasMuonsInAcceptance = true;
			genMuonCounter++;
			histogramBuilder.fillPtHistogram(genIt->pt(),gen_key);
			histogramBuilder.fillEtaPhiGraph(genIt->eta(),genIt->phi(),gen_key);
			for (int i = 0; i < 200; i+=2) {
				if(genIt->pt() >= i){
					histogramBuilder.fillTrigRateHistograms(i,gen_key);
				}
			}
		}
	}
	histogramBuilder.fillMultiplicityHistogram(genMuonCounter,gen_key);
	//###############################
	// Loop over Gen Particles only DONE
	//###############################
	if(!hasMuonsInAcceptance)
		return;

	histogramBuilder.fillCountHistogram("Events");
	/*
	 * Level 1 Muons
	 */
	string l1muon_key = "L1Muon";

	/**
	 * first loop over all L1 Muon objects. The contents of this Loop
	 * may be moved to the larger loop over l1 objects later in the code
	 */
	//Define iterators
	l1extra::L1MuonParticleCollection::const_iterator bl1Muon = l1Muons->begin();
	l1extra::L1MuonParticleCollection::const_iterator el1Muon = l1Muons->end();
	for( unsigned int i = 0 ; i < l1Muons->size(); i++  ) {
		const l1extra::L1MuonParticle* bl1Muon = &(l1Muons->at(i));
		const reco::GenParticle* genMatch = getBestGenMatch(bl1Muon->eta(),bl1Muon->phi());
		if(genMatch){
			histogramBuilder.fillDeltaVzHistogam( (genMatch->vz() - bl1Muon->vz()) ,l1muon_key);
			histogramBuilder.fillPtCorrelationHistogram(genMatch->pt(),bl1Muon->pt(),l1muon_key);
			fillEfficiencyHistograms(bl1Muon->pt(),genMatch->pt(),"L1MuonPt");
		}
		edm::RefToBase<l1extra::L1MuonParticle> l1MuonCandiateRef(l1MuonView,i);
		reco::GenParticleRef ref = (*l1MuonGenMatches)[l1MuonCandiateRef];
		if(ref.isNonnull())
			histogramBuilder.fillPdgIdHistogram(ref->pdgId(),l1muon_key);
		else
			histogramBuilder.fillPdgIdHistogram(0,l1muon_key);
	}
	//###############################
	// Loop over L1MuonObjects DONE
	//###############################

	//###############################
	// BEGIN Loop over HO Rec hits only
	//###############################
	string horeco_key = "horeco";
	string horecoT_key ="horecoAboveThreshold";
	/**
	 * Collect information of all HO Rec hits when there are
	 * l1 muons in the acceptance region
	 */
	int recHitAbThrCounter = 0;
	auto hoRecoIt = hoRecoHits->begin();
	for( ; hoRecoIt != hoRecoHits->end() ; hoRecoIt++){
		double ho_eta = caloGeo->getPosition(hoRecoIt->id()).eta();
		double ho_phi = caloGeo->getPosition(hoRecoIt->id()).phi();
		histogramBuilder.fillTimeHistogram(hoRecoIt->time(),std::string("hoRecHits"));
		if(hoRecoIt->energy() >= threshold){
			histogramBuilder.fillTimeHistogram(hoRecoIt->time(),std::string("hoRecHitsAboveThr"));
			histogramBuilder.fillEtaPhiHistograms(ho_eta, ho_phi, std::string("hoRecHitsAboveThr"));
			recHitAbThrCounter++;
		}
		histogramBuilder.fillCountHistogram(horeco_key);
		histogramBuilder.fillEnergyHistograms(hoRecoIt->energy(),horeco_key);
		histogramBuilder.fillEtaPhiHistograms(ho_eta, ho_phi, horeco_key);
	}
	histogramBuilder.fillMultiplicityHistogram(recHitAbThrCounter,horecoT_key);
	histogramBuilder.fillMultiplicityHistogram(hoRecoHits->size(),horeco_key);

	/*
	 * L1 Trigger Decisions
	 */
	singleMu3Trig = processTriggerDecision(singleMu3TrigName,iEvent);
	doubleMu0Trig = processTriggerDecision(doubleMu0TrigName,iEvent);
	//	processTriggerDecision(doubleMu5TrigName,iEvent);
	//###############################
	// Loop over HO Rec hits only DONE
	//###############################

	int countGenMatches = 0;
	string l1MuonWithHoMatch_key = "L1MuonWithHoMatch";
	bl1Muon = l1Muons->begin();
	el1Muon = l1Muons->end();
	histogramBuilder.fillMultiplicityHistogram(l1Muons->size(),"L1MuonPresent");
	for( unsigned int i = 0 ; i < l1Muons->size(); i++ ){
		const l1extra::L1MuonParticle* bl1Muon = &(l1Muons->at(i));
		float l1Muon_eta = bl1Muon->eta();
		float l1Muon_phi = bl1Muon->phi();
		histogramBuilder.fillCountHistogram(std::string("L1MuonPresent"));
		histogramBuilder.fillBxIdHistogram(bl1Muon->bx(),std::string("L1MuonPresent"));
		histogramBuilder.fillBxIdVsPt(bl1Muon->bx(),bl1Muon->pt(),"L1MuonPresent");
		histogramBuilder.fillL1MuonPtHistograms(bl1Muon->pt(),std::string("L1MuonPresent"));
		histogramBuilder.fillPdgIdHistogram(bl1Muon->pdgId(),l1muon_key);
		histogramBuilder.fillVzHistogram(bl1Muon->vz(),l1muon_key);
		histogramBuilder.fillEtaPhiGraph(bl1Muon->eta(), bl1Muon->phi(), l1muon_key);
		//For variable binning
		listL1MuonPt.push_back(bl1Muon->pt());
		/*
		 * Fill histogram for different pt thresholds
		 * CAREFUL!! THIS IS NOT A REAL RATE YET!!
		 */
		for (int j = 0; j < 200; j+=2) {
			if(bl1Muon->pt() >= j){
				histogramBuilder.fillTrigRateHistograms(j,"L1MuonPresent");
			}
		}
		//##################################################
		//##################################################
		// L1 Muons for the "Oliver Style" efficiency
		//##################################################
		//##################################################
		if(MuonHOAcceptance::inGeomAccept(l1Muon_eta,l1Muon_phi)){
			histogramBuilder.fillCountHistogram("L1MuonInGA_L1Dir");
			//TODO write function to find central tile (and search 3x3 area around) with respect to the given direction
			GlobalPoint l1Direction(
					bl1Muon->p4().X(),
					bl1Muon->p4().Y(),
					bl1Muon->p4().Z()
					);
			histogramBuilder.fillCorrelationGraph(l1Direction.eta(),l1Muon_eta,"Correlationp4AndL1Object");
			if(hasHoHitInGrid(l1Direction,0)){
				histogramBuilder.fillCountHistogram("L1MuonCentral");
				histogramBuilder.fillEfficiency(true,bl1Muon->pt(),"L1MuonCentral");
			} else{
				histogramBuilder.fillEfficiency(false,bl1Muon->pt(),"L1MuonCentral");
			}
			if(hasHoHitInGrid(l1Direction,1)){
				histogramBuilder.fillCountHistogram("L1Muon3x3");
				histogramBuilder.fillEfficiency(true,bl1Muon->pt(),"L1Muon3x3");
			} else {
				histogramBuilder.fillEfficiency(false,bl1Muon->pt(),"L1Muon3x3");
			}
		}

		const HORecHit* matchedRecHit = hoMatcher->matchByEMaxDeltaR(l1Muon_eta,l1Muon_phi,deltaR_Max,*hoRecoHits);
		if(matchedRecHit){
			double hoEta,hoPhi;
			hoEta = caloGeo->getPosition(matchedRecHit->detid()).eta();
			hoPhi = caloGeo->getPosition(matchedRecHit->detid()).phi();
			histogramBuilder.fillCountHistogram("L1MuonPresentHoMatch");
			histogramBuilder.fillTimeHistogram(matchedRecHit->time(),std::string("L1MuonPresentHoMatch"));
			histogramBuilder.fillDeltaTimeHistogram(matchedRecHit->time(),bl1Muon->bx(),std::string("L1MuonPresentHoMatch"));
			histogramBuilder.fillBxIdHistogram(bl1Muon->bx(),std::string("L1MuonPresentHoMatch"));
			if (MuonHOAcceptance::inGeomAccept(l1Muon_eta,l1Muon_phi/*,deltaR_Max,deltaR_Max*/)){
				histogramBuilder.fillCountHistogram(std::string("L1MuonPresentHoMatchInAcc"));
				histogramBuilder.fillBxIdHistogram(bl1Muon->bx(),std::string("L1MuonPresentHoMatchInAcc"));

				//This energy check is done to test, whether the results depend on the order of the cuts applied
				//So far, the answer is no
				if(matchedRecHit->energy() >= threshold ){
					histogramBuilder.fillCountHistogram(std::string("L1MuonPresentHoMatchInAccThr"));

				}

				if (MuonHOAcceptance::inNotDeadGeom(l1Muon_eta,l1Muon_phi/*,deltaR_Max,deltaR_Max*/)){
					histogramBuilder.fillCountHistogram(std::string("L1MuonPresentHoMatchInAccNotDead"));
					histogramBuilder.fillBxIdHistogram(bl1Muon->bx(),std::string("L1MuonPresentHoMatchInAccNotDead"));
					//This one is filled for the sake of completeness. The SiPM regions are hard-coded in the class!!
					if (MuonHOAcceptance::inSiPMGeom(l1Muon_eta,l1Muon_phi/*,deltaR_Max,deltaR_Max*/)){
						histogramBuilder.fillCountHistogram(std::string("L1MuonPresentHoMatchInAccNotDeadInSipm"));
					}
				}
			}
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
				countGenMatches++;
				fillEfficiencyHistograms(bl1Muon->pt(),bestGenMatch->pt(),"L1MuonHoReco");
			}

			//###########################################################
			//###########################################################
			//Now fill information for hits above threshold
			//###########################################################
			//###########################################################
			if(matchedRecHit->energy() >= threshold){
				//Fill some counting histograms. Can be used for cut flow in efficiency
				histogramBuilder.fillCountHistogram(std::string("L1MuonAboveThr"));
				histogramBuilder.fillBxIdHistogram(bl1Muon->bx(),std::string("L1MuonAboveThr"));
				histogramBuilder.fillDeltaTimeHistogram(matchedRecHit->time(),bl1Muon->bx(),std::string("L1MuonAboveThr"));
				histogramBuilder.fillTimeHistogram(matchedRecHit->time(),std::string("L1MuonAboveThr"));
				histogramBuilder.fillBxIdVsPt(bl1Muon->bx(),bl1Muon->pt(),"L1MuonAboveThr");
				double hoEta,hoPhi;
				hoEta = caloGeo->getPosition(matchedRecHit->detid()).eta();
				hoPhi = caloGeo->getPosition(matchedRecHit->detid()).phi();
				//Fill the HO information
				//Fill the counters
				if (MuonHOAcceptance::inGeomAccept(l1Muon_eta,l1Muon_phi/*,deltaR_Max,deltaR_Max*/)){
					histogramBuilder.fillCountHistogram(std::string("L1MuonAboveThrInAcc"));
					histogramBuilder.fillBxIdHistogram(bl1Muon->bx(),std::string("L1MuonAboveThrInAcc"));
					if (MuonHOAcceptance::inNotDeadGeom(l1Muon_eta,l1Muon_phi/*,deltaR_Max,deltaR_Max*/)){
						histogramBuilder.fillTimeHistogram(matchedRecHit->time(),std::string("L1MuonAboveThrInAccNotDead"));
						histogramBuilder.fillDeltaTimeHistogram(matchedRecHit->time(),bl1Muon->bx(),std::string("L1MuonAboveThrInAccNotDead"));
						histogramBuilder.fillCountHistogram(std::string("L1MuonAboveThrInAccNotDead"));
						histogramBuilder.fillBxIdHistogram(bl1Muon->bx(),std::string("L1MuonAboveThrInAccNotDead"));
						histogramBuilder.fillTrigHistograms(caloGeo->present(matchedRecHit->id()),std::string("caloGeoPresent_L1MuonHoMatchAboveThrFilt"));
						histogramBuilder.fillEnergyHistograms(matchedRecHit->energy(),std::string("L1MuonWithHoMatchAboveThrFilt"));
						histogramBuilder.fillEtaPhiHistograms(hoEta,hoPhi,std::string("L1MuonWithHoMatchAboveThrFilt_HO"));
						histogramBuilder.fillDeltaEtaDeltaPhiHistograms(l1Muon_eta,hoEta,l1Muon_phi, hoPhi,std::string("L1MuonWithHoMatchAboveThrFilt"));
						histogramBuilder.fillL1MuonPtHistograms(bl1Muon->pt(),std::string("L1MuonWithHoMatchAboveThrFilt"));
						histogramBuilder.fillEnergyVsPosition(hoEta,hoPhi,matchedRecHit->energy(),std::string("L1MuonWithHoMatchAboveThrFilt"));

						const reco::GenParticle* bestGenMatch = getBestGenMatch(bl1Muon->eta(),bl1Muon->phi());
						if(bestGenMatch){
							fillEfficiencyHistograms(bl1Muon->pt(),bestGenMatch->pt(),"L1MuonHoRecoAboveThrFilt");
						}

						//This one is filled for the sake of completeness. The SiPM regions are hardcoded in the class!!
						if (MuonHOAcceptance::inSiPMGeom(l1Muon_eta,l1Muon_phi/*,deltaR_Max,deltaR_Max*/)){
							histogramBuilder.fillCountHistogram(std::string("L1MuonAboveThrInAccNotDeadInSipm"));
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
					fillEfficiencyHistograms(bl1Muon->pt(),bestGenMatch->pt(),"L1MuonHoRecoAboveThr");
					histogramBuilder.fillBxIdVsPt(bl1Muon->bx(),bl1Muon->pt(),"L1MuonAboveThrGenMatch");
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
				histogramBuilder.fillEtaPhiGraph(bl1Muon->eta(), bl1Muon->phi(), std::string("L1MuonWithHoMatchAboveThr_L1Mu"));
			}// E > thr.
		}
	}//<-- For loop over all l1muons
	histogramBuilder.fillMultiplicityHistogram(countGenMatches,std::string("nL1WithGenMatch"));
	//################################
	//################################
	//		This is for the case where no L1Muon was found
	//################################
	//################################
	if(l1Muons->size() == 0){
		histogramBuilder.fillCountHistogram("NoL1Muon");
		int recHitAbThrNoL1Counter = 0;
		auto hoRecoIt = hoRecoHits->begin();
		for( ; hoRecoIt != hoRecoHits->end() ; hoRecoIt++){
			if(hoRecoIt->energy() >= threshold){
				recHitAbThrNoL1Counter++;
				double ho_eta = caloGeo->getPosition(hoRecoIt->id()).eta();
				double ho_phi = caloGeo->getPosition(hoRecoIt->id()).phi();
				histogramBuilder.fillCountHistogram(horeco_key);
				histogramBuilder.fillEnergyHistograms(hoRecoIt->energy(),std::string("NoL1"));
				histogramBuilder.fillEtaPhiHistograms(ho_eta, ho_phi, std::string("NoL1"));
				histogramBuilder.fillEnergyVsPosition(ho_eta,ho_phi,hoRecoIt->energy(),std::string("NoL1"));
			}
		}
		histogramBuilder.fillMultiplicityHistogram(recHitAbThrNoL1Counter,std::string("NoL1"));

		for(reco::GenParticleCollection::const_iterator genIt = truthParticles->begin();
				genIt != truthParticles->end(); genIt++){
			//Check for muons in Full barrel only
			//Try to find a corresponding Gen Muon
			float genEta = genIt->eta();
			float genPhi = genIt->phi();

			/**
			 * #############################################
			 * # Use TrackDetMatchInfo to see where the gen particle ends up in HO. When selecting only events, where gen is in
			 * # the geometric acceptance of HO, this gives a more realistic estimator for the number of recoverable
			 * # Triggers
			 * #############################################
			 */
			TrackDetMatchInfo * muMatch = getTrackDetMatchInfo(*genIt,theMagField,iEvent,iSetup);

			double muMatchPhi = muMatch->trkGlobPosAtHO.phi();
			double muMatchEta = muMatch->trkGlobPosAtHO.eta();
			histogramBuilder.fillEtaPhiGraph(genEta,genPhi,"NoL1GenAny");
			histogramBuilder.fillEtaPhiGraph(muMatchEta,muMatchPhi,"NoL1TdmiAny");
			if(MuonHOAcceptance::inGeomAccept(muMatchEta,muMatchPhi) && MuonHOAcceptance::inNotDeadGeom(muMatchEta,muMatchPhi)){
				histogramBuilder.fillEtaPhiGraph(genEta,genPhi,"NoL1GenInGA");
				histogramBuilder.fillEtaPhiGraph(muMatchEta,muMatchPhi,"NoL1TdmiInGA");
			}
		}

	}// <-- l1muons size == 0
	else{
		/**
		 * #################################
		 * # L1 Muon objects contain data
		 * # FIXME: Loop over l1 and try to find gens. This way, the direction information of the strange l1 is already available
		 * # Loop over gens and inspect also the case, where the matching from gen to l1 failed
		 * # This might be a hint on ghost reduction
		 * #################################
		 */
		for(reco::GenParticleCollection::const_iterator genIt = truthParticles->begin();
				genIt != truthParticles->end(); genIt++){
			float genEta = genIt->eta();
			float genPhi = genIt->phi();

			TrackDetMatchInfo * muMatch = getTrackDetMatchInfo(*genIt,theMagField,iEvent,iSetup);
			double muMatchPhi = muMatch->trkGlobPosAtHO.phi();
			double muMatchEta = muMatch->trkGlobPosAtHO.eta();

			if(MuonHOAcceptance::inGeomAccept(muMatchEta,muMatchPhi)){
				histogramBuilder.fillCountHistogram("TdmiInGA_TdmiDir");
				//TODO write function to find central tile (and search 3x3 area around) with respect to the given direction
				std::vector<const HORecHit*> crossedHoRecHits = muMatch->crossedHORecHits;
				if(	hasHoHitInGrid(GlobalPoint(
						muMatch->trkGlobPosAtHO.X(),
						muMatch->trkGlobPosAtHO.Y(),
						muMatch->trkGlobPosAtHO.Z()
					),0)
						//hasHoHitInGrid(muMatchEta,muMatchPhi,crossedHoRecHits,0)
						){
					histogramBuilder.fillCountHistogram("TdmiCentral");
					histogramBuilder.fillEfficiency(true,genIt->pt(),"tdmiCentral");
				} else {
					histogramBuilder.fillEfficiency(false,genIt->pt(),"tdmiCentral");

				}
				if( hasHoHitInGrid(GlobalPoint(
						muMatch->trkGlobPosAtHO.X(),
						muMatch->trkGlobPosAtHO.Y(),
						muMatch->trkGlobPosAtHO.Z()
					),1)
					//hasHoHitInGrid(muMatchEta,muMatchPhi,crossedHoRecHits,1)
					){
					histogramBuilder.fillCountHistogram("Tdmi3x3");
					histogramBuilder.fillEfficiency(true,genIt->pt(),"tdmi3x3");
				} else {
					histogramBuilder.fillEfficiency(false,genIt->pt(),"tdmi3x3");

				}
			}
			const l1extra::L1MuonParticle* l1Part = getBestL1MuonMatch(muMatchEta,muMatchPhi);
			if(l1Part){
				double deltaEta = muMatchEta - l1Part->eta();
				double deltaPhi = muMatchPhi - l1Part->phi();
				histogramBuilder.fillGraph(deltaEta,deltaPhi,"deltaEtaDeltaPhiTdmiL1");
			}
			const HORecHit* matchedRecHit = hoMatcher->matchByEMaxDeltaR(genEta,genPhi,deltaR_Max,*hoRecoHits);
			if(matchedRecHit){
				double hoEta = caloGeo->getPosition(matchedRecHit->id()).eta();
				double hoPhi = caloGeo->getPosition(matchedRecHit->id()).phi();
				histogramBuilder.fillDeltaEtaDeltaPhiEnergyHistogram(genEta,hoEta,genPhi,hoPhi,matchedRecHit->energy(),std::string("WithSingleMu"));
				if(matchedRecHit->energy() >= threshold){
					histogramBuilder.fillDeltaEtaDeltaPhiHistograms(genEta,hoEta,genPhi,hoPhi,std::string("WithSingleMuAboveThr"));
					if (MuonHOAcceptance::inGeomAccept(genEta,genPhi/*,deltaR_Max,deltaR_Max*/)){
						histogramBuilder.fillDeltaEtaDeltaPhiHistograms(genEta,hoEta,genPhi,hoPhi,std::string("WithSingleMuGeomAcc"));
						if (MuonHOAcceptance::inNotDeadGeom(genEta,genPhi/*,deltaR_Max,deltaR_Max*/)){
							histogramBuilder.fillDeltaEtaDeltaPhiHistograms(genEta,hoEta,genPhi,hoPhi,std::string("WithSingleMuNotDead"));
						}
					}
				}
			}//Matched rec hit
		}//Gen particle loop
	}

	//#############################################################
	//#############################################################
	// NO SINGLE MU TRIGGER
	//#############################################################
	//#############################################################


	if(!singleMu3Trig){
		histogramBuilder.fillCountHistogram(std::string("NoSingleMu"));
		histogramBuilder.fillMultiplicityHistogram(l1Muons->size(),std::string("NoSingleMu_L1Muon"));

		//################################
		//################################
		// Match Ho to gen info and try to recover mu trigger
		//################################
		//################################
		for(reco::GenParticleCollection::const_iterator genIt = truthParticles->begin();
				genIt != truthParticles->end(); genIt++){
			//Check for muons in Full barrel only
			//Try to find a corresponding Gen Muon
			float genEta = genIt->eta();
			float genPhi = genIt->phi();

			/**
			 * #############################################
			 * # Use TrackDetMatchInfo to see where the gen particle ends up in HO. When selecting only events, where gen is in
			 * # the geometric acceptance of HO, this gives a more realistic estimator for the number of recoverable
			 * # Triggers
			 * #############################################
			 */
			TrackDetMatchInfo * muMatch = getTrackDetMatchInfo(*genIt,theMagField,iEvent,iSetup);
			double muMatchPhi = muMatch->trkGlobPosAtHO.phi();
			double muMatchEta = muMatch->trkGlobPosAtHO.eta();

			//Studies depending on whether there are L1 Objects or not
			if(l1Muons->size()>0){
				histogramBuilder.fillCountHistogram(std::string("NoTriggerButL1Muons"));
			}
			else{
				histogramBuilder.fillCountHistogram("NoTrgNoL1Any");
				histogramBuilder.fillEtaPhiGraph(genEta,genPhi,"NoTrgNoL1GenAny");
				histogramBuilder.fillEtaPhiGraph(muMatchEta,muMatchPhi,"NoTrgNoL1TdmiAny");
				if(MuonHOAcceptance::inGeomAccept(muMatchEta,muMatchPhi)){
					histogramBuilder.fillEtaPhiGraph(genEta,genPhi,"NoTrgNoL1GenInGA");
					histogramBuilder.fillEtaPhiGraph(muMatchEta,muMatchPhi,"NoTrgNoL1TdmiInGA");
				}
			}
			histogramBuilder.fillPtHistogram(genIt->pt(),std::string("NoSingleMu"));

			histogramBuilder.fillEtaPhiGraph(genEta,genPhi,std::string("NoTrgGenAny"));
			histogramBuilder.fillEtaPhiGraph(muMatchEta,muMatchPhi,std::string("NoTrgTdmiAny"));
			//The muon needs to hit the HO geometric acceptance
			if(MuonHOAcceptance::inGeomAccept(muMatchEta,muMatchPhi)){
				histogramBuilder.fillEtaPhiGraph(muMatchEta,muMatchPhi,"NoTrgTdmiInGA");
				histogramBuilder.fillCountHistogram("NoTrgTdmiInGA");
				histogramBuilder.fillEnergyVsPosition(muMatchEta,muMatchPhi,muMatch->hoCrossedEnergy(),std::string("NoTrgTdmiXedE"));
				const HORecHit* matchedRecHit = hoMatcher->matchByEMaxDeltaR(muMatchEta,muMatchPhi,deltaR_Max,*hoRecoHits);
				//Where is the Rec hit in a delta R cone with the largest E?
				//Did we find any?
				if(matchedRecHit){
					double hoEta = caloGeo->getPosition(matchedRecHit->id()).eta();
					double hoPhi = caloGeo->getPosition(matchedRecHit->id()).phi();
					histogramBuilder.fillDeltaEtaDeltaPhiHistograms(muMatchEta,hoEta,muMatchPhi,hoPhi,std::string("NoTrgTdmi"));
					//Apply energy cut on the matched RecHit
					if(matchedRecHit->energy() >= threshold ){
						histogramBuilder.fillDeltaEtaDeltaPhiHistograms(muMatchEta,hoEta,muMatchPhi,hoPhi,std::string("NoTrgTdmiAboveThr"));
						histogramBuilder.fillDeltaEtaDeltaPhiHistograms(genEta,hoEta,genPhi,hoPhi,std::string("NoTrgGenAboveThr"));
						histogramBuilder.fillEnergyVsPosition(muMatchEta,muMatchPhi,muMatch->hoCrossedEnergy(),std::string("NoTrgTdmiAboveThrXedE"));
						histogramBuilder.fillEnergyVsPosition(hoEta,hoPhi,matchedRecHit->energy(),std::string("NoTrgTdmiAboveThrHoE"));
					//inspect the crossed energy, when the matched Rec hit in the cone was below threshold
					} else{
						histogramBuilder.fillEnergyVsPosition(muMatchEta,muMatchPhi,muMatch->hoCrossedEnergy(),std::string("NoTrgTdmiBelowThrXedE"));
					}
				//Count the events, where we could not match a Rec hit in the delta dR cone
				} else{
					histogramBuilder.fillCountHistogram(std::string("NoTrgHoMatchFail"));
					histogramBuilder.fillEtaPhiGraph(muMatchEta,muMatchPhi,std::string("NoTrgHoMatchFail"));
				}
			}//<-- in GA
			else{
				histogramBuilder.fillEtaPhiGraph(muMatchEta,muMatchPhi,"NoTrgTdmiNotInGA");
			}
		}//Loop over gen particles
	}//<-- Not single mu trg
	else {
		/**
		 * #######################
		 * ######################
		 * The following part serves for checking cases where there is a L1 Muon trigger
		 * It's possible that some code is similar or the same as above. But for clarity reasons
		 * the code below is used
		 * #######################
		 * ######################
		 */
		for(reco::GenParticleCollection::const_iterator genIt = truthParticles->begin();
				genIt != truthParticles->end(); genIt++){
			float genEta = genIt->eta();
			float genPhi = genIt->phi();

			TrackDetMatchInfo * muMatch = getTrackDetMatchInfo(*genIt,theMagField,iEvent,iSetup);
			double muMatchPhi = muMatch->trkGlobPosAtHO.phi();
			double muMatchEta = muMatch->trkGlobPosAtHO.eta();

			//Require the muon to hit the HO area
			if(MuonHOAcceptance::inGeomAccept(muMatchEta,muMatchPhi)){

				histogramBuilder.fillCountHistogram("SMuTrgTdmiInGA");
				const l1extra::L1MuonParticle* l1Ref = getBestL1MuonMatch(genEta,genPhi);
				if(l1Ref){
					histogramBuilder.fillCountHistogram("SMuTrgFoundL1Match");
					float l1Muon_eta = l1Ref->eta();
					float l1Muon_phi = l1Ref->phi();
					fillEfficiencyHistograms(l1Ref->pt(),genIt->pt(),"SMuTrgL1AndGenMatch");
					const HORecHit* matchedRecHit = hoMatcher->matchByEMaxDeltaR(l1Muon_eta,l1Muon_phi,deltaR_Max,*hoRecoHits);
					//Check whether an HO match could be found by the delta R method
					if(matchedRecHit){
						histogramBuilder.fillCountHistogram("SMuTrgL1AndFoundHoMatch");
						//inspect the data where HO was above the threshold
						if(matchedRecHit->energy() >= threshold){
							histogramBuilder.fillCountHistogram("SMuTrgL1AndHoAboveThr");
							fillEfficiencyHistograms(l1Ref->pt(),genIt->pt(),"SMuTrgL1AndGenMatchHoAboveThr");
						}
					}
				}//<-- Found L1 ref
				else{
					const HORecHit* matchedRecHit = hoMatcher->matchByEMaxDeltaR(muMatchEta,muMatchPhi,deltaR_Max,*hoRecoHits);
					//Check whether an HO match could be found by the delta R method
					if(matchedRecHit){
						histogramBuilder.fillCountHistogram("SMuTrgAndFoundHoMatch");
						//inspect the data where HO was above the threshold
						if(matchedRecHit->energy() >= threshold){
							histogramBuilder.fillCountHistogram("SMuTrgAndHoAboveThr");
						}
					}
				}
			}
		}//Gen loop


		//Loop over L1 Objects
		//##################################################
		//##################################################
		// L1 Muons for the "Oliver Style" efficiency
		//##################################################
		//##################################################
		for( unsigned int i = 0 ; i < l1Muons->size(); i++  ) {
			const l1extra::L1MuonParticle* bl1Muon = &(l1Muons->at(i));
			double l1Muon_eta = bl1Muon->eta();
			double l1Muon_phi = bl1Muon->phi();
			if(MuonHOAcceptance::inGeomAccept(l1Muon_eta,l1Muon_phi)){
				histogramBuilder.fillCountHistogram("L1MuonSMuTrgInGA_L1Dir");
				//TODO write function to find central tile (and search 3x3 area around) with respect to the given direction
				GlobalPoint l1Direction(
						bl1Muon->p4().X(),
						bl1Muon->p4().Y(),
						bl1Muon->p4().Z()
				);
				if(hasHoHitInGrid(l1Direction,0)){
					histogramBuilder.fillCountHistogram("L1MuonSMuTrgCentral");
				}
				if(hasHoHitInGrid(l1Direction,1)){
					histogramBuilder.fillCountHistogram("L1MuonSMuTrg3x3");
				}
			}
		}
	}//<-- End of Single mu trg
}
//#############################
// End of Analyze function
//#############################


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
		cout<< coutPrefix << "trigger " << algorithmName << " does not exist in the L1 menu" << endl;
	} else {
		// error - see error code
		cout << coutPrefix << "Error Code " << iErrorCode;
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
	std::cout << coutPrefix << "getL1GtRunCache" << std::endl;
	std::cout << coutPrefix << "UseL1EventSetup: " << useL1EventSetup << std::endl;
	std::cout << coutPrefix << "UseL1GtTriggerMenuLite: " << useL1GtTriggerMenuLite << std::endl;
	m_l1GtUtils.getL1GtRunCache(iRun, evSetup, useL1EventSetup, useL1GtTriggerMenuLite);

}


// ------------ method called when ending the processing of a run  ------------

void 
hoMuonAnalyzer::endRun(const edm::Run& iRun, const edm::EventSetup& evSetup)
{

	//Only interested in unique values
	listL1MuonPt.sort();
	listL1MuonPt.unique();  //NB it is called after sort
	if(debug){
		std::cout << coutPrefix << "The list contains " << listL1MuonPt.size() << "unique entries:";
		std::list<float>::iterator it;
		for (it=listL1MuonPt.begin(); it!=listL1MuonPt.end(); ++it){
			std::cout << ' ' << *it;
		}
		std::cout << endl;
	}
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
 * Helper Functions
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
 * than delta R < delta R max
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
			if (dR < deltaR_L1MuonMatching && dR < bestDR) { // CB get it from CFG
				bestDR = dR;
				bestGen = &(*genIt);
			}
		}
	}
	return bestGen;
}
/**
 * Returns a pointer to the closest l1 muon particle of all particles that are closer
 * than delta R given by delta R max
 */
const l1extra::L1MuonParticle* hoMuonAnalyzer::getBestL1MuonMatch(double eta, double phi){
	const l1extra::L1MuonParticle* bestL1 = 0;
	float bestDR = 999.;
	l1extra::L1MuonParticleCollection::const_iterator l1It = l1Muons->begin();
	l1extra::L1MuonParticleCollection::const_iterator l1End = l1Muons->end();
	for(; l1It!=l1End; ++l1It) {
		float genPhi = l1It->phi();
		float genEta = l1It->eta();
		float dR = deltaR(eta,phi,genEta,genPhi);
		if (dR < deltaR_L1MuonMatching && dR < bestDR) { // CB get it from CFG
			bestDR = dR;
			bestL1 = &(*l1It);
		}
	}
	return bestL1;
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

/**
 * Gets the TrackDetMatchInfo for a Gen Particle by using its vertex, momentum and charge information
 * Needs the magnetic field, the edm::event and the edm::setup of an event
 */
TrackDetMatchInfo* hoMuonAnalyzer::getTrackDetMatchInfo(reco::GenParticle genPart,edm::ESHandle<MagneticField> theMagField,const edm::Event& iEvent,
		const edm::EventSetup& iSetup){
	//Create the Track det match info
	GlobalPoint vertexPoint(genPart.vertex().X(),genPart.vertex().Y(),genPart.vertex().Z());
	GlobalVector mom (genPart.momentum().x(),genPart.momentum().y(),genPart.momentum().z());
	int charge = genPart.charge();
	const FreeTrajectoryState *freetrajectorystate_ = new FreeTrajectoryState(vertexPoint, mom ,charge , &(*theMagField));
	return new TrackDetMatchInfo(assoc.associate(iEvent, iSetup, *freetrajectorystate_, assocParams));
}

/**
 * Automatically call the histogram builder to fill the efficiency objects with different cut thresholds
 * Needs the pt for evaluation of the efficiency (ptMeasured) and the real pT
 */
void hoMuonAnalyzer::fillEfficiencyHistograms(double ptMeasured, double ptReal,std::string key){
	histogramBuilder.fillEfficiency(ptMeasured >= 5, ptReal, key + "Pt5");
	histogramBuilder.fillEfficiency(ptMeasured >= 10, ptReal, key + "Pt10");
	histogramBuilder.fillEfficiency(ptMeasured >= 15, ptReal, key + "Pt15");
	histogramBuilder.fillEfficiency(ptMeasured >= 20, ptReal, key + "Pt20");
	histogramBuilder.fillEfficiency(ptMeasured >= 25, ptReal, key + "Pt25");
}

/**
 * Find out whether a given direction, represented by a point (Thank You, CMSSW)
 * points to an HORecHit with E > 0.2,
 * The Gridsize determines the search area. So far the code is only designed for odd
 * grid sizes, e.g.:
 *
 * 		Size: 0		Size: 1		Size: 2
 *
 * 								# # # # #
 * 					# # #		# # # # #
 * 			O		# O #		# # O # #
 * 					# # #		# # # # #
 * 								# # # # #
 */
bool hoMuonAnalyzer::hasHoHitInGrid(GlobalPoint direction, int gridSize){
	if(gridSize < 0){
		if(debug){
			std::cout << coutPrefix << "Negative grid size in hasHoHitInGrid(GlobalPoint,int)! Returning false." << std::endl;
		}
		return false;
	}
	//Check for odd grid size
	if(!gridSize%2 && gridSize!=0){
		if(debug){
			std::cout << coutPrefix << "GridSize in hasHoHitInGrid(GlobalPoint,int) is not odd! Reducing grid size by 1." << std::endl;
		}
		gridSize--;
	}

	//Loop over the det Ids close to the point
	std::set<DetId> detIdSet = hoDetIdAssociator_->getDetIdsCloseToAPoint(direction,gridSize);
	for(auto it = detIdSet.begin(); it != detIdSet.end(); it++){
		//Find the corresponding DetId in the rec hits
		for(auto itRecHits = hoRecoHits->begin(); itRecHits != hoRecoHits->end(); itRecHits++){
			if(itRecHits->detid() == *it){
				if(itRecHits->energy() > threshold)
					return true;
			}
		}
	}
	return false;
}
/*
 * Find out, whether HO sees a hit in a given grid
 * The Gridsize determines the search area. So far the code is only designed for odd
 * grid sizes, e.g.:
 */
bool hoMuonAnalyzer::hasHoHitInGrid(double eta, double phi, std::vector<const HORecHit*> recHits, int gridSize){
	if(gridSize < 0){
		if(debug){
			std::cout << coutPrefix << "Negative grid size in hasHoHitInGrid(double,double,std::vector<HORecHit*>,int)! Returning false." << std::endl;
		}
		return false;
	}
	//Check for odd grid size
	if(!gridSize%2 && gridSize!=0){
		if(debug){
			std::cout << coutPrefix << "GridSize in hasHoHitInGrid(double,double,std::vector<HORecHit*>,int) is not odd! Reducing grid size by 1." << std::endl;
		}
		gridSize--;
	}
	for( auto it = recHits.begin(); it != recHits.end(); it++){
		int deltaIeta = hoMatcher->getDeltaIeta(eta,*it);
		int deltaIphi = hoMatcher->getDeltaIphi(phi,*it);
		if(deltaIeta <= gridSize && deltaIphi <= gridSize){
			if((*it)->energy() >= threshold )
				return true;
		}
	}
	return false;
}
//define this as a plug-in
DEFINE_FWK_MODULE(hoMuonAnalyzer);
