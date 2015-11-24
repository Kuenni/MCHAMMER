import os

from plotting.OutputModule import CommandLineHandler
from plotting.RootFileHandler import RootFileHandler
from plotting.PlotStyle import *
from plotting.Utils import getTGraphErrors,getLegend

from ROOT import TCanvas

class PtResolution:
	def __init__(self,filename,data =False):
		self.commandLine = CommandLineHandler('[PtResolution] ')
		self.fileHandler = RootFileHandler(filename)
		self.fileHandler.printStatus()
		if( not os.path.exists('plots')):
			os.mkdir('plots')
		if( not os.path.exists('plots/ptResolution')):
			os.mkdir('plots/ptResolution')
		setPlotStyle()
		
	def plotPtResolutionHistograms(self):
		ptVals = []
		rmsL1 = []
		rmsL1Err = []
		rmsL1AndHo = []
		rmsL1AndHoErr = []
		
		for i in range(0,101):
			#Change "xGev" to "Binx"
			#Then calculate pt range from bin number
			histPt = self.fileHandler.getHistogram('hoMuonAnalyzer/l1PtResolution/L1MuonTruth%dGeV' % i)
			histPtMatch = self.fileHandler.getHistogram('hoMuonAnalyzer/l1PtResolution/L1MuonTruthHoMatch%dGeV' % i)
			c = TCanvas()
			ptVals.append(i*2)
			if histPt == None:
				rmsL1.append(0)
				rmsL1Err.append(0)
				continue
			rmsL1.append(histPt.GetRMS())
			rmsL1Err.append(histPt.GetRMSError())
			setupAxes(histPt)
			histPt.SetLineWidth(3)
			histPt.SetLineColor(colorRwthDarkBlue)
			histPt.Draw()
			if histPtMatch != None:
				rmsL1AndHo.append(histPtMatch.GetRMS())
				rmsL1AndHoErr.append(histPtMatch.GetRMSError())
				histPtMatch.SetLineWidth(3)
				histPtMatch.SetLineColor(colorRwthMagenta)
				histPtMatch.Draw('same')
			else:
				rmsL1AndHo.append(0)
				rmsL1AndHoErr.append(0)
			c.SaveAs('plots/ptResolution/L1Muon%d.gif' % i)
		
		c = TCanvas()
		graphL1 = getTGraphErrors(ptVals,rmsL1,ey = rmsL1Err)
		graphL1.SetMarkerStyle(20)
		graphL1.SetMarkerColor(colorRwthDarkBlue)
		graphL1.SetLineColor(colorRwthDarkBlue)
		graphL1.SetTitle("RMS of L1 Objects;p_{T} / GeV;RMS / GeV")
		graphL1.Draw('ap')
		
		graphL1AndHo = getTGraphErrors(ptVals,rmsL1AndHo,ey = rmsL1AndHoErr)
		graphL1AndHo.SetMarkerStyle(21)
		graphL1AndHo.SetMarkerColor(colorRwthMagenta)
		graphL1AndHo.SetLineColor(colorRwthMagenta)
		graphL1AndHo.Draw('samep')
		
		setupAxes(graphL1)
		
		legend = getLegend(y2 = .9)
		legend.AddEntry(graphL1,'RMS L1','ep')
		legend.AddEntry(graphL1AndHo,'RMS L1 and HO','ep')
		legend.Draw()
		
		c.Update()
		
		c.SaveAs('plots/ptResolution/rmsVsPt.gif')
		c.SaveAs('plots/ptResolution/rmsVsPt.pdf')
		
		return c,graphL1,graphL1AndHo,legend
			
			