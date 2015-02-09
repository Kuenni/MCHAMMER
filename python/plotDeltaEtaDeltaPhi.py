#!/usr/bin/python
from ROOT import ROOT,gROOT,gStyle,TCanvas,TFile,TH1D,TH2D,TH2F,TLegend,THStack,TPaveText,TBox
import sys
import os
sys.path.append(os.path.abspath("../../python"))
import PlotStyle
import numpy as np


DEBUG = 1
prefix = '[plotDeltaEtaDeltaPhi] '

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
def plotDeltaEtaDeltaPhi(folder,sourceHistogram = 'L1MuonWithHoMatch_DeltaEtaDeltaPhi', sourceFile = 'L1MuonHistogram.root',storeSubdir = 'deltaEtaDeltaPhi'):

	if(DEBUG):
		print prefix + 'was called'

	if(folder == None):
		print prefix + 'Error! Filename as first argument needed.'
		return
	if( not os.path.exists('plots')):
	    os.mkdir('plots')
	if( not os.path.exists('plots/' + storeSubdir)):
		os.mkdir('plots/' + storeSubdir)
        
	filename = folder + '/' + sourceFile
	if( not os.path.exists(filename)):
		print 'Error! File ' + filename + ' does not exist!'
		return
	print prefix + 'Opening file:',filename

	file = TFile.Open(filename)
	PlotStyle.setPlotStyle()
	h2dDeltaEtaDeltaPhi = file.Get("hoMuonAnalyzer/etaPhi/" + sourceHistogram)
	hEventCount = file.Get("hoMuonAnalyzer/count/Events_Count")
	hNoTrgCount = file.Get("hoMuonAnalyzer/count/NoSingleMu_Count")
	if(h2dDeltaEtaDeltaPhi == None):
		print 'Could not get histogram %s from file %s'%("hoMuonAnalyzer/etaPhi/" + sourceHistogram,filename)
	
	canv = TCanvas("canvasDeltaEtaDeltaPhi" + sourceHistogram,'canvasDeltaEtaDeltaPhi',1200,1200)
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

	paveText = TPaveText(0.2,0.1,0.65,0.2,'NDC')
	paveText.AddText('Total Events: %d' % (hEventCount.GetBinContent(2)))
	paveText.AddText('Events with no Single #mu Trg: %d' % (hNoTrgCount.GetBinContent(2)))
	paveText.SetBorderSize(1)
	paveText.Draw()

	PlotStyle.labelCmsPrivateSimulation.Draw()

	legend = TLegend(0.7,0.8,0.9,0.9)
	legend.AddEntry(boxList[0],"HO tile dimensions","le")
	legend.Draw()

	canv.SaveAs("plots/" + storeSubdir + "/" + sourceHistogram + ".png")
	canv.SaveAs("plots/" + storeSubdir + "/" + sourceHistogram + ".pdf")
	canv.SaveAs("plots/" + storeSubdir + "/" + sourceHistogram + ".root")

	if(h2dDeltaEtaDeltaPhi == None):
		print 'Why is the hist None?!'
	return [h2dDeltaEtaDeltaPhi,canv,legend,boxList,stats,pal,paveText]

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
	PlotStyle.setPlotStyle()

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
