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
	TFileDirectory countDir = _fileService->mkdir("count");
	if(!_h1Counter.count(key)){
		_h1Counter[key] = countDir.make<TH1F>(Form("%s_Count",key.c_str()),
				Form("%s Count",key.c_str()),
				3, -0.5, 2.5);
	}
	_h1Counter[key]->Fill(1);
}                                                                               

void HistogramBuilder::fillMultiplicityHistogram(int nEvents, std::string key){
	if(!_h1Multiplicity.count(key)){
		_h1Multiplicity[key] = _fileService->make<TH1D>(Form("%s_Multiplicity",key.c_str()),
				Form("%s Digis Per Event",key.c_str()),
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

};

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
	deltaEta = eta1 - eta2;
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
	TString simHitKey(key);
	key.append("simHits");
	if(!_h1Energy.count(simHitKey.Data())){
		_h1Energy[simHitKey.Data()] = energyDir.make<TH1F>(Form("%s_Energy_SimHits",key.c_str()),
				Form("%s Energy;Sim Hits / GeV;#",key.c_str()),
				2100, -5.0, 100.0);
	}
	_h1Energy[simHitKey.Data()]->Fill(simHitEnergy);

	//Fill rec hit energy histo
	TString recHitKey(key);
	key.append("recHits");
	if(!_h1Energy.count(recHitKey.Data())){
		_h1Energy[recHitKey.Data()] = energyDir.make<TH1F>(Form("%s_Energy_RecHits",key.c_str()),
				Form("%s Energy;Rec Hits / GeV;#",key.c_str()),
				2100, -5.0, 100.0);
	}
	_h1Energy[recHitKey.Data()]->Fill(recHitEnergy);

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
	deltaEta = eta1 - eta2;
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
	 * With ths it should be possible to perform a landau fit to the energy instead of using the mean
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
					161,-80.5,80.5);
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
	if(!_h2TimeCorrelation.count(key)){
		_h2TimeCorrelation[key] = _fileService->make<TH2D>(Form("%s_TimeCorrelation",key.c_str()),
				Form("%s Time Correlation;HO time / ns;L1 Time / ns",key.c_str()),
				200, -100.5,100.5,	//1ns bins
				200, -100.5,100.5	//1ns bins
				);
	}
	_h2TimeCorrelation[key]->Fill(time,bx*25);
}

/**
 * Fill a 2D histogram with BX id vs pt information
 */
void HistogramBuilder::fillBxIdVsPt(int bxId, double pt, std::string key){
	TFileDirectory timeDir = _fileService->mkdir("time");

	//Fill energy vs eta
	if(!_h2BxIdVsPt.count(key)){
		_h2BxIdVsPt[key] = timeDir.make<TH2D>(Form("%s_BxIdVsPt",key.c_str()),
				Form("%s BX ID vs p_{T};p_{T} / GeV;BX ID",key.c_str()),
				200,0,100, //0.5 GeV Bins
				5,-2.5,2.5
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
 * Fill a 3D histogram with eta phi and pt information
 */
void HistogramBuilder::fillEtaPhiPtHistogram(double eta, double phi, double pt, std::string key){
	TFileDirectory etaPhiDir = _fileService->mkdir("etaPhi");
	TFileDirectory etaPhiSubdir = _fileService->mkdir("etaPhi/3D");
	if(!_h3EtaPhiPt.count(key)){
		etaPhiSubdir.make<TH3D>(Form("%s_EtaPhiPt",key.c_str()),
					Form("%s #eta #Phi p_{T};#eta;#phi;p_{T} / 5 GeV",key.c_str()),
					40, -1.6, 1.6,	//0.08 Eta bins
					80, -3.2, 3.2,	//0.08 Phi bins
					40,0,200);		//5 GeV p_T bins
	}
	_h3EtaPhiPt[key]->Fill(eta,phi,pt);

}
