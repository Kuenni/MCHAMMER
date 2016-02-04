from plotting.PlotStyle import setPlotStyle, drawLabelCmsPrivateData,\
	drawLabelCmsPrivateSimulation
from plotting.OutputModule import CommandLineHandler
from plotting.RootFileHandler import RootFileHandler

import os

class Plot:
	def __init__(self,filename = None,data = False):
		setPlotStyle()
		self.commandLine = CommandLineHandler('[' + self.__class__.__name__ + '] ')
		self.key = 'L1MuonPresent' if data else 'L1MuonTruth'
		self.data = data
		if filename != None:
			self.fileHandler = self.createFileHandler(filename)
		pass
	
	def createFileHandler(self,filename):
		fh = RootFileHandler(filename)
		fh.printStatus()
		return fh
	
	def createPlotSubdir(self,subdirname):
		if( not os.path.exists('plots')):
			os.mkdir('plots')
		if( not os.path.exists('plots/' + subdirname)):
			os.mkdir('plots/' + subdirname)
		pass
	
	def drawLabel(self):
		label = None
		if self.data:
			label = drawLabelCmsPrivateData()
		else:
			label = drawLabelCmsPrivateSimulation()
		return label