#!/usr/bin/python
from ROOT import ROOT,gROOT,TCanvas,TFile,TH1D,TH2D,TLegend,THStack,TPaveText
import sys,os
import PlotStyle
import numpy as np

DEBUG = 1
prefix = '[plotEnergy] '

def plotEnergy(folder):
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

	ho = file.Get("hoMuonAnalyzer/energy/horeco_Energy")
	L1MuonAndHoMatch = file.Get('hoMuonAnalyzer/energy/L1MuonWithHoMatch_Energy')
	L1MuonAndHoMatchAboveThr = file.Get('hoMuonAnalyzer/energy/L1MuonWithHoMatchAboveThr_Energy')

	canv = TCanvas("energieCanvas",'Energy canvas',1200,1200)
	canv.SetLogy()

	ho.SetStats(0)
	ho.SetTitle('Energy distribution of HO hits')
	ho.GetXaxis().SetTitle('Reconstructed HO energy / GeV')
	ho.GetYaxis().SetTitle('N')
	ho.GetXaxis().SetRangeUser(-2,6)

	ho.SetLineColor(ROOT.kBlack)
	L1MuonAndHoMatch.SetLineColor(ROOT.kBlue)
	L1MuonAndHoMatchAboveThr.SetLineColor(ROOT.kRed)

	ho.SetLineWidth(3)
	L1MuonAndHoMatch.SetLineWidth(3)
	L1MuonAndHoMatchAboveThr.SetLineWidth(3)

	ho.Draw()
	L1MuonAndHoMatch.Draw('same')
	L1MuonAndHoMatchAboveThr.Draw('same')

	legend = TLegend(0.5,0.65,0.9,0.9)
	legend.AddEntry(ho,'All HO hits','l')
	legend.AddEntry(L1MuonAndHoMatch,'L1Muon + HO match','l')
	legend.AddEntry(L1MuonAndHoMatchAboveThr,'L1Muon + HO match > 0.2 GeV','l')
	legend.Draw()

	canv.SaveAs("plots/" + folder + "/energy.png")
	canv.SaveAs("plots/" + folder + "/energy.pdf")

	f = TFile.Open("plots/" + folder + "/energy.root","RECREATE")
	canv.Write()
	f.Close()
	return canv

def plotEnergyVsEta(folder,filename = 'L1MuonHistogram.root'):
	if(DEBUG):
		print prefix + ' energy vs eta was called.'
	if(folder == None):
		print 'Error! Folder as first argument needed.'
		return

	if( not os.path.exists('plots')):
		if(DEBUG):
			print prefix + ' creating dir plots.'
		os.mkdir('plots')
	if( not os.path.exists('plots/' + folder)):
		if(DEBUG):
			print prefix + ' creating dir plots/' + folder + '.'
		os.mkdir('plots/' + folder)

	fullname = folder + '/' + filename
	print 'Opening file:',fullname
	file = TFile.Open(fullname)
	
	PlotStyle.setPlotStyle()

	canv = TCanvas("energieCanvas",'Energy canvas',1200,1200)

	energyVsEta = file.Get("hoMuonAnalyzer/energy/L1MuonWithHoMatch_EnergyVsEta")
	energyVsEta.Rebin2D(10,1)
	energyVsEta.GetXaxis().SetRangeUser(-1.1,1.1)
	energyVsEta.GetYaxis().SetRangeUser(0,2.5)
	energyVsEta.SetStats(0)

	energyVsEta.GetZaxis().SetTitle('Entries / 0.05 GeV')
	
	energyVsEta.Draw('colz')
	
	canv.Update()
	pal = energyVsEta.GetListOfFunctions().FindObject("palette")
	pal.SetX2NDC(0.92)
	
	canv.SaveAs("plots/" + folder + "/energyVsEta.png")
	canv.SaveAs("plots/" + folder + "/energyVsEta.pdf")

	f = TFile.Open("plots/" + folder + "/energyVsEta.root","RECREATE")
	canv.Write()
	f.Close()
	return canv

def plotEnergyVsPhi(folder,filename = 'L1MuonHistogram.root'):
	if(DEBUG):
		print prefix + ' energy vs phi was called.'
	if(folder == None):
		print 'Error! Folder as first argument needed.'
		return

	if( not os.path.exists('plots')):
		if(DEBUG):
			print prefix + ' creating dir plots.'
		os.mkdir('plots')
	if( not os.path.exists('plots/' + folder)):
		if(DEBUG):
			print prefix + ' creating dir plots/' + folder + '.'
		os.mkdir('plots/' + folder)

	fullname = folder + '/' + filename
	print 'Opening file:',fullname
	file = TFile.Open(fullname)
	
	PlotStyle.setPlotStyle()

	canv = TCanvas("energieCanvas",'Energy canvas',1200,1200)

	energyVsEta = file.Get("hoMuonAnalyzer/energy/L1MuonWithHoMatch_EnergyVsPhi")
	energyVsEta.Rebin2D(10,1)
	energyVsEta.GetXaxis().SetRangeUser(-3.17,3.17)
	energyVsEta.GetYaxis().SetRangeUser(0,2.5)
	energyVsEta.SetStats(0)

	energyVsEta.GetZaxis().SetTitle('Entries / 0.05 GeV')
	
	energyVsEta.Draw('colz')
	
	canv.Update()
	pal = energyVsEta.GetListOfFunctions().FindObject("palette")
	pal.SetX2NDC(0.92)
	
	canv.SaveAs("plots/" + folder + "/energyVsPhi.png")
	canv.SaveAs("plots/" + folder + "/energyVsPhi.pdf")

	f = TFile.Open("plots/" + folder + "/energyVsPhi.root","RECREATE")
	canv.Write()
	f.Close()
	return canv