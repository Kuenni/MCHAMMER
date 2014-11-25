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
	L1MuonAndHoMatchAboveThrFilt = file.Get('hoMuonAnalyzer/energy/L1MuonWithHoMatchAboveThrFilt_Energy')

	canv = TCanvas("energieCanvas",'Energy canvas',1200,1200)
	canv.SetLogy()

	ho.SetStats(0)
	ho.SetTitle('Energy distribution of HO hits')
	ho.GetXaxis().SetTitle('Reconstructed HO energy / GeV')
	ho.GetYaxis().SetTitle('N')
	ho.GetXaxis().SetRangeUser(-2,6)

	ho.SetLineColor(ROOT.kBlack)
	ho.SetLineWidth(3)
	ho.Draw()
	
	legend = TLegend(0.5,0.65,0.9,0.9)
	legend.AddEntry(ho,'All HO hits','l')
	legend.Draw()

	if(L1MuonAndHoMatch):
		L1MuonAndHoMatch.SetLineColor(ROOT.kBlue)
		L1MuonAndHoMatch.SetLineWidth(3)
		L1MuonAndHoMatch.Draw('same')
		legend.AddEntry(L1MuonAndHoMatch,'L1Muon + HO match','l')
		
	if(L1MuonAndHoMatchAboveThr):
		L1MuonAndHoMatchAboveThr.SetLineColor(ROOT.kRed)
		L1MuonAndHoMatchAboveThr.SetLineWidth(3)
		L1MuonAndHoMatchAboveThr.Draw('same')
		legend.AddEntry(L1MuonAndHoMatchAboveThr,'L1Muon + HO match > 0.2 GeV','l')


	if(L1MuonAndHoMatchAboveThrFilt):
		L1MuonAndHoMatchAboveThrFilt.SetLineColor(ROOT.kGreen)
		L1MuonAndHoMatchAboveThrFilt.SetLineWidth(3)
		L1MuonAndHoMatchAboveThrFilt.Draw('same')
		legend.AddEntry(L1MuonAndHoMatchAboveThrFilt,'L1Muon + HO match > 0.2 GeV (In Ho Geom.)','l')

	

	canv.SaveAs("plots/" + folder + "/energy.png")
	canv.SaveAs("plots/" + folder + "/energy.pdf")

	f = TFile.Open("plots/" + folder + "/energy.root","RECREATE")
	canv.Write()
	f.Close()
	return canv

def plotEnergyVsEta(folder,sourceHistogram = 'L1MuonWithHoMatch_EnergyVsEta',filename = 'L1MuonHistogram.root'):
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
	if( not os.path.exists(fullname)):
		print 'Error! File ' + fullname + ' does not exist!'
		return
	print 'Opening file:',fullname
	file = TFile.Open(fullname)
	
	PlotStyle.setPlotStyle()

	canv = TCanvas("energieCanvas",'Energy canvas',1200,1200)

	energyVsEta = file.Get("hoMuonAnalyzer/energy/" + sourceHistogram)
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

def plotEnergyVsPhi(folder,sourceHistogram = 'L1MuonWithHoMatch_EnergyVsPhi',filename = 'L1MuonHistogram.root'):
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
	if( not os.path.exists(fullname)):
		print 'Error! File ' + fullname + ' does not exist!'
		return
	print 'Opening file:',fullname
	file = TFile.Open(fullname)
	
	PlotStyle.setPlotStyle()

	canv = TCanvas("energieCanvas",'Energy canvas',1200,1200)

	if(DEBUG):
		print prefix + 'Getting histogram: ' + "hoMuonAnalyzer/energy/" + sourceHistogram
	
	energyVsEta = file.Get("hoMuonAnalyzer/energy/" + sourceHistogram)
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

# Generate the plot based on the energy vs eta and phin histogram
def plotEnergyVsEtaPhi(folder,sourceHistogram = 'L1MuonWithHoMatch_EnergyVsEtaPhi',filename = 'L1MuonHistogram.root'):
	if(DEBUG):
		print prefix + ' energy vs eta phi was called.'
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
	if( not os.path.exists(fullname)):
		print 'Error! File ' + fullname + ' does not exist!'
		return
	print 'Opening file:',fullname
	file = TFile.Open(fullname)
	
	PlotStyle.setPlotStyle()
	canv = TCanvas("energieVsPositionCanvas",'Energy canvas',1200,1200)
	
	if(DEBUG):
		print prefix + 'Getting histogram: ' + "hoMuonAnalyzer/energy/" + sourceHistogram
	
	energyVsPos = file.Get("hoMuonAnalyzer/energy/" + sourceHistogram)
	projection = energyVsPos.Project3DProfile()
	projection.GetXaxis().SetTitle(energyVsPos.GetXaxis().GetTitle())
	projection.GetYaxis().SetTitle(energyVsPos.GetYaxis().GetTitle())
	projection.GetZaxis().SetTitle(energyVsPos.GetZaxis().GetTitle())
	projection.Draw('colz')
	
	canv.Update()
	pal = projection.GetListOfFunctions().FindObject("palette")
	pal.SetX2NDC(0.92)
	
	stats = projection.GetListOfFunctions().FindObject("stats")
	stats.SetX1NDC(.1)
	stats.SetX2NDC(.3)
	stats.SetY1NDC(.7)
	stats.SetY2NDC(.9)
	
	canv.SaveAs("plots/" + folder + "/energyVsPosition.png")
	canv.SaveAs("plots/" + folder + "/energyVsPosition.pdf")

	f = TFile.Open("plots/" + folder + "/energyVsPosition.root","RECREATE")
	canv.Write()
	f.Close()
	return canv
	