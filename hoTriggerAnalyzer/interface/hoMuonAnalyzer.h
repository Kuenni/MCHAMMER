#ifndef __HOMUON_HOMUONANALYZER_H__
#define __HOMUON_HOMUONANALYZER_H__
//
// Class:hoMuonAnalyzer
// 
/*
 Description: Currently the header file for the entire HOMuon Trigger Analysis

 Implementation:
     [Notes on implementation]
 */
//
// Original Author:  Christopher Anelli  
//         Created:  Fri, 16 May 2014 04:20:05 GMT


// system include files
#include <CommonTools/UtilAlgos/interface/TFileService.h>
#include <DataFormats/Common/interface/Handle.h>
#include <DataFormats/HcalRecHit/interface/HcalRecHitCollections.h>
#include <DataFormats/HepMCCandidate/interface/GenParticleFwd.h>
#include <DataFormats/HLTReco/interface/TriggerObject.h>
#include <DataFormats/L1Trigger/interface/L1MuonParticleFwd.h>
#include <DataFormats/MuonReco/interface/Muon.h>
#include <DataFormats/MuonReco/interface/MuonFwd.h>
#include "DataFormats/VertexReco/interface/Vertex.h"
#include "DataFormats/VertexReco/interface/VertexFwd.h"
#include <FWCore/Framework/interface/EDAnalyzer.h>
#include <FWCore/ParameterSet/interface/ConfigurationDescriptions.h>
#include <FWCore/ServiceRegistry/interface/Service.h>
#include <FWCore/Utilities/interface/InputTag.h>
#include <L1Trigger/GlobalTriggerAnalyzer/interface/L1GtUtils.h>
#include <TrackingTools/TrackAssociator/interface/TrackAssociatorParameters.h>
#include <TrackingTools/TrackAssociator/interface/TrackDetectorAssociator.h>
#include <TrackingTools/TrackAssociator/plugins/HODetIdAssociator.h>

#include <DataFormats/PatCandidates/interface/Muon.h>
#include <DataFormats/L1GlobalMuonTrigger/interface/L1MuRegionalCand.h>
#include <DataFormats/L1GlobalMuonTrigger/interface/L1MuGMTReadoutCollection.h>

#include <list>
#include <map>
#include <string>
#include <vector>

#include "GenMuonData.h"
#include "HistogramBuilder.h"
#include "HoRecHitData.h"
#include "L1MuonData.h"

#include "../interface/HoMatcher.h"
#include "FWCore/Framework/interface/EventSetup.h"

#include "DataFormats/DetId/interface/DetId.h"

#include "DataFormats/HcalDigi/interface/HODataFrame.h"

#include "DataFormats/HcalDigi/interface/HcalDigiCollections.h"

#include "../interface/CommonFunctionsHandler.h"
using namespace::std;
//
// class declaration
//

class hoMuonAnalyzer : public edm::EDAnalyzer {
public:
	explicit hoMuonAnalyzer(const edm::ParameterSet&);
	~hoMuonAnalyzer();

	static void fillDescriptions(edm::ConfigurationDescriptions&
			descriptions);

	/**
	 * Offset for the L1 Phi information
	 * (Introduced as suggested by Luigi Guiducci)
	 */
	static const float L1PHI_OFFSET;

private:

	virtual void beginJob() override;
	virtual void analyze(const edm::Event&, const edm::EventSetup&) override;
	virtual void endJob() override;
	virtual void beginRun (const edm::Run& iRun, const edm::EventSetup& evSetup);
	virtual void endRun(const edm::Run& iRun, const edm::EventSetup& evSetup);

	void defineTriggersOfInterest();
	void printChannelQualities(const edm::EventSetup & iEvent);
	void analyzeEnergyDeposit(const edm::Event& iEvent,const edm::EventSetup& iSetup);
	void analyzeNoSingleMuEventsL1Loop(const edm::Event& iEvent,const edm::EventSetup& iSetup);
	void analyzeNoSingleMuEventsGenLoop(const edm::Event& iEvent,const edm::EventSetup& iSetup);
	void analyzeWithGenLoop(const edm::Event& iEvent,const edm::EventSetup& iSetup);
	void analyzeL1Resolution();
	void fillL1ResolutionPlots(const l1extra::L1MuonParticle* l1Part, const pat::Muon* patMuon,std::string label);
	void analyzeL1Sources();
	void analyzeHoTriggerPrimitives();
	void analyzeTimingSupport();
	void fillEfficiencyHistograms(double ptMeasured,double ptReal,std::string key);
	void fillTimingHistograms(const l1extra::L1MuonParticle* l1Muon,const HORecHit* hoRecHit, bool isTight, std::string extraId  = "");
	void fillHoGeomAcceptanceGraph(reco::GenParticle genParticle);
	void fillAverageEnergyAroundL1Direction(const l1extra::L1MuonParticle*,std::string);
	void fillGridMatchingHistograms(bool passed, int grid, double pt, double time, std::string key, double eta, double phi);
	void fillGridMatchingQualityCodes(const l1extra::L1MuonParticle* l1muon, float pt, std::string key);
	void calculateGridMatchingEfficiency(const l1extra::L1MuonParticle* l1muon, float pt, std::string key);
	void calculateGridMatchingEfficiency(double eta, double phi, float pt, std::string key);
	void makeHoRecHitThresholdScan();

	void analyzeGridMatching();

	void processGenInformation(const edm::Event& iEvent,const edm::EventSetup& iSetup);
	void processRecoInformation(const edm::Event& iEvent,const edm::EventSetup& iSetup);

	void fillTriggerRatesForQualityCodes();

	void recoControlPlots();

	const L1MuRegionalCand* findBestCandMatch(const l1extra::L1MuonParticle* l1Muon);
	const reco::GenParticle* getBestGenMatch(float,float);
	const pat::Muon* getBestPatMatch(float eta, float phi);
	const l1extra::L1MuonParticle* getMatchedL1Object(trigger::TriggerObject,edm::Handle<l1extra::L1MuonParticleCollection>);
	const reco::Vertex getPrimaryVertex();
	const reco::Vertex getArtificialPrimaryVertex();

	bool processTriggerDecision(string algorithmName,const edm::Event& );
	bool isInTimeWindow(double time){
		return fabs(time) <= 12.5;
	}

	TrackDetMatchInfo* getTrackDetMatchInfo(reco::GenParticle,const edm::Event& iEvent,const edm::EventSetup& iSetup);

	edm::Service<TFileService> _fileService;

	edm::InputTag _genInput;
	edm::InputTag _l1MuonInput;
	edm::InputTag _horecoInput;
	edm::InputTag _l1MuonGenMatchInput;
	edm::InputTag _hltSumAODInput;

	edm::Handle<reco::BeamSpot> recoBeamSpotHandle;
	edm::Handle<reco::GenParticleCollection> truthParticles;
	edm::Handle<l1extra::L1MuonParticleCollection> l1Muons;
	edm::Handle<HORecHitCollection> hoRecoHits;
	edm::Handle<HOTrigPrimDigiCollection> hoTPDigis;
	edm::Handle<reco::GenParticleMatch> l1MuonGenMatches;
	edm::Handle<edm::View<l1extra::L1MuonParticle> > l1MuonView;
	edm::Handle<reco::MuonCollection> recoMuons;
	edm::Handle<std::vector<pat::Muon>> patMuons;
	edm::Handle<reco::VertexCollection> vertexColl;
	edm::Handle<L1MuGMTReadoutCollection> pCollection;
	edm::Handle<std::vector<L1MuRegionalCand>> dtRegionalCands;

	edm::ESHandle<CaloGeometry> caloGeo;
	edm::ESHandle<MagneticField> theMagField;

	HistogramBuilder histogramBuilder;

	TrackDetectorAssociator assoc;
	TrackAssociatorParameters assocParams;

	HoMatcher* hoMatcher;
	CommonFunctionsHandler* functionsHandler;

	/*
	 * Maps of selected hlt triggers to get the trigger decisions,
	 * and hlt filters to get the trigger objects.
	 */

	std::map<std::string, std::string> hltNamesOfInterest;
	std::map<std::string, edm::InputTag> hltFiltersOfInterest;
	std::vector<trigger::TriggerObject> hltTriggerObjects;
	std::map<std::string, std::vector<trigger::TriggerObject> > hltTriggerObjectsOfInterest;

	// I would prefer to run without an InputTag, the L1GtUtility should be
	// able to find it automatically from the Providence information.

	//edm::InputTag m_l1GtTmLInputTag;

	L1GtUtils m_l1GtUtils;
	string singleMuOpenTrigName;
	string singleMu3TrigName;
	string singleMu7TrigName;
	string singleMu10TrigName;
	string doubleMu0TrigName;
	string doubleMu5TrigName;
	bool trigDecision;
	bool singleMu3Trig,singleMu7Trig,singleMu10Trig,singleMuOpenTrig,doubleMu0Trig;
	bool debug;
	bool firstRun;
	bool isData;
	bool useArtificialPrimaryVertex;


	/**
	 * Maximum Eta value that is allowed for muons
	 */
	static const float MAX_ETA;

	/**
	 * Energy threshold for HO rec hits
	 */
	float threshold;

	/**
	 * Maximum delta R to be used for matching
	 */
	float deltaR_Max;

	/**
	 * max delta R for matching a L1Muon object to a gen particle
	 */
	float deltaR_L1MuonMatching;

	//toFigureOutL1VariableBinning
	std::list<float> listL1MuonPt;

	std::string coutPrefix;

	//virtual void beginLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&) override;
	//virtual void endLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&) override;

	// ----------member data ---------------------------
};

#endif
