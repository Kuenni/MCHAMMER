#include "TFile.h"
#include "TTree.h"
#include "TString.h"
#include "TROOT.h"
#include "TSystemDirectory.h"

#include "additionalFiles/headers/L1MuonData.h"
#include "additionalFiles/headers/GenMuonData.h"
#include "additionalFiles/headers/HoRecHitData.h"

#include <stdio.h>
#include <iostream>

static const int N_EVTS_PER_FILE = 10000;

void splitTree(){

	gROOT->ProcessLine(".L ./additionalFiles/loader.C+");

	TFile* oldFile = TFile::Open("additionalFiles/L1MuonHistogram.root");
	TTree* oldTree = (TTree*)oldFile->Get("hoMuonAnalyzer/dataTree");
	std::vector<L1MuonData>* muonVector = 0;
	std::vector<GenMuonData>* genVector = 0;
	std::vector<HoRecHitData>* recHitVector = 0;

	oldTree->SetBranchAddress("l1MuonData",&muonVector);
	oldTree->SetBranchAddress("genMuonData",&genVector);
	oldTree->SetBranchAddress("hoRecHitData",&recHitVector);

	int totalEvents = oldTree->GetEntries();
	int splitEventNumber = N_EVTS_PER_FILE;
	TFile* newFile = 0;
	TTree* newTree = 0;
	int counter = 0;
	for (int i = 0; i < totalEvents; ++i) {
		if (i % splitEventNumber == 0){
			TString filename = TString::Format("additionalFiles/data/L1MuonHistogram_%d.root", counter);
			if (newFile != 0){
				if(i == 0){
					std::cout << "This should not be possible..." << std::endl;
				}
				newFile->cd();
				newTree->Write();
				delete newFile;
			}
			newFile = new TFile(filename,"RECREATE");
			newFile->cd();
			newTree = oldTree->CloneTree(0);
			counter += 1;
		}
		oldTree->GetEntry(i);
		newTree->Fill();
		std::cout << TString::Format("\rProgress: %5.2f%% done.",(i/float(totalEvents)*100));
		std::cout.flush();
	}
	newTree->Write();
	delete newFile;
}

int main(int argc, char** argv){
	splitTree();
	return 0;
}

