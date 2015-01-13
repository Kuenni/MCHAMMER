#ifndef GENMUONDATA
#define GENMUONDATA

struct GenMuonData{
	double eta;
	double phi;
	double pt;
	int pdgId;
	bool inGeomAcceptance;
	bool inNotDeadGeom;
	bool inSiPMGeom;

	GenMuonData(double _eta, double _phi, double _pt, int _pdgId, bool _iga, bool _indg, bool _isg):eta(_eta),phi(_phi),pt(_pt),pdgId(_pdgId),inGeomAcceptance(_iga),inNotDeadGeom(_indg),inSiPMGeom(_isg){}
	GenMuonData(){}
};

#endif
