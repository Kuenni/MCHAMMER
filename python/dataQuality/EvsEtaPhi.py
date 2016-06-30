#!/usr/bin/python
from ROOT import TCanvas,ROOT,TFile,TF1,TLine,gROOT,TPaveText,TH1D,Double,TH2D,THStack,gStyle,TMarker
from plotting.PlotStyle import getLabelCmsPrivateSimulation,setupPalette,\
	calcSigma
from plotting.PlotStyle import setupAxes,drawHoBoxes
from plotting.PlotStyle import setStatBoxOptions,setStatBoxPosition,pyplotCmsPrivateLabel
from plotting.Utils import setupEAvplot, L1_PHI_BIN, L1_ETA_BIN, calcPercent

from plotting.Plot import Plot

import numpy as np
import matplotlib.pyplot as plt
import math

class EvsEtaPhi(Plot):
	
	def __init__(self,filename,data = False):
		Plot.__init__(self,filename,data)
		self.createPlotSubdir('averageEnergy')
		self.fileHandler.printNEvents()
	'''
	Plots the average energy seen in in the tiles around the direction
	of the L1 muons
	'''
	def plotAverageEnergyAroundL1(self):
		canvas = TCanvas('canvasAverageEnergy','Average energy',1200,1200)
		canvas.cd().SetLogz()
		
		hSum = self.fileHandler.getHistogram('hoMuonAnalyzer/averageEnergy/averageEnergyAroundPoint' + self.key + '_SummedEnergy')
		hCounter = self.fileHandler.getHistogram('hoMuonAnalyzer/averageEnergy/averageEnergyAroundPoint' + self.key + '_Counter')
	
		for i in range(0,hSum.GetNbinsX()):
			for j in range(0,hSum.GetNbinsY()):
				if hCounter.GetBinContent(hCounter.GetBin(i,j)) != 0:
					hSum.SetBinContent(hSum.GetBin(i,j),hSum.GetBinContent(hSum.GetBin(i,j))/hCounter.GetBinContent(hCounter.GetBin(i,j)))
					pass
		hSum.GetXaxis().SetRangeUser(-0.6,0.6)
		hSum.GetYaxis().SetRangeUser(-0.6,0.6)
	#	hSum.SetStats(0)
		hSum.GetXaxis().SetTitle('#Delta#eta')
		hSum.GetYaxis().SetTitle('#Delta#phi')
		hSum.GetZaxis().SetTitle('Reconstructed Energy / GeV')
		hSum.SetTitle('Average Energy in HO tiles around L1 direction')
		hSum.Draw('colz')
	#	hCounter.Draw('same,text')
		
		label = getLabelCmsPrivateSimulation()
		label.Draw()
		
		canvas.Update()
		
		#Setup plot style
		setupAxes(hSum)	
		setStatBoxOptions(hSum,1100)
		setStatBoxPosition(hSum)
		setupPalette(hSum)
	
		canvas.Update()
		self.storeCanvas(canvas,'averageEnergy')
		return canvas,hSum,label,hCounter
	
	
	def calculateCentralFractionInTight(self):
		hSum = self.fileHandler.getHistogram('hoMuonAnalyzer/deltaEtaDeltaPhiEnergy/averageEMaxAroundPointpatTightToL1Muons_2dSummedWeights')
		hCounter = self.fileHandler.getHistogram('hoMuonAnalyzer/deltaEtaDeltaPhiEnergy/averageEMaxAroundPointpatTightToL1Muons_2dCounter')

		points = []
		sum = 0
		for x in range(0,5):
			for y in range(0,5):
				sum += hCounter.GetBinContent(hSum.FindBin(x*0.0435 - 0.087,y*0.0435 - 0.087))
				p = TMarker(x*0.0435 - 0.087,y*0.0435 - 0.087,20)
		#		p.Draw('same')
				points.append(p)
		print sum
		print hCounter.Integral()
		print '-----'
		print sum/hCounter.Integral()
	
	def plotAverageEMaxAroundL1(self):
		canvas = TCanvas('canvasAverageEMax','Average EMax',1200,1200)
		canvas.cd().SetLogz()
		
		hSum = self.fileHandler.getHistogram('hoMuonAnalyzer/deltaEtaDeltaPhiEnergy/averageEMaxAroundPoint' + self.key + '_2dSummedWeights')
		hCounter = self.fileHandler.getHistogram('hoMuonAnalyzer/deltaEtaDeltaPhiEnergy/averageEMaxAroundPoint' + self.key + '_2dCounter')
		
		hSum = setupEAvplot(hSum, hCounter,same=True,limitForAll=0.3)
		hSum.SetTitle('Mean E_{Max} in HO tiles around L1 direction')
		hSum.SetMaximum(2)
		hSum.Draw('colz')
		setupEAvplot(hCounter,same=True,limitForAll=0.3).Draw('same,text')
	
		label = getLabelCmsPrivateSimulation()
		label.Draw()
		
		canvas.Update()		
				
		setupPalette(hSum)
		
		canvas.Update()
		self.storeCanvas(canvas, 'averageEmax')
		hCounter.SaveAs('histogramEMaxCounter.root')
		
		return canvas,hSum,label,hCounter
	
	def plot1DEnergyAroundL1(self):	
		'''
			eta[P,M][2,1,0]phi[P,M][2,1,0]_averageEnergyAroundPoint
			Central tile is central
		'''
		histList = []
		fitList = []
		labelList = []
		canvas = TCanvas('canvas1DEnergy','1D energy',1200,1200)
		for p in reversed(range(-2,3)):
			for e in range(-2,3):
				if e == 0 and p == 0:
					histList.append(self.fileHandler.getHistogram('hoMuonAnalyzer/etaPhi/energy1D/central_averageEnergyAroundPoint' + self.key))
				else:
					histName = ('hoMuonAnalyzer/etaPhi/energy1D/eta%s%dPhi%s%d_averageEnergyAroundPoint' + self.key) % ('P' if e >= 0 else 'M',abs(e),'P' if p >= 0 else 'M',abs(p))
					histList.append(self.fileHandler.getHistogram(histName))
		canvas.Divide(5,5)
		for i,hist in enumerate(histList):
			canvas.cd(i+1).SetLogy()
			hist.GetXaxis().SetRangeUser(-0.5,4)
			hist.SetLineWidth(3)
			setupAxes(hist)
			hist.Draw()
			fit = TF1('fit%d' % (i),'landau',0.5,2)
			hist.Fit(fit,'RQ')
			label = TPaveText(0.6,0.7,0.9,0.9,"NDC")
			label.AddText('MPV: %5.2f' % (fit.GetParameter(1)))
			label.Draw()
			labelList.append(label)
			fitList.append(fit)
		canvas.Update()
		self.storeCanvas(canvas, '1DPlots')
		return histList,canvas,fitList,labelList
	
	def plot1DEMaxAroundL1(self):	
		'''
			eta[P,M][2,1,0]phi[P,M][2,1,0]_averageEnergyAroundPoint
			Central tile is central
		'''
		histList = []
		fitList = []
		labelList = []
		canvas = TCanvas('canvas1DEMax','1D EMax',1200,1200)
		for p in reversed(range(-2,3)):
			for e in range(-2,3):
				if e == 0 and p == 0:
					histList.append(self.fileHandler.getHistogram('hoMuonAnalyzer/etaPhi/energy1D/central_averageEMaxAroundPoint' + self.key))
				else:
					histName = ('hoMuonAnalyzer/etaPhi/energy1D/eta%s%dPhi%s%d_averageEMaxAroundPoint' + self.key) % ('P' if e >= 0 else 'M',abs(e),'P' if p >= 0 else 'M',abs(p))
					histList.append(self.fileHandler.getHistogram(histName))
		canvas.Divide(5,5)
		for i,hist in enumerate(histList):
			canvas.cd(i+1).SetLogy()
			hist.GetXaxis().SetRangeUser(-0.5,4)
			hist.SetLineWidth(3)
			setupAxes(hist)
			hist.Draw()
			fit = TF1('fit%d' % (i),'landau',0.5,2)
			hist.Fit(fit,'RQ')
			label = TPaveText(0.6,0.7,0.9,0.9,"NDC")
			label.AddText('MPV: %5.2f' % (fit.GetParameter(1)))
			label.Draw()
			labelList.append(label)
			fitList.append(fit)
		canvas.Update()
		self.storeCanvas(canvas, '1DEMaxPlots')
		return histList,canvas,fitList,labelList
	
	def plotMPVs(self,fitList):
		x = np.arange(-2,3)
		y = np.arange(-2,3)
		z = []
		for fit in fitList:
			z.append(fit.GetParameter(1))
		
		z = np.reshape(z, [len(x), len(y)])
		z = np.flipud(z)
		
		fig, ax = plt.subplots()
		im = ax.pcolor(z)
		ax.set_xticks(np.arange(z.shape[0])+0.5, minor=False)
		ax.set_yticks(np.arange(z.shape[1])+0.5, minor=False)
		ax.set_xticklabels(x, minor=False)
		ax.set_yticklabels(y, minor=False)
		
		colorbar = fig.colorbar(im)
		colorbar.set_label('MPV reconstructed energy / GeV')
		ax.axis('tight')
		pyplotCmsPrivateLabel(ax,y=1)
		plt.xlabel(r'$\Delta i\eta$')
		plt.ylabel(r'$\Delta i\phi$')
		plt.savefig('plots/averageEnergy/mpv.png')
		plt.show()
	
	def compareHistogramMethods(self):
		canvas = TCanvas('cComparison','Comparison btween histograms')
		
	#	canvas.Divide(2,1)
		
		histNormal = self.fileHandler.getHistogram('hoMuonAnalyzer/averageEnergy/averageEnergyAroundPoint' + self.key + '_SummedEnergy')
		histNormalCounter = self.fileHandler.getHistogram('hoMuonAnalyzer/averageEnergy/averageEnergyAroundPoint' + self.key + '_Counter')
		
		histNormal = setupEAvplot(histNormal, histNormalCounter,same=True,limitForAll=0.6)
		
	#	histNew = self.fileHandler.getHistogram('hoMuonAnalyzer/deltaEtaDeltaPhiEnergy/averageEnergyAroundPoint_2dSummedWeightsIEtaIPhi')
	#	histNewCounter = self.fileHandler.getHistogram('hoMuonAnalyzer/deltaEtaDeltaPhiEnergy/averageEnergyAroundPoint_2dCounterIEtaIPhi')
		
		canvas.cd(1).SetLogz()
		
		histNormal.SetTitle('Average Energy in HO tiles around L1 direction, i#eta by binning')
		histNormal.SetStats(1)
		histNormal.Draw('colz')
		
		label = getLabelCmsPrivateSimulation()
		label.Draw()
		
	#	canvas.cd(2).SetLogz()
		
	#	histNew = average2DHistogramBinwise(histNew, histNewCounter)
	#	histNew.GetXaxis().SetRangeUser(-8,8)
	#	histNew.GetYaxis().SetRangeUser(-8,8)
	#	histNew.GetXaxis().SetTitle('#Delta#eta')
	#	histNew.GetYaxis().SetTitle('#Delta#phi')
	#	histNew.GetZaxis().SetTitle('Reconstructed Energy / GeV')
	#	histNew.SetTitle('Mean Energy in HO tiles around L1 direction, i#eta by binning')
	#	histNew.Draw('colz')
			
	#	label2 = getLabelCmsPrivateSimulation()
	#	label2.Draw()
		
		canvas.Update()
		
		#Setup plot style
		setStatBoxOptions(histNormal,1100)
		setStatBoxPosition(histNormal)
		setupPalette(histNormal)
		
	#	setupAxes(histNew)	
	#	setStatBoxOptions(histNew,1100)
	#	setStatBoxPosition(histNew)
	#	setupPalette(histNew)
	
		canvas.Update()
		
		#TODO: Print the bin contents subtracted
		
		return canvas, histNormal,label#,histNew,label2
	
	def plotEavForTightMuons(self):
		canvas = TCanvas('canvasEavTightMuons','EAv Tight muons',1200,1200)
		canvas.cd().SetLogz()
			
		hSum = self.fileHandler.getHistogram('hoMuonAnalyzer/averageEnergy/averageEnergyAroundPointpatTightToL1Muons_SummedEnergy')
		hCounter = self.fileHandler.getHistogram('hoMuonAnalyzer/averageEnergy/averageEnergyAroundPointpatTightToL1Muons_Counter')
	
		hSum = setupEAvplot(hSum, hCounter,same=True,limitForAll=0.3)
		hSum.SetTitle('Average E_{Rec} in HO tiles around tight L1 direction')
		hSum.SetMaximum(1.2)
		hSum.SetMinimum(5e-3)
		hSum.Draw('colz')
		label = self.drawLabel()
		canvas.Update()		
		setupPalette(hSum)
		canvas.Update()
		#boxes = drawHoBoxes(canvas)
		self.storeCanvas(canvas,'eAverageTightMuons')
		return canvas,hSum,label#,boxes
	
	def plotEMaxCountsForTightMuons(self):
		canvas = TCanvas('canvasEmaxcountsTightMuons','E max counts Tight muons',1200,1200)
		canvas.cd().SetLogz()
			
		hCounter = self.fileHandler.getHistogram('hoMuonAnalyzer/deltaEtaDeltaPhiEnergy/averageEMaxAroundPointpatTightToL1Muons_2dCounter')

		hCounter.SetTitle('# of E_{Max} in HO tiles around tight L1 direction;#Delta#eta;#Delta#phi;# Entries')
		hCounter.SetStats(0)
		hCounter.GetXaxis().SetRangeUser(-.5,.5)
		hCounter.GetYaxis().SetRangeUser(-.5,.5)
		hCounter.Draw('colz')
		label = self.drawLabel()
		canvas.Update()		
		setupPalette(hCounter)
		canvas.Update()
		#boxes = drawHoBoxes(canvas)
		self.storeCanvas(canvas,'eMaxCountsTightMuons')
		
		#Calculate fraction in 3x3 grid
		integralCentral = hCounter.Integral(hCounter.GetXaxis().FindBin(-.0435),hCounter.GetXaxis().FindBin(.0435),
									hCounter.GetYaxis().FindBin(-.0435),hCounter.GetYaxis().FindBin(.0435))
		integral3x3 = hCounter.Integral(hCounter.GetXaxis().FindBin(-.1305),hCounter.GetXaxis().FindBin(.1305),
									hCounter.GetYaxis().FindBin(-.1305),hCounter.GetYaxis().FindBin(.1305))
		integralTotal = hCounter.Integral()
		
		self.output(80*'#')
		self.output('Emax fraction for Tight')
		self.output('%20s:%5.2f%% +/- %5.2f%%' % ('Central Fraction',calcPercent(integralCentral,integralTotal),
												calcSigma(integralCentral,integralTotal)*100))
		self.output('%20s:%5.2f%% +/- %5.2f%%' % ('3x3 Fraction',calcPercent(integral3x3,integralTotal),
												calcSigma(integral3x3,integralTotal)*100))
		
		self.output(80*'#')
		
		return canvas,label,hCounter
	
	def plotEMaxCounts(self):
		canvas = TCanvas('canvasEmaxcounts','E max counts',1200,1200)
		canvas.cd().SetLogz()
			
		hCounter = self.fileHandler.getHistogram('hoMuonAnalyzer/deltaEtaDeltaPhiEnergy/averageEMaxAroundPointL1MuonPresent_2dCounter')
		#hSum = setupEAvplot(hSum, hCounter,same=True,limitForAll=0.3)
		hCounter.SetTitle('# of E_{Max} in HO tiles around L1 direction;#Delta#eta;#Delta#phi;# Entries')
		hCounter.SetStats(0)
		hCounter.GetXaxis().SetRangeUser(-.5,.5)
		hCounter.GetYaxis().SetRangeUser(-.5,.5)
		hCounter.Draw('colz')
		label = self.drawLabel()
		canvas.Update()		
		setupPalette(hCounter)
		canvas.Update()
		#boxes = drawHoBoxes(canvas)
		self.storeCanvas(canvas,'eMaxCounts')
		
		#Calculate fraction in 3x3 grid
		integralCentral = hCounter.Integral(hCounter.GetXaxis().FindBin(-.0435),hCounter.GetXaxis().FindBin(.0435),
									hCounter.GetYaxis().FindBin(-.0435),hCounter.GetYaxis().FindBin(.0435))
		integral3x3 = hCounter.Integral(hCounter.GetXaxis().FindBin(-.1305),hCounter.GetXaxis().FindBin(.1305),
									hCounter.GetYaxis().FindBin(-.1305),hCounter.GetYaxis().FindBin(.1305))
		integralTotal = hCounter.Integral()
		
		self.output(80*'#')
		self.output('%20s:%5.2f%% +/- %5.2f%%' % ('Central Fraction',calcPercent(integralCentral,integralTotal),
												calcSigma(integralCentral,integralTotal)*100))
		self.output('%20s:%5.2f%% +/- %5.2f%%' % ('3x3 Fraction',calcPercent(integral3x3,integralTotal),
												calcSigma(integral3x3,integralTotal)*100))
		
		self.output(80*'#')
		return canvas,label,hCounter
		
	def plotEavPerWheelForTightMuons(self):
		canvas = TCanvas('canvasEavPerWheelTightMuons','EAv Per Wheel Tight muons',1800,800)
		canvas.Divide(3,1)
				
		hM1Energy = self.fileHandler.getHistogram('hoMuonAnalyzer/averageEnergy/wh1m/averageEnergyAroundPointpatTightToL1Muons_wh-1SummedEnergy')
		hM1Counter = self.fileHandler.getHistogram('hoMuonAnalyzer/averageEnergy/wh1m/averageEnergyAroundPointpatTightToL1Muons_wh-1Counter')
		hM1Energy = setupEAvplot(hM1Energy, hM1Counter)
		hM1Energy.SetStats(0)
	
		h0Energy = self.fileHandler.getHistogram('hoMuonAnalyzer/averageEnergy/wh0/averageEnergyAroundPointpatTightToL1Muons_wh0SummedEnergy')
		h0Counter = self.fileHandler.getHistogram('hoMuonAnalyzer/averageEnergy/wh0/averageEnergyAroundPointpatTightToL1Muons_wh0Counter')
		h0Energy = setupEAvplot(h0Energy, h0Counter)
		h0Energy.SetStats(0)
	
		hP1Energy = self.fileHandler.getHistogram('hoMuonAnalyzer/averageEnergy/wh1p/averageEnergyAroundPointpatTightToL1Muons_wh1SummedEnergy')
		hP1Counter = self.fileHandler.getHistogram('hoMuonAnalyzer/averageEnergy/wh1p/averageEnergyAroundPointpatTightToL1Muons_wh1Counter')
		hP1Energy = setupEAvplot(hP1Energy, hP1Counter)
		hP1Energy.SetStats(0)
	
		canvas.cd(1).SetLogz()
		setupAxes(hM1Energy)
		hM1Energy.SetMaximum(1.2)
		hM1Energy.SetMinimum(5e-3)
		hM1Energy.Draw('colz')
		canvas.Update()
		setupPalette(hM1Energy)
		label1 = self.drawLabel()
		
		canvas.cd(2).SetLogz()
		setupAxes(h0Energy)
		h0Energy.SetMaximum(1.2)
		h0Energy.SetMinimum(5e-3)
		h0Energy.Draw('colz')
		canvas.Update()
		setupPalette(h0Energy)
		label2 = self.drawLabel()
		
		canvas.cd(3).SetLogz()
		setupAxes(hP1Energy)
		hP1Energy.SetMaximum(1.2)
		hP1Energy.SetMinimum(5e-3)
		hP1Energy.Draw('colz')
		canvas.Update()
		setupPalette(hP1Energy)
		label3 = self.drawLabel()
	
		canvas.Update()
		
		self.storeCanvas(canvas,'eAveragePerWheelTightMuons')
		
		return hM1Energy,canvas,h0Energy,hP1Energy,h0Counter,label1,label2,label3

	def plotEAveragePerWheel(self):
		canvas = TCanvas('cEAvPerWheel',"E Average per Wheel",1800,800)
		canvas.Divide(3,1)
	
		hM1Energy = self.fileHandler.getHistogram('hoMuonAnalyzer/averageEnergy/wh1m/averageEnergyAroundPoint' + self.key + '_wh-1SummedEnergy')
		hM1Counter = self.fileHandler.getHistogram('hoMuonAnalyzer/averageEnergy/wh1m/averageEnergyAroundPoint' + self.key + '_wh-1Counter')
		hM1Energy = setupEAvplot(hM1Energy, hM1Counter)
		hM1Energy.SetStats(0)
	
		h0Energy = self.fileHandler.getHistogram('hoMuonAnalyzer/averageEnergy/wh0/averageEnergyAroundPoint' + self.key + '_wh0SummedEnergy')
		h0Counter = self.fileHandler.getHistogram('hoMuonAnalyzer/averageEnergy/wh0/averageEnergyAroundPoint' + self.key + '_wh0Counter')
		h0Energy = setupEAvplot(h0Energy, h0Counter)
		h0Energy.SetStats(0)
	
		hP1Energy = self.fileHandler.getHistogram('hoMuonAnalyzer/averageEnergy/wh1p/averageEnergyAroundPoint' + self.key + '_wh1SummedEnergy')
		hP1Counter = self.fileHandler.getHistogram('hoMuonAnalyzer/averageEnergy/wh1p/averageEnergyAroundPoint' + self.key + '_wh1Counter')
		hP1Energy = setupEAvplot(hP1Energy, hP1Counter)
		hP1Energy.SetStats(0)
	
		canvas.cd(1).SetLogz()
		setupAxes(hM1Energy)
		hM1Energy.SetMaximum(1.2)
		hM1Energy.SetMinimum(5e-3)
		hM1Energy.Draw('colz')
		canvas.Update()
		setupPalette(hM1Energy)
		label1 = self.drawLabel()

		canvas.cd(2).SetLogz()
		setupAxes(h0Energy)
		h0Energy.SetMaximum(1.2)
		h0Energy.SetMinimum(5e-3)
		h0Energy.Draw('colz')
		#h0Counter.Draw('same,text')
		canvas.Update()
		setupPalette(h0Energy)
		label2 = self.drawLabel()
		
		canvas.cd(3).SetLogz()
		setupAxes(hP1Energy)
		hP1Energy.SetMaximum(1.2)
		hP1Energy.SetMinimum(5e-3)
		hP1Energy.Draw('colz')
		canvas.Update()
		setupPalette(hP1Energy)
		label3 = self.drawLabel()
	
		canvas.Update()
		self.storeCanvas(canvas,'eAveragePerWheel')
		
		return hM1Energy,canvas,h0Energy,hP1Energy,h0Counter,label1,label2,label3
	
	def plotEtaPhiForTightL1(self):
		canvas = TCanvas("cEtaPhi","Eta Phi",1200,1200)
		canvas.Divide(2,1)
		graphAll = self.fileHandler.getGraph('hoMuonAnalyzer/graphs/patTightToL1Muons')
		graphWithHo = self.fileHandler.getGraph('hoMuonAnalyzer/graphs/patTightToL1Muons3x3')
				
		halfPhiBinwidth = L1_PHI_BIN/2.
		l1BinOffset = L1_PHI_BIN*3/4.
		
		histAll = TH2D('hEtaPhiAll',"#eta#phi for tight L1",30,-15*L1_ETA_BIN	,15*L1_ETA_BIN,
					144, -math.pi,math.pi)
		histWithHo = TH2D('hEtaPhiWithHO',"#eta#phi tight L1 + HO (3x3)",30,-15*L1_ETA_BIN,15*L1_ETA_BIN,
					144, -math.pi,math.pi)
		
		x = Double(0)
		y = Double(0)
		
		for i in range(0,graphAll.GetN()):
			graphAll.GetPoint(i,x,y)
			histAll.Fill(x,y)
			
		for i in range(0,graphWithHo.GetN()):
			graphWithHo.GetPoint(i,x,y)
			histWithHo.Fill(x,y)
		
		canvas.cd(1)
		histAll.SetStats(0)
		histAll.GetXaxis().SetRangeUser(-1,1)
		histAll.SetTitle(histAll.GetTitle() + ';#eta_{L1};#phi_{L1};Entries')
		setupAxes(histAll)
		histAll.Draw('colz')
		label1 = self.drawLabel()
		canvas.Update()
		
		setupPalette(histAll)
		
		canvas.cd(2)
		histWithHo.SetStats(0)
		histWithHo.GetXaxis().SetRangeUser(-1,1)
		histWithHo.SetTitle(histWithHo.GetTitle() + ';#eta_{L1};#phi_{L1};Entries')
		setupAxes(histWithHo)
		histWithHo.Draw('colz')
		label2 = self.drawLabel()
		
		canvas.Update()
		setupPalette(histWithHo)
		
		canvas.Update()
		
		self.storeCanvas(canvas, 'etaPhiForTightL1')
		return canvas,histAll,histWithHo,label1,label2
	