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
#include <DataFormats/HepMCCandidate/interface/GenParticleFwd.h>
#include <DataFormats/HLTReco/interface/TriggerObject.h>
#include <DataFormats/L1Trigger/interface/L1MuonParticleFwd.h>
#include <FWCore/Framework/interface/EDAnalyzer.h>
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include <FWCore/ParameterSet/interface/ConfigurationDescriptions.h>
#include <FWCore/ServiceRegistry/interface/Service.h>
#include <FWCore/Utilities/interface/InputTag.h>
#include <L1Trigger/GlobalTriggerAnalyzer/interface/L1GtUtils.h>
#include <TrackingTools/TrackAssociator/interface/TrackAssociatorParameters.h>
#include <TrackingTools/TrackAssociator/interface/TrackDetectorAssociator.h>
#include <list>
#include <map>
#include <string>
#include <vector>

#include "HistogramBuilder.h"

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
  

private:
  virtual void beginJob() override;
  virtual void analyze(const edm::Event&, 
		       const edm::EventSetup&) override;
  virtual void endJob() override;
  virtual void beginRun (const edm::Run& iRun, 
			 const edm::EventSetup& evSetup);
  virtual void endRun(const edm::Run& iRun, 
		      const edm::EventSetup& evSetup);
  
  void defineTriggersOfInterest();

  const reco::GenParticle* getBestGenMatch(float,float);
  const l1extra::L1MuonParticle* getBestL1MuonMatch(float,float);

  const l1extra::L1MuonParticle* getMatchedL1Object(trigger::TriggerObject,edm::Handle<l1extra::L1MuonParticleCollection>);
  bool hasL1Match(trigger::TriggerObject,edm::Handle<l1extra::L1MuonParticleCollection>);

  bool processTriggerDecision(string algorithmName,const edm::Event& );

  edm::Service<TFileService> _fileService;

  edm::InputTag _genInput;
  edm::InputTag _l1MuonInput;
  edm::InputTag _horecoInput;
  edm::InputTag _l1MuonGenMatchInput;
  edm::InputTag _hltSumAODInput;

  edm::Handle<reco::GenParticleCollection> truthParticles;
  edm::Handle<l1extra::L1MuonParticleCollection> l1Muons;

  HistogramBuilder histogramBuilder;

//  TrackDetectorAssociator assoc;
//  TrackAssociatorParameters assocParams;

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
  string singleMu3TrigName;
  string doubleMu0TrigName;
  string doubleMu5TrigName;
  bool trigDecision;
  bool singleMu3Trig,doubleMu0Trig;
  bool debug;

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

  //virtual void beginLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&) override;
  //virtual void endLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&) override;

      // ----------member data ---------------------------
};

#endif
