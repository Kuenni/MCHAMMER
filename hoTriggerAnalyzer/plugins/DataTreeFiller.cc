#include "HoMuonTrigger/hoTriggerAnalyzer/interface/DataTreeFiller.h"

#include <DataFormats/L1Trigger/interface/L1MuonParticle.h>
#include <RecoMuon/MuonIdentification/interface/MuonHOAcceptance.h>
#include <TROOT.h>
#include <DataFormats/L1Trigger/interface/L1MuonParticleFwd.h>

//
// constants, enums and typedefs
//

//
// static data member definitions
//

//
// constructors and destructor
//
DataTreeFiller::DataTreeFiller(const edm::ParameterSet& iConfig)

{
   //now do what ever initialization is needed
	/**
	 * Create the root tree for tuple storage. After that tell root to process the loader
	 * script which will provide support for the vectors of structs in the tree
	 */
	dataTree = _fileService->make<TTree>("dataTree","Tree with L1, Gen, and HO data");

	gROOT->ProcessLine(".L $CMSSW_BASE/src/HoMuonTrigger/loader.C+");

	l1MuonVector = new std::vector<L1MuonData>();
	genMuonVector = new std::vector<GenMuonData>();
	hoRecHitVector = new std::vector<HoRecHitData>();

	dataTree->Branch("l1MuonData","vector<L1MuonData>",l1MuonVector);
	dataTree->Branch("hoRecHitData","vector<HoRecHitData>",hoRecHitVector);
	dataTree->Branch("genMuonData","vector<GenMuonData>",genMuonVector);

	_genInput = iConfig.getParameter<edm::InputTag>("genSrc");
	_l1MuonInput = iConfig.getParameter<edm::InputTag>("l1MuonSrc");
	_horecoInput = iConfig.getParameter<edm::InputTag>("horecoSrc");

	threshold = iConfig.getParameter<double>("hoEnergyThreshold");

	hoMatcher = new HoMatcher(iConfig);

	assoc.useDefaultPropagator();

	edm::ParameterSet parameters = iConfig.getParameter<edm::ParameterSet>("TrackAssociatorParameters");
	edm::ConsumesCollector iC = consumesCollector();
	assocParams.loadParameters( parameters, iC );

}


DataTreeFiller::~DataTreeFiller()
{
 
   // do anything here that needs to be done at desctruction time
   // (e.g. close files, deallocate resources etc.)

}


//
// member functions
//

// ------------ method called for each event  ------------
void
DataTreeFiller::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup)
{
   using namespace edm;

	iEvent.getByLabel(_genInput,truthParticles);
	iEvent.getByLabel(_l1MuonInput, l1Muons);
	iEvent.getByLabel(_horecoInput, hoRecoHits);

	iSetup.get<CaloGeometryRecord>().get(caloGeo);
	iSetup.get<IdealMagneticFieldRecord>().get(theMagField );

	hoMatcher->getEvent(iEvent,iSetup);
	if (!MuonHOAcceptance::Inited()) MuonHOAcceptance::initIds(iSetup);

	/**
	 * Loop over the collections for gen muons, l1muons and hoRechits
	 * Fill the information in vectors of structs and write this data to
	 * the root tree
	 */
	genMuonVector->clear();
	for( reco::GenParticleCollection::const_iterator genPart = truthParticles->begin() ; genPart != truthParticles->end(); genPart++){

		TrackDetMatchInfo * muMatch = getTrackDetMatchInfo(*genPart,iEvent,iSetup);
		double muMatchEta = muMatch->trkGlobPosAtHO.eta();
		double muMatchPhi = muMatch->trkGlobPosAtHO.phi();

		genMuonVector->push_back(GenMuonData(
				genPart->eta(),
				genPart->phi(),
				muMatchEta,
				muMatchPhi,
				genPart->pt(),
				genPart->pdgId(),
				(MuonHOAcceptance::inGeomAccept(genPart->eta(),genPart->phi()) && !hoMatcher->isInChimney(genPart->eta(),genPart->phi())),
				MuonHOAcceptance::inNotDeadGeom(genPart->eta(),genPart->phi()),
				MuonHOAcceptance::inSiPMGeom(genPart->eta(),genPart->phi())
		));

		if( MuonHOAcceptance::inGeomAccept(muMatchEta,muMatchPhi) && MuonHOAcceptance::inNotDeadGeom(muMatchEta,muMatchPhi) ){
			histogramBuilder.fillEtaPhiGraph(muMatchEta,muMatchPhi,"tdmiInGaNotDead");
		}

		//The mu match position is inside HO acceptance
		if(MuonHOAcceptance::inGeomAccept(muMatchEta,muMatchPhi)
			&& MuonHOAcceptance::inNotDeadGeom(muMatchEta,muMatchPhi)
			&& !hoMatcher->isInChimney(muMatchEta,muMatchPhi)){

			histogramBuilder.fillCountHistogram("tdmiInGA");
			histogramBuilder.fillEtaPhiGraph(muMatchEta,muMatchPhi,"tdmiInGA");

			const HORecHit* matchedRecHit = hoMatcher->matchByEMaxDeltaR(muMatch->trkGlobPosAtHO.eta(),muMatch->trkGlobPosAtHO.phi());
			//Found the Rec Hit with largest E
			if(matchedRecHit){
				double ho_eta = caloGeo->getPosition(matchedRecHit->id()).eta();
				double ho_phi = caloGeo->getPosition(matchedRecHit->id()).phi();
				histogramBuilder.fillDeltaEtaDeltaPhiHistograms(
						muMatch->trkGlobPosAtHO.eta(),
						ho_eta,
						muMatch->trkGlobPosAtHO.phi(),
						ho_phi,
						"tdmiHoMatch"
				);
				//Energy is above threshold
				if(matchedRecHit->energy() > threshold){
					histogramBuilder.fillDeltaEtaDeltaPhiHistograms(
							muMatch->trkGlobPosAtHO.eta(),
							ho_eta,
							muMatch->trkGlobPosAtHO.phi(),
							ho_phi,
							"tdmiHoAboveThr"
					);
					//TDMI has energy entry > 0
					if(muMatch->hoCrossedEnergy() > 0 ){
						histogramBuilder.fillDeltaEtaDeltaPhiHistograms(
								muMatch->trkGlobPosAtHO.eta(),
								ho_eta,
								muMatch->trkGlobPosAtHO.phi(),
								ho_phi,
								"tdmiHoAboveThrGt0"
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
								"tdmiHoAboveThrEq0"
						);
						histogramBuilder.fillEtaPhiGraph(
								muMatch->trkGlobPosAtHO.eta(),
								muMatch->trkGlobPosAtHO.phi(),
								"tdmiHoAboveThrEq0"
						);
					}
				}
			} else{
				/**
				 * There could not be found a rec hit by delta R matching
				 */
				histogramBuilder.fillCountHistogram("tdmiMatchHoFail");
				histogramBuilder.fillEtaPhiGraph(muMatchEta,muMatchPhi,"tdmiMatchHoFail");
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
						(MuonHOAcceptance::inGeomAccept(it->eta(),it->phi() && !hoMatcher->isInChimney(it->eta(),it->phi()))),
						MuonHOAcceptance::inNotDeadGeom(it->eta(),it->phi()),
						MuonHOAcceptance::inSiPMGeom(it->eta(),it->phi())
				)
		);
	}

	hoRecHitVector->clear();
	for( auto it = hoRecoHits->begin(); it != hoRecoHits->end(); it++ ){
		histogramBuilder.fillMultiplicityHistogram(hoMatcher->countHoDigisByDetId(it->detid()),"hoDigiMatchesPerDetId");
		short* adcSamples = new short[10];
		const HODataFrame* dataFrame = hoMatcher->findHoDigiById(it->detid());
		for(int i = 0; i < std::min(10,dataFrame->size()); i++){
			adcSamples[i] = dataFrame->sample(i).adc();
		}
		hoRecHitVector->push_back(
				HoRecHitData(
						caloGeo->getPosition(it->id()).eta(),
						caloGeo->getPosition(it->id()).phi(),
						it->energy(),
						it->time(),
						adcSamples
				)
		);
		//Take care of memory! Adc samples are copied in the struct's constructor
		delete[] adcSamples;
	}

	dataTree->Fill();


}


// ------------ method called once each job just before starting event loop  ------------
void 
DataTreeFiller::beginJob()
{
}

// ------------ method called once each job just after ending the event loop  ------------
void 
DataTreeFiller::endJob() 
{
}

// ------------ method called when starting to processes a run  ------------
/*
void 
DataTreeFiller::beginRun(edm::Run const&, edm::EventSetup const&)
{
}
*/

// ------------ method called when ending the processing of a run  ------------
/*
void 
DataTreeFiller::endRun(edm::Run const&, edm::EventSetup const&)
{
}
*/

// ------------ method called when starting to processes a luminosity block  ------------
/*
void 
DataTreeFiller::beginLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&)
{
}
*/

// ------------ method called when ending the processing of a luminosity block  ------------
/*
void 
DataTreeFiller::endLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&)
{
}
*/

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void
DataTreeFiller::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  //The following says we do not know what parameters are allowed so do no validation
  // Please change this to state exactly what you do use, even if it is no parameters
  edm::ParameterSetDescription desc;
  desc.setUnknown();
  descriptions.addDefault(desc);
}

//define this as a plug-in
DEFINE_FWK_MODULE(DataTreeFiller);
