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

#include "../interface/HoDigiAnalyzer.h"

//init static float
const float HoDigiAnalyzer::wpksamp0_hbheho = 0.5;

//
// constructors and destructor
//
HoDigiAnalyzer::HoDigiAnalyzer(const edm::ParameterSet& iConfig){
	deltaR_Max = iConfig.getParameter<double>("maxDeltaR");
	ADC_THR = iConfig.getParameter<int>("hoAdcThreshold");
	hoDigiInput = iConfig.getParameter<edm::InputTag>("hoDigiSrc");
	functionsHandler =  new CommonFunctionsHandler(iConfig);
	hoMatcher = new HoMatcher(iConfig);
}


HoDigiAnalyzer::~HoDigiAnalyzer()
{
	delete functionsHandler;
	delete hoMatcher;
	hoMatcher = 0;
	functionsHandler = 0;
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
	iEvent.getByLabel( hoDigiInput, hoDigis);

	//Do this at the beginning to get the correct collections for the event
	functionsHandler->getEvent(iEvent);
	hoMatcher->getEvent(iEvent,iSetup);

	//Call the analyzer functions
	analyzeHoDigiTiming(iEvent);
}

/**
 * The function contains the code that is used for studying the ho digi
 * timing. The DIGI studies are more suited to assess the usability of HO
 * than the RECO information
 *
 */
void HoDigiAnalyzer::analyzeHoDigiTiming(const edm::Event& iEvent){
	std::map<HcalDetId,int> idCounterMap;

	if(!hoDigis.isValid()) std::cout << "No HO digis collection found" << std::endl;
	auto dataFrame = hoDigis->begin();

	//Loop over all ho digis
	for(; dataFrame != hoDigis->end() ; ++dataFrame){
		double hitTime = calculateHitTimeFromDigi(&*dataFrame);
		histogramBuilder.fillTimeHistogram(hitTime,"hoTimeFromDigi");
		idCounterMap[dataFrame->id()] += 1;
		if(isFrameAboveThr(&(*dataFrame))){
			double digiEta = caloGeo->getPosition(dataFrame->id()).eta();
			double digiPhi = caloGeo->getPosition(dataFrame->id()).phi();
			histogramBuilder.fillTimeHistogram(hitTime,"hoTimeFromDigiAboveThr");
			histogramBuilder.fillCorrelationGraph(digiEta,hitTime,"hoTimeFromDigiEta");
			histogramBuilder.fillCorrelationGraph(digiPhi,hitTime,"hoTimeFromDigiPhi");
			const HORecHit* recHit = hoMatcher->findHoRecHitById(dataFrame->id());
			if(recHit){
				histogramBuilder.fillCorrelationGraph(hitTime,recHit->time(),"hoTimeRecHitVsDigi");
				histogramBuilder.fillGraph2D(digiEta,digiPhi,recHit->time() - hitTime,"etaPhiDeltaHoTime");
			}
			const l1extra::L1MuonParticle* l1muon = functionsHandler->getBestL1MuonMatch(digiEta,digiPhi);
			if(l1muon)
				histogramBuilder.fillDeltaTimeHistogram(calculateHitTimeFromDigi(&*dataFrame),l1muon->bx(),"hoTimeFromDigi");
		}
		double adcSum = 0;
		int maxTSIdx = findMaximumTimeSlice(&*dataFrame);
		int maxAdcVal = 0;

		if(maxTSIdx != -1)
			maxAdcVal = dataFrame->sample(maxTSIdx).adc();

		for (int i = 0 ; i < dataFrame->size() ; i++){
			adcSum += dataFrame->sample(i).adc();
			histogramBuilder.fillCorrelationHistogram(i,dataFrame->sample(i).adc(),"adc samples");
		}
		//Fill histogram with maximum TS ID
		histogramBuilder.fillBxIdHistogram(maxTSIdx,"maxTimeSlice");
		histogramBuilder.fillCorrelationHistogram(maxTSIdx,maxAdcVal,"MaxTimeSliceVsAdc");
		histogramBuilder.fillMultiplicityHistogram(adcSum,"hoDigiAdcSum");
		histogramBuilder.fillMultiplicityHistogram(dataFrame->sample(4).adc(),"hoDigiAdcTS4");
		//get Data frame i eta and i phi to check the energy vs time only for a specific tile
		if( dataFrame->id().ieta() == 1 && dataFrame->id().iphi() == 1 ){
			//Fill correlation between ADC sum (charge) and calculated time
			histogramBuilder.fillCorrelationGraph(calculateHitTimeFromDigi(&*dataFrame),get4TsAdcSum(&*dataFrame,maxTSIdx),"digiTimeVs4TSSum");
		}
		if( maxTSIdx != -1 ){
			histogramBuilder.fillMultiplicityHistogram(get4TsAdcSum(&*dataFrame,maxTSIdx),"hoDigi4TsSum");
		}
	}//Loop over data frames
	//Fill a histogram with the number of occurences for the given Det ID
	for(auto iterator = idCounterMap.begin(); iterator != idCounterMap.end(); iterator++){
		histogramBuilder.fillCorrelationGraph(iterator->first.rawId(),iterator->second,"detIdInDigiCounter");
	}
}

/**
 * Calculate the 4 TS Sum for an HO data frame around the max adc Sample
 */
int HoDigiAnalyzer::get4TsAdcSum(const HODataFrame* dataFrame, int sliceMax){
	int adcSum = 0;
	//Define start for the loop. Do not go below 0 index
	int index = (sliceMax - 1) < 0 ? 0 : sliceMax - 1;
	//Run the loop until +2 TS or end of frame
	for( ; index <= std::min(sliceMax + 2,dataFrame->size() - 1) ; index++){
		adcSum += dataFrame->sample(index).adc();
	}
	return adcSum;
}

/**
 * Returns the time slice number with the maximum ADC value in an HO Data Frame
 */
int HoDigiAnalyzer::findMaximumTimeSlice(const HODataFrame* dataFrame){
	int maxSlice = -1;
	int adcMax = -1;
	for (int i = 0 ; i < dataFrame->size() ; i++){
		if(adcMax < dataFrame->sample(i).adc()){
			adcMax = dataFrame->sample(i).adc();
			maxSlice = i;
		}
	}
	return maxSlice;
}

/**
 * Test whether the data Frame is in the 4 TS ADC sum above a given threshold
 * TODO: Catch the case where slice max is >= N-Samples - 2
 */
bool HoDigiAnalyzer::isFrameAboveThr(const HODataFrame* dataFrame){
	int sliceMax = -1;
	double adcSum = -1;
	sliceMax = findMaximumTimeSlice(dataFrame);
	if(sliceMax != -1){
		if(sliceMax == 0){
			adcSum = dataFrame->sample(0).adc() + dataFrame->sample(1).adc() + dataFrame->sample(2).adc();
		} else {
			adcSum = dataFrame->sample(sliceMax - 1).adc() + dataFrame->sample(sliceMax).adc() + dataFrame->sample(sliceMax + 1).adc() + dataFrame->sample(sliceMax + 2).adc();
		}
	}
	return adcSum >= ADC_THR;
}

/**
 * Calculates the raw hit time for the digi using the amplitude weighted bin position
 * as described in the paper about hcal timing reconstruction CMS-IN 2008/011
 *
 * FIXME: Use the time slew correction
 */
double HoDigiAnalyzer::calculateHitTimeFromDigi(const HODataFrame* dataFrame){
	double hitTime = -1;
	int sliceMax = findMaximumTimeSlice(dataFrame);
	if( sliceMax != -1 ){
		int sliceM1 = 0;
		int sliceP1 = 0;
		int maxA	= dataFrame->sample(sliceMax).adc();

		if (sliceMax -1 >= 0){
			sliceM1 = dataFrame->sample(sliceMax - 1).adc();
		}
		if (sliceMax + 1 < dataFrame->size()){
			sliceP1 = dataFrame->sample(sliceMax + 1).adc();
		}
		//Calculate sum of weights
		float wpksamp = (sliceM1 + maxA + sliceP1);
		if (wpksamp!=0){
			//calculate weighted position of max, assuming maxA in slice 1
			wpksamp=(maxA + 2.0*sliceP1) / wpksamp;
		}
		//subtract the pre-samples and convert from time slice number to ns
		//Add time shift
		hitTime = (sliceMax - dataFrame->presamples())*25.0 + timeshift_ns_hbheho(wpksamp);
		return hitTime;
	} else {
		return -9999;
	}
}

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

/**
 * float array with the time shift values
 */
const float HoDigiAnalyzer::actual_ns_hbheho[] = {
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

//define this as a plug-in
DEFINE_FWK_MODULE(HoDigiAnalyzer);
