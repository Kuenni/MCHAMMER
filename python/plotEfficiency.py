#!/usr/bin/python
from ROOT import ROOT,gROOT,TCanvas,TFile,TH1D,TH2D,TLegend,THStack,TPaveText
import sys,os
import PlotStyle

DEBUG = 1
prefix = '[plotEfficiency] '

def plotEfficiency(folder):
	if(DEBUG):
		print prefix + 'was called'
	
	if(folder == None):
		print prefix + 'Error! Filename as first argument needed.'
		return
		
	if( not os.path.exists('plots')):
		os.mkdir('plots')
   	if( not os.path.exists('plots/' + folder)):
		os.mkdir('plots/' + folder)
	
	filename = folder + '/L1MuonHistogram.root'
	if( not os.path.exists(filename)):
		print 'Error! File ' + filename + ' does not exist!'
		return
	print prefix + 'Opening file:',filename
	
	file = TFile.Open(filename)
	
	#Set plot style
	PlotStyle.setPlotStyle()
	
	l1Muon = file.Get("hoMuonAnalyzer/efficiency/L1MuonPt20_Efficiency")
	l1MuonAndHo = file.Get("hoMuonAnalyzer/efficiency/L1MuonPt20HoReco_Efficiency")
	l1MuonAndHoAboveThr = file.Get("hoMuonAnalyzer/efficiency/L1MuonPt20HoRecoAboveThr_Efficiency")
	
	canv = TCanvas("efficiencyCanvas",'efficiencyCanvas',1200,1200)
	
	frame = TH2D('frame','L1 Efficiency',1,5,150,1,0,1.1)
	frame.SetStats(0)
	frame.GetXaxis().SetTitle('p_{T} / GeV')
	frame.GetYaxis().SetTitle('Efficiency')
	frame.Draw()
	
	l1Muon.SetMarkerStyle(20)
	l1MuonAndHo.SetMarkerStyle(21)
	l1MuonAndHoAboveThr.SetMarkerStyle(22)
	
	l1Muon.SetMarkerColor(ROOT.kBlack)
	l1MuonAndHo.SetMarkerColor(ROOT.kBlue)
	l1MuonAndHoAboveThr.SetMarkerColor(ROOT.kRed)   
	
	l1Muon.SetLineColor(ROOT.kBlack)
	l1MuonAndHo.SetLineColor(ROOT.kBlue)
	l1MuonAndHoAboveThr.SetLineColor(ROOT.kRed)
	
	l1Muon.Draw('same')
	l1MuonAndHo.Draw('same')
	l1MuonAndHoAboveThr.Draw('same')
	
	legend = TLegend(0.5,0.1,0.9,0.35)
	legend.AddEntry(l1Muon,'L1 Efficiency','ep')
	legend.AddEntry(l1MuonAndHo,'L1 + HO hits','ep')
	legend.AddEntry(l1MuonAndHoAboveThr,'L1 + HO hits > 0.2 GeV','ep')
	legend.Draw()
	
	canv.SaveAs("plots/" + folder + "/Efficiency.png")
	canv.SaveAs("plots/" + folder + "/Efficiency.pdf")
	
	f = TFile.Open("plots/" + folder + "/Efficiency.root","RECREATE")
	canv.Write()
	f.Close()
