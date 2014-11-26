#!/usr/bin/python
from ROOT import ROOT,gROOT,gStyle,TCanvas,TFile,TH1D,TH2D,TLegend,THStack,TPaveText,TBox
import sys
import os
import PlotStyle
import numpy as np

sys.path.append(os.path.abspath("/user/kuensken/ChrisAnelliCode/CMSSW_6_2_0_SLHC11/src/HoMuonTrigger/python"))

DEBUG = 1
prefix = '[plotDeltaEtaDeltaPhi] '


PlotStyle.setPlotStyle()
gStyle.SetPalette(1)


def drawHoBoxes(canvas):
    canvas.cd()
    boxes = []
    for i in range(1,8):
        for j in range(1,8):
            box = TBox(-0.3045 + (i-1)*0.087,-0.3045 + (j-1)*0.087,-0.3045 + i*0.087,-0.3045 + j*0.087)
            box.SetFillStyle(0)
            box.SetLineColor(ROOT.kBlack)
            box.SetLineWidth(2)
            box.Draw()
            boxes.append(box)
    return boxes

#Create plot for delta eta and delta phi between two objects
def plotDeltaEtaDeltaPhi(folder,sourceHistogram = 'L1MuonWithHoMatch_DeltaEtaDeltaPhi', sourceFile = 'L1MuonHistogram.root'):

	if(DEBUG):
		print prefix + 'was called'

	if(folder == None):
		print prefix + 'Error! Filename as first argument needed.'
		return
	if( not os.path.exists('plots')):
	    os.mkdir('plots')
	if( not os.path.exists('plots/' + folder)):
		os.mkdir('plots/' + folder)
        
	filename = folder + '/' + sourceFile
	if( not os.path.exists(filename)):
		print 'Error! File ' + filename + ' does not exist!'
		return
	print prefix + 'Opening file:',filename

	file = TFile.Open(filename)

	h2dDeltaEtaDeltaPhi = file.Get("hoMuonAnalyzer/etaPhi/" + sourceHistogram)

	canv = TCanvas("canvasDeltaEtaDeltaPhi",'canvasDeltaEtaDeltaPhi',1200,1200)
	canv.SetLogz()
	h2dDeltaEtaDeltaPhi.GetXaxis().SetRangeUser(-.45,.45)
	h2dDeltaEtaDeltaPhi.GetXaxis().SetTitle("#Delta#eta")
	h2dDeltaEtaDeltaPhi.GetYaxis().SetRangeUser(-.45,.45)
	h2dDeltaEtaDeltaPhi.GetYaxis().SetTitle("#Delta#phi")
	h2dDeltaEtaDeltaPhi.GetZaxis().SetTitle("N")
	h2dDeltaEtaDeltaPhi.Draw("colz")
	boxList = drawHoBoxes(canv)

	canv.Update()
	pal = h2dDeltaEtaDeltaPhi.GetListOfFunctions().FindObject("palette")
	pal.SetX2NDC(0.92)

	stats = h2dDeltaEtaDeltaPhi.GetListOfFunctions().FindObject("stats")
	stats.SetX1NDC(.1)
	stats.SetX2NDC(.2)
	stats.SetY1NDC(.1)
	stats.SetY2NDC(.25)

	legend = TLegend(0.7,0.8,0.9,0.9)
	legend.AddEntry(boxList[0],"HO tile dimensions","le")
	legend.Draw()

	canv.Update();

	canv.SaveAs("plots/" + folder + "/" + sourceHistogram + ".png")
	canv.SaveAs("plots/" + folder + "/" + sourceHistogram + ".pdf")

	f = TFile.Open("plots/" + folder + "/" + sourceHistogram + ".root","RECREATE")
	canv.Write()
	f.Close()
	return canv

#Plots the x-y-projection of the 3D-Histogram
def plotDeltaEtaDeltaPhiEnergyProjection(folder,sourceHistogram = 'NoDoubleMuAboveThr_DeltaEtaDeltaPhiEnergy', sourceFile = 'L1MuonHistogram.root'):

	if(DEBUG):
		print prefix + 'was called'

	if(folder == None):
		print prefix + 'Error! Filename as first argument needed.'
		return
	if( not os.path.exists('plots')):
	    os.mkdir('plots')
	if( not os.path.exists('plots/' + folder)):
		os.mkdir('plots/' + folder)
        
	filename = folder + '/' + sourceFile
	if( not os.path.exists(filename)):
		print 'Error! File ' + filename + ' does not exist!'
		return
	print prefix + 'Opening file:',filename

	file = TFile.Open(filename)
	
	sourceHisto = file.Get("hoMuonAnalyzer/etaPhi/" + sourceHistogram)
	histo = sourceHisto.Project3DProfile('yx')

	canv = TCanvas("canvasDeltaEtaDeltaPhiEnergy",'canvasDeltaEtaDeltaPhiEnergy',1200,1200)
	histo.GetXaxis().SetRangeUser(-.45,.45)
	histo.GetXaxis().SetTitle("#Delta#eta")
	histo.GetYaxis().SetRangeUser(-.45,.45)
	histo.GetYaxis().SetTitle("#Delta#phi")
	histo.GetZaxis().SetTitle(sourceHisto.GetZaxis().GetTitle())
	histo.Draw("colz")
	boxList = drawHoBoxes(canv)

	canv.Update()
	pal = histo.GetListOfFunctions().FindObject("palette")
	pal.SetX2NDC(0.92)

	stats = histo.GetListOfFunctions().FindObject("stats")
	stats.SetX1NDC(.1)
	stats.SetX2NDC(.2)
	stats.SetY1NDC(.1)
	stats.SetY2NDC(.25)

	legend = TLegend(0.7,0.8,0.9,0.9)
	legend.AddEntry(boxList[0],"HO tile dimensions","le")
	legend.Draw()

	canv.Update();

	canv.SaveAs("plots/" + folder + "/" + sourceHistogram + ".png")
	canv.SaveAs("plots/" + folder + "/" + sourceHistogram + ".pdf")

	f = TFile.Open("plots/" + folder + "/" + sourceHistogram + ".root","RECREATE")
	canv.Write()
	f.Close()
	return histo
