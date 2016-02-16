from plotting.Plot import Plot

from ROOT import TCanvas,TH1D,TH2D,TText
from plotting.PlotStyle import calcSigma, colorRwthDarkBlue, colorRwthMagenta,\
	colorRwthTuerkis, setupAxes, setupPalette, colorRwthOrange
from plotting.Utils import getLegend, L1_ETA_BIN, L1_PHI_BIN, fillGraphIn2DHist,calcPercent,getXinNDC

import math

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
		
		hL1 = self.fileHandler.getHistogram('hoMuonAnalyzer/count/energyDeposit_L1_Count')
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
			self.commandLine.output('%-20s:%8d\t=> %5.2f' % (names[i],h.GetBinContent(2),calcPercent(h.GetBinContent(2),nL1)))
		self.commandLine.output('###############################################')

		
		nL1Reco 		= hL1Reco.GetBinContent(2)
		nL1RecoHo 		= hL1RecoHo.GetBinContent(2)
		nL1RecoHoTight 	= hL1RecoHoTight.GetBinContent(2)
		nL1RecoTight 	= hL1RecoTight.GetBinContent(2)
		nL1RecoTightHo	= hL1RecoTightHo.GetBinContent(2)
		
		N_BINS = 4
		
		binContents = [nL1,nL1Reco,nL1RecoHo,nL1RecoHoTight]
		binLabels = ['L1','L1 -> Reco','L1 + R -> HO','L1 + R + HO -> tight']
		
		binContentsInverted = [nL1,nL1Reco,nL1RecoTight,nL1RecoTightHo]
		binLabelsInverted = ['L1','L1 -> Reco','L1 + R -> tight','L1 + R + tight -> HO']

		c = TCanvas('cL1AndTightL1Count','L1AndTightL1Count')
		
		h = TH1D('hL1AndTightL1Count','L1 Cutflow',4,-0.5,N_BINS - .5)
		hInverted = TH1D('hL1AndTightL1CountInverted','L1 Efficiency',4,-0.5,N_BINS - .5)
		hInverted.SetFillStyle(3002)
		hInverted.SetFillColor(colorRwthOrange)
		hInverted.SetLineColor(colorRwthOrange)
		hInverted.SetLineStyle(3)
		
		hL13x3Alone = TH1D('hL1And3x3Alone','',1,1.5,2.5)
		hL13x3Alone.SetBinContent(1,nL1RecoHo/nL1Reco)
		hL13x3Alone.SetBinError(1,calcSigma(nL1RecoHo,nL1Reco))
		hL13x3Alone.SetLineColor(colorRwthMagenta)
		
		hTightL13x3Alone = TH1D('hTightL1And3x3Alone','',1,2.5,3.5)
		hTightL13x3Alone.SetBinContent(1,nL1RecoHoTight/nL1RecoHo)
		hTightL13x3Alone.SetBinError(1,calcSigma(nL1RecoHoTight,nL1RecoHo))
		hTightL13x3Alone.SetLineColor(colorRwthTuerkis)
		
		for i in range(2,N_BINS + 1):
			h.SetBinContent(i,binContents[i-1]/binContents[1])
			h.GetXaxis().SetBinLabel(i,binLabels[i-1])
			hInverted.SetBinContent(i,binContentsInverted[i-1]/binContentsInverted[1])
			hInverted.GetXaxis().SetBinLabel(i,binLabelsInverted[i-1])
			
		h.GetXaxis().SetBinLabel(1,'L1')
		h.SetBinContent(1,1)
		hInverted.GetXaxis().SetBinLabel(1,'L1')
		hInverted.SetBinContent(1,1)
		
		h.SetLineColor(colorRwthDarkBlue)
		h.SetStats(0)
		h.GetYaxis().SetTitle('rel. fraction')
		h.Draw()
#		hL13x3Alone.Draw('same e')
#		hTightL13x3Alone.Draw('same e')
		hInverted.Draw('same')
		hInverted.GetXaxis().Draw('same')
		
		setupAxes(h)
		
		legend = getLegend(y2=.9,x1=.55)
		legend.AddEntry(h,'First match HO then use tight','l')
#		legend.AddEntry(hL13x3Alone,'3x3 matching normed to # L1 + R','le')
#		legend.AddEntry(hTightL13x3Alone,'Normed to # L1 + R + HO','l')
		legend.AddEntry(hInverted,'Inverted order for HO and tight','f')
		legend.Draw()
		
		label = self.drawLabel()
		
		textObjects = []

		#for (Int_t i=1;i<=30;i++) t.DrawText(h->GetBinCenter(i),yt,Form("%d",i%10));
		for i in range(1,4):
			t = TText()
			t.SetTextSize(0.025)
			t.SetTextAlign(22)
			t.SetTextColor(colorRwthOrange)
			t.DrawTextNDC(getXinNDC(hInverted.GetBinCenter(i+1)),0.05,binLabelsInverted[i])
#			Double_t yt = - h->GetMaximum()/15.;
			textObjects.append(t)
		c.Update()
		c.SaveAs('plots/efficiency/l1AndTightL1Counters.gif')
		
		return h,c,hL13x3Alone,hTightL13x3Alone,label,legend,hInverted,textObjects
	
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
		hEta.Scale(1/float(72))#72 phi bins
		hEta.Draw()
		
		c2.cd(2)
		hPhi = hRatio.ProjectionY()
		hPhi.Scale(1/float(30))#16 eta bins, cutoff due to |eta| < 0.8
		hPhi.Draw()
		
		return c,hRatio,label,c2,hEta,hPhi
	