/**
 *	Struct definition for HO Rec hit data that will be stored in a tree 
 */

#ifndef HORECHITDATA
#define HORECHITDATA 1

static const int MAXSAMPLES = 10;

#include <algorithm>

struct HoRecHitData{
	double eta;
	double phi;
	double energy;
	double time;
	short adcSamples[MAXSAMPLES];
	HoRecHitData(double _eta, double _phi, double _energy,double _time, short* _adcSamples):eta(_eta),phi(_phi),energy(_energy),time(_time){
		//Copy array content
		std::copy(_adcSamples,_adcSamples + MAXSAMPLES,adcSamples);
	}
	HoRecHitData(){
		eta = 0;
		phi = 0;
		energy = 0;
		time = -1;
		for(int i = 0; i < MAXSAMPLES; i++){
			adcSamples[i] = -1;
		}
	}
	HoRecHitData(const HoRecHitData& recHitData):eta(recHitData.eta),phi(recHitData.phi),energy(recHitData.energy),time(recHitData.time){
		//Copy array content
		std::copy(recHitData.adcSamples,recHitData.adcSamples + MAXSAMPLES,adcSamples);
	}
};

#endif

