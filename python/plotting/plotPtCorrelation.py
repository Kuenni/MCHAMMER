#!/usr/bin/python
from ROOT import ROOT,gROOT,TCanvas,TFile,TH1D,TH2D,TLegend,THStack,TPaveText
import sys,os
import PlotStyle

DEBUG = 1
prefix = '[plotPtCorrelation] '

def plotPtCorrelation(folder,filename = 'L1MuonHistogram.root'):
	if(DEBUG):
		print prefix + 'was called'
	
	if(folder == None):
		print prefix + 'Error! Folder as first argument needed.'
		return
		
	if( not os.path.exists('plots')):
		os.mkdir('plots')
   	if( not os.path.exists('plots/' + folder)):
		os.mkdir('plots/' + folder)
	
	fullname = folder + '/' + filename
	if( not os.path.exists(fullname)):
		print 'Error! File ' + fullname + ' does not exist!'
		return
	print 'Opening file:',fullname
	file = TFile.Open(fullname)
	
	#Set plot style
	PlotStyle.setPlotStyle()
	
	l1Muon = file.Get("hoMuonAnalyzer/L1Muon_PtCorrelation")
	
	canv = TCanvas("ptCorrelationCanvas",'ptCorrelationCanvas',1200,1200)
	
# 	frame = TH2D('frame','L1 Efficiency',1,5,150,1,0,1.1)
# 	frame.SetStats(0)
# 	frame.GetXaxis().SetTitle('p_{T} / GeV')
# 	frame.GetYaxis().SetTitle('Efficiency')
# 	frame.Draw()
	
	l1Muon.SetMarkerStyle(20)

	l1Muon.SetMarkerColor(ROOT.kBlack)
	
	l1Muon.SetLineColor(ROOT.kBlack)

	l1Muon.GetXaxis().SetRangeUser(97,103)
	l1Muon.GetXaxis().SetTitle('p_{T} Gen / GeV')
	l1Muon.GetYaxis().SetTitle('p_{T} L1Muon / GeV')
	l1Muon.GetYaxis().SetRangeUser(0,150)

	l1Muon.Draw('colz')
	
	
	canv.Update()
	pal = l1Muon.GetListOfFunctions().FindObject("palette")
	pal.SetX2NDC(0.92)
	canv.SaveAs("plots/" + folder + "/ptCorrelation.png")
	canv.SaveAs("plots/" + folder + "/ptCorrelation.pdf")
	
	f = TFile.Open("plots/" + folder + "/Efficiency.root","RECREATE")
	canv.Write()
	f.Close()
	return canv
