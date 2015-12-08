#!/usr/bin/python
import os
from plotting.Plot import Plot
from ROOT import TCanvas,ROOT,TFile,TF1,TLine,gROOT,TPaveText,TH1D,Double,TH2D,THStack,gStyle
from plotting.PlotStyle import setPlotStyle,drawLabelCmsPrivateSimulation,colorRwthDarkBlue,\
	setStatBoxOptions, setStatBoxPosition, setupPalette, drawLabelCmsPrivateData
from plotting.PlotStyle import colorRwthMagenta,setupAxes,printProgress
from plotting.RootFileHandler import RootFileHandler
from plotting.OutputModule import CommandLineHandler
from array import array
import math


class ControlPlots(Plot):
	
	def __init__(self,filename,data = False):
		Plot.__init__(self,filename,data)
		gROOT.ProcessLine(".L $HOMUONTRIGGER_BASE/python/loader.C+");
		self.createPlotSubdir('controlPlots')

	def getIEtaIPhiPlot(self,key):
	#	canvas = TCanvas('cHoIEtaIPhi' + key,'HO iEta iPhi',0,50,600,500)
		hoEtaPhi = self.fileHandler.getHistogram('hoMuonAnalyzer/etaPhi/' + key + '_iEtaIPhi')
		hoEtaPhi.SetTitle('HO RecHits > 0.2GeV;i#eta;i#phi;# entries')
		hoEtaPhi.Draw('colz')
	#	canvas.Update()
		hoEtaPhi.SetStats(0)
		setupAxes(hoEtaPhi)
	#	setupPalette(hoEtaPhi)
	#	label = self.drawLabel()
	#	canvas.Update()
		return hoEtaPhi#,label,canvas

	def plotIEtaIPhiOnSameScales(self):
		canvas = TCanvas('gfdhgfdhg','kjfgkjhg',1900,500)
		canvas.Divide(3,1)
		canvas.cd(1).SetLogz()
		res1 = self.getIEtaIPhiPlot('hoRecHitsAboveThr')
		canvas.cd(2).SetLogz()
		res2 = self.getIEtaIPhiPlot('L1Muon3x3')
		res2.SetMaximum(res1.GetMaximum())
		canvas.cd(3).SetLogz()
		res3 = self.getIEtaIPhiPlot('L1TightMuons3x3')
		res3.SetMaximum(res1.GetMaximum())
		canvas.Update()
		res2.SetTitle('L1 #Rightarrow ' + res2.GetTitle())
		res3.SetTitle('L1 Tight #Rightarrow ' + res3.GetTitle())
		canvas.cd(1)
		setupPalette(res1)
		label1 = self.drawLabel()
		canvas.cd(1).Update()
		canvas.cd(2)
		setupPalette(res2)
		label2 = self.drawLabel()
		canvas.Update()
		canvas.cd(3)
		setupPalette(res3)
		label3 = self.drawLabel()
		canvas.Update()
		canvas.SaveAs('plots/controlPlots/hoIEtaIPhiSameScales.gif')
		return res1,res2,res3,canvas,label1,label2,label3
		
	'''
	Plot the eta phi distribution of HO > Thr
	'''
	def plotHoIEtaIPhi(self):
		canvas = TCanvas('cHoIEtaIPhi','HO iEta iPhi',0,50,600,500)
		hoEtaPhi = self.fileHandler.getHistogram('hoMuonAnalyzer/etaPhi/hoRecHitsAboveThr_iEtaIPhi')
		hoEtaPhi.SetTitle('HO RecHits > 0.2GeV;i#eta;i#phi;# entries')
		hoEtaPhi.Draw('colz')
		canvas.Update()
		hoEtaPhi.SetStats(0)
		setupAxes(hoEtaPhi)
		setupPalette(hoEtaPhi)
		label = self.drawLabel()
		canvas.Update()
		canvas.SaveAs('plots/controlPlots/HoEtaPhi.pdf')
		return label,canvas,hoEtaPhi

	
	'''
	Plot the eta phi distribution of HO > Thr matched to L1
	'''
	def plotHoEtaPhiMatchedToL1(self):
		canvas = TCanvas('cHoEtaPhiAndL1','HO Eta Phi And L1')
		hoEtaPhi = self.fileHandler.getHistogram('hoMuonAnalyzer/etaPhi/L1MuonWithHoMatchAboveThr_HO_EtaPhi')
		hoEtaPhi.SetTitle('L1 matched to HO RecHits > 0.2GeV;#eta_{HO};#phi_{HO};# entries')
		hoEtaPhi.Rebin2D(10,10)
		hoEtaPhi.GetXaxis().SetRangeUser(-1.5,1.5)
		hoEtaPhi.Draw('colz')
		canvas.Update()
		hoEtaPhi.SetStats(0)
		setupAxes(hoEtaPhi)
		setupPalette(hoEtaPhi)
		label = self.drawLabel()
		canvas.Update()
		canvas.SaveAs('plots/controlPlots/L1MatchedToHoEtaPhi.pdf')
		return label,canvas,hoEtaPhi
		
	'''
	Plot the eta phi distribution of HO > Thr matched to Tight L1
	'''
	def plotHoEtaPhiMatchedToTightL1(self):
		canvas = TCanvas('cHoEtaPhiAndTightL1','HO Eta Phi And Tight L1')
		hoEtaPhi = self.fileHandler.getHistogram('hoMuonAnalyzer/etaPhi/patMuonsTight_HO_EtaPhi')
		hoEtaPhi.SetTitle('Tight L1 matched to HO RecHits > 0.2GeV;#eta_{HO};#phi_{HO};# entries')
		hoEtaPhi.Rebin2D(10,10)
		hoEtaPhi.GetXaxis().SetRangeUser(-1.5,1.5)
		hoEtaPhi.Draw('colz')
		canvas.Update()
		hoEtaPhi.SetStats(0)
		setupAxes(hoEtaPhi)
		setupPalette(hoEtaPhi)
		label = self.drawLabel()
		canvas.Update()
		canvas.SaveAs('plots/controlPlots/tightPatToHoEtaPhi.pdf')
		return label,canvas,hoEtaPhi
		
	'''
	Plot the ieta iphi distribution of HO > Thr matched to tight L1
	'''
	def plotHoIEtaIPhiMatchedToTightL1(self):
		canvas = TCanvas('cHoIEtaIPhiAndTightL1','HO iEta iPhi And Tight L1',1300,50,600,500)
		hoEtaPhi = self.fileHandler.getHistogram('hoMuonAnalyzer/etaPhi/L1TightMuons3x3_iEtaIPhi')
		hoEtaPhi.SetTitle('Tight L1 matched to HO RecHits > 0.2GeV;i#eta;i#phi;# entries')
		hoEtaPhi.Draw('colz')
		canvas.Update()
		hoEtaPhi.SetStats(0)
		setupAxes(hoEtaPhi)
		setupPalette(hoEtaPhi)
		label = self.drawLabel()
		canvas.Update()
		canvas.SaveAs('plots/controlPlots/tightL1MatchedToHoIEtaIPhi.pdf')
		return label,canvas,hoEtaPhi

	'''
	Plot the ieta iphi distribution of HO > Thr matched to L1
	'''
	def plotHoIEtaIPhiMatchedToL1(self):
		canvas = TCanvas('cHoIEtaIPhiAndL1','HO iEta iPhi And L1',650,50,600,500)
		hoEtaPhi = self.fileHandler.getHistogram('hoMuonAnalyzer/etaPhi/L1Muon3x3_iEtaIPhi')
		hoEtaPhi.SetTitle('L1 matched to HO RecHits > 0.2GeV;i#eta;i#phi;# entries')
		hoEtaPhi.Draw('colz')
		canvas.Update()
		hoEtaPhi.SetStats(0)
		setupAxes(hoEtaPhi)
		setupPalette(hoEtaPhi)
		label = self.drawLabel()
		canvas.Update()
		canvas.SaveAs('plots/controlPlots/l1MatchedToHoIEtaIPhi.pdf')
		return label,canvas,hoEtaPhi

	'''
	Control Plot that shows the number of matches in Det Ids for a given RecHit Det id
	'''
	def plotHoDigiMatchesPerDetId(self):
		canvas = TCanvas('canvasDigiMatchesMultiplicity')
		digiMatches = self.fileHandler.getHistogram('hoMuonAnalyzer/hoDigiMatchesPerDetId_Multiplicity')
		setupAxes(digiMatches)
		digiMatches.SetTitle('Number of matches between RecHit and Digi for a given DetId')
		digiMatches.GetXaxis().SetRangeUser(0,5)
		digiMatches.GetXaxis().SetTitle('Number of matches per DetId')
		digiMatches.GetYaxis().SetTitle('#')
		canvas.cd().SetLogy()
		digiMatches.SetLineWidth(3)
		digiMatches.SetLineColor(colorRwthDarkBlue)
		digiMatches.Draw()
		
		label = drawLabelCmsPrivateSimulation()
		
		canvas.Update()
		
		stats = digiMatches.GetListOfFunctions().FindObject("stats")
		stats.SetX1NDC(.7)
		stats.SetX2NDC(.9)
		stats.SetY1NDC(.75)
		stats.SetY2NDC(.9)
		
		canvas.Update()
		
		canvas.SaveAs('plots/controlPlots/digiMatchesPerDetId.pdf')
		canvas.SaveAs('plots/controlPlots/digiMatchesPerDetId.png')
		
		return canvas,digiMatches,label
	
	def plotL1PerPt(self):
		ptValues = [0.,1.5,2.0,2.5,3.0,3.5,4.0,4.5,5.0,6.0,7.0,8.0,10.0,12.0,14.0,16.0,18.0,20.0,25.0,30.0,35.0,40.0,45.0,50.0,60.0,70.0,80.0,90.0,100.0,120.0,140.0]
		ptBins = [0]
		for i in range(len(ptValues)-1):
			ptBins.append( (ptValues[i]+ptValues[i+1])/2. )
		ptBins.append(200)
		canvas = TCanvas('cL1PerPt')
		hist = TH1D('hist','# L1 per p_{T}',len(ptBins)-1,array('d',ptBins))
		chain = self.fileHandler.getTChain()
		eventCounter = 0
		liste = []
		nEvents = chain.GetEntries()
		for event in chain:
			eventCounter += 1
			for l1 in event.l1MuonData:
				if not l1.pt in liste:
					liste.append(l1.pt)
				hist.Fill(l1.pt)
			if not eventCounter%10000:
				printProgress(eventCounter,nEvents)
			if eventCounter == 50000:
				break
		print
		setupAxes(hist)
		hist.SetStats(0)
		hist.Scale(1,"width")
		hist.Draw()
		
		label = drawLabelCmsPrivateSimulation()
		
		canvas.Update()
		
	#	print liste
		return hist, canvas, label
	
	def plotEfficiencyCountCheck(self):
		c = TCanvas()
		genHist = self.fileHandler.getHistogram('hoMuonAnalyzer/count/Gen_Count')
		l1AndGenHist = self.fileHandler.getHistogram('hoMuonAnalyzer/count/GenAndL1Muon_Count')
		plusHoHist = self.fileHandler.getHistogram('hoMuonAnalyzer/count/GenAndL1MuonAndHoAboveThr_Count')
		plusHoHist.SetLineColor(colorRwthMagenta)
		genHist.SetLineColor(colorRwthDarkBlue)
	
		genHist.SetLineWidth(3)
		l1AndGenHist.SetLineWidth(3)
		plusHoHist.SetLineWidth(3)
	
		setPlotStyle()
	
		genHist.Draw()
		l1AndGenHist.Draw('same')
		plusHoHist.Draw('same')
		
		return c,l1AndGenHist,plusHoHist,genHist

	def plotGenEtaPhi(self):
		c = TCanvas('cGenEta','Gen eta phi',1200,1600)
		c.Divide(2,1)
		gen = self.fileHandler.getGraph('hoMuonAnalyzer/graphs/gen')
		
		histEta = TH1D('hEtaGen',"#eta GEN;#eta;#",288, -math.pi,math.pi)
		histPhi = TH1D('hPhiGen',"#phi GEN;#phi;#",288, -math.pi,math.pi)
		
		x = Double(0)
		y = Double(0)
		
		for i in range(0,gen.GetN()):
			gen.GetPoint(i,x,y)
			histPhi.Fill(y)
			histEta.Fill(x)
		
		setupAxes(histEta)
		setupAxes(histPhi)
	
		histEta.GetXaxis().SetRangeUser(-1,1)
	
		c.cd(1)
		histEta.Draw()
		label1 = drawLabelCmsPrivateSimulation()
		c.cd(2)
	
		histPhi.Draw()
		label2 = drawLabelCmsPrivateSimulation()
		
		c.Update()
		
		setStatBoxOptions(histEta,10)
		setStatBoxPosition(histEta,y1=0.85)
		setStatBoxOptions(histPhi,10)
		setStatBoxPosition(histPhi,y1=0.85)
		
		c.Update()
		
		c.SaveAs('plots/controlPlots/genEtaPhi.pdf')
		
		return c,gen,histEta,histPhi,label1,label2
