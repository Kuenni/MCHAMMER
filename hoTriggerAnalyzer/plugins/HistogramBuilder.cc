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
#include "TH2F.h"
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
 * Fill a correlation histogram for Pt of two objects
 */
void HistogramBuilder::fillPtCorrelationHistogram(float pt1, float pt2, std::string key){
	if(!_h2PtCorrelation.count(key)){
		_h2PtCorrelation[key] = _fileService->make<TH2D>(Form("%s_PtCorrelation",key.c_str()),
				Form("%s P_{T} Correlation;p_{T}1;p_{T}2",key.c_str()),
				500, 0,500,500,0,500);
	}
	_h2PtCorrelation[key]->Fill(pt1,pt2);
}

void HistogramBuilder::fillEfficiency(bool passed, float pt, std::string key){
	TFileDirectory efficiencyDir = _fileService->mkdir("efficiency");
	if(!_effMap.count(key)){
		_effMap[key] = efficiencyDir.make<TEfficiency>(Form("%s_Efficiency",key.c_str()),
				Form("%s Efficiency",key.c_str()),
				251, -0.5, 250.5);
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
	if(!_h1Counter.count(key)){
		_h1Counter[key] = _fileService->make<TH1F>(Form("%s_Count",key.c_str()),
				Form("%s Count",key.c_str()),
				3, -0.5, 2.5);
	}
	_h1Counter[key]->Fill(1);
}                                                                               

void HistogramBuilder::fillMultiplicityHistogram(int nEvents, std::string key){
	if(!_h1Multiplicity.count(key)){
		_h1Multiplicity[key] = _fileService->make<TH1D>(Form("%s_Multiplicity",key.c_str()),
				Form("%s Digis Per Event",key.c_str()),
				2001, -0.5, 2000.5);
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
	float variableBinArray[] = {0,0.5,1,1.5,2,2.5,3,3.5,4,4.5,5,6,7,8,9,10,12,14,16,18,20,25,30,35,40,45,50,60,70,80,100,120,140,180};
	if(!_h1TrigRate.count(key)){
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

/*                                                                              
 *Eta Phi Histograms                                                            
 */

void HistogramBuilder::fillEtaPhiHistograms(float eta, float phi, std::string key){
	TFileDirectory etaPhiDir = _fileService->mkdir("etaPhi");
	if(!_h1Eta.count(key)){
		_h1Eta[key] = etaPhiDir.make<TH1F>(Form("%s_Eta",key.c_str()),
				Form("%s Eta",key.c_str()),
				500, -1.5, 1.5);  //HO has 72 iphis and 30 ietas
	}
	_h1Eta[key]->Fill(eta);

	if(!_h1Phi.count(key)){
		_h1Phi[key] = etaPhiDir.make<TH1F>(Form("%s_Phi",key.c_str()),
				Form("%s Phi",key.c_str()),
				500, -3.14, 3.14);  //HO has 72 iphis and 30 ietas
	}
	_h1Phi[key]->Fill(phi);

	if(!_h2EtaPhiMap.count(key)){
		_h2EtaPhiMap[key] = etaPhiDir.make<TH2F>(Form("%s_EtaPhi",key.c_str()),
				Form("%s_EtaPhi",key.c_str()),
				500, -1.5, 1.5, 500, -3.14, 3.14);
	}
	_h2EtaPhiMap[key]->Fill(eta, phi);

};

/*
 *Delta Eta Delta Phi Histograms
 */

void HistogramBuilder::fillDeltaEtaDeltaPhiHistograms(float eta1, float eta2, 
		float phi1, float phi2,
		std::string key){
	TFileDirectory etaPhiDir = _fileService->mkdir("etaPhi");
	float deltaEta, deltaPhi;
	deltaEta = eta1 - eta2;
	deltaPhi = FilterPlugin::wrapCheck(phi1, phi2);

	//Delta Eta Histograms Fill
	if(!_h1DeltaEta.count(key)){
		_h1DeltaEta[key] =  etaPhiDir.make<TH1F>(Form("%s_DeltaEta",
				key.c_str()),
				Form("#Delta #Eta %s",
						key.c_str()),
						510, -2.2185, 2.2185);//510 times 0.087/10; 0 in center of a bin
	}
	_h1DeltaEta[key]->Fill(deltaEta);
	//Delta Eta Histograms Fill
	if(!_h1DeltaPhi.count(key)){
		_h1DeltaPhi[key] = etaPhiDir.make<TH1F>(Form("%s_DeltaPhi",
				key.c_str()),
				Form("%s #Delta #Phi",
						key.c_str()),
						730, -3.1755, 3.1755);//730 times 0.087/10; 0 in center of a bin
	}
	_h1DeltaPhi[key]->Fill(deltaPhi);

	//DeltaEta Delta Phi Histograms Fill
	if(!_h2DeltaEtaDeltaPhi.count(key)){
		_h2DeltaEtaDeltaPhi[key] = etaPhiDir.make<TH2F>(Form("%s_DeltaEtaDeltaPhi",key.c_str()),Form("%s #Delta#eta #Delta#Phi",key.c_str()),51, -2.2185, 2.2185, 73, -3.1755, 3.1755);
	}
	_h2DeltaEtaDeltaPhi[key]->Fill(deltaEta, deltaPhi);
} 

/*
 *L1Muon Pt Histograms
 *has variable binning
 */
void HistogramBuilder::fillL1MuonPtHistograms(float pt, std::string key){
	if(!_h1L1MuonPt.count(key)){
		float variableBinArray[] = {0,0.5,1,1.5,2,2.5,3,3.5,4,4.5,5,6,7,8,9,10,12,14,16,18,20,25,30,35,40,45,50,60,70,80,100,120,140,180};
		_h1L1MuonPt[key] = _fileService->make<TH1F>(Form("%s_Pt",key.c_str()),
				Form("%s Pt",key.c_str()),
				33,
				variableBinArray);
	}
	_h1L1MuonPt[key]->Fill(pt);
}         

void HistogramBuilder::fillPtHistogram(float pt, std::string key){
	if(!_h1L1MuonPt.count(key)){
		_h1L1MuonPt[key] = _fileService->make<TH1F>(Form("%s_Pt",key.c_str()),
				Form("%s Pt",key.c_str()),
				5000,0,500);
	}
	_h1L1MuonPt[key]->Fill(pt);
}

