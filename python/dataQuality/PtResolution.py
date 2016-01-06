import os

from plotting.OutputModule import CommandLineHandler
from plotting.RootFileHandler import RootFileHandler
from plotting.PlotStyle import *
from plotting.Utils import getTGraphErrors,getLegend

from ROOT import TCanvas,TF1,TGraphErrors
from plotting.Plot import Plot

class PtResolution(Plot):
	def __init__(self,filename,data =False):
		Plot.__init__(self,filename,data)
		self.createPlotSubdir('ptResolution')
		
	def plotPtResolutionHistograms(self):
		ptVals = []
		rmsL1 = []
		rmsL1Err = []
		rmsL1Tight = []
		rmsL1TightErr = []
		rmsL1AndHo = []
		rmsL1AndHoErr = []
		rmsL1TightAndHo = []
		rmsL1TightAndHoErr = []
		fitL1 = []
		fitL1Err = []
		
		graphL1Fit = TGraphErrors()
		
		for i in range(0,101):
			#calculate pt range from bin number
			histPt = self.fileHandler.getHistogram('hoMuonAnalyzer/l1PtResolution/L1MuonTruthBin%d' % i)
			histPtTight = self.fileHandler.getHistogram('hoMuonAnalyzer/l1PtResolution/L1MuonTightTruthBin%d' % i)
			histPtMatch = self.fileHandler.getHistogram('hoMuonAnalyzer/l1PtResolution/L1MuonTruthHoMatchBin%d' % i)
			histPtTightMatch = self.fileHandler.getHistogram('hoMuonAnalyzer/l1PtResolution/L1MuonTightTruthHoMatchBin%d' % i)
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
			if(i < 20):
				f1 = TF1("f1", "gaus", histPt.GetBinCenter(histPt.GetMaximumBin()) - 5, 2*i + 5);
				histPt.Fit(f1,"R")
				graphL1Fit.SetPoint(graphL1Fit.GetN(),i*2,f1.GetParameter(2))#,0,f1.GetParameter(3))
				#raw_input('-')
				
			if histPtMatch != None:
				rmsL1AndHo.append(histPtMatch.GetRMS())
				rmsL1AndHoErr.append(histPtMatch.GetRMSError())
				histPtMatch.SetLineWidth(3)
				histPtMatch.SetLineColor(colorRwthMagenta)
				histPtMatch.Draw('same')
			else:
				rmsL1AndHo.append(0)
				rmsL1AndHoErr.append(0)
			
			if histPtTight != None:
				rmsL1Tight.append(histPtMatch.GetRMS())
				rmsL1TightErr.append(histPtMatch.GetRMSError())
				histPtMatch.SetLineWidth(3)
				histPtMatch.SetLineColor(colorRwthGruen)
				histPtMatch.Draw('same')
			else:
				rmsL1Tight.append(0)
				rmsL1TightErr.append(0)
				
			if histPtTightMatch != None:
				rmsL1TightAndHo.append(histPtTightMatch.GetRMS())
				rmsL1TightAndHoErr.append(histPtTightMatch.GetRMSError())
				histPtTightMatch.SetLineWidth(3)
				histPtTightMatch.SetLineColor(colorRwthTuerkis)
				histPtTightMatch.Draw('same')
			else:
				rmsL1TightAndHo.append(0)
				rmsL1TightAndHoErr.append(0)
			c.SaveAs('plots/ptResolution/L1Muon%d.gif' % i)
		
		c = TCanvas()
		graphL1 = getTGraphErrors(ptVals,rmsL1,ey = rmsL1Err)
		graphL1.SetMarkerStyle(20)
		graphL1.SetMarkerColor(colorRwthDarkBlue)
		graphL1.SetLineColor(colorRwthDarkBlue)
		graphL1.SetTitle("RMS of L1 Objects;p_{T} / GeV;RMS / GeV")
		graphL1.GetYaxis().SetRangeUser(0,75)
		graphL1.Draw('ap')
		
		graphL1Tight = getTGraphErrors(ptVals,rmsL1Tight,ey = rmsL1TightErr)
		graphL1Tight.SetMarkerStyle(23)
		graphL1Tight.SetMarkerColor(colorRwthGruen)
		graphL1Tight.SetLineColor(colorRwthGruen)
		graphL1Tight.Draw('samep')
		
		graphL1AndHo = getTGraphErrors(ptVals,rmsL1AndHo,ey = rmsL1AndHoErr)
		graphL1AndHo.SetMarkerStyle(21)
		graphL1AndHo.SetMarkerColor(colorRwthMagenta)
		graphL1AndHo.SetLineColor(colorRwthMagenta)
		graphL1AndHo.Draw('samep')
		
		graphL1TightAndHo = getTGraphErrors(ptVals,rmsL1TightAndHo,ey = rmsL1TightAndHoErr)
		graphL1TightAndHo.SetMarkerStyle(22)
		graphL1TightAndHo.SetMarkerColor(colorRwthTuerkis)
		graphL1TightAndHo.SetLineColor(colorRwthTuerkis)
		graphL1TightAndHo.Draw('samep')
		
		setupAxes(graphL1)
		
		legend = getLegend(y2 = .9)
		legend.AddEntry(graphL1,'RMS L1','ep')
		legend.AddEntry(graphL1AndHo,'RMS L1 and HO','ep')
		legend.AddEntry(graphL1Tight,'RMS L1 Tight','ep')
		legend.AddEntry(graphL1TightAndHo,'RMS L1 Tight and HO','ep')
		legend.Draw()
		
		label = self.drawLabel()
		
		c.Update()
		
		c.SaveAs('plots/ptResolution/rmsVsPt.gif')
		c.SaveAs('plots/ptResolution/rmsVsPt.pdf')
		
		c2 = TCanvas('cfitResults','fitResults',800,0,800,600)
		graphL1Fit.Draw('AP')
		return c,graphL1,graphL1AndHo,legend,c2,graphL1Fit,label,graphL1TightAndHo,graphL1Tight
			