from plotting import OutputModule
from plotting.PlotStyle import setupAxes

from ROOT import Double,TGraphErrors,TLegend,vector,TMath,gPad,TPad
from plotting.RootFileHandler import commandLine
from array import array

import math

import math
from numpy import nan, dtype
import numpy as np

commandLine = OutputModule.CommandLineHandler('[Utils.py] ')

L1_PHI_BIN = math.pi/72.
L1_ETA_BIN = 0.1

def average2DHistogramBinwise(histWeights,histCounter):
	for i in range(0,histWeights.GetNbinsX()):
		for j in range(0,histWeights.GetNbinsY()):
			if histCounter.GetBinContent(histCounter.GetBin(i,j)) != 0:
				histWeights.SetBinContent(histWeights.GetBin(i,j),histWeights.GetBinContent(histWeights.GetBin(i,j))
										/histCounter.GetBinContent(histCounter.GetBin(i,j)))
	return histWeights

#Set axis range and labels for the 2D histograms showing E Average around L1 direction
def setupEAvplot(histE,histC = None,xmin = -0.4, xmax = 0.4, ymin = -0.4, ymax = 0.4,same = False, limitForAll = None):
	if histC != None:
		histE = average2DHistogramBinwise(histE,histC)
	if same:
		if limitForAll == None:
			commandLine.output('WARNING: Requested same histogram borders for all ranges but '
							'did not give limitForAll parameter. Using default values instead!')
		else:
			xmin = ymin = -limitForAll
			xmax = ymax = limitForAll
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
	
def getTGraphErrors(x,y,ex = None,ey = None):
	if (ex == None):
		ex = [0]*len(x)
	if (ey == None):
		ey = [0]*len(x)
	return TGraphErrors(len(x),array('f',x),array('f',y),array('f',ex),array('f',ey))
	
def getLegend(x1=.6,y1=.8,x2=.9,y2=.85):
	l =  TLegend(x1,y1,x2,y2)
#	l.SetTextFont(62)
	return l

def makeResidualsPad(pad):
	pad.Divide(1,2)
	pad.cd(1).SetBottomMargin(0)
	pad.cd(1).SetPad(0,0.3,1,1)
	pad.cd(2).SetTopMargin(0)
	pad.cd(2).SetBottomMargin(0.15)
	pad.cd(2).SetPad(0,0,1,0.3)
	pad.cd(1)
	return pad
	
def calcPercent(numerator, denominator):
	if(denominator == 0):
		commandLine.error('Tried to divide by 0')
		return nan
	return numerator/float(denominator)*100

def getXinNDC(x):
	gPad.Update()
	return (x - gPad.GetX1())/(gPad.GetX2()-gPad.GetX1())

def getMedian(th1d):
	n = th1d.GetXaxis().GetNbins()
	xVect = vector('double')(n)
	print xVect
	xVect = np.array(xVect)
	print xVect
 	th1d.GetXaxis().GetCenter( xVect )
 	print xVect
 	yVect = th1d.GetArray()
 	print yVect
 	yVect.SetSize(n)
 	print yVect
 	yVect = np.array(yVect)
 	print yVect
 	print np.median([xVect,yVect])
 	print TMath.Median(n,xVect,yVect)
 #  const double * y = h1->GetArray();
 #  // exclude underflow/overflows from bin content array y
 #  return TMath::Median(n, &x[0], &y[1]);
