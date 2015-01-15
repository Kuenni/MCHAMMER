/**
 *	Struct definition for HO Rec hit data that will be stored in a tree 
 */

#ifndef HORECHITDATA
#define HORECHITDATA 1

struct HoRecHitData{
	double eta;
	double phi;
	double energy;
	double time;
	HoRecHitData(double _eta, double _phi, double _energy,double _time):eta(_eta),phi(_phi),energy(_energy),time(_time){}
	HoRecHitData(){
		eta = 0;
		phi = 0;
		energy = 0;
		time = -1;
	}
	HoRecHitData(const HoRecHitData& recHitData):eta(recHitData.eta),phi(recHitData.phi),energy(recHitData.energy),time(recHitData.time){}
};

#endif

