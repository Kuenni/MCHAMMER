#!/usr/bin/python
import os,sys

from ROOT import TFile,TCanvas,TF1,TH3D,TPaveText,TBox,ROOT

sys.path.append(os.path.abspath("/user/kuensken/ChrisAnelliCode/CMSSW_6_2_0_SLHC11/src/HoMuonTrigger/python"))

import PlotStyle

PlotStyle.setPlotStyle()

def calcSigma(num,denom):
	return sqrt(num/(denom*denom) + num*num/(pow(denom, 3)))

def drawHoBoxes(canvas):
    canvas.cd()
    boxes = []
    for i in range(1,6):
        for j in range(1,6):
            box = TBox(-2.5 + i-1,-2.5 + j-1,-2.5 + i,-2.5 + j)
            box.SetFillStyle(0)
            box.SetLineColor(ROOT.kBlack)
            box.SetLineWidth(2)
            box.Draw()
            boxes.append(box)
    return boxes

def drawFilledBox(ieta,iphi,canvas):
	canvas.cd()
	box = TBox(ieta - 0.5, iphi - 0.5, ieta + 0.5, iphi + 0.5)
	box.SetLineColor(ROOT.kBlack)
	box.SetFillStyle(3013)
	box.SetFillColor(ROOT.kBlack)
	box.Draw()
	return box
	
print 'Plot landau for delta eta delta phi'

file = TFile.Open('./L1MuonHistogram.root')

canvasList = []

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
paveList = []
lowStatisticsList = []
boxList = []

h3D = TH3D("histMpvs","MPV results;Relative i#eta;Relative i#phi;Rec. E / GeV",7,-3.5,3.5,7,-3.5,3.5,20,0,4)


for i,scenario in enumerate(scenarioNameList):
	canvasList.append(	TCanvas("canvasLandau" + str(i),"Canvas Landau" + str(i), 900,900))
	canvasList[-1].Divide(5,5)
	for j,nameTrunk in enumerate(nameTrunkList):
		canvasList[i].cd(j+1)
		localHist = file.Get( nameTrunk + scenario )
		if(localHist):
			localHist.GetXaxis().SetRangeUser(-.1,5)
			histoList.append(localHist)
			localHist.Draw()
			localHist.SetStats(0)
			paveText = TPaveText(0.4,0.6,0.9,0.9,'NDC')
			paveText.AddText('%s: %.2f' % ('Mean',localHist.GetMean()))
			if(localHist.GetEntries() > 3):
				localFit = TF1('fit' + str(i*len(nameTrunkList)+j),"landau")
				localFit.SetParameter(1,0.8)
				localFit.SetParameter(2,0.15)
				if(j == int(len(nameTrunkList)/2)):
					localHist.Fit(localFit,"Q","",0.2,3)
				else:
					localHist.Fit(localFit,"Q","",0.2,3)
				if( i == 2 ):
					localI = j%5
					h3D.Fill(localI - 2 , 2 - j/5 ,localFit.GetParameter(1))
					if(localFit.GetNDF() < 4):
						lowStatisticsList.append([localI - 2, 2 - j/5])		
				paveText.AddText('%s: %.2f' % ('MPV',localFit.GetParameter(1)))
				paveText.AddText('%s: %.2f/%d' % ('#Chi^{2}/NDF',localFit.GetChisquare(),localFit.GetNDF()))
				fitList.append(localFit)
			paveText.SetBorderSize(1)
			paveList.append(paveText)
			paveText.Draw()
		canvasList[i].Update()

canvasList.append(TCanvas("canvasMpv","Canvas MPV",900,0,900,900))
canvasList[3].cd()
projection = h3D.Project3DProfile('yx')
projection.SetStats(0)
projection.GetXaxis().SetTitle(h3D.GetXaxis().GetTitle())
projection.GetYaxis().SetTitle(h3D.GetYaxis().GetTitle())
projection.GetZaxis().SetTitle(h3D.GetZaxis().GetTitle())
projection.Draw('colz')

for coords in lowStatisticsList:
	boxList.append([drawFilledBox(coords[0],coords[1],canvasList[3])])

for c in canvasList:
	c.Update()

pal = projection.GetListOfFunctions().FindObject("palette")
pal.SetX2NDC(0.92)

boxList.append(drawHoBoxes(canvasList[3]))

for c in canvasList:
	c.Update()
	c.SaveAs(c.GetName() + '.pdf')
