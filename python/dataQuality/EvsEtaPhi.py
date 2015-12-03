#!/usr/bin/python
from ROOT import TCanvas,ROOT,TFile,TF1,TLine,gROOT,TPaveText,TH1D,Double,TH2D,THStack,gStyle
from plotting.PlotStyle import getLabelCmsPrivateSimulation,setupPalette
from plotting.PlotStyle import setupAxes
from plotting.PlotStyle import setStatBoxOptions,setStatBoxPosition,pyplotCmsPrivateLabel
from plotting.Utils import setupEAvplot

from plotting.Plot import Plot

import numpy as np
import matplotlib.pyplot as plt

class EvsEtaPhi(Plot):
	
	def __init__(self,filename,data = False):
		Plot.__init__(self,filename,data)
		self.createPlotSubdir('averageEnergy')

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
		hSum.SetTitle('Mean Energy in HO tiles around L1 direction')
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
		canvas.SaveAs('plots/averageEnergy/averageEnergy.pdf')
	
		return canvas,hSum,label,hCounter
	
	
	def plotAverageEMaxAroundL1(self):
		canvas = TCanvas('canvasAverageEMax','Average EMax',1200,1200)
		canvas.cd().SetLogz()
		
		hSum = self.fileHandler.getHistogram('hoMuonAnalyzer/deltaEtaDeltaPhiEnergy/averageEMaxAroundPoint' + self.key + '_2dSummedWeights')
		hCounter = self.fileHandler.getHistogram('hoMuonAnalyzer/deltaEtaDeltaPhiEnergy/averageEMaxAroundPoint' + self.key + '_2dCounter')
		
		hSum = setupEAvplot(hSum, hCounter,same=True,borderAll=0.3)
		hSum.SetTitle('Mean E_{Max} in HO tiles around L1 direction')
		hSum.SetMaximum(2)
		hSum.Draw('colz')
		setupEAvplot(hCounter,same=True,borderAll=0.3).Draw('same,text')
	
		label = getLabelCmsPrivateSimulation()
		label.Draw()
		
		canvas.Update()		
				
		setupPalette(hSum)
		
		canvas.Update()
		canvas.SaveAs('plots/averageEnergy/averageEmax.pdf')

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
		canvas.SaveAs('plots/averageEnergy/1DPlots.pdf')
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
		canvas.SaveAs('plots/averageEnergy/1DEMaxPlots.pdf')
		return histList,canvas,fitList,labelList
	
	def plotMPVs(self,fitList):
		x = np.arange(-2,3)
		y = np.arange(-2,3)
		z = []
		for fit in fitList:
			z.append(fit.GetParameter(1))
		
		z = np.reshape(z, [len(x), len(y)])
		z = np.flipud(z)
		data = np.random.rand(4,4)
		
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
		
		histNormal = setupEAvplot(histNormal, histNormalCounter,same=True,borderAll=0.6)
		
	#	histNew = self.fileHandler.getHistogram('hoMuonAnalyzer/deltaEtaDeltaPhiEnergy/averageEnergyAroundPoint_2dSummedWeightsIEtaIPhi')
	#	histNewCounter = self.fileHandler.getHistogram('hoMuonAnalyzer/deltaEtaDeltaPhiEnergy/averageEnergyAroundPoint_2dCounterIEtaIPhi')
		
		canvas.cd(1).SetLogz()
		
		histNormal.SetTitle('Mean Energy in HO tiles around L1 direction, i#eta by binning')
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
			
		hSum = self.fileHandler.getHistogram('hoMuonAnalyzer/averageEnergy/averageEnergyAroundPointL1TightMuons_SummedEnergy')
		hCounter = self.fileHandler.getHistogram('hoMuonAnalyzer/averageEnergy/averageEnergyAroundPointL1TightMuons_Counter')
		
		hSum = setupEAvplot(hSum, hCounter,same=True,borderAll=0.3)
		hSum.SetTitle('Average E_{Rec} in HO tiles around tight L1 direction')
		hSum.SetMaximum(2)
		hSum.Draw('colz')
		label = self.drawLabel()
		canvas.Update()		
		setupPalette(hSum)
		canvas.Update()
		canvas.SaveAs('plots/averageEnergy/eAverageTightMuons.gif')
		return canvas,hSum,label
	