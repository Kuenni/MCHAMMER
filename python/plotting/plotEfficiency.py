#!/usr/bin/python
from ROOT import ROOT,gROOT,TCanvas,TFile,TH1D,TH2D,TLegend,THStack,TPaveText, TMarker,TLine,gPad,TF1,TF2,TGraph,Double,TPad
import sys,os,math
from plotting.PlotStyle import calcSigma,setPlotStyle,colorRwthDarkBlue,colorRwthMagenta,drawLabelCmsPrivateSimulation
from plotting.RootFileHandler import RootFileHandler

DEBUG = 1
prefix = '[plotEfficiency] '

markerpairs = [	[20,24],[21,25],[22,26],[23,32],[34,28] ]

if len(sys.argv) < 2:
	print 'First argument has to be the file name scheme!'
fileHandler = RootFileHandler(sys.argv[1])
fileHandler.printStatus()

if( not os.path.exists('plots')):
	os.mkdir('plots')
if( not os.path.exists('plots/efficiency')):
	os.mkdir('plots/efficiency')

setPlotStyle()

def plotEfficiencyForPt(folder,pt):
	if(DEBUG):
		print prefix + 'was called'
	
	#Set plot style
	
	if(DEBUG):
		print prefix + "Getting histogram: %s" % ("hoMuonAnalyzer/efficiency/GenAndL1MuonPt" + str(pt) + "_Efficiency")
	
	l1Muon = fileHandler.getHistogram("hoMuonAnalyzer/efficiency/GenAndL1MuonPt" + str(pt) + "_Efficiency")
	l1MuonAndHo = fileHandler.getHistogram("hoMuonAnalyzer/efficiency/L1MuonHoRecoPt" + str(pt) + "_Efficiency")
	if(DEBUG):
		print prefix + "Getting histogram: %s" % ("hoMuonAnalyzer/efficiency/GenAndL1MuonAndHoAboveThrPt" + str(pt) + "_Efficiency")
	l1MuonAndHoAboveThr = fileHandler.getHistogram("hoMuonAnalyzer/efficiency/GenAndL1MuonAndHoAboveThrPt" + str(pt) + "_Efficiency")
	
	canv = TCanvas("efficiencyCanvas" + str(pt),'efficiencyCanvas' + str(pt),1200,1200)
	
	l1Muon.SetMarkerStyle(markerpairs[pt/5 -1][0])
	l1MuonAndHo.SetMarkerStyle(21)
	l1MuonAndHoAboveThr.SetMarkerStyle(markerpairs[pt/5 -1][1])
	
	l1Muon.SetMarkerColor(colorRwthDarkBlue)
	l1MuonAndHo.SetMarkerColor(ROOT.kBlue)
	l1MuonAndHoAboveThr.SetMarkerColor(colorRwthMagenta)   
	
	l1Muon.SetLineColor(colorRwthDarkBlue)
	l1MuonAndHo.SetLineColor(ROOT.kBlue)
	l1MuonAndHoAboveThr.SetLineColor(colorRwthMagenta)
	
	upperPad = TPad("upperPad", "upperPad", .005, .25, .995, .995);
	lowerPad = TPad("lowerPad", "lowerPad", .005, .005, .995, .25);
	upperPad.SetBottomMargin(0)
	lowerPad.SetTopMargin(0)
	upperPad.Draw()
	lowerPad.Draw()
	upperPad.cd()
	l1Muon.Draw()
#	l1MuonAndHo.Draw('same')
	l1MuonAndHoAboveThr.Draw('same')
	
	canv.Update()
	l1Muon.GetPaintedGraph().GetYaxis().SetTitleFont(62)
	l1Muon.GetPaintedGraph().GetYaxis().SetLabelFont(62)
	l1Muon.GetPaintedGraph().GetXaxis().SetRangeUser(0,50)
	#.GetPaintedGraph()
	l1Muon.SetTitle("Efficiency, p_{T} = " + str(pt) + " GeV;p_{T};Eff.")
	canv.Update()

	line = TLine(pt,0,pt,1)
	line.SetLineColor(ROOT.kRed)
	line.SetLineWidth(2)
	line.Draw()

	legend = TLegend(0.5,0.1,0.9,0.35)
	legend.AddEntry(l1Muon,'L1 Efficiency','ep')
	legend.AddEntry(l1MuonAndHoAboveThr,'L1 + HO hits > 0.2 GeV','ep')
	legend.AddEntry(line,'Trg. threshold','e')
	legend.Draw()
	
	integralL1 = 0
	integralL1AndHo = 0
	for i in range(0,pt+1):
		integralL1 += l1Muon.GetPassedHistogram().GetBinContent(pt+1)
		integralL1AndHo += l1MuonAndHoAboveThr.GetPassedHistogram().GetBinContent(pt+1)

	paveText = TPaveText(0.5,0.35,0.9,0.4,'NDC')
	if(not integralL1 == 0):
		paveText.AddText('%s: %.2f%% #pm %.2f%%' % ('Reduction below threshold',100 - integralL1AndHo/integralL1*100,calcSigma(integralL1AndHo, integralL1)*100))
		paveText.SetBorderSize(1)
		paveText.Draw()

	label = drawLabelCmsPrivateSimulation()
	##### Try creating residuals
	lowerPad.cd()
	l1MuonGraph = l1Muon.GetPaintedGraph()
	l1MuonAndHoAboveThrGraph = l1MuonAndHoAboveThr.GetPaintedGraph()

	newGraph = TGraph()

	x1 = Double(0)
	y1 = Double(0)
	x2 = Double(0)
	y2 = Double(0)
	
	for i in range(0,50):
		l1MuonGraph.GetPoint(i,x1,y1)
		l1MuonAndHoAboveThrGraph.GetPoint(i,x2,y2)
		newGraph.SetPoint(i,x1,(y1-y2)*100)
	
	
	newGraph.SetMarkerStyle(20)
	newGraph.GetYaxis().SetTitle("%")
	newGraph.Draw("a,p")
	newGraph.GetXaxis().SetLimits(0,50)
	line2 = TLine(0,0,50,0)
	line2.SetLineColor(ROOT.kRed)
	line2.SetLineWidth(2)
	line2.Draw()
	
	##### Finally save the stuff
	
	canv.SaveAs("plots/efficiency/efficiency" + str(pt) + ".png")
	canv.SaveAs("plots/efficiency/efficiency" + str(pt) + ".pdf")
	
	f = TFile.Open("plots/efficiency/efficiency" + str(pt) + ".root","RECREATE")
	canv.Write()
	f.Close()
	return [l1Muon,l1MuonAndHoAboveThr,canv,legend,line,paveText,label,newGraph]

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
		
	
	hl[0][1].SetFillColor(colorRwthMagenta)
	hl[0][0].SetFillColor(colorRwthDarkBlue)
	leg.AddEntry(hl[0][0],"L1","f")
	leg.AddEntry(hl[0][1],"L1 + HO","f")
	markers = []
	for i,pair in enumerate(markerpairs):
		markers.append(TMarker(1,1,pair[0]))
		markers[i].SetMarkerSize(3)
		leg.AddEntry(markers[i],"p_{T} = " + str((i+1)*5) + " GeV","p")
	leg.Draw()
	
	label = drawLabelCmsPrivateSimulation()
	
	if( not os.path.exists('plots')):
		os.mkdir('plots')
	if( not os.path.exists('plots/efficiency')):
		os.mkdir('plots/efficiency')
	
	canv.SaveAs('plots/efficiency/combinedEfficiency.png')	
	canv.SaveAs('plots/efficiency/combinedEfficiency.pdf')
	canv.SaveAs('plots/efficiency/combinedEfficiency.root')			
	return canv,leg,hl,label

def plotEfficiencyPerHoTiles(dataSource = 'L1Muon',gridsize = 0):
	gridType = ''
	if (gridsize == 0) :
		gridType = 'Central'
	else:
		gridType = '3x3'
	
	fullName = 'hoMuonAnalyzer/efficiency/' + dataSource + gridType + '_Efficiency'
	
	if( not os.path.exists('plots')):
		os.mkdir('plots')
	if( not os.path.exists('plots/effPerGrid')):
		os.mkdir('plots/effPerGrid')
	
	c = TCanvas("eff" + dataSource + gridType, "Efficiency " + dataSource + " " + gridType)

	graph = fileHandler.getHistogram(fullName)
	
	graph.SetMarkerStyle(20)
	graph.SetMarkerColor(colorRwthDarkBlue)
	
	graph.Draw()
	c.Update()
	graph.GetPaintedGraph().GetYaxis().SetTitleFont(62)
	graph.GetPaintedGraph().GetYaxis().SetLabelFont(62)
	graph.GetPaintedGraph().GetXaxis().SetRangeUser(0,50)
	
	c.Update()
	c.SaveAs('plots/effPerGrid/'+dataSource+gridType+'.pdf')
	
	return [c,graph]
	