// -*- C++ -*-
//
// Package:    HoMuonTrigger/DataTreeFiller
// Class:      DataTreeFiller
//
/**\class DataTreeFiller DataTreeFiller.cc HoMuonTrigger/DataTreeFiller/plugins/DataTreeFiller.cc

 Description: [one line class summary]

 Implementation:
     [Notes on implementation]
*/
//
// Original Author:  Andreas Künsken
//         Created:  Mon, 24 Aug 2015 11:39:56 GMT
//
//


// system include files
#include <CommonTools/UtilAlgos/interface/TFileService.h>
#include <DataFormats/HepMCCandidate/interface/GenParticle.h>
#include <DataFormats/HepMCCandidate/interface/GenParticleFwd.h>
#include <DataFormats/L1Trigger/interface/L1MuonParticleFwd.h>
#include <TrackingTools/TrackAssociator/interface/TrackAssociatorParameters.h>
#include <TrackingTools/TrackAssociator/interface/TrackDetectorAssociator.h>
#include <memory>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDAnalyzer.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"

#include "../../hoTriggerAnalyzer/interface/GenMuonData.h"
#include "../../hoTriggerAnalyzer/interface/HoRecHitData.h"
#include "../../hoTriggerAnalyzer/interface/L1MuonData.h"
#include "DataFormats/HcalRecHit/interface/HcalRecHitCollections.h"

#include "Geometry/CaloGeometry/interface/CaloGeometry.h"

#include "FWCore/Utilities/interface/InputTag.h"

#include "FWCore/Framework/interface/ESHandle.h"

#include "../interface/HoMatcher.h"
#include "../interface/HistogramBuilder.h"

#include <TrackingTools/TrackAssociator/interface/TrackDetMatchInfo.h>
#include <TrackingTools/TrajectoryState/interface/FreeTrajectoryState.h>
#include <TrackPropagation/SteppingHelixPropagator/interface/SteppingHelixPropagator.h>

//
// class declaration
//

class DataTreeFiller : public edm::EDAnalyzer {
   public:
      explicit DataTreeFiller(const edm::ParameterSet&);
      ~DataTreeFiller();

      static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);


   private:

  	/**
  	 * Prepare a TTree and some vectors for storing the data.
  	 * Analysis and adding of new plots should be faster, and cmssw would only needed
  	 * to be rerun if a new data member is needed. The data in the vectors is stored in structs
  	 * for the different objects (L1, HoRechit, Gen)
  	 */

  	TTree* dataTree;

  	std::vector<L1MuonData>* l1MuonVector;
  	std::vector<HoRecHitData>* hoRecHitVector;
  	std::vector<GenMuonData>* genMuonVector;

	edm::Service<TFileService> _fileService;

	edm::Handle<reco::GenParticleCollection> truthParticles;
	edm::Handle<l1extra::L1MuonParticleCollection> l1Muons;
	edm::Handle<HORecHitCollection> hoRecoHits;

	edm::ESHandle<CaloGeometry> caloGeo;

	edm::InputTag _genInput;
	edm::InputTag _l1MuonInput;
	edm::InputTag _horecoInput;

	TrackDetectorAssociator assoc;
	TrackAssociatorParameters assocParams;

	edm::ESHandle<MagneticField> theMagField;

	HistogramBuilder histogramBuilder;
	HoMatcher* hoMatcher;

	/**
	 * Energy threshold for HO rec hits
	 */
	float threshold;

	/**
	 * Gets the TrackDetMatchInfo for a Gen Particle by using its vertex, momentum and charge information
	 * Needs the magnetic field, the edm::event and the edm::setup of an event
	 */
	TrackDetMatchInfo* getTrackDetMatchInfo(reco::GenParticle genPart,const edm::Event& iEvent,
			const edm::EventSetup& iSetup){
		//Create the Track det match info
		GlobalPoint vertexPoint(genPart.vertex().X(),genPart.vertex().Y(),genPart.vertex().Z());
		GlobalVector mom (genPart.momentum().x(),genPart.momentum().y(),genPart.momentum().z());
		int charge = genPart.charge();
		const FreeTrajectoryState *freetrajectorystate_ = new FreeTrajectoryState(vertexPoint, mom ,charge , &(*theMagField));
		return new TrackDetMatchInfo(assoc.associate(iEvent, iSetup, *freetrajectorystate_, assocParams));
	};

      virtual void beginJob() override;
      virtual void analyze(const edm::Event&, const edm::EventSetup&) override;
      virtual void endJob() override;

      //virtual void beginRun(edm::Run const&, edm::EventSetup const&) override;
      //virtual void endRun(edm::Run const&, edm::EventSetup const&) override;
      //virtual void beginLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&) override;
      //virtual void endLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&) override;

      // ----------member data ---------------------------
};
