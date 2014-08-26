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

#include "FWCore/Framework/interface/Frameworkfwd.h"

#include "FWCore/ServiceRegistry/interface/Service.h"
#include "CommonTools/UtilAlgos/interface/TFileService.h"


#include "TH1F.h"
#include "TH2.h"
#include "TEfficiency.h"
#include <map>



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
  void fillPdgIdHistogram(int pdgId,std::string key);
  void fillDigiPerEvtHistogram(int nDigis, std::string key);
  void fillHltIndexHistogram(int hltIndex, std::string key);
  void fillEfficiency(bool,float,std::string);


 private:

  std::map<std::string,TH1F*> _h1L1MuonPt;
  std::map<std::string,TH1F*> _h1Energy;
  std::map<std::string,TH1D*> _h1pdgId;
  std::map<std::string,TH1D*> _h1DigisPerEvt;
  std::map<std::string,TH1D*> _h1HltIndex;
  
  std::map<std::string,TH1F*> _h1Eta;
  std::map<std::string,TH1F*> _h1Phi;
  std::map<std::string,TH2F*> _h2EtaPhiMap;
  
  std::map<std::string,TH1F*> _h1DeltaEta;                                      
  std::map<std::string,TH1F*> _h1DeltaPhi;                                      
  std::map<std::string,TH2F*> _h2DeltaEtaDeltaPhi;                              
  std::map<std::string,TH1F*> _h1Trig;                                          
  std::map<std::string,TH1F*> _h1Counter;

  std::map<std::string,TEfficiency*> _effMap;
  
};

#endif
