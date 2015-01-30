#ifndef __HOMUON__HISTOGRAMBUILDER_H__
#define __HOMUON__HISTOGRAMBUILDER_H__

/*
 * Class Test Class
 * Author Chris Anelli
 * 6.13.2013
 * Edited by Andreas Kuensken
 * kuensken@physik.rwth-aachen.de
 * 26. Aug 2014
 */

#include <CommonTools/UtilAlgos/interface/TFileService.h>
#include <FWCore/ServiceRegistry/interface/Service.h>
#include <TEfficiency.h>
#include <TH1.h>
#include <TH2.h>
#include <TH3.h>
#include <TTree.h>
#include <TGraph.h>
#include <map>
#include <string>



class HistogramBuilder {

 public:
 
  edm::Service<TFileService> _fileService;
  
  /*
   * Functions for HistogramBuilder                                       
   */
  
  void fillL1MuonPtHistograms(float pt, std::string key);                     
  void fillEnergyHistograms(float energy, std::string key);                   
  void fillEtaPhiHistograms(float eta, float phi, std::string key);
  void fillDeltaEtaDeltaPhiHistograms(float eta1, float eta2, 
				      float phi1, float phi2,  std::string key);
  void fillCountHistogram(std::string key);                                   
  void fillTrigHistograms(bool trigDecision,std::string key);
  void fillTrigRateHistograms(float ptThreshold, std::string key);
  void fillTrigRateL1Histograms(float,std::string);
  void fillPdgIdHistogram(int pdgId,std::string key);
  void fillMultiplicityHistogram(int , std::string );
  void fillHltIndexHistogram(int hltIndex, std::string key);
  void fillEfficiency(bool,float,std::string);
  void fillDeltaVzHistogam(float,std::string);
  void fillPtCorrelationHistogram(float,float,std::string);
  void fillPtHistogram(float,std::string);
  void fillVzHistogram(float,std::string);
  void fillEnergyCorrelationHistogram(double,double,std::string);
  void fillEnergyVsPosition(double eta,double phi,double energy,std::string);
  void fillDeltaEtaDeltaPhiEnergyHistogram(float,float,float,float,float,std::string);
  void fillEtaPhiGraph(double eta, double phi, std::string key);
  void fillBxIdHistogram(int bxId,std::string key);
  void fillBxIdVsPt(int bxId,double pt,std::string key);
  void fillTimeHistogram(double,std::string);
  void fillDeltaTimeHistogram(double, int, std::string);
  void fillCorrelationGraph(double xVal, double yVal, std::string key);

 private:

  std::map<std::string,TH1F*> _h1Eta;
  std::map<std::string,TH1F*> _h1Phi;
  std::map<std::string,TH1F*> _h1L1MuonPt;
  std::map<std::string,TH1F*> _h1Energy;
  std::map<std::string,TH1F*> _h1DeltaEta;
  std::map<std::string,TH1F*> _h1DeltaPhi;
  std::map<std::string,TH1F*> _h1Trig;
  std::map<std::string,TH1F*> _h1Counter;
  std::map<std::string,TH1D*> _h1pdgId;
  std::map<std::string,TH1D*> _h1Multiplicity;
  std::map<std::string,TH1D*> _h1HltIndex;
  std::map<std::string,TH1D*> _h1DeltaVz;
  std::map<std::string,TH1D*> _h1Vz;
  std::map<std::string,TH1D*> _h1BxId;
  std::map<std::string,TH1D*> _h1Time;
  std::map<std::string,TH1D*> _h1DeltaTime;
  std::map<std::string,TH1D*> _h1TrigRate;
  std::map<std::string,TH1D**> _hArrDeltaEtaDeltaPhiEnergy;

  std::map<std::string,TH2D*> _h2PtCorrelation;
  std::map<std::string,TH2D*> _h2EnergyCorrelation;
  std::map<std::string,TH2D*> _h2EnergyVsPhi;
  std::map<std::string,TH2D*> _h2EnergyVsEta;
  std::map<std::string,TH2D*> _h2EnergyEtaPhiEnergies;
  std::map<std::string,TH2D*> _h2EnergyEtaPhiCounter;
  std::map<std::string,TH2D*> _h2BxIdVsPt;
  std::map<std::string,TH2D*> _h2TimeCorrelation;
  std::map<std::string,TH2D*> _h2EtaPhiMap;
  std::map<std::string,TH2D*> _h2DeltaEtaDeltaPhi;

  std::map<std::string,TGraph*> _grEtaPhi;
  std::map<std::string,TGraph*> _grCorrelation;

  std::map<std::string,TH3D*> _h3EtaPhiEnergy;
  std::map<std::string,TH3D*> _h3DeltaEtaDeltaPhiEnergy;

  std::map<std::string,TEfficiency*> _effMap;
  
  std::map<std::string,TTree*> _treeDeltaEtaDeltaPhiEnergy;


};

#endif
