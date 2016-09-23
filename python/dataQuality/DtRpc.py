'''
Created on Sep 23, 2016

@author: kuensken
'''
import math

from plotting.Plot import Plot

from ROOT import TCanvas,TH2D,Double

from plotting.Utils import L1_ETA_BIN, fillGraphIn2DHist
from plotting.PlotStyle import setupAxes

class DtRpc(Plot):

	def __init__(self,filename,data,debug):
		'''
		Constructor
		'''
		Plot.__init__(self,filename,data,debug)
		self.createPlotSubdir('dtRpc')
		
	### ============================================
	### Plots of the Coordinates for DT only L1Muons
	### ============================================
	def makeCoordinatePlot(self,source):
		c  = TCanvas(source,source,1200,1200)
		graphDt = self.fileHandler.getGraph('graphs/L1MuonPresent_' + source)
		histAll = TH2D('hEtaPhi' + source,";#eta_{L1};#phi_{L1};#",30,-15*L1_ETA_BIN,15*L1_ETA_BIN,
			144, -math.pi,math.pi)
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
	
	def plotDtRpc(self):
		return self.makeCoordinatePlot('DT_RPC')
	
	def plotDtRpcFine(self):
		return self.makeCoordinatePlot('DT_RPC_Fine')
	
	def plotDtRpcNotFine(self):
		return self.makeCoordinatePlot('DT_RPC_NotFine')