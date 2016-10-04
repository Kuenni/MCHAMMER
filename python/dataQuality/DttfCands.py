'''
Created on Sep 23, 2016

@author: kuensken
'''
import math

from plotting.Plot import Plot

from ROOT import TCanvas,TH2D,Double

from plotting.Utils import L1_ETA_BIN,L1_PHI_BIN, fillGraphIn2DHist
from plotting.PlotStyle import setupAxes

class DttfCands(Plot):

	def __init__(self,filename,data,debug):
		'''
		Constructor
		'''
		Plot.__init__(self,filename,data,debug)
		self.createPlotSubdir('dttfCands')
		
	### ============================================
	### Plots of the Coordinates for DT only L1Muons
	### ============================================
	def makeCoordinatePlot(self,source):
		c  = TCanvas(source,source,1200,1200)
		graphDt = self.fileHandler.getGraph('graphs/' + source)
		histAll = TH2D('hEtaPhi' + source,";#eta_{L1};#phi_{L1};#",30,-15*L1_ETA_BIN,15*L1_ETA_BIN,
			144, 0,2*math.pi - L1_PHI_BIN/2.)
		fillGraphIn2DHist(graphDt, histAll)
		
		###
		'''
		Temporary stuff to check the eta coordinates in the graphs
		'''
		x = Double(0)
		y = Double(0)
		listeDt = []
		for i in range(0,graphDt.GetN()):
			graphDt.GetPoint(i,x,y)
			listeDt.append(float(x))

		histAll.SetStats(0)
		histAll.Draw('colz')
		c.Update()
		setupAxes(histAll)
		label = self.drawLabel()
		c.Update()
		return c,histAll,label
	
	### ========================
	### Predefined Plotter calls
	### ========================

	def plotDttfCands(self):
		return self.makeCoordinatePlot('DttfCands')
	
	def plotDttfCandsFine(self):
		return self.makeCoordinatePlot('DttfCands_Fine')
	
	def plotDttfCandsNotFine(self):
		return self.makeCoordinatePlot('DttfCands_NotFine')
	