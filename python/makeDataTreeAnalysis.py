#!/usr/bin/python
from plotting.OutputModule import CommandLineHandler
import sys,os
from plotting.RootFileHandler import RootFileHandler
from ROOT import TH1D,TCanvas,gROOT,TH2D
from OfflineAnalysis.matchingLibrary import calculateDeltaPhi,getDeltaEtaList,getDeltaPhiList
from OfflineAnalysis.HoMatcher import isHoHitInGrid,getEMaxHoHitInGrid,HO_BIN,getEMaxMatches
from plotting.Utils import comparePythonAndRoot2DHist,compareTwoRoot2DHists
import matplotlib
from matplotlib.colors import LogNorm

commandLine = CommandLineHandler('[makeDataTreeAnalysis] ')

import matplotlib.pyplot as plt
import numpy as np
import math

if len(sys.argv) < 2:
	print 'First argument has to be the file name scheme!'
	
if( not os.path.exists('plots')):
	os.mkdir('plots')
if( not os.path.exists('plots/dataTreeAnalysis')):
	os.mkdir('plots/dataTreeAnalysis')
	
gROOT.ProcessLine(".L $HOMUONTRIGGER_BASE/python/loader.C+");
	
fileHandler = RootFileHandler(sys.argv[1])
dataChain = fileHandler.getTChain()
nEvents = dataChain.GetEntries()

eMaxMatches = getEMaxMatches(dataChain)
eMaxDeltaPhiList = getDeltaPhiList(eMaxMatches)
eMaxDeltaEtaList = getDeltaEtaList(eMaxMatches)

def histogramDeltaPhi():
	deltaPhiList = []
	eventCounter = 0
	for event in dataChain:
		eventCounter += 1
		if not eventCounter % 1000:
			commandLine.printProgress(eventCounter, nEvents)
		if(eventCounter == nEvents):
			commandLine.printProgress(nEvents,nEvents)
		for l1 in event.l1MuonData:
			for ho in event.hoRecHitData:
				if isHoHitInGrid(l1,ho,2):
					deltaPhiList.append(calculateDeltaPhi(l1.phi,ho.phi))
	print	
	
	fig = plt.figure()
	ax1 = fig.add_subplot(121)	
	bins = []
	for i in range(0.,22):
		bins.append(-5*HO_BIN - HO_BIN/4. + i*(HO_BIN/2.))
		
	entries, binEdgesLeft = np.histogram(deltaPhiList, bins=bins)
	width = (binEdgesLeft[1] - binEdgesLeft[0])
	ax1.bar(binEdgesLeft[:-1],entries,width=width)
	
	#Now with slightly larger HO bins
	HO_BIN = math.pi/36. + 0.001
	ax2 = fig.add_subplot(122)
	bins2 = []
	for i in range(0.,22):
		bins2.append(-5*HO_BIN - HO_BIN/4. + i*(HO_BIN/2.))
	entries2, binEdgesLeft2 = np.histogram(deltaPhiList, bins=bins2)
	width2 = (binEdgesLeft2[1] - binEdgesLeft2[0])
	ax2.bar(binEdgesLeft2[:-1],entries2,width=width2)
	plt.show()
	return

def histogramDeltaPhiEMax():
	fig = plt.figure()
	ax1 = fig.add_subplot(121)
	bins = []
	
	HO_BIN = math.pi/36.
	for i in range(0.,12):
		bins.append(-5*HO_BIN - HO_BIN/2. + i*(HO_BIN))
	entries, binEdgesLeft = np.histogram(eMaxDeltaPhiList, bins=bins)
	width = (binEdgesLeft[1] - binEdgesLeft[0])
	ax1.bar(binEdgesLeft[:-1],entries,width=width)
		
	ax2 = fig.add_subplot(122)
	HO_BIN = math.pi/36. + 0.001
	bins = []
	for i in range(0.,12):
		bins.append(-5*HO_BIN - HO_BIN/2. + i*(HO_BIN))
	entries, binEdgesLeft = np.histogram(eMaxDeltaPhiList, bins=bins)
	width = (binEdgesLeft[1] - binEdgesLeft[0])
	ax2.bar(binEdgesLeft[:-1],entries,width=width)
	plt.show()
	
def histogram2DEMax():
	bins = []
	HO_BIN = math.pi/36.
	for i in range(0,12):
		bins.append(-5*HO_BIN - HO_BIN/2. + i*(HO_BIN))
	entries,xEdges,yEdges = np.histogram2d(eMaxDeltaEtaList,eMaxDeltaPhiList, bins=bins)
	# H needs to be rotated and flipped
	entries = np.rot90(entries)
	entries = np.flipud(entries)
	
	#Create ROOThistogram for later comparison
	histNormalBins = TH2D('histNormalBins','EMax in normal bins',11,-5*HO_BIN - HO_BIN/2.,5*HO_BIN+HO_BIN/2.,
						11,-5*HO_BIN - HO_BIN/2.,5*HO_BIN+HO_BIN/2.)
	
	
	# Plot 2D histogram using pcolor
	fig2 = plt.figure(figsize = (8,4))
	plt.subplot(1,2,1)

	plt.pcolormesh(xEdges,yEdges,entries,norm=matplotlib.colors.LogNorm())
	plt.xlim(-.3,.3)
	plt.ylim(-.3,.3)
	plt.xlabel(r'$\eta$')
	plt.ylabel(r'$\phi$')
	cbar = plt.colorbar()
	cbar.ax.set_ylabel('Counts')

	ax2 = fig2.add_subplot(122)
	bins = []
	HO_BIN = HO_BIN + 0.01
	for i in range(0,12):
		bins.append(-5*HO_BIN - HO_BIN/2. + i*(HO_BIN))
	ax2.hist2d(eMaxDeltaEtaList,eMaxDeltaPhiList,bins,norm = matplotlib.colors.LogNorm())
	cbar2 = plt.colorbar()
	cbar2.ax.set_ylabel('Counts')
#	plt.xlim(-.3,.3)
#	plt.ylim(-.3,.3)
	plt.xlabel(r'$\eta$')
	plt.ylabel(r'$\phi$')
	
	#Create Root Histograms for later comparison
	histWiderBins = TH2D('histWiderBins','EMax in wider bins',11,-5*HO_BIN - HO_BIN/2.,5*HO_BIN+HO_BIN/2.,
						11,-5*HO_BIN - HO_BIN/2.,5*HO_BIN+HO_BIN/2.)
	
	##
	#	Do some ROOT stuff
	##
	for x,y in zip(eMaxDeltaEtaList,eMaxDeltaPhiList):
		histNormalBins.Fill(x,y)
		histWiderBins.Fill(x,y)
	
	canvas = TCanvas('c','c',1800,800)
	canvas.Divide(3,1)
	canvas.cd(1).SetLogz()
	histNormalBins.Draw('colz')
	canvas.cd(2)
	histWiderBins.Draw('colz')

	canvas.cd(3)
	newHist = compareTwoRoot2DHists(histWiderBins, histNormalBins)
	res = newHist.DrawClone('col text')
	newHist.GetZaxis().SetRangeUser(-1,1)
	newHist.Draw('z,same')
	
	canvas.Update()

	return canvas, newHist,res, histNormalBins,histWiderBins
	
	
#histogramDeltaPhi()
#histogramDeltaPhiEMax()
res = histogram2DEMax()
raw_input('-->')