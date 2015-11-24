import os

from plotting.OutputModule import CommandLineHandler
from plotting.RootFileHandler import RootFileHandler
from plotting.PlotStyle import *

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
		for i in range(0,101):
			#Change "xGev" to "Binx"
			#Then calculate pt range from bin number
			histPt = self.fileHandler.getHistogram('hoMuonAnalyzer/l1PtResolution/L1MuonTruth%dGeV')
			if histPt == None:
				continue