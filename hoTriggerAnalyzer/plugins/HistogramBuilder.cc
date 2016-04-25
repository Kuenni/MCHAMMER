#include "HoMuonTrigger/hoTriggerAnalyzer/interface/HistogramBuilder.h"

/*
 * The HistogramBuilder Class contains  
 * functions to build generic histograms of                           
 * different types.  The type of object (or a specific                          
 * selection cut) can be specified by the key.
 * All histograms are saved through the TFileService                            
 * Created by Christopher Anelli
 * On 6.15.2014
 *
 * Modified: Andreas Kuensken <kuensken@physik.rwth-aachen.de>
 */

#include "TH1F.h"
#include "TH2D.h"

#include "HoMuonTrigger/hoTriggerAnalyzer/interface/HoMatcher.h"
#include "HoMuonTrigger/hoTriggerAnalyzer/interface/FilterPlugin.h"

/**
 *
 * Fill a histogram with the difference of two vz values from the vertex position
 */
void HistogramBuilder::fillDeltaVzHistogam(float deltaVz, std::string key){
	TFileDirectory vertexDir = _fileService->mkdir( "vertex" );
	if(!_h1DeltaVz.count(key)){
		_h1DeltaVz[key] = vertexDir.make<TH1D>(Form("%s_DeltaVz",key.c_str()),
				Form("%s #Delta V_{z}",key.c_str()),
				1000, -10, 10);
	}
	_h1DeltaVz[key]->Fill(deltaVz);
}

/**
 * Fill a histogram with the vz values from the vertex position
 */
void HistogramBuilder::fillVzHistogram(float vz, std::string key){
	TFileDirectory vertexDir = _fileService->mkdir( "vertex" );
	if(!_h1Vz.count(key)){
		_h1Vz[key] = vertexDir.make<TH1D>(Form("%s_Vz",key.c_str()),
				Form("%s V_{z}",key.c_str()),
				1000, -10, 10);
	}
	_h1Vz[key]->Fill(vz);
}

/**
 * Fill a 2D histogram
 */
void HistogramBuilder::fillCorrelationHistogram(double x, double y, std::string key,TH2D* histogram){
	TFileDirectory correlationDir = _fileService->mkdir( "correlation" );
	if(!_h2Correlation.count(key)){
		_h2Correlation[key] = correlationDir.make<TH2D>(Form("%s_Correlation",key.c_str()),
				Form("%s Correlation;x;y",key.c_str()),
				500, 0,500,500,0,500);
		if(histogram){
			histogram->Copy(*_h2Correlation[key]);
			_h2Correlation[key]->SetDirectory(correlationDir.getBareDirectory());
		}
	}
	_h2Correlation[key]->Fill(x,y);
}

/**
 * Fill a 1D histogram
 */
void HistogramBuilder::fillHistogram(double x, std::string key,TH1D* histogram){
	TFileDirectory correlationDir = _fileService->mkdir( "histograms1D" );
	if(!_h1histograms.count(key)){
		_h1histograms[key] = correlationDir.make<TH1D>(Form("%s",key.c_str()),
				Form("%s",key.c_str()),
				101, -0.5,100.5);
		if(histogram){
			histogram->Copy(*_h1histograms[key]);
			_h1histograms[key]->SetDirectory(correlationDir.getBareDirectory());
		}
	}
	_h1histograms[key]->Fill(x);
}

void HistogramBuilder::fillEfficiency(bool passed, float pt, std::string key){
	TFileDirectory efficiencyDir = _fileService->mkdir("efficiency");
	if(!_effMap.count(key)){
		_effMap[key] = efficiencyDir.make<TEfficiency>(Form("%s_Efficiency",key.c_str()),
				Form("%s Efficiency",key.c_str()),
				502, -0.75, 250.25);
	}
	_effMap[key]->Fill(passed,pt);
}

void HistogramBuilder::fillHltIndexHistogram(int hltIndex, std::string key){
	TFileDirectory hltDir = _fileService->mkdir("hlt");
	if(!_h1HltIndex.count(key)){
		_h1HltIndex[key] = hltDir.make<TH1D>(Form("%s_hltIndex",key.c_str()),
				Form("%s HLT Index",key.c_str()),
				251, -0.5, 250.5);
	}
	_h1HltIndex[key]->Fill(hltIndex);
}

/*                                                                              
 *Counting Histograms                                                           
 *Fills the 1 bin.                                                              
 */
void HistogramBuilder::fillCountHistogram(std::string key){
	TFileDirectory countDir = _fileService->mkdir("count");
	if(!_h1Counter.count(key)){
		_h1Counter[key] = countDir.make<TH1F>(Form("%s_Count",key.c_str()),
				Form("%s Count",key.c_str()),
				3, -0.5, 2.5);
	}
	_h1Counter[key]->Fill(1);
}                                                                               

void HistogramBuilder::fillMultiplicityHistogram(int nEvents, std::string key){
	TFileDirectory dir = _fileService->mkdir("multiplicity");
	if(!_h1Multiplicity.count(key)){
		_h1Multiplicity[key] = dir.make<TH1D>(Form("%s_Multiplicity",key.c_str()),
				Form("%s Multiplicity",key.c_str()),
				3001, -0.5, 3000.5);
	}
	_h1Multiplicity[key]->Fill(nEvents);
}

void HistogramBuilder::fillPdgIdHistogram(int pdgId, std::string key){
	if(!_h1pdgId.count(key)){
		_h1pdgId[key] = _fileService->make<TH1D>(Form("%s_pdgId",key.c_str()),
				Form("%s PDG ID",key.c_str()),
				501, -250.5, 250.5);
	}
	_h1pdgId[key]->Fill(pdgId);
}

/*                                                                              
 *Trigger Histograms                                                            
 */
void HistogramBuilder::fillTrigHistograms(bool trigDecision,std::string key){   
	if(!_h1Trig.count(key)){
		_h1Trig[key] = _fileService->make<TH1F>(Form("%s_Trig",key.c_str()),
				Form("%s Trigger",key.c_str()),
				3, -0.5, 2.5);
	}
	_h1Trig[key]->Fill(trigDecision);
}      

/*
 * Trigger rate histograms
 */
void HistogramBuilder::fillTrigRateHistograms(float ptThreshold,std::string key){
	if(!_h1TrigRate.count(key)){
		_h1TrigRate[key] = _fileService->make<TH1D>(Form("%s_TrigRate",key.c_str()),
				Form("%s Trigger Pseudo Rate",key.c_str()),
				500, 0,500);
	}
	_h1TrigRate[key]->Fill(ptThreshold);

}

/**
 * Trig rate histogram with special x binning for L1 resolution
 */
void HistogramBuilder::fillTrigRateL1Histograms(float ptThreshold, std::string key){
	if(!_h1TrigRate.count(key)){
		float variableBinArray[] = {0,0.5,1,1.5,2,2.5,3,3.5,4,4.5,5,6,7,8,9,10,12,14,16,18,20,25,30,35,40,45,50,60,70,80,100,120,140,180};
		_h1TrigRate[key] = _fileService->make<TH1D>(Form("%s_TrigRate",key.c_str()),
				Form("%s Trigger Pseudo Rate",key.c_str()),
				33,variableBinArray);
	}
	_h1TrigRate[key]->Fill(ptThreshold);
}

/*                                                                              
 *Energy Histograms                                                             
 */
void HistogramBuilder::fillEnergyHistograms(float energy, std::string key){
	TFileDirectory energyDir = _fileService->mkdir("energy");
	if(!_h1Energy.count(key)){
		_h1Energy[key] = energyDir.make<TH1F>(Form("%s_Energy",key.c_str()),
				Form("%s Energy",key.c_str()),
				2100, -5.0, 100.0);
	}
	_h1Energy[key]->Fill(energy);
}

void HistogramBuilder::fillEnergyVsIEta(float energy, int iEta, std::string key){
	TFileDirectory energyDir = _fileService->mkdir("energy");
	TFileDirectory energySubDir = _fileService->mkdir("energy/perWheel");
	TString localKey;
	if(iEta >= -15 && iEta <= -11){
		localKey = Form("%s_Energy_%s",key.c_str(),"M2");
	} else if (iEta >= -10 && iEta <= -5){
		localKey = Form("%s_Energy_%s",key.c_str(),"M1");
	} else if(iEta >= -4 && iEta <= -1){
		localKey = Form("%s_Energy_%s",key.c_str(),"M0");
	} else if(iEta >= 1 && iEta <= 4){
		localKey = Form("%s_Energy_%s",key.c_str(),"P0");
	} else if(iEta >= 5 && iEta <= 10){
		localKey = Form("%s_Energy_%s",key.c_str(),"P1");
	} else if(iEta >= 11 && iEta <= 15){
		localKey = Form("%s_Energy_%s",key.c_str(),"P2");
	}
	if(!_h1Energy.count(localKey.Data())){
		_h1Energy[localKey.Data()] = energySubDir.make<TH1F>(localKey.Data(),
				localKey.Data(),
				2100, -5.0, 100.0);
	}
	_h1Energy[localKey.Data()]->Fill(energy);
	fillEnergyHistograms(energy,key);
}

/*                                                                              
 *Eta Phi Histograms                                                            
 */
void HistogramBuilder::fillEtaPhiHistograms(float eta, float phi, std::string key){
	TFileDirectory etaPhiDir = _fileService->mkdir("etaPhi");
	if(!_h1Eta.count(key)){
		_h1Eta[key] = etaPhiDir.make<TH1F>(Form("%s_Eta",key.c_str()),
				Form("%s Eta",key.c_str()),
				720, -3.132, 3.132);  //HO has 72 iphis and 30 ietas
	}
	_h1Eta[key]->Fill(eta);

	if(!_h1Phi.count(key)){
		_h1Phi[key] = etaPhiDir.make<TH1F>(Form("%s_Phi",key.c_str()),
				Form("%s Phi",key.c_str()),
				720, -3.132, 3.132);  //HO has 72 iphis and 30 ietas
	}
	_h1Phi[key]->Fill(phi);

	if(!_h2EtaPhiMap.count(key)){
		_h2EtaPhiMap[key] = etaPhiDir.make<TH2D>(Form("%s_EtaPhi",key.c_str()),
				Form("%s_EtaPhi",key.c_str()),
				720, -3.132, 3.132,
				720, -3.132, 3.132);
	}
	_h2EtaPhiMap[key]->Fill(eta, phi);
}

void HistogramBuilder::fillIEtaIPhiHistogram(int iEta, int iPhi, std::string key){
	TFileDirectory etaPhiDir = _fileService->mkdir("etaPhi");
	if(!_h2iEtaIPhiMap.count(key)){
		_h2iEtaIPhiMap[key] = etaPhiDir.make<TH2D>(Form("%s_iEtaIPhi",key.c_str()),Form("%s iEta iPhi",key.c_str())
				,33,-16.5,16.5,74,-0.5,73.5);
	}
	_h2iEtaIPhiMap[key]->Fill(iEta,iPhi);
}

/**
 * Delta Eta Delta Phi Histograms
 *  	eta1 -> l1
 * 		eta2 -> Ho
 * 		phi1 -> l1
 * 		phi2 -> Ho
 */
void HistogramBuilder::fillDeltaEtaDeltaPhiHistograms(float eta1, float eta2, 
		float phi1, float phi2,
		std::string key){
	TFileDirectory etaPhiDir = _fileService->mkdir("etaPhi");
	float deltaEta, deltaPhi;
	deltaEta = eta2 - eta1;
	deltaPhi = FilterPlugin::wrapCheck(phi1, phi2);

	//Delta Eta Histograms Fill
	if(!_h1DeltaEta.count(key)){
		_h1DeltaEta[key] =  etaPhiDir.make<TH1F>(Form("%s_DeltaEta",
				key.c_str()),
				Form("#Delta #Eta %s",
						key.c_str()),
						51, -2.2185, 2.2185);//510 times 0.087/10; 0 in center of a bin
	}
	_h1DeltaEta[key]->Fill(deltaEta);
	//Delta Eta Histograms Fill
	if(!_h1DeltaPhi.count(key)){
		_h1DeltaPhi[key] = etaPhiDir.make<TH1F>(Form("%s_DeltaPhi",
				key.c_str()),
				Form("%s #Delta #Phi",
						key.c_str()),
						73, -3.1755, 3.1755);//730 times 0.087/10; 0 in center of a bin
	}
	_h1DeltaPhi[key]->Fill(deltaPhi);

	//DeltaEta Delta Phi Histograms Fill
	if(!_h2DeltaEtaDeltaPhi.count(key)){
		_h2DeltaEtaDeltaPhi[key] = etaPhiDir.make<TH2D>(Form("%s_DeltaEtaDeltaPhi",key.c_str()),Form("%s #Delta#eta #Delta#Phi",key.c_str()),
				51, -2.2185, 2.2185, 	//eta
				73, -3.1755, 3.1755);	//phi
	}
	_h2DeltaEtaDeltaPhi[key]->Fill(deltaEta, deltaPhi);

} 

/**
 * Dedicated function for the average energy plots
 */
void HistogramBuilder::fillAverageEnergyHistograms(double eta1, double etaHo, double phi1, double phiHo, double energy, std::string key){
	TFileDirectory averageEnergyDir = _fileService->mkdir("averageEnergy");
	TFileDirectory subdir;
	int wheel = 9;
	/**
	 * Check the L1 direction but use the wheel boundaries from HO
	 */
	if(eta1 <= -0.868){	wheel = -2;	}
	else if (eta1 > -0.868 && eta1 <= -0.336){ wheel = -1;}
	else if (eta1 > -0.336 && eta1 < 0.336) {wheel = 0;}
	else if (eta1 >= 0.336 && eta1 < 0.868) {wheel = 1;}
	else if (eta1 >= 0.868) {wheel = 2;}
	switch (wheel) {
		case -2:
			subdir = averageEnergyDir.mkdir("wh2m");
			break;
		case -1:
			subdir = averageEnergyDir.mkdir("wh1m");
			break;
		case -0:
			subdir = averageEnergyDir.mkdir("wh0");
			break;
		case 1:
			subdir = averageEnergyDir.mkdir("wh1p");
			break;
		case 2:
			subdir = averageEnergyDir.mkdir("wh2p");
			break;
		default:
			break;
	}
	std::string histNameEnergy = Form("%s_wh%dSummedEnergy",key.c_str(),wheel);
	std::string histNameCounter = Form("%s_wh%dCounter",key.c_str(),wheel);
	std::string histNameAllEnergies = Form("%s_SummedEnergy",key.c_str());
	std::string histNameAllCounter = Form("%s_Counter",key.c_str());
	std::string histTitle = Form("Wheel %d;#Delta#Eta;#Delta#phi;E_{Rec} / GeV",wheel);
	std::string histAllTitle = Form("AverageEnergyHistogram;#Delta#eta;#Delta#phi");
	double deltaEta, deltaPhi;
	deltaEta = etaHo - eta1;
	deltaPhi = FilterPlugin::wrapCheck(phi1, phiHo);
	//Here I'am using the double resolution than what HO can do

	int nBinsPerHO = 4;
	double hoShiftForZeroCentered = 1/double(nBinsPerHO*2);
	int lateralSpreadForPlot = 10;
	int nTotalBins = 2*nBinsPerHO*lateralSpreadForPlot + 1;

	if(!_h2AverageEnergy.count(histNameEnergy)){
		_h2AverageEnergy[histNameEnergy] = subdir.make<TH2D>(histNameEnergy.c_str(),histTitle.c_str(),
				nTotalBins,-lateralSpreadForPlot*HoMatcher::HO_BIN - HoMatcher::HO_BIN/hoShiftForZeroCentered,
				lateralSpreadForPlot*HoMatcher::HO_BIN + HoMatcher::HO_BIN/hoShiftForZeroCentered,
				nTotalBins,-lateralSpreadForPlot*HoMatcher::HO_BIN - HoMatcher::HO_BIN/hoShiftForZeroCentered,
				lateralSpreadForPlot*HoMatcher::HO_BIN + HoMatcher::HO_BIN/hoShiftForZeroCentered);
	}
	if(!_h2AverageEnergy.count(histNameCounter)){
		_h2AverageEnergy[histNameCounter] = subdir.make<TH2D>(histNameCounter.c_str(),histTitle.c_str(),
				nTotalBins,-lateralSpreadForPlot*HoMatcher::HO_BIN - HoMatcher::HO_BIN/hoShiftForZeroCentered,
				lateralSpreadForPlot*HoMatcher::HO_BIN + HoMatcher::HO_BIN/hoShiftForZeroCentered,
				nTotalBins,-lateralSpreadForPlot*HoMatcher::HO_BIN - HoMatcher::HO_BIN/hoShiftForZeroCentered,
				lateralSpreadForPlot*HoMatcher::HO_BIN + HoMatcher::HO_BIN/hoShiftForZeroCentered);
	}
	_h2AverageEnergy[histNameEnergy]->Fill(deltaEta, deltaPhi, energy);
	_h2AverageEnergy[histNameCounter]->Fill(deltaEta, deltaPhi);

	//Also fill a histogram for all wheels together
	if(!_h2AverageEnergy.count(histNameAllEnergies)){
		_h2AverageEnergy[histNameAllEnergies] = averageEnergyDir.make<TH2D>(histNameAllEnergies.c_str(),(histAllTitle + ";E_{Rec} / GeV").c_str(),
				nTotalBins,-lateralSpreadForPlot*HoMatcher::HO_BIN - HoMatcher::HO_BIN/hoShiftForZeroCentered,
				lateralSpreadForPlot*HoMatcher::HO_BIN + HoMatcher::HO_BIN/hoShiftForZeroCentered,
				nTotalBins,-lateralSpreadForPlot*HoMatcher::HO_BIN - HoMatcher::HO_BIN/hoShiftForZeroCentered,
				lateralSpreadForPlot*HoMatcher::HO_BIN + HoMatcher::HO_BIN/hoShiftForZeroCentered);
	}
	if(!_h2AverageEnergy.count(histNameAllCounter)){
		_h2AverageEnergy[histNameAllCounter] = averageEnergyDir.make<TH2D>(histNameAllCounter.c_str(),(histAllTitle + ";# Entries").c_str(),
				nTotalBins,-lateralSpreadForPlot*HoMatcher::HO_BIN - HoMatcher::HO_BIN/hoShiftForZeroCentered,
				lateralSpreadForPlot*HoMatcher::HO_BIN + HoMatcher::HO_BIN/hoShiftForZeroCentered,
				nTotalBins,-lateralSpreadForPlot*HoMatcher::HO_BIN - HoMatcher::HO_BIN/hoShiftForZeroCentered,
				lateralSpreadForPlot*HoMatcher::HO_BIN + HoMatcher::HO_BIN/hoShiftForZeroCentered);
	}
	_h2AverageEnergy[histNameAllEnergies]->Fill(deltaEta, deltaPhi, energy);
	_h2AverageEnergy[histNameAllCounter]->Fill(deltaEta, deltaPhi);

	if(HoMatcher::getDeltaIphi(phi1,phiHo) == 1){
		fillEtaPhiGraph(eta1,phi1,"averageEnergyDeltaPhi1");
	}
}

/**
 * Fill a delta eta delta phi histogram bin by a given weight
 */
void HistogramBuilder::fillDeltaEtaDeltaPhiHistogramsWithWeights(double eta1, double eta2,
		double phi1, double phi2, double weight, std::string key){
	TFileDirectory etaPhiDir = _fileService->mkdir("deltaEtaDeltaPhiEnergy");
	double deltaEta, deltaPhi;
	deltaEta = eta2 - eta1;
	deltaPhi = FilterPlugin::wrapCheck(phi1, phi2);

	//DeltaEta Delta Phi Histograms Fill
	if(!_h2DeltaEtaDeltaPhiWeights.count(key)){
		_h2DeltaEtaDeltaPhiWeights[key] = etaPhiDir.make<TH2D>(Form("%s_2dSummedWeights",key.c_str()),Form("%s #Delta#eta #Delta#Phi Energy",key.c_str()),
				41,-10*HoMatcher::HO_BIN - HoMatcher::HALF_HO_BIN/2.,10*HoMatcher::HO_BIN + HoMatcher::HALF_HO_BIN/2.,
				41,-10*HoMatcher::HO_BIN - HoMatcher::HALF_HO_BIN/2.,10*HoMatcher::HO_BIN + HoMatcher::HALF_HO_BIN/2.);
	}
	//DeltaEta Delta Phi Histograms Fill
	if(!_h2DeltaEtaDeltaPhiCounter.count(key)){
		_h2DeltaEtaDeltaPhiCounter[key] = etaPhiDir.make<TH2D>(Form("%s_2dCounter",key.c_str()),Form("%s #Delta#eta #Delta#Phi Energy",key.c_str()),
				41,-10*HoMatcher::HO_BIN - HoMatcher::HALF_HO_BIN/2.,10*HoMatcher::HO_BIN + HoMatcher::HALF_HO_BIN/2.,
				41,-10*HoMatcher::HO_BIN - HoMatcher::HALF_HO_BIN/2.,10*HoMatcher::HO_BIN + HoMatcher::HALF_HO_BIN/2.);
	}
	_h2DeltaEtaDeltaPhiWeights[key]->Fill(deltaEta, deltaPhi, weight);
	_h2DeltaEtaDeltaPhiCounter[key]->Fill(deltaEta, deltaPhi);


	//#####################################
	//Delta I Eta Delta I Phi Histograms Fill
	//Same as above but doing the grid binning online.
	//Check for the phi systematic
	//#####################################
	if(!_h2DeltaIEtaDeltaIPhiWeights.count(key)){
		_h2DeltaIEtaDeltaIPhiWeights[key] = etaPhiDir.make<TH2D>(Form("%s_2dSummedWeightsIEtaIPhi",key.c_str()),
				Form("%s #Deltai#eta #Deltai#Phi Energy",key.c_str()),
				21,-10,10,
				21,-10,10);
	}
	//Delta I Eta Delta I Phi Histograms Fill
	if(!_h2DeltaIEtaDeltaIPhiCounter.count(key)){
		_h2DeltaIEtaDeltaIPhiCounter[key] = etaPhiDir.make<TH2D>(Form("%s_2dCounterIEtaIPhi",key.c_str()),
				Form("%s #Deltai#eta #Deltai#Phi Energy",key.c_str()),
				21,-10,10,
				21,-10,10);
	}

	int deltaIEta = HoMatcher::getDeltaIeta(eta1,eta2);
	int deltaIPhi = HoMatcher::getDeltaIphi(phi1,phi2);
	_h2DeltaIEtaDeltaIPhiWeights[key]->Fill(deltaIEta, deltaIPhi, weight);
	_h2DeltaIEtaDeltaIPhiCounter[key]->Fill(deltaIEta, deltaIPhi);
}

/*
 *L1Muon Pt Histograms
 *has variable binning
 */
void HistogramBuilder::fillL1MuonPtHistograms(float pt, std::string key){
	if(!_h1L1MuonPt.count(key)){
		float variableBinArray[] = {0,0.5,1,1.5,2,2.5,3,3.5,4,4.5,5,6,7,8,10,12,14,16,18,20,25,30,35,40,45,50,60,70,80,100,120,140,180};
		_h1L1MuonPt[key] = _fileService->make<TH1F>(Form("%s_Pt",key.c_str()),
				Form("%s Pt;p_{T};#",key.c_str()),
				32,
				variableBinArray);
	}
	_h1L1MuonPt[key]->Fill(pt);
}         

void HistogramBuilder::fillPtHistogram(float pt, std::string key){
	if(!_h1L1MuonPt.count(key)){
		_h1L1MuonPt[key] = _fileService->make<TH1F>(Form("%s_Pt",key.c_str()),
				Form("%s Pt;p_{T};#",key.c_str()),
				5000,0,500);
	}
	_h1L1MuonPt[key]->Fill(pt);
}

/**
 * Fill histogram with correlation between sim hit energy and rec hit energy
 */
void HistogramBuilder::fillEnergyCorrelationHistogram(double simHitEnergy, double recHitEnergy, std::string key){
	TFileDirectory energyDir = _fileService->mkdir("energy");

	//Fill Sim hit energy histo
	std::string simHitKey(key);
	key.append("simHits");
	if(!_h1Energy.count(simHitKey.c_str())){
		_h1Energy[simHitKey.c_str()] = energyDir.make<TH1F>(Form("%s_Energy_SimHits",key.c_str()),
				Form("%s Energy;Sim Hits / GeV;#",key.c_str()),
				2100, -5.0, 100.0);
	}
	_h1Energy[simHitKey.c_str()]->Fill(simHitEnergy);

	//Fill rec hit energy histo
	std::string recHitKey(key);
	key.append("recHits");
	if(!_h1Energy.count(recHitKey.c_str())){
		_h1Energy[recHitKey.c_str()] = energyDir.make<TH1F>(Form("%s_Energy_RecHits",key.c_str()),
				Form("%s Energy;Rec Hits / GeV;#",key.c_str()),
				2100, -5.0, 100.0);
	}
	_h1Energy[recHitKey.c_str()]->Fill(recHitEnergy);

	//Fill correlation
	if(!_h2EnergyCorrelation.count(key)){
		_h2EnergyCorrelation[key] = energyDir.make<TH2D>(Form("%s_EnergyCorrelation",key.c_str()),
				Form("%s Energy correlation;Sim Hits / GeV;Rec Hits / GeV",key.c_str()),
				51, -2.2185, 2.2185,
				73, -3.1755, 3.1755);
	}
	_h2EnergyCorrelation[key]->Fill(simHitEnergy, recHitEnergy);
}

/**
 * Fill histograms for energy depending on position
 */
void HistogramBuilder::fillEnergyVsPosition(double eta, double phi, double energy, std::string key){
	TFileDirectory energyDir = _fileService->mkdir("energy");

	//Fill energy vs eta
	if(!_h2EnergyVsEta.count(key)){
		_h2EnergyVsEta[key] = energyDir.make<TH2D>(Form("%s_EnergyVsEta",key.c_str()),
				Form("%s Energy vs #eta;#eta;Energy / GeV;Entries / 0.05GeV",key.c_str()),
				720, -3.132, 3.132, //0.0087 eta bins
				2000,0,100 //50 MeV bins
		);
	}
	_h2EnergyVsEta[key]->Fill(eta,energy);

	//Fill energy vs phi
	if(!_h2EnergyVsPhi.count(key)){
		_h2EnergyVsPhi[key] = energyDir.make<TH2D>(Form("%s_EnergyVsPhi",key.c_str()),
				Form("%s Energy vs #phi;#phi;Energy / GeV",key.c_str()),
				720, -3.132, 3.132, //0.0087 phi bins
				2000,0,100 //50 MeV bins
		);
	}
	_h2EnergyVsPhi[key]->Fill(phi,energy);

//	//Fill Eta phi energy histogram
	if(!_h3EtaPhiEnergy.count(key)){
		_h3EtaPhiEnergy[key] = energyDir.make<TH3D>(Form("%s_EnergyVsEtaPhi",key.c_str()),
				Form("%s Energy vs #eta#phi;#eta;#phi;Energy / 0.05 GeV",key.c_str()),
				72, -3.132, 3.132, //0.087 eta bins
				72, -3.132, 3.132, //0.087 phi bins
				2000,0,100 //50 MeV bins
		);
	}
	_h3EtaPhiEnergy[key]->Fill(eta,phi,energy);
}

/**
 * Delta Eta Delta Phi and energy Histograms
 * Create 3D histogram to access also the energy information of the hits
 *  	eta1 -> Gen
 * 		eta2 -> Ho
 * 		phi1 -> Gen
 * 		phi2 -> Ho
 */
void HistogramBuilder::fillDeltaEtaDeltaPhiEnergyHistogram(float eta1, float eta2,
		float phi1, float phi2,float energy,
		std::string key){
	TFileDirectory etaPhiDir = _fileService->mkdir("etaPhi");
	TFileDirectory etaPhiSubdir = _fileService->mkdir("etaPhi/energy1D");
	float deltaEta, deltaPhi;
	deltaEta = eta2 - eta1;
	deltaPhi = FilterPlugin::wrapCheck(phi1, phi2);

	//DeltaEta Delta Phi Histograms Fill
	if(!_h3DeltaEtaDeltaPhiEnergy.count(key)){
		_h3DeltaEtaDeltaPhiEnergy[key] = etaPhiDir.make<TH3D>(Form("%s_DeltaEtaDeltaPhiEnergy",key.c_str()),
				Form("%s #Delta#eta #Delta#Phi Energy;#eta;#phi;Energy / 0.05 GeV",key.c_str()),
				51, -2.2185, 2.2185,	//0.087 Eta bins
				73, -3.1755, 3.1755,	//0.087 Phi bins
				2000,0,100);
	}
	_h3DeltaEtaDeltaPhiEnergy[key]->Fill(deltaEta, deltaPhi, energy);


	/**
	 * This is done to track the deposited energies in a tile in delta eta delta phi coordinates.
	 * With this it should be possible to perform a landau fit to the energy instead of using the mean
	 * which leads to a wrong Edep estimate.
	 *
	 * The coordinates are in iEta and iPhi relative to the central tile.
	 *
	 */
	if(!_hArrDeltaEtaDeltaPhiEnergy.count(key)){
		_hArrDeltaEtaDeltaPhiEnergy[key] = new TH1D*[49];
		std::string histName;
		for(int i = 0; i < 49; i++){
			int iEta,iPhi;
			std::string signStringEta,signStringPhi;
			if(i == 24){
				histName = Form("central_%s",key.c_str());
			} else{
				iEta = ( (i) % 7) - 3;
				iPhi = 3 - ( (i) / 7);
				signStringEta = ( iEta < 0 ) ? "M" : "P";
				signStringPhi = ( iPhi < 0 ) ? "M" : "P";
				iEta = abs(iEta);
				iPhi = abs(iPhi);
				histName = Form("eta%s%dPhi%s%d_%s",signStringEta.c_str(),iEta,signStringPhi.c_str(),iPhi,key.c_str());
			}
			std::string title;
			if(i == 24){
				title = Form("%s central Energy;Rec Hits / GeV;#",key.c_str());
			} else {
				title = Form("%s %s%d %s%d Energy;Rec Hits / GeV;#",key.c_str(),signStringEta.c_str(),iEta,signStringPhi.c_str(),iPhi);
			}
			_hArrDeltaEtaDeltaPhiEnergy[key][i] = etaPhiSubdir.make<TH1D>(histName.c_str(),title.c_str(),300,-5.0, 10.0);
		}
	}

	/**
	 * 0.087 is the tile size in eta and phi, but a shift by the half tile size is necessary,
	 * since we are looking into relative coordinates from the center of the tile
	 */
	int iDeltaEta = 0;
	int iDeltaPhi = 0;

	//Calculate i delta eta
	if( fabs(deltaEta) <= 0.0435){
		iDeltaEta = 0;
	} else{
		iDeltaEta = 1 + int(fabs(deltaEta)/0.087 - 0.5);
	}

	//calculate i delta phi
	if( fabs(deltaPhi) <= 0.0435){
		iDeltaPhi = 0;
	} else{
		iDeltaPhi = 1 + int(fabs(deltaPhi)/0.087 - 0.5);
	}

	if(deltaEta != 0){
		iDeltaEta = deltaEta / fabs(deltaEta)*iDeltaEta;
	}

	if(deltaPhi != 0)
		iDeltaPhi = deltaPhi / fabs(deltaPhi)*iDeltaPhi;

	if(abs(iDeltaEta) < 4 && abs(iDeltaPhi) < 4){
		int histNumberInArray = ( 3 - iDeltaPhi )*7 + ( iDeltaEta + 3 );
		_hArrDeltaEtaDeltaPhiEnergy[key][histNumberInArray]->Fill(energy);
	}
}

/**
 * Fill a histogram with a given BX ID for the given histogram key
 */
void HistogramBuilder::fillBxIdHistogram(int bxid, std::string key){
	if(!_h1BxId.count(key)){
		_h1BxId[key] = _fileService->make<TH1D>(Form("%s_BxId",key.c_str()),
					Form("%s BX ID;BX ID;#",key.c_str()),
					26,-5.5,20.5);
		}
	_h1BxId[key]->Fill(bxid);
}

/**
 * Fill a histogram with a given time in ns for the given histogram key
 */
void HistogramBuilder::fillTimeHistogram(double time, std::string key){
	if(!_h1Time.count(key)){
		_h1Time[key] = _fileService->make<TH1D>(Form("%s_Time",key.c_str()),
					Form("%s Time;ns;#",key.c_str()),
					201,-200.5,200.5);
		}
	_h1Time[key]->Fill(time);
}

/**
 * Fill a histogram with the time difference between the HO Rec hit Time in ns and the
 * L1MuonParticle bx, calculated in ns
 */
void HistogramBuilder::fillDeltaTimeHistogram(double time, int bx, std::string key){
	if(!_h1DeltaTime.count(key)){
		_h1DeltaTime[key] = _fileService->make<TH1D>(Form("%s_DeltaTime",key.c_str()),
					Form("%s #DeltaTime;ns;#",key.c_str()),
					201,-100.5,100.5);
	}
	_h1DeltaTime[key]->Fill(bx*25 - time);
	TFileDirectory correlationDir = _fileService->mkdir("correlation");
	if(!_h2TimeCorrelation.count(key)){
		_h2TimeCorrelation[key] = correlationDir.make<TH2D>(Form("%s_TimeCorrelation",key.c_str()),
				Form("%s Time Correlation;HO time / ns;L1 Time / ns",key.c_str()),
				201, -100.5,100.5,	//1ns bins
				21, -10.5,10.5	//1 BX bins
				);
	}
	_h2TimeCorrelation[key]->Fill(time,bx);
}

/**
 * Fill a 2D histogram with BX id vs pt information
 */
void HistogramBuilder::fillQualityCodeVsPt(int qc, double pt, std::string key){
	TFileDirectory timeDir = _fileService->mkdir("qualityCode");
	double variableBinArray[] = {0,0.5,1,1.5,2,2.5,3,3.5,4,4.5,5,6,7,8,10,12,14,16,18,20,25,30,35,40,45,50,60,70,80,100,120,140,180};

	//Fill energy vs eta
	if(!_h2qualityCodeVsPt.count(key)){
		_h2qualityCodeVsPt[key] = timeDir.make<TH2D>(Form("%s_QcVsPt",key.c_str()),
				Form("%s QC vs p_{T};p_{T} / GeV;QC;# Entries",key.c_str()),
				32,variableBinArray,
				401,-200.5,200.5
		);
	}
	_h2qualityCodeVsPt[key]->Fill(pt,qc);
}

/**
 * Fill a 2D histogram with BX id vs pt information
 */
void HistogramBuilder::fillBxIdVsPt(int bxId, double pt, std::string key){
	TFileDirectory timeDir = _fileService->mkdir("time");
	double variableBinArray[] = {0,0.5,1,1.5,2,2.5,3,3.5,4,4.5,5,6,7,8,10,12,14,16,18,20,25,30,35,40,45,50,60,70,80,100,120,140,180};

	//Fill energy vs eta
	if(!_h2BxIdVsPt.count(key)){
		_h2BxIdVsPt[key] = timeDir.make<TH2D>(Form("%s_BxIdVsPt",key.c_str()),
				Form("%s BX ID vs p_{T};p_{T} / GeV;BX ID",key.c_str()),
				32,variableBinArray,
				25,-12.5,12.5
		);
	}
	_h2BxIdVsPt[key]->Fill(pt,bxId);
}

/**
 * Fill A TGraph for exact position in eta and phi in a scatterplot
 */
void HistogramBuilder::fillEtaPhiGraph(double eta, double phi, std::string key){
	TFileDirectory graphDir = _fileService->mkdir("graphs");
	if(!_grEtaPhi.count(key)){
		_grEtaPhi[key] = graphDir.make<TGraph>();
		_grEtaPhi[key]->SetTitle(key.c_str());
		_grEtaPhi[key]->SetName(key.c_str());
		}
	_grEtaPhi[key]->SetPoint(_grEtaPhi[key]->GetN(),eta, phi);
};

/**
 * Fill a graph that is stored in the correlation subdirectory
 */
void HistogramBuilder::fillCorrelationGraph(double xVal, double yVal, std::string key){
	TFileDirectory correlation = _fileService->mkdir("correlation");
		if(!_grCorrelation.count(key)){
			_grCorrelation[key] = correlation.make<TGraph>();
			_grCorrelation[key]->SetTitle(key.c_str());
			_grCorrelation[key]->SetName(key.c_str());
			}
		_grCorrelation[key]->SetPoint(_grCorrelation[key]->GetN(),xVal, yVal);
}

/**
 * Fill a TGraph with given x, y and key
 */
void HistogramBuilder::fillGraph(double x, double y, std::string key){
	TFileDirectory graphDir = _fileService->mkdir("graphs");
	if(!_graphs.count(key)){
		_graphs[key] = graphDir.make<TGraph>();
		_graphs[key]->SetTitle(key.c_str());
		_graphs[key]->SetName(key.c_str());
	}
	_graphs[key]->SetPoint(_graphs[key]->GetN(),x, y);
}

/**
 * Fill a TGraph2D with given x, y, z and key
 */
void HistogramBuilder::fillGraph2D(double x, double y, double z, std::string key){
	TFileDirectory graphDir = _fileService->mkdir("graphs2d");
	if(!_graphs2d.count(key)){
		_graphs2d[key] = graphDir.make<TGraph2D>();
		_graphs2d[key]->SetTitle(key.c_str());
		_graphs2d[key]->SetName(key.c_str());
	}
	_graphs2d[key]->SetPoint(_graphs2d[key]->GetN(),x, y, z);
}

/**
 * Fill a 3D histogram with eta phi and pt information
 */
void HistogramBuilder::fillEtaPhiPtHistogram(double eta, double phi, double pt, std::string key){
	TFileDirectory etaPhiDir = _fileService->mkdir("etaPhi");
	TFileDirectory etaPhiSubdir = _fileService->mkdir("etaPhi/3D");
	if(!_h3EtaPhiPt.count(key)){
		_h3EtaPhiPt[key] = etaPhiSubdir.make<TH3D>(Form("%s_EtaPhiPt",key.c_str()),
					Form("%s #eta #Phi p_{T};#eta;#phi;p_{T} / 5 GeV",key.c_str()),
					40, -1.6, 1.6,	//0.08 Eta bins
					80, -3.2, 3.2,	//0.08 Phi bins
					40,0,200);		//5 GeV p_T bins
	}
	_h3EtaPhiPt[key]->Fill(eta,phi,pt);

}

void HistogramBuilder::fillL1ResolutionHistogram(double l1Pt, double recoPt, std::string key){
	TFileDirectory resolutionDir = _fileService->mkdir("l1PtResolution");
	float variableBinArray[] = {0,0.5,1,1.5,2,2.5,3,3.5,4,4.5,5,6,7,8,10,12,14,16,18,20,25,30,35,40,45,50,60,70,80,100,120,140,180};
	int ptBin = -1;
	if(recoPt < 40){
		ptBin = int (recoPt);
	} else {
		ptBin = 40 + int ((recoPt-40)/2);
	}
	if (ptBin > 220){
		ptBin = 220;
	}
	std::string histoKey = Form("%sBin%d",key.c_str(),ptBin);
	if(!_h1L1Resolution.count(histoKey)){
		_h1L1Resolution[histoKey] = resolutionDir.make<TH1D>(Form("%s",histoKey.c_str()),Form("%s",histoKey.c_str())
				,32,variableBinArray);
	}
	_h1L1Resolution[histoKey]->Fill(l1Pt);
}
