#include "TFile.h"
#include "TTree.h"
#include "TString.h"
#include "TROOT.h"

#include "headers/L1MuonData.h"
#include "headers/GenMuonData.h"
#include "headers/HoRecHitData.h"

#include <stdio.h>
#include <iostream>

static const int N_NEWFILES = 250;

void testFiles(){
	std::cout << "Testing files" << std::endl;
	for( int i = 0; i < N_NEWFILES; i++){
		TFile* file =  TFile::Open(TString::Format("data/L1MuonHistogram_%d.root", i));
		TTree* tree = (TTree*) file->Get("dataTree");

		tree->GetEntries();
		file->Close();
	}
	std::cout << "Files OK" << std::endl;
}
void splitTree(){

	gROOT->ProcessLine(".L ./loader.C+");

	TFile* oldFile = TFile::Open("L1MuonHistogram.root");
	TTree* oldTree = (TTree*)oldFile->Get("hoMuonAnalyzer/dataTree");
	std::vector<L1MuonData>* muonVector = 0;
	std::vector<GenMuonData>* genVector = 0;
	std::vector<HoRecHitData>* recHitVector = 0;

	oldTree->SetBranchAddress("l1MuonData",&muonVector);
	oldTree->SetBranchAddress("genMuonData",&genVector);
	oldTree->SetBranchAddress("hoRecHitData",&recHitVector);

	int totalEvents = oldTree->GetEntries();
	int splitEventNumber = int(totalEvents/float(N_NEWFILES));
	TFile* newFile = 0;
	TTree* newTree = 0;
	int counter = 0;
	for (int i = 0; i < totalEvents; ++i) {
		if (i % splitEventNumber == 0){
			TString filename = TString::Format("data/L1MuonHistogram_%d.root", counter);
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
	testFiles();
}

int main(int argc, char** argv){
	splitTree();
	return 0;
}

