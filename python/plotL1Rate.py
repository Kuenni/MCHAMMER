#!/usr/bin/python
from ROOT import ROOT,gROOT,TCanvas,TFile,TH1D,TH2D,TLegend,THStack,TPaveText
import sys,os
import PlotStyle
import numpy as np

DEBUG = 1
prefix = '[plotL1Rates] '

def plotL1Rates(folder):
    
    if(DEBUG):
	print prefix + 'was called'
	
	if(folder == None):
		print prefix + 'Error! Filename as first argument needed.'
		sys.exit(1)
		
	if( not os.path.exists('plots')):
		os.mkdir('plots')
   	if( not os.path.exists('plots/' + folder)):
		os.mkdir('plots/' + folder)
	
	filename = folder + '/L1MuonHistogram.root'
	print prefix + 'Opening file:',filename
    
    file = TFile.Open(filename)
    
    l1Muon_TrigRate = file.Get("hoMuonAnalyzer/L1Muon_TrigRate")
    l1MuWithHoMatch_TrigRate = file.Get('hoMuonAnalyzer/L1MuonWithHoMatch'
   #     HORecowithMipMatch
        '_TrigRate')
#    genMuons_TrigRate = file.Get('demo/gen_TrigRate')
    
    canv = TCanvas("pseudoTrigRateCanvas",'pseudoTrigRateCanvas')
    canv.cd(1).SetLogy()
    
    l1Muon_TrigRate.SetStats(0)
    l1Muon_TrigRate.GetXaxis().SetTitle('P_{T} Schwelle / GeV')
    l1Muon_TrigRate.GetYaxis().SetTitle('Anzahl Eintr#ddot{a}ge / 2 GeV')
 
    
    l1Muon_TrigRate.SetMarkerStyle(21)
    l1MuWithHoMatch_TrigRate.SetMarkerStyle(20)
#    genMuons_TrigRate.SetMarkerStyle(22)

    l1Muon_TrigRate.SetMarkerColor(ROOT.kBlue)
    l1MuWithHoMatch_TrigRate.SetMarkerColor(ROOT.kRed)
#    genMuons_TrigRate.SetMarkerColor(ROOT.kBlack)
    
    l1Muon_TrigRate.SetLineColor(ROOT.kBlack)    
    l1MuWithHoMatch_TrigRate.SetLineColor(ROOT.kBlack)
#    genMuons_TrigRate.SetLineColor(ROOT.kBlack)
    
    l1Muon_TrigRate.Rebin(2)
    l1MuWithHoMatch_TrigRate.Rebin(2)
    
    l1Muon_TrigRate.GetXaxis().SetRangeUser(0,140)
    
    l1Muon_TrigRate.Draw('p,e1')
    l1MuWithHoMatch_TrigRate.Draw('same,p,e1')
#    genMuons_TrigRate.Draw('same,p,e1')
    
    legend = TLegend(0.5,0.65,0.9,0.9)
    legend.AddEntry(l1Muon_TrigRate,'L1 Myonen','ep')
    legend.AddEntry(l1MuWithHoMatch_TrigRate,'L1 Myonen mit HO-Match','ep')
  #  legend.AddEntry(genMuons_TrigRate,'Gen Myonen','ep')
    legend.Draw()
    
    canv.SaveAs("plots/" + folder + "/PseudoTrigRateL1.png")
    canv.SaveAs("plots/" + folder + "/PseudoTrigRateL1.pdf")
    
    f = TFile.Open("plots/" + folder + "/PseudoTrigRatePlotsL1.root","RECREATE")
    canv.Write()
    f.Close()
    
