#ifndef GENMUONDATA
#define GENMUONDATA

/**
 * Simple struct to store data from gen particles.
 * inGeomAcceptance -> Check from HOMuonAcceptance + check whether eta phi points to HO Chimney
 * inNotDeadGeom & inSiPMGeom -> From HOMuonAcceptance, should now always be true
 */

struct GenMuonData{
	double eta;
	double phi;
	double extrapolatedEta;
	double extrapolatedPhi;
	double pt;
	int pdgId;
	bool inGeomAcceptance;
	bool inNotDeadGeom;
	bool inSiPMGeom;


	GenMuonData(double _eta, double _phi, double _extrapolatedEta, double _extrapolatedPhi, double _pt, int _pdgId, bool _iga, bool _indg, bool _isg):
		eta(_eta),phi(_phi),extrapolatedEta(_extrapolatedEta),extrapolatedPhi(_extrapolatedPhi),pt(_pt),pdgId(_pdgId),inGeomAcceptance(_iga),inNotDeadGeom(_indg),inSiPMGeom(_isg){}
	GenMuonData(){
		eta = 0;
		phi = 0;
		extrapolatedEta = 0;
		extrapolatedPhi = 0;
		pt = -1;
		pdgId = 0;
		inGeomAcceptance = false;
		inNotDeadGeom = false;
		inSiPMGeom = false;
	}
};

#endif
