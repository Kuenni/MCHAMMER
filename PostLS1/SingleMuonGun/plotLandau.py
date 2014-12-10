#!/usr/bin/python
import os,sys

from ROOT import TFile,TCanvas,TF1

sys.path.append(os.path.abspath("/user/kuensken/ChrisAnelliCode/CMSSW_6_2_0_SLHC11/src/HoMuonTrigger/python"))

def calcSigma(num,denom):
	return sqrt(num/(denom*denom) + num*num/(pow(denom, 3)))

#def plotLandau():
print 'Plot landau for delta eta delta phi'

file = TFile.Open('./L1MuonHistogram.root')

canvasList = [
	TCanvas("canvasLandau1","Canvas Landau1", 1200,1200),
	TCanvas("canvasLandau2","Canvas Landau2", 1200,1200),
	TCanvas("canvasLandau3","Canvas Landau3", 1200,1200)
	]

for c in canvasList:
	c.Divide(5,5)

nameTrunkList = [
				'hoMuonAnalyzer/etaPhi/etaM2PhiP2_',
				'hoMuonAnalyzer/etaPhi/etaM1PhiP2_',
				'hoMuonAnalyzer/etaPhi/etaP0PhiP2_',
				'hoMuonAnalyzer/etaPhi/etaP1PhiP2_',
				'hoMuonAnalyzer/etaPhi/etaP2PhiP2_',
				
				'hoMuonAnalyzer/etaPhi/etaM2PhiP1_',
				'hoMuonAnalyzer/etaPhi/etaM1PhiP1_',
				'hoMuonAnalyzer/etaPhi/etaP0PhiP1_',
				'hoMuonAnalyzer/etaPhi/etaP1PhiP1_',
				'hoMuonAnalyzer/etaPhi/etaP2PhiP1_',
				
				'hoMuonAnalyzer/etaPhi/etaM2PhiP0_',
				'hoMuonAnalyzer/etaPhi/etaM1PhiP0_',
				'hoMuonAnalyzer/etaPhi/central_',
				'hoMuonAnalyzer/etaPhi/etaP1PhiP0_',
				'hoMuonAnalyzer/etaPhi/etaP2PhiP0_',
				
				'hoMuonAnalyzer/etaPhi/etaM2PhiM1_',
				'hoMuonAnalyzer/etaPhi/etaM1PhiM1_',
				'hoMuonAnalyzer/etaPhi/etaP0PhiM1_',
				'hoMuonAnalyzer/etaPhi/etaP1PhiM1_',
				'hoMuonAnalyzer/etaPhi/etaP2PhiM1_',
				
				'hoMuonAnalyzer/etaPhi/etaM2PhiM2_',
				'hoMuonAnalyzer/etaPhi/etaM1PhiM2_',
				'hoMuonAnalyzer/etaPhi/etaP0PhiM2_',
				'hoMuonAnalyzer/etaPhi/etaP1PhiM2_',
				'hoMuonAnalyzer/etaPhi/etaP2PhiM2_'
				
				]

scenarioNameList = [
				'WithSingleMu'
				,'NoSingleMu'
				,'NoSingleMuAboveThr'
				]


histoList = []
fitList = []

for i,scenario in enumerate(scenarioNameList):
	for j,nameTrunk in enumerate(nameTrunkList):
		canvasList[i].cd(j+1)
		localHist = file.Get( nameTrunk + scenario )
		if(localHist):
			localHist.GetXaxis().SetRangeUser(-.1,5)
			localFit = TF1('fit' + str(i*len(nameTrunkList)+j),"landau")
			localFit.SetParameter(1,0.8)
			if(localHist.GetEntries() > 5):
				localHist.Fit(localFit,"","",0,5)
			histoList.append(localHist)
			fitList.append(localFit)
			localHist.Draw()

for c in canvasList:
	c.Update()

#for i in range(0,9):
#	c.cd(i+1)
#	histoList[i].Draw()

