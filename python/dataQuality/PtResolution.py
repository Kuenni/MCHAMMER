import os

from plotting.PlotStyle import *
from plotting.Utils import getTGraphErrors,getLegend

from ROOT import TCanvas,TF1,TGraphErrors
from plotting.Plot import Plot
import math

class PtResolution(Plot):
	def __init__(self,filename,data = False):
		Plot.__init__(self,filename,data)
		self.createPlotSubdir('ptResolution')

	###
	#	Get data from the histograms in a python list
	###
	def getHistoDataAsList(self,sourceName):
		values 		= []
		valuesErr 	= []
		
		for i in range(0,121):
			hist = self.fileHandler.getHistogram(sourceName + 'Bin%d' % i)
			if hist != None:
				values.append(hist.GetRMS())
				valuesErr.append(hist.GetRMSError())
			else:
				values.append(0)
				valuesErr.append(0)
		
		return values,valuesErr
	
	###
	#	Get the intrgrals of the source histograms
	###
	def getHistogramIntegralsAsList(self,sourceName):
		values 		= []
		valuesErr 	= []
		
		for i in range(0,121):
			hist = self.fileHandler.getHistogram(sourceName + 'Bin%d' % i)
			if hist != None:
				integral = hist.Integral()
				values.append(integral)
				valuesErr.append(math.sqrt(integral))
			else:
				values.append(0)
				valuesErr.append(0)
		
		return values,valuesErr
	
	###
	#	Get the pT values for the x axes as list
	###
	def getXaxisData(self):
		x 		= []
		xErr	= []

		for i in range(0,121):
			if i < 40:
				x.append(i + 0.5)
				xErr.append(0.5)
			else:
				x.append(i*2 - 40 + 1)
				xErr.append(1)
			
		return x,xErr
		
	def plotPtResolutionHistograms(self):
		ptVals = []
		ptErr = []
		rmsL1 = []
		rmsL1Err = []
		rmsL1Tight = []
		rmsL1TightErr = []
		rmsL1AndHo = []
		rmsL1AndHoErr = []
		rmsL1TightAndHo = []
		rmsL1TightAndHoErr = []
		rmsL1NotHo = []
		rmsL1NotHoErr = []
		rmsL1TightNotHo = []
		rmsL1TightNotHoErr = []
		
		graphL1Fit = TGraphErrors()
		
		for i in range(0,121):
			#calculate pt range from bin number
			histPt = self.fileHandler.getHistogram('hoMuonAnalyzer/l1PtResolution/L1MuonTruthBin%d' % i)
			histPtTight = self.fileHandler.getHistogram('hoMuonAnalyzer/l1PtResolution/L1MuonTightTruthBin%d' % i)
			histPtMatch = self.fileHandler.getHistogram('hoMuonAnalyzer/l1PtResolution/L1MuonTruthHoMatchBin%d' % i)
			histPtTightMatch = self.fileHandler.getHistogram('hoMuonAnalyzer/l1PtResolution/L1MuonTightTruthHoMatchBin%d' % i)
			histNoMatch = self.fileHandler.getHistogram('hoMuonAnalyzer/l1PtResolution/L1MuonTruthNotHoMatchBin%d' % i)
			histTightNoMatch = self.fileHandler.getHistogram('hoMuonAnalyzer/l1PtResolution/L1MuonTightTruthNotHoMatchBin%d' % i)
			c = TCanvas()
			c.SetLogy()
			if i < 40:
				ptVals.append(i + 0.5)
				ptErr.append(0.5)
			else:
				ptVals.append(i*2 - 40 + 1)
				ptErr.append(1)
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
				rmsL1Tight.append(histPtTight.GetRMS())
				rmsL1TightErr.append(histPtTight.GetRMSError())
				histPtTight.SetLineWidth(3)
				histPtTight.SetLineColor(colorRwthGruen)
				histPtTight.SetFillStyle(3002)
				histPtTight.SetFillColor(colorRwthGruen)
				histPtTight.Draw('same')
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
			if histNoMatch != None:
				rmsL1NotHo.append(histNoMatch.GetRMS())
				rmsL1NotHoErr.append(histNoMatch.GetRMSError())
			else:
				rmsL1NotHo.append(0)
				rmsL1NotHoErr.append(0)
			if histTightNoMatch != None:
				rmsL1TightNotHo.append(histTightNoMatch.GetRMS())
				rmsL1TightNotHoErr.append(histTightNoMatch.GetRMSError())
			else:
				rmsL1TightNotHo.append(0)
				rmsL1TightNotHoErr.append(0)
			self.storeCanvas(c, 'hists/L1Muon%d' % i)
		
		c = TCanvas()
		graphL1 = getTGraphErrors(ptVals,rmsL1,ey = rmsL1Err,ex=ptErr)
		graphL1.SetMarkerStyle(20)
		graphL1.SetMarkerColor(colorRwthDarkBlue)
		graphL1.SetLineColor(colorRwthDarkBlue)
		graphL1.SetTitle("RMS of L1 Objects;p_{T} / GeV;RMS / GeV")
		graphL1.GetYaxis().SetRangeUser(0,75)
		graphL1.Draw('ap')
		
		graphL1Tight = getTGraphErrors(ptVals,rmsL1Tight,ey = rmsL1TightErr,ex=ptErr)
		graphL1Tight.SetMarkerStyle(21)
		graphL1Tight.SetMarkerColor(colorRwthGruen)
		graphL1Tight.SetLineColor(colorRwthGruen)
		graphL1Tight.Draw('samep')
		
		graphL1AndHo = getTGraphErrors(ptVals,rmsL1AndHo,ey = rmsL1AndHoErr,ex=ptErr)
		graphL1AndHo.SetMarkerStyle(26)
		graphL1AndHo.SetMarkerColor(colorRwthMagenta)
		graphL1AndHo.SetLineColor(colorRwthMagenta)
		graphL1AndHo.Draw('samep')
		
		graphL1TightAndHo = getTGraphErrors(ptVals,rmsL1TightAndHo,ey = rmsL1TightAndHoErr,ex=ptErr)
		graphL1TightAndHo.SetMarkerStyle(27)
		graphL1TightAndHo.SetMarkerColor(colorRwthRot)
		graphL1TightAndHo.SetLineColor(colorRwthRot)
		graphL1TightAndHo.Draw('samep')
		
		graphL1NotHo = getTGraphErrors(ptVals, rmsL1NotHo, ex=ptErr, ey=rmsL1NotHoErr)
		graphL1NotHo.SetMarkerStyle(29)
		graphL1NotHo.SetMarkerColor(colorRwthOrange)
		graphL1NotHo.SetLineColor(colorRwthOrange)
		graphL1NotHo.Draw('samep')
		
		graphL1TightNotHo = getTGraphErrors(ptVals, rmsL1TightNotHo, ex=ptErr, ey=rmsL1TightNotHoErr)
		graphL1TightNotHo.SetMarkerStyle(34)
		graphL1TightNotHo.SetMarkerColor(colorRwthLila)
		graphL1TightNotHo.SetLineColor(colorRwthLila)
		graphL1TightNotHo.Draw('samep')
		
		setupAxes(graphL1)
		
		legend = getLegend(y2 = .9)
		legend.AddEntry(graphL1,'RMS L1','ep')
		legend.AddEntry(graphL1AndHo,'RMS L1 and HO','ep')
		legend.AddEntry(graphL1Tight,'RMS L1 Tight','ep')
		legend.AddEntry(graphL1TightAndHo,'RMS L1 Tight and HO','ep')
		legend.AddEntry(graphL1NotHo,'RMS L1 & !HO','ep')
		legend.AddEntry(graphL1TightNotHo,'RMS L1 Tight & !HO','ep')
		legend.Draw()
		
		label = self.drawLabel()
		
		c.Update()
		
		self.storeCanvas(c, 'rmsVsPt')
		c2 = TCanvas('cfitResults','fitResults',800,0,800,600)
		graphL1Fit.Draw('AP')
		return c,graphL1,graphL1AndHo,legend,c2,graphL1Fit,label,graphL1TightAndHo,graphL1Tight, graphL1NotHo, graphL1TightNotHo

	def plotTightPtResolution(self):
		c = TCanvas('cTightResolution','cTightResolution')
		xData = self.getXaxisData()
		tightAndHo = self.getHistoDataAsList('hoMuonAnalyzer/l1PtResolution/L1MuonTightTruthHoMatch')
		tightAndNotHo = self.getHistoDataAsList('hoMuonAnalyzer/l1PtResolution/L1MuonTightTruthNotHoMatch')
		
		graphL1TightHo = getTGraphErrors(xData[0], tightAndHo[0], ex=xData[1], ey=tightAndHo[1])
		graphL1TightNotHo = getTGraphErrors(xData[0], tightAndNotHo[0], ex=xData[1], ey=tightAndNotHo[1])
		
		graphL1TightHo.SetMarkerStyle(20)
		graphL1TightHo.SetTitle('RMS of tight L1 Objects;p_{T} / GeV;RMS / GeV')
		graphL1TightHo.SetMarkerColor(colorRwthDarkBlue)
		graphL1TightHo.SetLineColor(colorRwthDarkBlue)
		
		graphL1TightNotHo.SetMarkerStyle(34)
		graphL1TightNotHo.SetMarkerColor(colorRwthMagenta)
		graphL1TightNotHo.SetLineColor(colorRwthMagenta)
		
		graphL1TightHo.Draw('ap')
		graphL1TightNotHo.Draw('samep')
		
		label = self.drawLabel()
		
		setupAxes(graphL1TightHo)
		legend = getLegend(y2 = .9)
		legend.AddEntry(graphL1TightHo,'L1 Tight & HO','ep')
		legend.AddEntry(graphL1TightNotHo,'L1 Tight & !HO','ep')
		legend.Draw()
		c.Update()
		
		self.storeCanvas(c, 'rmsVsPt_tight')
		##
		# Plot the integral for each histogram as a control plot
		##
		cControlPlot = TCanvas('cControlPlots','control plot integral')
		dataMatch,errorMatch = self.getHistogramIntegralsAsList('hoMuonAnalyzer/l1PtResolution/L1MuonTightTruthHoMatch')
		dataNoMatch,errorNoMatch = self.getHistogramIntegralsAsList('hoMuonAnalyzer/l1PtResolution/L1MuonTightTruthNotHoMatch')
		graphIntegralsMatch = getTGraphErrors(xData[0], dataMatch, ex=xData[1], ey=errorMatch)
		graphIntegralsNoMatch = getTGraphErrors(xData[0], dataNoMatch, ex=xData[1], ey=errorNoMatch)
		
		graphIntegralsMatch.SetMarkerStyle(20)
		graphIntegralsMatch.SetTitle('Integrals of tight L1 Object histograms;p_{T} / GeV;# entries')
		graphIntegralsMatch.SetMarkerColor(colorRwthDarkBlue)
		graphIntegralsMatch.SetLineColor(colorRwthDarkBlue)
		
		graphIntegralsNoMatch.SetMarkerStyle(34)
		graphIntegralsNoMatch.SetMarkerColor(colorRwthMagenta)
		graphIntegralsNoMatch.SetLineColor(colorRwthMagenta)
		
		graphIntegralsMatch.Draw('ap')
		graphIntegralsNoMatch.Draw('samep')
		
		label = self.drawLabel()
		
		setupAxes(graphIntegralsMatch)
		legend2 = getLegend(y2 = .9)
		legend2.AddEntry(graphIntegralsMatch,'L1 Tight & HO','ep')
		legend2.AddEntry(graphIntegralsNoMatch,'L1 Tight & !HO','ep')
		legend2.Draw()
		cControlPlot.Update()
		
		self.storeCanvas(cControlPlot, 'rmsVsPt_tight_integrals')
		return c,graphL1TightHo,graphL1TightNotHo,legend,label, legend2, graphIntegralsMatch, graphIntegralsNoMatch, cControlPlot
	
	def plotLoosePtResolution(self):
		c = TCanvas('cLooseResolution','cLooseResolution')
		xData = self.getXaxisData()
		tightAndHo = self.getHistoDataAsList('hoMuonAnalyzer/l1PtResolution/L1MuonTruthHoMatch')
		tightAndNotHo = self.getHistoDataAsList('hoMuonAnalyzer/l1PtResolution/L1MuonTruthNotHoMatch')
		
		graphL1TightHo = getTGraphErrors(xData[0], tightAndHo[0], ex=xData[1], ey=tightAndHo[1])
		graphL1TightNotHo = getTGraphErrors(xData[0], tightAndNotHo[0], ex=xData[1], ey=tightAndNotHo[1])
		
		graphL1TightHo.SetMarkerStyle(20)
		graphL1TightHo.SetTitle('RMS of loose L1 Objects;p_{T} / GeV;RMS / GeV')
		graphL1TightHo.SetMarkerColor(colorRwthDarkBlue)
		graphL1TightHo.SetLineColor(colorRwthDarkBlue)
		
		graphL1TightNotHo.SetMarkerStyle(34)
		graphL1TightNotHo.SetMarkerColor(colorRwthMagenta)
		graphL1TightNotHo.SetLineColor(colorRwthMagenta)
		
		graphL1TightHo.Draw('ap')
		graphL1TightNotHo.Draw('samep')
		
		label = self.drawLabel()
		
		setupAxes(graphL1TightHo)
		legend = getLegend(y2 = .9)
		legend.AddEntry(graphL1TightHo,'L1 & HO','ep')
		legend.AddEntry(graphL1TightNotHo,'L1 & !HO','ep')
		legend.Draw()
		c.Update()

		self.storeCanvas(c, 'rmsVsPt_loose')
		##
		# Plot the integral for each histogram as a control plot
		##
		cControlPlot = TCanvas('cControlPlotsLoose','control plot integral')
		dataMatch,errorMatch = self.getHistogramIntegralsAsList('hoMuonAnalyzer/l1PtResolution/L1MuonTruthHoMatch')
		dataNoMatch,errorNoMatch = self.getHistogramIntegralsAsList('hoMuonAnalyzer/l1PtResolution/L1MuonTruthNotHoMatch')
		graphIntegralsMatch = getTGraphErrors(xData[0], dataMatch, ex=xData[1], ey=errorMatch)
		graphIntegralsNoMatch = getTGraphErrors(xData[0], dataNoMatch, ex=xData[1], ey=errorNoMatch)
		
		graphIntegralsMatch.SetMarkerStyle(20)
		graphIntegralsMatch.SetTitle('Integral of loose L1 Object histograms;p_{T} / GeV;# entries')
		graphIntegralsMatch.SetMarkerColor(colorRwthDarkBlue)
		graphIntegralsMatch.SetLineColor(colorRwthDarkBlue)
		
		graphIntegralsNoMatch.SetMarkerStyle(34)
		graphIntegralsNoMatch.SetMarkerColor(colorRwthMagenta)
		graphIntegralsNoMatch.SetLineColor(colorRwthMagenta)
		
		graphIntegralsMatch.Draw('ap')
		graphIntegralsNoMatch.Draw('samep')
		
		label = self.drawLabel()
		
		setupAxes(graphIntegralsMatch)
		legend2 = getLegend(y2 = .9)
		legend2.AddEntry(graphIntegralsMatch,'L1 & HO','ep')
		legend2.AddEntry(graphIntegralsNoMatch,'L1 & !HO','ep')
		legend2.Draw()
		cControlPlot.Update()
		
		self.storeCanvas(cControlPlot, 'rmsVsPt_loose_integrals')
		return c,graphL1TightHo,graphL1TightNotHo,legend,label,graphIntegralsMatch,graphIntegralsNoMatch,legend2,cControlPlot
		