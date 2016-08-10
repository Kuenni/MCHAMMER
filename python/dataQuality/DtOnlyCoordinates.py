from ROOT import TCanvas,ROOT,TFile,TLegend,TF1,TLine,gROOT,TPaveText,TH1D,Double,TH2D,THStack,gStyle,TEfficiency,TBox
from plotting.Plot import Plot

from plotting.PlotStyle import setupAxes
from plotting.Utils import L1_ETA_BIN, fillGraphIn2DHist, calcPercent, calcSigma
from numpy import math

class DtOnlyCoordinates(Plot):
	'''
	Constructor for this specific plot class is different. It is possible to
	give a string with a pT cut argument. When given, the plots are created only
	for the selection of L1Muons that passed the given pT cut. Possbile values
	for the pT cut parameter are (at the moment):
		pt10, pt15, pt20, pt25
	'''
	def __init__(self,filename,data,debug, ptCut=""):
		Plot.__init__(self,filename,data,debug)
		self.createPlotSubdir('timing')
		self.ptCut = ('_' + ptCut) if ptCut != "" else ""
		
	### ==========================================
	### Plots of the fraction of L1muons remaining
	### after applying different cuts
	### ==========================================	
	def printFractionsForDtOnly(self):
		allL1 = self.fileHandler.getHistogram('count/timingSupport__Count')
		allTightL1 = self.fileHandler.getHistogram('count/timingSupport_tight__Count')
		dtOnly = self.makeDtOnlyPlot(sourceDt='UnmatchedDt', sourceDtHo='UnmatchedDtHo')[1]
		dtOnlyBxWrong = self.makeDtOnlyPlot(sourceDt='UnmatchedDtBxNot0', sourceDtHo='UnmatchedDtHoBxNot0')[1]
		dtOnlyBxWrongHo = self.makeDtOnlyPlot(sourceDt='UnmatchedDtHoBxNot0', sourceDtHo='')[1]
		dtOnlyTight = self.makeDtOnlyPlot(sourceDt='tight_UnmatchedDt', sourceDtHo='tight_UnmatchedDtHo')[1]
		dtOnlyTightBxWrong = self.makeDtOnlyPlot(sourceDt='tight_UnmatchedDtBxNot0', sourceDtHo='tight_UnmatchedDtHoBxNot0')[1]
		dtOnlyTightBxWrongHo = self.makeDtOnlyPlot(sourceDt='tight_UnmatchedDtHoBxNot0', sourceDtHo='')[1]
		
		nAllL1 = allL1.GetEntries()
		nAllL1Tight = allTightL1.GetEntries()
		nDtOnly = dtOnly.GetEntries()
		nDtOnlyBxWrong = dtOnlyBxWrong.GetEntries()
		nDtOnlyBxWrongHo = dtOnlyBxWrongHo.GetEntries()
		nDtOnlyTight = dtOnlyTight.GetEntries()
		nDtOnlyTightBxWrong = dtOnlyTightBxWrong.GetEntries()
		nDtOnlyTightBxWrongHo = dtOnlyTightBxWrongHo.GetEntries()
		
		print
		header = "%30s  %7s    %s" % ('Data source','Entries','Fraction of total L1')
		self.debug(header)
		self.debug('-'*len(header))
		self.debug("%30s: %7d" % ('L1',nAllL1))
		self.debug("%30s: %7d => %6.2f +/- %6.2f" % ('DT only',nDtOnly,calcPercent(nDtOnly, nAllL1),calcSigma(nDtOnly,nAllL1)*100))
		self.debug("%30s: %7d => %6.2f +/- %6.2f"
				 % ('DT only, BX wrong',nDtOnlyBxWrong,calcPercent(nDtOnlyBxWrong, nAllL1),calcSigma(nDtOnlyBxWrong,nAllL1)*100))
		self.debug("%30s: %7d => %6.2f +/- %6.2f"
				 % ('DT only, BX wrong + HO',nDtOnlyBxWrongHo,calcPercent(nDtOnlyBxWrongHo, nAllL1),calcSigma(nDtOnlyBxWrongHo,nAllL1)*100))
		print
		self.debug("%30s: %7d => %6.2f +/- %6.2f"
				 % ('Tight L1',nAllL1Tight,calcPercent(nAllL1Tight, nAllL1),calcSigma(nAllL1Tight,nAllL1)*100))
		self.debug("%30s: %7d => %6.2f +/- %6.2f"
				 % ('Tight DT only',nDtOnlyTight,calcPercent(nDtOnlyTight, nAllL1),calcSigma(nDtOnlyTight,nAllL1)*100))
		self.debug("%30s: %7d => %6.2f +/- %6.2f"
				 % ('Tight DT only, BX wrong',nDtOnlyTightBxWrong,calcPercent(nDtOnlyTightBxWrong, nAllL1)
				,calcSigma(nDtOnlyTightBxWrong,nAllL1)*100))
		self.debug("%30s: %7d => %6.2f +/- %6.2f"
				 % ('Tight DT only, BX wrong + HO',nDtOnlyTightBxWrongHo,calcPercent(nDtOnlyTightBxWrongHo, nAllL1)
				,calcSigma(nDtOnlyTightBxWrongHo,nAllL1)*100))
		print
		return
	
	### ============================================
	### Plots of the Coordinates for DT only L1Muons
	### ============================================
	def makeDtOnlyPlot(self,sourceDt,sourceDtHo):
		c  = TCanvas(sourceDt,sourceDt,1200,1200)
		graphDt = self.fileHandler.getGraph('graphs/timingSupport_' + sourceDt)
		histAll = TH2D('hEtaPhi' + sourceDt,";#eta_{L1};#phi_{L1};#",30,-15*L1_ETA_BIN,15*L1_ETA_BIN,
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
		self.warning('eta: %s' % (sourceDt))
		self.warning(str(sorted(set(listeDt))))
		###
				
		if(sourceDtHo != ''):
			graphDtHo = self.fileHandler.getGraph('graphs/timingSupport_' + sourceDtHo)
			fillGraphIn2DHist(graphDtHo, histAll)
			###
			'''
			Temporary stuff to check the eta coordinates in the graphs
			'''
			x = Double(0)
			y = Double(0)
			listeDtHo = []
			for i in range(0,graphDtHo.GetN()):
				graphDtHo.GetPoint(i,x,y)
				listeDtHo.append(float(x))
			self.warning('eta: %s' % (sourceDtHo))
			self.warning(str(sorted(set(listeDtHo))))
			###
		histAll.SetStats(0)
		histAll.Draw('colz')
		c.Update()
		setupAxes(histAll)
		label = self.drawLabel()
		c.Update()
		return c,histAll,label
	
	def plotDtOnlyCoordinates(self):
		c,hist,label = self.makeDtOnlyPlot(sourceDt='UnmatchedDt', sourceDtHo='UnmatchedDtHo')
		hist.SetTitle('#eta#phi for DT-only')
		self.storeCanvas(c, 'dtOnlyCoordinates')
		return hist,c,label
	
	def plotDtOnlyTightCoordinates(self):
		c,hist,label = self.makeDtOnlyPlot(sourceDt='tight_UnmatchedDt', sourceDtHo='tight_UnmatchedDtHo')
		hist.SetTitle('#eta#phi for tight DT-only')
		self.storeCanvas(c, 'dtOnlyTightCoordinates')
		return hist,c,label
	
	def plotDtOnlyBxWrongCoordinates(self):
		c,hist,label = self.makeDtOnlyPlot(sourceDt='UnmatchedDtBxNot0', sourceDtHo='UnmatchedDtHoBxNot0')
		hist.SetTitle('#eta#phi for DT-only, BX Wrong')
		self.storeCanvas(c, 'dtOnlyBxWrongCoordinates')
		return hist,c,label
	
	def plotDtOnlyTightBxWrongCoordinates(self):
		c,hist,label = self.makeDtOnlyPlot(sourceDt='tight_UnmatchedDtBxNot0', sourceDtHo='tight_UnmatchedDtHoBxNot0')
		hist.SetTitle('#eta#phi for tight DT-only, BX Wrong')
		self.storeCanvas(c, 'dtOnlyTightBxWrongCoordinates')
		return hist,c,label
	
	def plotDtOnlyAndHoBxWrongCoordinates(self):
		c,hist,label = self.makeDtOnlyPlot(sourceDt='UnmatchedDtHoBxNot0', sourceDtHo='')
		hist.SetTitle('#eta#phi for DT-only + HO, BX Wrong')
		self.storeCanvas(c, 'dtOnlyAndHoBxWrongCoordinates')
		return hist,c,label
	
	def plotDtOnlyTightAndHoBxWrongCoordinates(self):
		c,hist,label = self.makeDtOnlyPlot(sourceDt='tight_UnmatchedDtHoBxNot0', sourceDtHo='')
		hist.SetTitle('#eta#phi for tight DT-only + HO, BX Wrong')
		self.storeCanvas(c, 'dtOnlyTightAndHoBxWrongCoordinates')
		return hist,c,label
	
	
	def plotDtOnlyTightAndHoBxWrongCoordinatesFineEta(self):
		c,hist,label = self.makeDtOnlyPlot(sourceDt='tight_UnmatchedDtHoBxNot0Fine', sourceDtHo='')
		hist.SetTitle('#eta#phi for tight DT-only + HO, BX Wrong, #eta fine')
		self.storeCanvas(c, 'dtOnlyTightAndHoBxWrongCoordinatesFine')
		return hist,c,label
	