#!/usr/bin/python
import os,sys
from math import sqrt
from ROOT import TCanvas,ROOT,TFile,TLegend,TF1,TLine,gROOT,TPaveText,TH1D,Double,TH2D,THStack,gStyle
from plotting.PlotStyle import setPlotStyle,calcSigma,getLabelCmsPrivateSimulation,colorRwthDarkBlue,setupPalette
from plotting.PlotStyle import colorRwthMagenta,setupAxes,convertToHcalCoords,chimney1,chimney2,printProgress
from plotting.PlotStyle import setStatBoxOptions,setStatBoxPosition
from plotting.RootFileHandler import RootFileHandler
from matchingLibrary import findBestL1Match

import numpy as np
import matplotlib.pyplot as plt

gROOT.Reset()
gROOT.ProcessLine("gErrorIgnoreLevel = 3000;")
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
	hSum.GetXaxis().SetTitle('#Delta#eta')
	hSum.GetYaxis().SetTitle('#Delta#phi')
	hSum.GetZaxis().SetTitle('Reconstructed Energy / GeV')
	hSum.SetTitle('Mean Energy in HO tiles around L1 direction')
	hSum.Draw('colz')
	
	label = getLabelCmsPrivateSimulation()
	label.Draw()
	
	canvas.Update()
	
	#Setup plot style
	setupAxes(hSum)	
	setStatBoxOptions(hSum,1100)
	setStatBoxPosition(hSum)
	setupPalette(hSum)

	canvas.Update()
	
	return canvas,hSum,label

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
		output('MPV: %5.2f\tX2: %5.2f\tNDF:%d\t X2/NDF: %5.2f' % (fit.GetParameter(1),fit.GetChisquare(),fit.GetNDF(),fit.GetChisquare()/float(fit.GetNDF())))
		label = TPaveText(0.6,0.7,0.9,0.9,"NDC")
		label.AddText('MPV: %5.2f' % (fit.GetParameter(1)))
		label.Draw()
		labelList.append(label)
		fitList.append(fit)
	canvas.Update()
	return histList,canvas,fitList,labelList

def plotMPVs(fitList):
	x = np.arange(-2,3)
	y = np.arange(-2,3)
	z = []
	for fit in fitList:
		z.append(fit.GetParameter(1))
	
	z = np.reshape(z, [len(x), len(y)])
	print z
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
	plt.xlabel(r'$\Delta i\eta$')
	plt.ylabel(r'$\Delta i\phi$')
	plt.show()

res = plotAverageEnergyAroundL1()
res2 = plot1DEnergyAroundL1()
res3 = plotMPVs(fitList=res2[2])

# chain = fileHandler.getTChain()
# totalEvents = chain.GetEntries()
# eventCounter = 0
# 
# for event in chain:
# 	eventCounter += 1
# 	printProgress(eventCounter,totalEvents)
# 	for genMuon in chain.genMuonData:
# 		l1 = findBestL1Match(genMuon,chain.l1MuonData,0.3)
# 		if l1 != None:
# #			output('Eta: %5.2f\tPhi:%5.2f'%(l1.eta,l1.phi))
# 			pass
# 		else:
# 			
# 			output('No L1 Match')
	
# def plotDeltaTime():
# 	hDeltaTAllHo = fileHandler.getHistogram('hoMuonAnalyzer/L1MuonPresentHoMatch_DeltaTime')
# 	hDeltaTCleanHo = fileHandler.getHistogram('hoMuonAnalyzer/L1MuonAboveThr_DeltaTime')
# 	
# 	c = TCanvas("c","Delta Time",1200,1200)
# 	c.SetLogy()
# 	
# 	hDeltaTAllHo.SetLineColor(ROOT.kBlue)
# 	hDeltaTAllHo.SetLineWidth(3)
# 	hDeltaTAllHo.SetFillColor(ROOT.kBlue)
# 	hDeltaTAllHo.SetFillStyle(3017)
# 	hDeltaTAllHo.SetTitle("#Delta time")
# 	hDeltaTAllHo.SetStats(0)
# 	
# 	hDeltaTCleanHo.SetLineColor(8)
# 	hDeltaTCleanHo.SetFillColor(8)
# 	hDeltaTCleanHo.SetLineWidth(3)
# 	hDeltaTCleanHo.SetFillStyle(3002)
# 	
# 	#hDeltaTAllHo.Scale(1/hDeltaTAllHo.Integral())
# 	#hDeltaTCleanHo.Scale(1/hDeltaTCleanHo.Integral())
# 	
# 	print hDeltaTCleanHo.Integral(),hDeltaTAllHo.Integral()
# 	
# 	fitFirstMin = TF1("fitFirstMin","[0]+x*[1]+[2]*x**2")
# 	fitSecondMin = TF1("fitsecondMin","[0]+x*[1]+[2]*x**2",10,20)
# 	
# 	hDeltaTCleanHo.Fit(fitFirstMin,"+q","",-20,-10)
# 	hDeltaTCleanHo.Fit(fitSecondMin,"R+q","")
# 	
# 	hDeltaTAllHo.Draw()
# 	legend = TLegend(0.6,0.75,0.9,0.9)
# 	legend.AddEntry(hDeltaTAllHo,"L1Muon matched to any HO","le")
# 	legend.Draw()
# 	
# 	label = getLabelCmsPrivateSimulation()
# 	label.Draw()
# 	c.Update()
# 	
# 	c.SaveAs("plots/timing/deltaTimeAllHo.png")
# 	c.SaveAs("plots/timing/deltaTimeAllHo.pdf")
# 	
# 	hDeltaTCleanHo.Draw('same')
# 	
# 	fitFirstMin.SetRange(-50,50)
# 	fitSecondMin.SetRange(-50,50)
# 	
# 	#fitFirstMin.Draw('lSame')
# 	#fitSecondMin.Draw('lSame')
# 	
# 	lineFirstMin = TLine(fitFirstMin.GetMinimumX(-20,-10),hDeltaTAllHo.GetMinimum(),fitFirstMin.GetMinimumX(-20,-10),hDeltaTAllHo.GetMaximum())
# 	lineFirstMin.SetLineWidth(3)
# 	lineFirstMin.SetLineColor(ROOT.kRed)
# 	lineFirstMin.Draw()
# 	
# 	lineSecondMin = TLine(fitSecondMin.GetMinimumX(10,20),hDeltaTAllHo.GetMinimum(),fitSecondMin.GetMinimumX(10,20),hDeltaTAllHo.GetMaximum())
# 	lineSecondMin.SetLineWidth(3)
# 	lineSecondMin.SetLineColor(ROOT.kRed)
# 	lineSecondMin.Draw()
# 	
# 	
# 	legend.AddEntry(hDeltaTCleanHo,"L1Muon matched to HO > 0.2 GeV","le")
# 	legend.AddEntry(lineFirstMin,"Integral boundaries","e")
# 	legend.Draw()
# 	
# 	integralCenter = hDeltaTCleanHo.Integral(hDeltaTCleanHo.FindBin(fitFirstMin.GetMinimumX(-20,-10)),hDeltaTCleanHo.FindBin(fitSecondMin.GetMinimumX(10,20)))
# 	integralCenterAll = hDeltaTAllHo.Integral(hDeltaTAllHo.FindBin(fitFirstMin.GetMinimumX(-20,-10)),hDeltaTAllHo.FindBin(fitSecondMin.GetMinimumX(10,20)))
# 	print 80*'#'
# 	print 'Integral of center area in clean histogram :',integralCenter
# 	print '==> %.2f%% +/- %.2f%%' % (integralCenter/hDeltaTCleanHo.Integral()*100,calcSigma(integralCenter, hDeltaTCleanHo.Integral())*100)
# 	print 'Integral of center area in all matched HO events:',integralCenterAll
# 	print '==> %.2f%% +/- %.2f%%' % (integralCenterAll/hDeltaTAllHo.Integral()*100,calcSigma(integralCenterAll, hDeltaTAllHo.Integral())*100)
# 	print 80*'#'
# 	
# 	paveText = TPaveText(0.6,0.7,0.9,0.75,'NDC')
# 	paveText.AddText('%s' % ('Central peak contains (filtered hist.)'))
# 	paveText.AddText('%.2f%% +/- %.2f%%' % (integralCenter/hDeltaTCleanHo.Integral()*100,calcSigma(integralCenter, hDeltaTCleanHo.Integral())*100))
# 	paveText.SetBorderSize(1)
# 	paveText.Draw()
# 	
# 	label = getLabelCmsPrivateSimulation()
# 	label.Draw()
# 	c.Update()
# 	
# 	
# 	c.SaveAs("plots/timing/deltaTime.png")
# 	c.SaveAs("plots/timing/deltaTime.pdf")


raw_input('-->')
