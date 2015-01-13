/**
 *	Struct definition for HO Rec hit data that will be stored in a tree 
 */

#ifndef HORECHITDATA
#define HORECHITDATA 1

struct HoRecHitData{
	double eta;
	double phi;
	double energy;
	HoRecHitData(double _eta, double _phi, double _energy):eta(_eta),phi(_phi),energy(_energy){}
	HoRecHitData(){
		eta = 0;
		phi = 0;
		energy = 0;
	}
};

#endif

