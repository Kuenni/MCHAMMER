#ifndef __PIONANALYZER_H__
#define __PIONANALYZER_H__
//
// Class:PionAnalyzer
// 
/*
 * Pion Analyzer
 *
 */


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
#include "DataFormats/HcalRecHit/interface/HORecHit.h"

#include "HoMuonTrigger/hoTriggerAnalyzer/interface/HistogramBuilder.h"

#include "DataFormats/HLTReco/interface/TriggerEvent.h"
#include "FWCore/Common/interface/TriggerNames.h"
#include "DataFormats/HLTReco/interface/TriggerObject.h"
#include "DataFormats/Common/interface/TriggerResults.h"
#include "DataFormats/L1Trigger/interface/L1MuonParticle.h"
#include "DataFormats/L1Trigger/interface/L1MuonParticleFwd.h"
#include "DataFormats/HepMCCandidate/interface/GenParticle.h"

#include <vector>
#include <iostream>
#include <map>
#include <list>

using namespace::std;

static const float threshold = 0.2;
static const float deltaR_Max = 0.3;

//
// class declaration
//

class PionAnalyzer : public edm::EDAnalyzer {
public:
  explicit PionAnalyzer(const edm::ParameterSet&);
  ~PionAnalyzer();
  
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
  
  const reco::GenParticle* getBestGenMatch(float,float);

  edm::Service<TFileService> _fileService;

  edm::InputTag _genInput;
  edm::InputTag _l1MuonInput;
  edm::InputTag _horecoInput;
  edm::InputTag _l1MuonGenMatchInput;
  edm::InputTag _hltSumAODInput;

  edm::Handle<reco::GenParticleCollection> truthParticles;

  HistogramBuilder histogramBuilder;

  
  L1GtUtils m_l1GtUtils;
  string singleMu3TrigName;
  string doubleMu0TrigName;
  string doubleMu5TrigName;
  bool trigDecision;
  bool singleMu3Trig,doubleMu0Trig;

  //toFigureOutL1VariableBinning
  std::list<float> listL1MuonPt;

  bool processTriggerDecision(string algorithmName,const edm::Event& );


  //virtual void beginLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&) override;
  //virtual void endLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&) override;

      // ----------member data ---------------------------
};

#endif
