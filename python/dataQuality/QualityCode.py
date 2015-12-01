import os

from plotting.OutputModule import CommandLineHandler
from plotting.RootFileHandler import RootFileHandler
from plotting.PlotStyle import setPlotStyle, setupPalette,\
	drawLabelCmsPrivateData, drawLabelCmsPrivateSimulation

from ROOT import TCanvas,TBox

class QualityCode:
	def __init__(self,filename,data =False):
		self.commandLine = CommandLineHandler('[QualityCode] ')
		self.fileHandler = RootFileHandler(filename)
		self.fileHandler.printStatus()
		if( not os.path.exists('plots')):
			os.mkdir('plots')
		if( not os.path.exists('plots/qualityCode')):
			os.mkdir('plots/qualityCode')
		setPlotStyle()
		self.data = data
		
	def plot3x3MatchQualityCodes(self):
		c = TCanvas('cMatchQC3x3','Match QC 3x3',0,0,900,700)
		c.SetLogz()
		hist = self.fileHandler.getHistogram('hoMuonAnalyzer/qualityCode/L1Muon3x3Match_QcVsPt')
		hist.SetStats(0)
		hist.Scale(1,'width')
		hist.Draw('colz')
		c.Update()
		setupPalette(hist)
		c.Update()
				
		label = None
		if self.data:
			label = drawLabelCmsPrivateData()
		else:
			label = drawLabelCmsPrivateSimulation()
		
		c.Update()
		
		box = TBox(0,6.5,180,7.5)
		box.SetLineColor(3)
		box.SetLineWidth(2)
		box.Draw()
		
		c.Update()
		
		return hist,c,label,box
	
	def plot3x3FailQualityCodes(self):
		c = TCanvas('cFailQC3x3','Fail QC 3x3',910,0,900,700)
		c.SetLogz()
		hist = self.fileHandler.getHistogram('hoMuonAnalyzer/qualityCode/L1Muon3x3Fail_QcVsPt')
		hist.SetStats(0)
		hist.Scale(1,'width')
		hist.Draw('colz')
		c.Update()
		setupPalette(hist)
		c.Update()

		label = None
		if self.data:
			label = drawLabelCmsPrivateData()
		else:
			label = drawLabelCmsPrivateSimulation()		

		c.Update()

		return hist,c,label
		