/**
 *	Struct definition for L1 Muon data that will be stored in a vector which
 *	again will be stored in a root tree
 */
#ifndef L1MUONDATA
#define L1MUONDATA 1

struct L1MuonData {
	double eta;
	double phi;
	double pt;
	int bx;
	bool inGeomAcceptance;
	bool inNotDeadGeom;
	bool inSiPMGeom;
	L1MuonData(double _eta, double _phi, double _pt, int _bx, bool iga, bool indg, bool isg):
		eta(_eta),phi(_phi),pt(_pt),bx(_bx),inGeomAcceptance(iga),inNotDeadGeom(indg),inSiPMGeom(isg){}
	L1MuonData(){
		eta = 0;
		phi = 0;
		pt = -1;
		bx = 0;
		inGeomAcceptance = false;
		inNotDeadGeom = false;
		inSiPMGeom = false;
	}
};
#endif
