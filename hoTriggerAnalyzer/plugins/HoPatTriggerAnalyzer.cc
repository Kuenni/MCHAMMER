#include "../interface/HoPatTriggerAnalyzer.h"

#include <DataFormats/L1Trigger/interface/L1MuonParticleFwd.h>
#include "DataFormats/HLTReco/interface/TriggerTypeDefs.h" // gives access to the (release cycle dependent) trigger object codes
#include "DataFormats/PatCandidates/interface/TriggerEvent.h"
#include "PhysicsTools/PatUtils/interface/TriggerHelper.h"
#include "DataFormats/Common/interface/Handle.h"

//
// constants, enums and typedefs
//

//
// static data member definitions
//

//
// constructors and destructor
//
HoPatTriggerAnalyzer::HoPatTriggerAnalyzer(const edm::ParameterSet& iConfig)
{
   //now do what ever initialization is needed
//	tagPatTriggerEvent_ = iConfig.getParameter<edm::InputTag>("triggerEvent");
	triggerEventToken_ = consumes< pat::TriggerEvent >( iConfig.getParameter< edm::InputTag >( "triggerEvent" ) ) ;
	hoMatcher = new HoMatcher(iConfig);

}


HoPatTriggerAnalyzer::~HoPatTriggerAnalyzer()
{
 
   // do anything here that needs to be done at desctruction time
   // (e.g. close files, deallocate resources etc.)
	delete hoMatcher;
	hoMatcher = 0;
}


//
// member functions
//

// ------------ method called for each event  ------------
void
HoPatTriggerAnalyzer::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup)
{
   using namespace edm;
//   edm::InputTag trigEventTag("hltTriggerSummaryAOD","","HLT"); //make sure have correct process on MC
//   //data process=HLT, MC depends, Spring11 is REDIGI311X
//   edm::Handle<trigger::TriggerEvent> trigEvent;
//   iEvent.getByLabel(trigEventTag,trigEvent);
//
//   std::string filterName("hltSingleJet190Regional");
//
//   //it is important to specify the right HLT process for the filter, not doing this is a common bug
//   trigger::size_type filterIndex = trigEvent->filterIndex(edm::InputTag(filterName,"",trigEventTag.process()));
//   if(filterIndex<trigEvent->sizeFilters()){
//       const trigger::Keys& trigKeys = trigEvent->filterKeys(filterIndex);
//       const trigger::TriggerObjectCollection & trigObjColl(trigEvent->getObjects());
//       //now loop of the trigger objects passing filter
//       for(trigger::Keys::const_iterator keyIt=trigKeys.begin();keyIt!=trigKeys.end();++keyIt){
//         const trigger::TriggerObject& obj = trigObjColl[*keyIt];
//         //do what you want with the trigger objects, you have
//         //eta,phi,pt,mass,p,px,py,pz,et,energy accessors
//       }
//
//   }//end filter size check
   const std::string labelMatcher("myMatcher");
   pat::helper::TriggerMatchHelper triggerMatchHelper;
   edm::Handle< pat::TriggerEvent > triggerEvent;
   iEvent.getByToken( triggerEventToken_, triggerEvent );
   // uses trigger object code from the enum in DataFormats/HLTReco/interface/TriggerTypeDefs.h
   const pat::TriggerObjectRefVector triggerMuons( triggerEvent->objects( trigger::TriggerMuon/*L1Mu*/ ) );
   if (triggerMuons.empty()){
	   std::cout << "Trigger Ref Vector empty!" << std::endl;
   }
   for (auto triggerObjectIterator = triggerMuons.begin(); triggerObjectIterator != triggerMuons.end(); triggerObjectIterator++){
	   std::cout << "Algorithms in Object: " << std::endl;
	   pat::TriggerAlgorithmRefVector refVect = triggerEvent->acceptedAlgorithms(*triggerObjectIterator);
	   std::cout << "AlgoVectSize " << refVect.size() << std::endl;
	   for(auto innerIterator = refVect.begin(); innerIterator != refVect.end(); innerIterator++){
		   std::cout << (*innerIterator)->name().c_str() << std::endl;
	   }
	   triggerEvent->
   }
   std::cout << triggerMuons.size() << std::endl;
   for ( pat::TriggerObjectRefVector::const_iterator it = triggerMuons.begin(); it != triggerMuons.end(); ++it ) {
	   const pat::TriggerObjectRef objRef( *it );
	   if(!objRef.isAvailable()){
		   std::cout << "No Trigger Object ref for L1mu" << std::endl;
		   continue;
	   }
	   const reco::CandidateBaseRefVector candRefs( triggerMatchHelper.triggerMatchCandidates(objRef, labelMatcher, iEvent , *triggerEvent) );
	   //With resolve ambiguities there should be only one candidate at maximum.
	   //If there is no candidate at all, the loop should not start
	   if (candRefs.empty()){
		   std::cout << "Candidate Ref Vector empty!" << std::endl;
	   }
	   for ( reco::CandidateBaseRefVector::const_iterator ic = candRefs.begin(); ic !=candRefs.end(); ++ic ) {
		   const reco::CandidateBaseRef candRef( *ic );
		   if(!candRef.isAvailable()){
			   std::cout << "No cand ref " << std::endl;
			   continue;
		   }

//		   objRef->hasFilterId() <-- L��sst sich damit nach einem einfachen HLT object suchen
//		   const L1MuonParticleRef* l1Muon = objRef->origL1MuonRef();

		   // ask for trigger accept of HLT_Mu9; otherwise we don't even start
//		  0099   if(!(triggerEvent->path("HLT_IsoMu17_v5")->wasRun() && triggerEvent->path("HLT_IsoMu17_v5")->wasAccept())){
//		  0100     return;
//		  0101   }
		   const pat::TriggerAlgorithm * algo = triggerEvent->algorithm("L1SingleMuOpen");
		   //TODO: Brauche ich den doppelten Check? L1Algo && HLT-Path? Was kann ich mit dem L1Algo und dem Prescale noch anstellen?
		   if(algo != 0 ){
		   std::cout << "After Mask " << algo->decisionAfterMask() << std::endl;
		   std::cout << "Before Mask " << algo->decisionBeforeMask() << std::endl;
		   if(algo->decisionAfterMask()){

			   if(triggerEvent->path("HLT_L1SingleMuOpen")->wasRun() && triggerEvent->path("HLT_L1SingleMuOpen")->wasAccept()){
				   const l1extra::L1MuonParticleRef l1Muon = objRef->origL1MuonRef();
				   histogramBuilder.fillL1ResolutionHistogram(l1Muon->pt(), candRef->pt(), "HLT_L1SingleMuOpen");
				   const HORecHit* matchedRecHit = 0;
				   matchedRecHit = hoMatcher->matchByEMaxDeltaR(l1Muon->eta(),l1Muon->phi());
				   if(matchedRecHit){
					   histogramBuilder.fillL1ResolutionHistogram(l1Muon->pt(), candRef->pt(), "HLT_L1SingleMuOpen_Matched");
				   }
			   }
		   }
		   }
	   }
   }
}


// ------------ method called once each job just before starting event loop  ------------
void 
HoPatTriggerAnalyzer::beginJob()
{
}

// ------------ method called once each job just after ending the event loop  ------------
void 
HoPatTriggerAnalyzer::endJob() 
{
}

// ------------ method called when starting to processes a run  ------------
/*
void 
PatTriggerAnalyzer::beginRun(edm::Run const&, edm::EventSetup const&)
{
}
*/

// ------------ method called when ending the processing of a run  ------------
/*
void 
PatTriggerAnalyzer::endRun(edm::Run const&, edm::EventSetup const&)
{
}
*/

// ------------ method called when starting to processes a luminosity block  ------------
/*
void 
PatTriggerAnalyzer::beginLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&)
{
}
*/

// ------------ method called when ending the processing of a luminosity block  ------------
/*
void 
PatTriggerAnalyzer::endLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&)
{
}
*/

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void
HoPatTriggerAnalyzer::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  //The following says we do not know what parameters are allowed so do no validation
  // Please change this to state exactly what you do use, even if it is no parameters
  edm::ParameterSetDescription desc;
  desc.setUnknown();
  descriptions.addDefault(desc);
}

//define this as a plug-in
DEFINE_FWK_MODULE(HoPatTriggerAnalyzer);
