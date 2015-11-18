from plotting import OutputModule
from plotting.PlotStyle import setupAxes

from ROOT import Double
from plotting.RootFileHandler import commandLine

import math

commandLine = OutputModule.CommandLineHandler('[Utils.py] ')

L1_BIN = math.pi/72.

def average2DHistogramBinwise(histWeights,histCounter):
	for i in range(0,histWeights.GetNbinsX()):
		for j in range(0,histWeights.GetNbinsY()):
			if histCounter.GetBinContent(histCounter.GetBin(i,j)) != 0:
				histWeights.SetBinContent(histWeights.GetBin(i,j),histWeights.GetBinContent(histWeights.GetBin(i,j))
										/histCounter.GetBinContent(histCounter.GetBin(i,j)))
	return histWeights

#Set axis range and labels for the 2D histograms showing E Average around L1 direction
def setupEAvplot(histE,histC = None,xmin = -0.4, xmax = 0.4, ymin = -0.4, ymax = 0.4,same = False, borderAll = None):
	if histC != None:
		histE = average2DHistogramBinwise(histE,histC)
	if same:
		if borderAll == None:
			commandLine.output('WARNING: Requested same histogram borders for all ranges but '
							'did not give borderAll parameter. Using default values instead!')
		else:
			xmin = ymin = -borderAll
			xmax = ymax = borderAll
	histE.GetXaxis().SetRangeUser(xmin,xmax)
	histE.GetYaxis().SetRangeUser(ymin,ymax)
	histE.SetStats(0)
	histE.GetXaxis().SetTitle('#Delta#eta')
	histE.GetYaxis().SetTitle('#Delta#phi')
	histE.GetZaxis().SetTitle('Reconstructed Energy / GeV')
	setupAxes(histE)
	return histE

def fillGraphIn2DHist(graph,hist):
	x = Double(0)
	y = Double(0)
	commandLine.output('Filling graph in 2D histogram:')
	nTotal = graph.GetN()
	for i in range(0,nTotal):
		graph.GetPoint(i,x,y)
		hist.Fill(x,y)
		if(not i%10000):
			commandLine.printProgress(i,nTotal)
		if(i == nTotal - 1):
			commandLine.printProgress(nTotal, nTotal)
	print
	return hist
