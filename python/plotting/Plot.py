from plotting.PlotStyle import setPlotStyle, drawLabelCmsPrivateData,\
	drawLabelCmsPrivateSimulation
from plotting.OutputModule import CommandLineHandler
from plotting.RootFileHandler import RootFileHandler

import os

class Plot:
	def __init__(self,filename = None,data = False, debug = False):
		setPlotStyle()
		self.commandLine = CommandLineHandler('[' + self.__class__.__name__ + '] ')
		self.key = 'L1MuonPresent' if data else 'L1MuonTruth'
		self.data = data
		self.DEBUG = debug
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
		self.plotSubdir = 'plots/' + subdirname
		return
	
	#Save a canvas as gif file with the source data file name attached
	def storeCanvas(self,canvas,plotname):
		canvas.SaveAs('%s/%s_%s.gif'%(self.plotSubdir,plotname,self.fileHandler.filename))
		return
	
	def drawLabel(self):
		label = None
		if self.data:
			label = drawLabelCmsPrivateData()
		else:
			label = drawLabelCmsPrivateSimulation()
		return label
	
	def debug(self,string):
		self.commandLine.debug(string)
	
	def warning(self,string):
		self.commandLine.warning(string)
		
	def error(self,string):
		self.commandLine.error(string)
		
	def output(self,string):
		self.commandLine.output(string)