from plotting.Plot import Plot

from ROOT import TCanvas,TH1D,TH2D
from plotting.PlotStyle import calcSigma, colorRwthDarkBlue, colorRwthMagenta,\
	colorRwthTuerkis, setupAxes, setupPalette
from plotting.Utils import getLegend, L1_ETA_BIN, L1_PHI_BIN, fillGraphIn2DHist,calcPercent

import math
from termios import NL1

class Counters(Plot):

	#Initialize
	def __init__(self,filename,data):
		Plot.__init__(self,filename,data)
		self.createPlotSubdir('efficiency')
		self.fileHandler.printNEvents()
		
	#plot counters for L1, tight l1, and matching to those
	def plotL1AndTightL1Counters(self):
		hEvent = self.fileHandler.getHistogram('hoMuonAnalyzer/count/Events_Count')
		hAllL1 = self.fileHandler.getHistogram('hoMuonAnalyzer/count/L1Muon_Count')
		hAllL13x3 = self.fileHandler.getHistogram('hoMuonAnalyzer/count/L1Muon3x3_Count')
		hTightL1 = self.fileHandler.getHistogram('hoMuonAnalyzer/count/L1TightMuons_Count')
		hTightL13x3 = self.fileHandler.getHistogram('hoMuonAnalyzer/count/L1TightMuons3x3_Count')
		
		hL1 = self.fileHandler.getHistogram('hoMuonAnalyzer/count/energyDeposit_L1Muon_Count')
		hL1Reco = self.fileHandler.getHistogram('hoMuonAnalyzer/count/energyDeposit_L1Reco_Count')
		hL1RecoHo = self.fileHandler.getHistogram('hoMuonAnalyzer/count/energyDeposit_L1RecoHo_Count')
		hL1RecoHoTight = self.fileHandler.getHistogram('hoMuonAnalyzer/count/energyDeposit_L1RecoHoTight_Count')
		hL1RecoTight = self.fileHandler.getHistogram('hoMuonAnalyzer/count/energyDeposit_L1RecoTight_Count')
		hL1RecoTightHo = self.fileHandler.getHistogram('hoMuonAnalyzer/count/energyDeposit_L1RecoTightHo_Count')
		hL1RecoHoNoThr = self.fileHandler.getHistogram('hoMuonAnalyzer/count/energyDeposit_L1RecoHoNoThr_Count')
		hL1RecoGaHoNoThr = self.fileHandler.getHistogram('hoMuonAnalyzer/count/energyDeposit_L1RecoGaHoNoThr_Count')
		
		histogramList = [ hL1, hL1Reco, hL1RecoHo, hL1RecoHoTight,
						hL1RecoTight, hL1RecoTightHo, hL1RecoHoNoThr, hL1RecoGaHoNoThr ]
		
		names = ['hL1','hL1Reco','hL1RecoHo','hL1RecoHoTight','hL1RecoTight','hL1RecoTightHo','hL1RecoHoNoThr','hL1RecoGaHoNoThr']
		nL1 = hL1.GetBinContent(2)
		
		self.commandLine.output('###############################################')
		for i,h in enumerate(histogramList):
			self.commandLine.output('%s:\t\t%d\t=> %5.2f' % (names[i],h.GetBinContent(2),calcPercent(h.GetBinContent(2),nL1)))
		self.commandLine.output('###############################################')

		
		nEvents 	= hEvent.GetBinContent(2)
		nAll 		= hAllL1.GetBinContent(2)
		nAll3x3 	= hAllL13x3.GetBinContent(2)
		nTight 		= hTightL1.GetBinContent(2)
		nTight3x3	= hTightL13x3.GetBinContent(2)
		
		N_BINS = 4
		
		binContents = [nEvents,nAll,nTight,nTight3x3]
		binLabels = ['Events','L1','L1 Tight','L1 Tight 3x3']
		
		c = TCanvas('cL1AndTightL1Count','L1AndTightL1Count')
		
		h = TH1D('hL1AndTightL1Count','L1 Efficiency',4,-0.5,N_BINS - .5)
		
		hL13x3Alone = TH1D('hL1And3x3Alone','',1,.5,1.5)
		hL13x3Alone.SetBinContent(1,nAll3x3/nAll)
		hL13x3Alone.SetBinError(1,calcSigma(nAll3x3,nAll))
		hL13x3Alone.SetLineColor(colorRwthMagenta)
		
		hTightL13x3Alone = TH1D('hTightL1And3x3Alone','',1,1.5,2.5)
		hTightL13x3Alone.SetBinContent(1,nTight3x3/nTight)
		hTightL13x3Alone.SetBinError(1,calcSigma(nTight3x3,nTight))
		hTightL13x3Alone.SetLineColor(colorRwthTuerkis)
		
		for i in range(2,N_BINS + 1):
			h.SetBinContent(i,binContents[i-1]/binContents[1])
			h.GetXaxis().SetBinLabel(i,binLabels[i-1])
			
		h.SetBinContent(1,1)
		
		h.SetLineColor(colorRwthDarkBlue)
		h.SetStats(0)
		h.GetYaxis().SetTitle('rel. fraction')
		h.Draw()
		hL13x3Alone.Draw('same e')
		hTightL13x3Alone.Draw('same e')
		
		setupAxes(h)
		
		legend = getLegend(y2=.9,x1=.55)
		legend.AddEntry(h,'Normed to total Events','l')
		legend.AddEntry(hL13x3Alone,'3x3 matching normed to # L1','le')
		legend.AddEntry(hTightL13x3Alone,'3x3 matching normed to # tight L1','le')
		legend.Draw()
		
		label = self.drawLabel()
		
		self.commandLine.output('###############################################')
		self.commandLine.output('n L1: \t\t%d \t=> %5.2f' 		% (nAll,nAll/float(nEvents)*100))
		self.commandLine.output('n L1 3x3: \t\t%d \t=> %5.2f (%5.2f)' 	% (nAll3x3,nAll3x3/float(nEvents)*100,nAll3x3/float(nAll)*100))
		self.commandLine.output('n tight L1: \t%d \t=> %5.2f'	% (nTight,nTight/float(nAll)*100))
		self.commandLine.output('n tight L1 3x3: \t%d \t=> %5.2f (%5.2f)' % (nTight3x3,nTight3x3/float(nEvents)*100,nTight3x3/float(nTight)*100))
		self.commandLine.output('###############################################')
		
		
		c.Update()
		c.SaveAs('plots/efficiency/l1AndTightL1Counters.gif')
		
		return h,c,hL13x3Alone,hTightL13x3Alone,label,legend
	
	def plotTightL1EtaPhiRatio(self):
		gL1Tight = self.fileHandler.getGraph('hoMuonAnalyzer/graphs/L1TightMuons')
		gL1Tight3x3 = self.fileHandler.getGraph('hoMuonAnalyzer/graphs/L1TightMuons3x3')
		
		halfPhiBinwidth = L1_PHI_BIN/2.
		
		hL1Tight = TH2D('hL1Tight','L1Tight',30,-15*L1_ETA_BIN	,15*L1_ETA_BIN,
					145, -math.pi - halfPhiBinwidth,math.pi + halfPhiBinwidth)
	
		hL1Tight3x3 = TH2D('hL1Tight3x3','L1Tight3x3',30,-15*L1_ETA_BIN	,15*L1_ETA_BIN,
					145, -math.pi - halfPhiBinwidth,math.pi + halfPhiBinwidth)

		hL1Tight = fillGraphIn2DHist(gL1Tight,hL1Tight)
		hL1Tight3x3 = fillGraphIn2DHist(gL1Tight3x3,hL1Tight3x3)
		
		hRatio = hL1Tight3x3.Clone('asdfasdf')
		hRatio.Divide(hL1Tight)
		
		c = TCanvas('2dMap')
		hRatio.SetTitle('Local Efficiency per tight L1 coordinate (3x3 Matching);#eta_{L1};#phi_{L1};#epsilon')
		hRatio.Draw('colz')
		hRatio.SetStats(0)
		c.Update()
		setupAxes(hRatio)
		setupPalette(hRatio)
		label = self.drawLabel()
		c.Update()
		c.SaveAs('plots/efficiency/localTightL1Efficiency.gif')

		c2 = TCanvas('projections')
		c2.Divide(2,1)
		c2.cd(1)
		hEta = hRatio.ProjectionX()
		hEta.Scale(1/float(hRatio.GetNbinsY()))
		hEta.Draw()
		
		c2.cd(2)
		hPhi = hRatio.ProjectionY()
		hPhi.Scale(1/float(hRatio.GetNbinsX()))
		hPhi.Draw()
		
		return c,hRatio,label,c2,hEta,hPhi
	