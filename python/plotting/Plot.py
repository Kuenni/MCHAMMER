from plotting.PlotStyle import setPlotStyle, drawLabelCmsPrivateData,\
	drawLabelCmsPrivateSimulation
from plotting.OutputModule import CommandLineHandler, CliColors
from plotting.RootFileHandler import RootFileHandler

import os
import sys
import inspect
import subprocess
import cmd
import shlex

class Plot:
	def __init__(self,filename = None,data = False, debug = False):
		setPlotStyle()
		self.commandLine = CommandLineHandler('[' + self.__class__.__name__ + ']')
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
	
	def getGitCommitHash(self):
		cmd = shlex.split("git show --abbrev-commit")
		process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
		gitOutput,err = process.communicate()
		gch = 'None'
		for line in gitOutput.split('\n'):
			if line.find('commit') != -1:
				gch = line.split(' ')[-1]
		return gch
	
	def createPlotSubdir(self,subdirname):
		if( not os.path.exists('plots')):
			self.debug('Creating dir plots')
			os.mkdir('plots')
		gitCommitHash = self.getGitCommitHash()
		if( not os.path.exists('plots/' + gitCommitHash)):
			self.debug('Creating dir plots/' + gitCommitHash)
			os.mkdir('plots/' + gitCommitHash)
		if( not os.path.exists('plots/' + gitCommitHash + '/' + subdirname)):
			self.debug('Creating dir plots/' + gitCommitHash + '/' + subdirname)
			os.mkdir('plots/' + gitCommitHash + '/' + subdirname)
		self.plotSubdir = 'plots/' + gitCommitHash + '/' + subdirname
		return
	
	#Save a canvas as gif file with the source data file name attached
	def storeCanvas(self,canvas,plotname):
		if(plotname.find('/') != -1):
			if( not os.path.exists(self.plotSubdir + '/' + plotname[0:plotname.rfind('/')])):
				os.makedirs(self.plotSubdir + '/' + plotname[0:plotname.rfind('/')])
				
		canvas.SaveAs('%s/%s_%s.gif'%(self.plotSubdir,plotname,self.fileHandler.filename))
		canvas.SaveAs('%s/%s_%s.png'%(self.plotSubdir,plotname,self.fileHandler.filename))
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
		self.commandLine.output(CliColors.BOLD + '<' + inspect.stack()[1][3] + '>  ' + CliColors.ENDC + str(string))