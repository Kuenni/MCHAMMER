from plotting import OutputModule
from plotting.PlotStyle import setupAxes

from ROOT import Double
from plotting.RootFileHandler import commandLine
from array import array

import math

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

#Returns a 2D hisotgram containing the binwise difference of both objects
#Python histogram means the entries matrix coming from numpy histogram 2d 
def comparePythonAndRoot2DHist(pythonHist, rootHist):
	contourLevels = [-1,-.2,-.1,.1,.2,1]
	
	if not (len(pythonHist) == rootHist.GetNbinsY() and len(pythonHist[0]) == rootHist.GetNbinsX()):
		commandLine.output('Error! Cannot compare python and root histogram with different number of bins!')
		return
	
	comparisonHist = rootHist.Clone('comparison' + rootHist.GetName())
	comparisonHist.Reset()
	comparisonHist.SetStats(0)
	comparisonHist.SetContour(len(contourLevels),array('d',contourLevels))
	for j,y in enumerate(reversed(pythonHist)):
		for i,x in enumerate(y):
			comparisonHist.SetBinContent(i+1,len(pythonHist)-j, x - rootHist.GetBinContent( i+1 , len(pythonHist) - j))
			#sys.stdout.write( str(x - histNormalBins.GetBinContent( i+1 , len(pythonHist) - j)) + '\t' )
			pass
	return comparisonHist

#Returns a 2D hisotgram containing the binwise difference of both objects
def compareTwoRoot2DHists(rootHist1, rootHist2):
	contourLevels = [-3.4e48,-.2,-.1,.1,.2,1]
	if not (rootHist1.GetNbinsX() == rootHist2.GetNbinsX() and rootHist1.GetNbinsY() == rootHist2.GetNbinsY()):
		commandLine.output('Error! Cannot compare two root histograms with different number of bins!')
		return
	comparisonHist = rootHist1.Clone('comparison' + rootHist1.GetName())
	comparisonHist.Reset()
	comparisonHist.SetStats(0)
	comparisonHist.SetContour(len(contourLevels),array('d',contourLevels))
	for x in range(0,rootHist1.GetNbinsX()):
		for y in range(0,rootHist1.GetNbinsY()):
			comparisonHist.SetBinContent(x,y,rootHist1.GetBinContent(x,y) - rootHist2.GetBinContent(x,y))
			pass
	return comparisonHist

def extractTEfficiencyToList(tEffObject):
	xVals = []
	yVals = []
	yErrLow = []
	yErrUp = []
	for i in range(tEffObject.GetPassedHistogram().GetNbinsX()):
		if tEffObject.GetTotalHistogram().GetBinContent(i) != 0:
			yVals.append(tEffObject.GetPassedHistogram().GetBinContent(i)/tEffObject.GetTotalHistogram().GetBinContent(i)*100)
			xVals.append(tEffObject.GetTotalHistogram().GetBinCenter(i))
			yErrLow.append(tEffObject.GetEfficiencyErrorLow(i))
			yErrUp.append(tEffObject.GetEfficiencyErrorUp(i))
	return xVals, yVals,yErrLow,yErrUp
	