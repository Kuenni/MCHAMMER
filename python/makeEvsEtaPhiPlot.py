#!/usr/bin/python
import os,sys
from math import sqrt
from ROOT import TCanvas,ROOT,TFile,TLegend,TF1,TLine,gROOT,TPaveText,TH1D,Double,TH2D,THStack,gStyle
from plotting.PlotStyle import setPlotStyle,calcSigma,getLabelCmsPrivateSimulation,colorRwthDarkBlue,setupPalette
from plotting.PlotStyle import colorRwthMagenta,setupAxes,convertToHcalCoords,chimney1,chimney2,printProgress
from plotting.PlotStyle import setStatBoxOptions,setStatBoxPosition,pyplotCmsPrivateLabel
from plotting.RootFileHandler import RootFileHandler
from plotting.Utils import average2DHistogramBinwise

import numpy as np
import matplotlib.pyplot as plt

gROOT.ProcessLine(".L $HOMUONTRIGGER_BASE/python/loader.C+");

setPlotStyle()

prefix = '[makeEvsEtaPhiPlot] '
def output(outString):
	print prefix,outString

if len(sys.argv) < 2:
	print 'First argument has to be the file name scheme!'
fileHandler = RootFileHandler(sys.argv[1])
fileHandler.printStatus()

if( not os.path.exists('plots')):
	os.mkdir('plots')
if( not os.path.exists('plots/averageEnergy')):
	os.mkdir('plots/averageEnergy')

'''
Plots the average energy seen in in the tiles around the direction
of the L1 muons
'''
def plotAverageEnergyAroundL1():
	canvas = TCanvas('canvasAverageEnergy','Average energy',1200,1200)
	canvas.cd().SetLogz()
	
	hSum = fileHandler.getHistogram('hoMuonAnalyzer/deltaEtaDeltaPhiEnergy/averageEnergyAroundPoint_2dSummedWeights')
	hCounter = fileHandler.getHistogram('hoMuonAnalyzer/deltaEtaDeltaPhiEnergy/averageEnergyAroundPoint_2dCounter')

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


def plotAverageEMaxAroundL1():
	canvas = TCanvas('canvasAverageEMax','Average EMax',1200,1200)
	canvas.cd().SetLogz()
	
	hSum = fileHandler.getHistogram('hoMuonAnalyzer/deltaEtaDeltaPhiEnergy/averageEMaxAroundPoint_2dSummedWeights')
	hCounter = fileHandler.getHistogram('hoMuonAnalyzer/deltaEtaDeltaPhiEnergy/averageEMaxAroundPoint_2dCounter')
	for i in range(0,hSum.GetNbinsX()):
		for j in range(0,hSum.GetNbinsY()):
			if hCounter.GetBinContent(hCounter.GetBin(i,j)) != 0:
				hSum.SetBinContent(hSum.GetBin(i,j),hSum.GetBinContent(hSum.GetBin(i,j))/hCounter.GetBinContent(hCounter.GetBin(i,j)))
				pass
			
	hSum.SetStats(0)
	hSum.GetXaxis().SetRangeUser(-0.6,0.6)
	hSum.GetYaxis().SetRangeUser(-0.6,0.6)
	hSum.GetXaxis().SetTitle('#Delta#eta')
	hSum.GetYaxis().SetTitle('#Delta#phi')
	hSum.GetZaxis().SetTitle('Reconstructed Energy / GeV')
	hSum.SetTitle('Mean E_{Max} in HO tiles around L1 direction')
	hSum.Draw('colz')
	
	hCounter.Draw('same,text')
	
	label = getLabelCmsPrivateSimulation()
	label.Draw()
	
	canvas.Update()		
			
	setupAxes(hSum)	
	setupPalette(hSum)
	
	canvas.Update()
	canvas.SaveAs('plots/averageEnergy/averageEmax.pdf')
	
	return canvas,hSum,label,hCounter

def plot1DEnergyAroundL1():	
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
				histList.append(fileHandler.getHistogram('hoMuonAnalyzer/etaPhi/energy1D/central_averageEnergyAroundPoint'))
			else:
				histName = 'hoMuonAnalyzer/etaPhi/energy1D/eta%s%dPhi%s%d_averageEnergyAroundPoint' % ('P' if e >= 0 else 'M',abs(e),'P' if p >= 0 else 'M',abs(p))
				histList.append(fileHandler.getHistogram(histName))
	canvas.Divide(5,5)
	for i,hist in enumerate(histList):
		canvas.cd(i+1).SetLogy()
		hist.GetXaxis().SetRangeUser(-0.5,4)
		hist.SetLineWidth(3)
		setupAxes(hist)
		hist.Draw()
		fit = TF1('fit%d' % (i),'landau',0.5,2)
		hist.Fit(fit,'RQ')
#		output('MPV: %5.2f\tX2: %5.2f\tNDF:%d\t X2/NDF: %5.2f' % (fit.GetParameter(1),fit.GetChisquare(),fit.GetNDF(),fit.GetChisquare()/float(fit.GetNDF())))
		label = TPaveText(0.6,0.7,0.9,0.9,"NDC")
		label.AddText('MPV: %5.2f' % (fit.GetParameter(1)))
		label.Draw()
		labelList.append(label)
		fitList.append(fit)
	canvas.Update()
	canvas.SaveAs('plots/averageEnergy/1DPlots.pdf')
	return histList,canvas,fitList,labelList

def plot1DEMaxAroundL1():	
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
				histList.append(fileHandler.getHistogram('hoMuonAnalyzer/etaPhi/energy1D/central_averageEMaxAroundPoint'))
			else:
				histName = 'hoMuonAnalyzer/etaPhi/energy1D/eta%s%dPhi%s%d_averageEMaxAroundPoint' % ('P' if e >= 0 else 'M',abs(e),'P' if p >= 0 else 'M',abs(p))
				histList.append(fileHandler.getHistogram(histName))
	canvas.Divide(5,5)
	for i,hist in enumerate(histList):
		canvas.cd(i+1).SetLogy()
		hist.GetXaxis().SetRangeUser(-0.5,4)
		hist.SetLineWidth(3)
		setupAxes(hist)
		hist.Draw()
		fit = TF1('fit%d' % (i),'landau',0.5,2)
		hist.Fit(fit,'RQ')
#		output('MPV: %5.2f\tX2: %5.2f\tNDF:%d\t X2/NDF: %5.2f' % (fit.GetParameter(1),fit.GetChisquare(),fit.GetNDF(),fit.GetChisquare()/float(fit.GetNDF())))
		label = TPaveText(0.6,0.7,0.9,0.9,"NDC")
		label.AddText('MPV: %5.2f' % (fit.GetParameter(1)))
		label.Draw()
		labelList.append(label)
		fitList.append(fit)
	canvas.Update()
	canvas.SaveAs('plots/averageEnergy/1DEMaxPlots.pdf')
	return histList,canvas,fitList,labelList

def plotMPVs(fitList):
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

def compareHistogramMethods():
	canvas = TCanvas('cComparison','Comparison btween histograms')
	
	canvas.Divide(2,1)
	
	histNormal = fileHandler.getHistogram('hoMuonAnalyzer/averageEnergy/averageEnergyAroundPoint_2dSummedWeights')
	histNormalCounter = fileHandler.getHistogram('hoMuonAnalyzer/deltaEtaDeltaPhiEnergy/averageEnergyAroundPoint_2dCounter')
	
	histNew = fileHandler.getHistogram('hoMuonAnalyzer/deltaEtaDeltaPhiEnergy/averageEnergyAroundPoint_2dSummedWeightsIEtaIPhi')
	histNewCounter = fileHandler.getHistogram('hoMuonAnalyzer/deltaEtaDeltaPhiEnergy/averageEnergyAroundPoint_2dCounterIEtaIPhi')
	
	canvas.cd(1).SetLogz()
	
	histNormal = average2DHistogramBinwise(histNormal, histNormalCounter)
	histNormal.GetXaxis().SetRangeUser(-0.6,0.6)
	histNormal.GetYaxis().SetRangeUser(-0.6,0.6)
	histNormal.GetXaxis().SetTitle('#Delta#eta')
	histNormal.GetYaxis().SetTitle('#Delta#phi')
	histNormal.GetZaxis().SetTitle('Reconstructed Energy / GeV')
	histNormal.SetTitle('Mean Energy in HO tiles around L1 direction, i#eta by binning')
	histNormal.Draw('colz')
	
	label = getLabelCmsPrivateSimulation()
	label.Draw()
	
	canvas.cd(2).SetLogz()
	
	histNew = average2DHistogramBinwise(histNew, histNewCounter)
	histNew.GetXaxis().SetRangeUser(-8,8)
	histNew.GetYaxis().SetRangeUser(-8,8)
	histNew.GetXaxis().SetTitle('#Delta#eta')
	histNew.GetYaxis().SetTitle('#Delta#phi')
	histNew.GetZaxis().SetTitle('Reconstructed Energy / GeV')
	histNew.SetTitle('Mean Energy in HO tiles around L1 direction, i#eta by binning')
	histNew.Draw('colz')
		
	label2 = getLabelCmsPrivateSimulation()
	label2.Draw()
	
	canvas.Update()
	
	#Setup plot style
	setupAxes(histNormal)	
	setStatBoxOptions(histNormal,1100)
	setStatBoxPosition(histNormal)
	setupPalette(histNormal)
	
	setupAxes(histNew)	
	setStatBoxOptions(histNew,1100)
	setStatBoxPosition(histNew)
	setupPalette(histNew)

	canvas.Update()
	
	#TODO: Print the bin contents subtracted
	
	return canvas, histNormal,label,histNew,label2

res6 = compareHistogramMethods()
raw_input('-->')
res5 = plot1DEMaxAroundL1()
res4 = plotAverageEMaxAroundL1()
res = plotAverageEnergyAroundL1()
res2 = plot1DEnergyAroundL1()
res3 = plotMPVs(fitList=res2[2])

raw_input('-->')
