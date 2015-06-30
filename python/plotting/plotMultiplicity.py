#!/usr/bin/python
from ROOT import ROOT,gROOT,TCanvas,TFile,TH1D,TH2D,TLegend,THStack,TPaveText
import sys,os
import PlotStyle
import numpy as np

def plotMultiplicity(folder):
	if(folder == None):
		print 'Error! Filename as first argument needed.'
		return

	if( not os.path.exists('plots')):
	    os.mkdir('plots')
	if( not os.path.exists('plots/' + folder)):
		os.mkdir('plots/' + folder)

	filename = folder + '/L1MuonHistogram.root'
	if( not os.path.exists(filename)):
		print 'Error! File ' + filename + ' does not exist!'
		return
	print 'Opening file:',filename
	file = TFile.Open(filename)


	#Set plot style
	PlotStyle.setPlotStyle()

	L1Muon = file.Get('hoMuonAnalyzer/L1MuonPresent_Multiplicity')
	ho = file.Get("hoMuonAnalyzer/horecoAboveThreshold_Multiplicity")

	canv = TCanvas("multiplicityCanvas",'Multiplicity canvas',1200,1200)
	canv.SetLogy()

	ho.SetStats(0)
	ho.SetTitle('Multiplicities')
	ho.GetXaxis().SetTitle('Multiplicity')
	ho.GetYaxis().SetTitle('N')
	ho.GetXaxis().SetRangeUser(-2,6)

	ho.SetLineColor(ROOT.kBlack)
	L1Muon.SetLineColor(ROOT.kRed)
	
	ho.SetLineWidth(3)
	L1Muon.SetLineWidth(3)

	ho.Draw()
	L1Muon.Draw('same')

	legend = TLegend(0.6,0.75,0.9,0.9)
	legend.AddEntry(ho,'HO Rec hits > 0.2 GeV','l')
	legend.AddEntry(L1Muon,'L1 Muons','l')
	legend.Draw()

	canv.SaveAs("plots/" + folder + "/Multiplicity.png")
	canv.SaveAs("plots/" + folder + "/Multiplicity.pdf")

	f = TFile.Open("plots/" + folder + "/Multiplicity.root","RECREATE")
	canv.Write()
	f.Close()
