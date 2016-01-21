// -*- C++ -*-
//
// Package:    HoMuonTrigger/PatTriggerAnalyzer
// Class:      PatTriggerAnalyzer
//
/**\class PatTriggerAnalyzer PatTriggerAnalyzer.cc HoMuonTrigger/PatTriggerAnalyzer/plugins/PatTriggerAnalyzer.cc

 Description: [one line class summary]

 Implementation:
     [Notes on implementation]
*/
//
// Original Author:  Andreas Künsken
//         Created:  Mon, 11 Jan 2016 09:56:34 GMT
//
//


// system include files
#include <memory>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDAnalyzer.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "DataFormats/PatCandidates/interface/TriggerEvent.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"

#include "../interface/HoMatcher.h"
#include "HistogramBuilder.h"

//
// class declaration
//

class HoPatTriggerAnalyzer : public edm::EDAnalyzer {
   public:
      explicit HoPatTriggerAnalyzer(const edm::ParameterSet&);
      ~HoPatTriggerAnalyzer();

      static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);


   private:
      virtual void beginJob() override;
      virtual void analyze(const edm::Event&, const edm::EventSetup&) override;
      virtual void endJob() override;

      /// histogram management
      HistogramBuilder histogramBuilder;
      HoMatcher* hoMatcher;

      edm::EDGetTokenT< pat::TriggerEvent > triggerEventToken_;

      //virtual void beginRun(edm::Run const&, edm::EventSetup const&) override;
      //virtual void endRun(edm::Run const&, edm::EventSetup const&) override;
      //virtual void beginLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&) override;
      //virtual void endLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&) override;

      // ----------member data ---------------------------
};
