// -*- C++ -*-
//
// Package:    tester
// Class:      tester
// 
/**
 *
	Author: Andreas Kuensken < kuensken@physik.rwth-aachen.de >


 Description: [one line class summary]

 Implementation:
     [Notes on implementation]
 */



// system include files
#include <memory>

// user include files

#include "../interface/FilterPlugin.h"

#include "CalibFormats/HcalObjects/interface/HcalDbRecord.h"

#include "CalibFormats/HcalObjects/interface/HcalDbService.h"
#include "DataFormats/GeometryVector/interface/GlobalTag.h"

#include "DataFormats/HcalDigi/interface/HcalDigiCollections.h"

#include "HoMuonTrigger/hoTriggerAnalyzer/interface/HistogramBuilder.h"
#include "RecoLocalCalo/HcalRecAlgos/interface/HcalSeverityLevelComputer.h"
#include "RecoLocalCalo/HcalRecAlgos/interface/HcalSeverityLevelComputerRcd.h"
#include "RecoLocalCalo/HcalRecAlgos/interface/HcalSimpleRecAlgo.h"
#include "TCanvas.h"

#include "TMultiGraph.h"
#include <cmath>
#include <cstdlib>
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
#include <DataFormats/HcalDetId/interface/HcalSubdetector.h>
#include <DataFormats/HcalRecHit/interface/HcalRecHitCollections.h>
#include <DataFormats/HcalRecHit/interface/HORecHit.h>
#include <DataFormats/HepMCCandidate/interface/GenParticle.h>
#include <DataFormats/L1Trigger/interface/L1MuonParticle.h>
#include <DataFormats/Math/interface/deltaR.h>
#include <DataFormats/Provenance/interface/EventID.h>
#include <DataFormats/TrajectorySeed/interface/PropagationDirection.h>
#include <fstream>
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

#include <iostream>
#include <iterator>

#include <list>
#include <MagneticField/Records/interface/IdealMagneticFieldRecord.h>
#include <map>
#include <Math/GenVector/DisplacementVector3D.h>
#include <RecoMuon/MuonIdentification/interface/MuonHOAcceptance.h>

#include <SimDataFormats/CaloHit/interface/PCaloHit.h>
#include <SimDataFormats/GeneratorProducts/interface/GenEventInfoProduct.h>
#include <string>
#include <TrackingTools/TrackAssociator/interface/TrackAssociatorParameters.h>
#include <TrackingTools/TrackAssociator/interface/TrackDetMatchInfo.h>
#include <TrackingTools/TrajectoryState/interface/FreeTrajectoryState.h>
#include <TrackPropagation/SteppingHelixPropagator/interface/SteppingHelixPropagator.h>
#include <TROOT.h>
#include <TTree.h>
#include <utility>
#include <vector>


//
// class declaration
//

class HoDigiAnalyzer : public edm::EDAnalyzer {
public:
	explicit HoDigiAnalyzer(const edm::ParameterSet&);
	~HoDigiAnalyzer();


private:
	virtual void beginJob() override;
	virtual void analyze(const edm::Event&, const edm::EventSetup&) override;
	virtual void endJob() override;
	virtual void beginRun(edm::Run const&, edm::EventSetup const&) override;
	virtual void endRun(edm::Run const&, edm::EventSetup const&) override;

	float timeshift_ns_hbheho(float wpksamp);

	edm::Service<TFileService> _fileService;

	HistogramBuilder histogramBuilder;
	HoMatcher* hoMatcher;

	edm::ESHandle<CaloGeometry> caloGeo;

	edm::Handle<HODigiCollection> hoDigis;
	/**
	 * ADC Threshold for 4 TS HO Digi
	 */
	int ADC_THR;
	/**
	 * Maximum delta R to be used for matching
	 */
	float deltaR_Max;

	/**
	 * Prefix for any cout
	 */
	const std::string coutPrefix = "[HoDigiAnalyzer] ";

};

//
// constants, enums and typedefs
//

//
// static data member definitions
//

//
// constructors and destructor
//
HoDigiAnalyzer::HoDigiAnalyzer(const edm::ParameterSet& iConfig){
	deltaR_Max = iConfig.getParameter<double>("maxDeltaR");
	ADC_THR = iConfig.getParameter<int>("hoAdcThreshold");

}


HoDigiAnalyzer::~HoDigiAnalyzer()
{
}

// ------------ method called when starting to processes a run  ------------

void
HoDigiAnalyzer::beginRun(const edm::Run & iRun, const edm::EventSetup& evSetup)
{



}


// ------------ method called when ending the processing of a run  ------------

void
HoDigiAnalyzer::endRun(const edm::Run& iRun, const edm::EventSetup& evSetup)
{

}

//
// member functions
//

// ------------ method called for each event  ------------
void
HoDigiAnalyzer::analyze(const edm::Event& iEvent, 
		const edm::EventSetup& iSetup)
{
	iSetup.get<CaloGeometryRecord>().get(caloGeo);
	hoMatcher = new HoMatcher(*caloGeo);

}
// timeshift implementation
// Copied from HcalSimpleRecAlgo
static const float wpksamp0_hbheho = 0.5;
static const int   num_bins_hbheho = 61;

/*
 * My interpretation of the commented columns:
 * The first is the weighted bin position.
 * The second is the range for the given value.
 */
static const float actual_ns_hbheho[num_bins_hbheho] = {
-5.44000, // 0.500, 0.000-0.017
-4.84250, // 0.517, 0.017-0.033
-4.26500, // 0.533, 0.033-0.050
-3.71000, // 0.550, 0.050-0.067
-3.18000, // 0.567, 0.067-0.083
-2.66250, // 0.583, 0.083-0.100
-2.17250, // 0.600, 0.100-0.117
-1.69000, // 0.617, 0.117-0.133
-1.23000, // 0.633, 0.133-0.150
-0.78000, // 0.650, 0.150-0.167
-0.34250, // 0.667, 0.167-0.183
 0.08250, // 0.683, 0.183-0.200
 0.50250, // 0.700, 0.200-0.217
 0.90500, // 0.717, 0.217-0.233
 1.30500, // 0.733, 0.233-0.250
 1.69500, // 0.750, 0.250-0.267
 2.07750, // 0.767, 0.267-0.283
 2.45750, // 0.783, 0.283-0.300
 2.82500, // 0.800, 0.300-0.317
 3.19250, // 0.817, 0.317-0.333
 3.55750, // 0.833, 0.333-0.350
 3.91750, // 0.850, 0.350-0.367
 4.27500, // 0.867, 0.367-0.383
 4.63000, // 0.883, 0.383-0.400
 4.98500, // 0.900, 0.400-0.417
 5.33750, // 0.917, 0.417-0.433
 5.69500, // 0.933, 0.433-0.450
 6.05000, // 0.950, 0.450-0.467
 6.40500, // 0.967, 0.467-0.483
 6.77000, // 0.983, 0.483-0.500
 7.13500, // 1.000, 0.500-0.517
 7.50000, // 1.017, 0.517-0.533
 7.88250, // 1.033, 0.533-0.550
 8.26500, // 1.050, 0.550-0.567
 8.66000, // 1.067, 0.567-0.583
 9.07000, // 1.083, 0.583-0.600
 9.48250, // 1.100, 0.600-0.617
 9.92750, // 1.117, 0.617-0.633
10.37750, // 1.133, 0.633-0.650
10.87500, // 1.150, 0.650-0.667
11.38000, // 1.167, 0.667-0.683
11.95250, // 1.183, 0.683-0.700
12.55000, // 1.200, 0.700-0.717
13.22750, // 1.217, 0.717-0.733
13.98500, // 1.233, 0.733-0.750
14.81500, // 1.250, 0.750-0.767
15.71500, // 1.267, 0.767-0.783
16.63750, // 1.283, 0.783-0.800
17.53750, // 1.300, 0.800-0.817
18.38500, // 1.317, 0.817-0.833
19.16500, // 1.333, 0.833-0.850
19.89750, // 1.350, 0.850-0.867
20.59250, // 1.367, 0.867-0.883
21.24250, // 1.383, 0.883-0.900
21.85250, // 1.400, 0.900-0.917
22.44500, // 1.417, 0.917-0.933
22.99500, // 1.433, 0.933-0.950
23.53250, // 1.450, 0.950-0.967
24.03750, // 1.467, 0.967-0.983
24.53250, // 1.483, 0.983-1.000
25.00000  // 1.500, 1.000-1.017 - keep for interpolation
};

// Copied from HcalSimpleRecAlgo
float HoDigiAnalyzer::timeshift_ns_hbheho(float wpksamp) {
  float flx = (num_bins_hbheho-1)*(wpksamp - wpksamp0_hbheho);
  int index = (int)flx;
  float yval;

  if      (index <    0)               return actual_ns_hbheho[0];
  else if (index >= num_bins_hbheho-1) return actual_ns_hbheho[num_bins_hbheho-1];

  // else interpolate:
  float y1 = actual_ns_hbheho[index];
  float y2 = actual_ns_hbheho[index+1];

  yval = y1 + (y2-y1)*(flx-(float)index);

  return yval;
}

// ------------ method called once each job just before starting event loop  ------------
void 
HoDigiAnalyzer::beginJob()
{
}

// ------------ method called once each job just after ending the event loop  ------------
void 
HoDigiAnalyzer::endJob() 
{
}

//define this as a plug-in
DEFINE_FWK_MODULE(HoDigiAnalyzer);
