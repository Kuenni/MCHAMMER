#!/usr/bin/python
from ROOT import ROOT,gROOT,TCanvas,TFile,TH1D,TH2D,TLegend,THStack,TPaveText, TMarker
import sys,os
import PlotStyle

DEBUG = 1
prefix = '[plotEfficiency] '

markerpairs = []
markerpairs = [	[20,24],[21,25],[22,26],[23,32],[34,28] ]


def plotEfficiencyForPt(folder,pt):
	if(DEBUG):
		print prefix + 'was called'
	
	if(folder == None):
		print prefix + 'Error! Folder as first argument needed.'
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
	
	if(DEBUG):
		print "Getting histogram: %s" % ("hoMuonAnalyzer/efficiency/L1MuonPt" + str(pt) + "_Efficiency")
	
	l1Muon = file.Get("hoMuonAnalyzer/efficiency/L1MuonPt" + str(pt) + "_Efficiency")
	l1MuonAndHo = file.Get("hoMuonAnalyzer/efficiency/L1MuonPt" + str(pt) + "HoReco_Efficiency")
	l1MuonAndHoAboveThr = file.Get("hoMuonAnalyzer/efficiency/L1MuonPt" + str(pt) + "HoRecoAboveThr_Efficiency")
	
	canv = TCanvas("efficiencyCanvas",'efficiencyCanvas',1200,1200)
	
# 	frame = TH2D('frame','L1 Efficiency',1,5,150,1,0,1.1)
# 	frame.SetStats(0)
# 	frame.GetXaxis().SetTitle('p_{T} / GeV')
# 	frame.GetYaxis().SetTitle('Efficiency')
# 	frame.Draw()
	
	l1Muon.SetMarkerStyle(markerpairs[pt/5 -1][0])
	l1MuonAndHo.SetMarkerStyle(21)
	l1MuonAndHoAboveThr.SetMarkerStyle(markerpairs[pt/5 -1][1])
	
	l1Muon.SetMarkerColor(PlotStyle.colorRwthDarkBlue)
	l1MuonAndHo.SetMarkerColor(ROOT.kBlue)
	l1MuonAndHoAboveThr.SetMarkerColor(PlotStyle.colorRwthMagenta)   
	
	l1Muon.SetLineColor(PlotStyle.colorRwthDarkBlue)
	l1MuonAndHo.SetLineColor(ROOT.kBlue)
	l1MuonAndHoAboveThr.SetLineColor(PlotStyle.colorRwthMagenta)
	
	l1Muon.Draw()
#	l1MuonAndHo.Draw('same')
	l1MuonAndHoAboveThr.Draw('same')
	
	canv.Update()
	l1Muon.GetPaintedGraph().GetYaxis().SetTitleFont(62)
	l1Muon.GetPaintedGraph().GetYaxis().SetLabelFont(62)
	l1Muon.GetPaintedGraph().GetXaxis().SetRangeUser(0,40)
	#.GetPaintedGraph()
	l1Muon.SetTitle("Efficiency, p_{T} = " + str(pt) + " GeV;p_{T};Eff.")
	canv.Update()

	legend = TLegend(0.5,0.1,0.9,0.35)
	legend.AddEntry(l1Muon,'L1 Efficiency','ep')
#	legend.AddEntry(l1MuonAndHo,'L1 + HO hits','ep')
	legend.AddEntry(l1MuonAndHoAboveThr,'L1 + HO hits > 0.2 GeV','ep')
	legend.Draw()
	
	canv.SaveAs("plots/" + folder + "/efficiency" + str(pt) + ".png")
	canv.SaveAs("plots/" + folder + "/efficiency" + str(pt) + ".pdf")
	
	f = TFile.Open("plots/" + folder + "/efficiency" + str(pt) + ".root","RECREATE")
	canv.Write()
	f.Close()
	return [l1Muon,l1MuonAndHoAboveThr]

def plotEfficiency(folder):
	histlist = []
	for i in range(5,30,5):
		histlist.append(plotEfficiencyForPt(folder, i))
	return histlist

def plotCombinedEfficiency():
	hl = plotEfficiency('.')
	canv = TCanvas("canvasCombinedEfficiency","Combined efficiency plot",1200,1200)
	leg = TLegend(0.55,0.1,0.9,0.5)
	for i,val in enumerate(hl):
		if(i == 0):
			val[0].Draw()
			val[0].SetTitle("Efficiency for several p_{T}")
		else:
			val[0].Draw('same')
		val[1].Draw('same')
		
	
	hl[0][1].SetFillColor(PlotStyle.colorRwthMagenta)
	hl[0][0].SetFillColor(PlotStyle.colorRwthDarkBlue)
	leg.AddEntry(hl[0][0],"L1","f")
	leg.AddEntry(hl[0][1],"L1 + HO","f")
	markers = []
	for i,pair in enumerate(markerpairs):
		markers.append(TMarker(1,1,pair[0]))
		markers[i].SetMarkerSize(3)
		leg.AddEntry(markers[i],"p_{T} = " + str((i+1)*5) + " GeV","p")
	leg.Draw()
	PlotStyle.labelCmsPrivateSimulation.Draw()
	canv.SaveAs('combinedEfficiency.png')	
	canv.SaveAs('combinedEfficiency.pdf')
	canv.SaveAs('combinedEfficiency.root')			
	return canv,leg