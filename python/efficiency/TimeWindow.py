import sys,os
from ROOT import TCanvas,TLegend
from plotting.RootFileHandler import RootFileHandler
from plotting.PlotStyle import setupAxes,setPlotStyle, colorRwthDarkBlue,\
	drawLabelCmsPrivateSimulation, colorRwthLightBlue, colorRwthGruen,\
	colorRwthTuerkis, colorRwthRot, colorRwthMagenta, setupPalette, pyplotCmsPrivateLabel,\
	drawLabelCmsPrivateData
from plotting.OutputModule import CommandLineHandler,CliColors
from plotting.Utils import extractTEfficiencyToList
import matplotlib.pyplot as plt


class TimeWindow:
	
	def __init__(self,filename,data = False):
		self.commandLine = CommandLineHandler('[TimeWindow] ')
		self.fileHandler = RootFileHandler(filename)
		self.fileHandler.printStatus()
		if( not os.path.exists('plots')):
			os.mkdir('plots')
		if( not os.path.exists('plots/efficiencyWithTime')):
			os.mkdir('plots/efficiencyWithTime')
		setPlotStyle()
		self.data = data
			
	def plotTimeWindowAlone(self):
		c = TCanvas('cTimeWindowAlone',"Time Window Alone")
		effL1Muon3x3Truth = self.fileHandler.getHistogram('hoMuonAnalyzer/efficiency/L1MuonTruthTimeWindow3x3_Efficiency')
		effL1Muon3x3 = self.fileHandler.getHistogram('hoMuonAnalyzer/efficiency/L1MuonTimeWindow3x3_Efficiency')
		
		effL1Muon3x3.SetMarkerStyle(22)
		effL1Muon3x3.SetMarkerColor(colorRwthDarkBlue)
		effL1Muon3x3.SetLineColor(colorRwthDarkBlue)
		effL1Muon3x3.SetTitle('Efficiency in 3x3 grid with time window;p_{T} / GeV;rel. fraction')
		effL1Muon3x3.Draw()
		c.Update()
		effL1Muon3x3.GetPaintedGraph().GetXaxis().SetRangeUser(0,40)
		#effL1Muon3x3.GetPaintedGraph().GetYaxis().SetRangeUser(0.996,1.001)
		effL1Muon3x3Truth.SetMarkerStyle(23)
		effL1Muon3x3Truth.SetMarkerColor(colorRwthMagenta)
		effL1Muon3x3Truth.SetLineColor(colorRwthMagenta)
		effL1Muon3x3Truth.Draw('same')
		
		setupAxes(effL1Muon3x3)
		
		legend = TLegend(0.55,0.1,0.9,0.3)
		legend.AddEntry(effL1Muon3x3,'Matches in 3x3 grid','ep')
		legend.AddEntry(effL1Muon3x3Truth,'Matches  to truth in 3x3 grid','ep')
		legend.Draw()
		
		label = None
		if self.data:
			label = drawLabelCmsPrivateData()
		else:
			label = drawLabelCmsPrivateSimulation()
		
		c.Update()
		
		return c, effL1Muon3x3,effL1Muon3x3Truth,label,legend
	
	def plotAllL1Together(self):
		c = TCanvas('cTimeWindowAllL1',"Time Window All L1")
		effL1Muon3x3 = self.fileHandler.getHistogram('hoMuonAnalyzer/efficiency/L1Muon3x3_Efficiency')
		effL1Muon3x3TW = self.fileHandler.getHistogram('hoMuonAnalyzer/efficiency/L1MuonTimeWindow3x3_Efficiency')

		effL1Muon3x3.SetMarkerStyle(22)
		effL1Muon3x3.SetMarkerColor(colorRwthDarkBlue)
		effL1Muon3x3.SetLineColor(colorRwthDarkBlue)
		effL1Muon3x3.SetTitle('Efficiency in 3x3 grid;p_{T} / GeV;rel. fraction')
		effL1Muon3x3.Draw()
		c.Update()
		#effL1Muon3x3.GetPaintedGraph().GetXaxis().SetRangeUser(0,40)
		#effL1Muon3x3.GetPaintedGraph().GetYaxis().SetRangeUser(0.996,1.001)
		effL1Muon3x3TW.SetMarkerStyle(23)
		effL1Muon3x3TW.SetMarkerColor(colorRwthMagenta)
		effL1Muon3x3TW.SetLineColor(colorRwthMagenta)
		effL1Muon3x3TW.Draw('same')
		
		setupAxes(effL1Muon3x3)
		
		legend = TLegend(0.55,0.1,0.9,0.3)
		legend.AddEntry(effL1Muon3x3,'Matches in 3x3 grid','ep')
		legend.AddEntry(effL1Muon3x3TW,'Matches in 3x3 grid and time window','ep')
		legend.Draw()
		
		label = None
		if self.data:
			label = drawLabelCmsPrivateData()
		else:
			label = drawLabelCmsPrivateSimulation()
					
		c.Update()
		return c, label, effL1Muon3x3, effL1Muon3x3TW, legend
		
	def plotTruthL1Together(self):
		c = TCanvas('cTimeWindowTruthL1',"Time Window Truth L1")
		effL1Muon3x3 = self.fileHandler.getHistogram('hoMuonAnalyzer/efficiency/L1MuonTruth3x3_Efficiency')
		effL1Muon3x3TW = self.fileHandler.getHistogram('hoMuonAnalyzer/efficiency/L1MuonTruthTimeWindow3x3_Efficiency')

		effL1Muon3x3.SetMarkerStyle(22)
		effL1Muon3x3.SetMarkerColor(colorRwthDarkBlue)
		effL1Muon3x3.SetLineColor(colorRwthDarkBlue)
		effL1Muon3x3.SetTitle('Efficiency Truth in 3x3 grid;p_{T} / GeV;rel. fraction')
		effL1Muon3x3.Draw()
		c.Update()
		effL1Muon3x3.GetPaintedGraph().GetXaxis().SetRangeUser(0,40)
		#effL1Muon3x3.GetPaintedGraph().GetYaxis().SetRangeUser(0.996,1.001)
		effL1Muon3x3TW.SetMarkerStyle(23)
		effL1Muon3x3TW.SetMarkerColor(colorRwthMagenta)
		effL1Muon3x3TW.SetLineColor(colorRwthMagenta)
		effL1Muon3x3TW.Draw('same')
		
		setupAxes(effL1Muon3x3)
		
		legend = TLegend(0.55,0.1,0.9,0.3)
		legend.AddEntry(effL1Muon3x3,'Matches to L1 Truth in 3x3 grid','ep')
		legend.AddEntry(effL1Muon3x3TW,'Matches to L1 Truth in 3x3 grid and time window','ep')
		legend.Draw()
		
		label = None
		if self.data:
			label = drawLabelCmsPrivateData()
		else:
			label = drawLabelCmsPrivateSimulation()
					
		c.Update()
		return c, label, effL1Muon3x3, effL1Muon3x3TW, legend
	
	def plotBxidVsPtFails(self):
		c = TCanvas('cBxidVsPtFails','BxidVsPtFails',800,1200)
		c.Divide(1,2)
		c.cd(1).SetLogz()
		hist = self.fileHandler.getHistogram('hoMuonAnalyzer/time/L1Muon3x3Fail_BxIdVsPt')
		setupAxes(hist)
		hist.SetTitle('Failed matching in 3x3;p_{T} / GeV;BX ID;# entries')
		hist.SetStats(0)
		hist.GetYaxis().SetRangeUser(-3,3)
		histCopy = hist.DrawCopy('colz')
		c.Update()
		setupPalette(histCopy)
		c.Update()
		label = None
		if self.data:
			label = drawLabelCmsPrivateData()
		else:
			label = drawLabelCmsPrivateSimulation()
			
		c.cd(2).SetLogz()
		hist.Scale(1,'width')
		hist.SetTitle(hist.GetTitle() + ', by bin width')
		hist.GetZaxis().SetTitle('# entries / GeV')
		hist.Draw('colz')
		c.Update()
		setupPalette(hist)
		c.Update()
		
		labelBottom = None
		if self.data:
			labelBottom = drawLabelCmsPrivateData()
		else:
			labelBottom = drawLabelCmsPrivateSimulation()
	
		c.Update()
		c.SaveAs('plots/efficiencyWithTime/bxIdVsPt3x3Fail.gif')
		return c, hist,label,labelBottom
	
	def plotBxidVsPtMatch(self):
		c = TCanvas('cBxidVsPtMatch','BxidVsPtMatch',800,1200)
		c.Divide(1,2)
		c.cd(1).SetLogz()
		hist = self.fileHandler.getHistogram('hoMuonAnalyzer/time/L1Muon3x3Match_BxIdVsPt')
		hist.SetStats(0)
		setupAxes(hist)
		hist.SetTitle('Successful matching in 3x3;p_{T} / GeV;BX ID;# entries')
		hist.GetYaxis().SetRangeUser(-3,3)
		
		histCopy = hist.DrawCopy('colz')
		c.Update()
		setupPalette(histCopy)
		c.Update()
		
		label = None
		if self.data:
			label = drawLabelCmsPrivateData()
		else:
			label = drawLabelCmsPrivateSimulation()
			
		c.cd(2).SetLogz()
		hist.Scale(1,'width')
		hist.SetTitle(hist.GetTitle() + ', by bin width')
		hist.GetZaxis().SetTitle('# entries / GeV')
		hist.Draw('colz')
		c.Update()
		setupPalette(hist)
		c.Update()
		
		labelBottom = None
		if self.data:
			labelBottom = drawLabelCmsPrivateData()
		else:
			labelBottom = drawLabelCmsPrivateSimulation()
		
		c.Update()
		c.SaveAs('plots/efficiencyWithTime/bxIdVsPt3x3Match.gif')
		
		return c, hist,label,labelBottom
	