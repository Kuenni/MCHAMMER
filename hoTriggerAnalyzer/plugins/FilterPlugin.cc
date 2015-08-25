/*
 * FilterPlugin.cc
 *
 *  Created on: Sep 23, 2014
 *      Author: kuensken
 */

#include "HoMuonTrigger/hoTriggerAnalyzer/interface/FilterPlugin.h"

#include <math.h>

double FilterPlugin::wrapCheck(double phi1, double phi2){
  float delta_phi = phi2 - phi1;
  if(delta_phi < -M_PI){
    return (2*M_PI + delta_phi);
  }
  if(delta_phi > M_PI){
    return (delta_phi - 2*M_PI);
  }
  return delta_phi;
};

bool FilterPlugin::isInsideDeltaR(double eta1, double eta2, double phi1, double phi2, double deltaR_Max){

	float delta_eta, delta_phi;

	delta_eta = eta2 - eta1;
	delta_phi = wrapCheck(phi1,phi2); //Finds difference in phi

	if(pow(delta_eta,2)+pow(delta_phi,2) <= pow(deltaR_Max,2)) return true;
	return false;
}
