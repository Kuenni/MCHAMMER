/*
 * HoDigiAnalyzer.h
 *
 *  Created on: Jun 17, 2015
 *      Author: kuensken
 *      <kuensken@physik.rwth-aachen.de>
 */

#ifndef HOTRIGGERANALYZER_INTERFACE_HODIGIANALYZER_H_
#define HOTRIGGERANALYZER_INTERFACE_HODIGIANALYZER_H_


// system include files
#include <CommonTools/UtilAlgos/interface/TFileService.h>
#include <DataFormats/Common/interface/Handle.h>
#include <DataFormats/HepMCCandidate/interface/GenParticleFwd.h>
#include <DataFormats/HLTReco/interface/TriggerObject.h>
#include <DataFormats/L1Trigger/interface/L1MuonParticleFwd.h>
#include <DataFormats/MuonReco/interface/Muon.h>
#include <DataFormats/MuonReco/interface/MuonFwd.h>
#include <FWCore/Framework/interface/EDAnalyzer.h>
#include <FWCore/ParameterSet/interface/ConfigurationDescriptions.h>
#include <FWCore/ServiceRegistry/interface/Service.h>
#include <FWCore/Utilities/interface/InputTag.h>
#include <L1Trigger/GlobalTriggerAnalyzer/interface/L1GtUtils.h>
#include <TrackingTools/TrackAssociator/interface/TrackAssociatorParameters.h>
#include <TrackingTools/TrackAssociator/interface/TrackDetectorAssociator.h>
#include <TrackingTools/TrackAssociator/plugins/HODetIdAssociator.h>


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

	void analyzeHoDigiTiming(const edm::Event& iEvent);

	bool isFrameAboveThr(const HODataFrame* dataFrame);
	double calculateHitTimeFromDigi(const HODataFrame* dataFrame);
	float timeshift_ns_hbheho(float wpksamp);
	int findMaximumTimeSlice(const HODataFrame* dataFrame);
	int get4TsAdcSum(const HODataFrame* dataFrame, int sliceMax);

	edm::Service<TFileService> _fileService;

	HistogramBuilder histogramBuilder;
	HoMatcher* hoMatcher;
	CommonFunctionsHandler* functionsHandler;

	edm::ESHandle<CaloGeometry> caloGeo;

	edm::InputTag hoDigiInput;

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
	// timeshift implementation
	// Copied from HcalSimpleRecAlgo
	static const float wpksamp0_hbheho;
	static const int   num_bins_hbheho = 61;
	/*
	 * My interpretation of the commented columns:
	 * The first is the weighted bin position.
	 * The second is the range for the given value.
	 */
	static const float actual_ns_hbheho[];
};


#endif /* HOTRIGGERANALYZER_INTERFACE_HODIGIANALYZER_H_ */
