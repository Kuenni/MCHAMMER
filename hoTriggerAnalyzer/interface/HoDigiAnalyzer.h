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
};


#endif /* HOTRIGGERANALYZER_INTERFACE_HODIGIANALYZER_H_ */
