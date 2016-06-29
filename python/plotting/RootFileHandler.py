#!/bin/env python
import os
from ROOT import TChain,TFile,SetOwnership,Double
from plotting.OutputModule import CommandLineHandler

commandLine = CommandLineHandler('[RootFileHandler] ')

class RootFileHandler:
	#Look, how many files with the given name trunk in filename exist in the directory
	def getNumberOfFiles(self):
		fileCounter = 0
		self.fileNameList = []
		#cut away file extension
		if self.filename.rfind('.root') != -1:
			self.filename = self.filename[:-5]
		commandLine.debug(self.filepath)
		commandLine.debug(self.filename)
		for f in os.listdir(self.filepath):
			if f.find(self.filename) != -1:
				fileCounter += 1
				self.fileNameList.append(f)
		self.numberOfFiles = fileCounter
		pass
	
	#Initialize object
	def __init__(self,filename,debug = False):
		self.DEBUG = debug
		if filename[0] == '/':
			self.filepath = ''
		else:
			self.filepath = './'
		directoryIndex = filename.rfind('/')
		if directoryIndex != -1:
			self.filepath += filename[0:directoryIndex+1]
		self.filename = filename[directoryIndex+1:]
		self.getNumberOfFiles()
		pass
	
	#Get a tChain for the dataTree in the result root files
	def getTChain(self):
		chain = TChain('hoDataTreeFiller/dataTree')
		for f in self.fileNameList:
			chain.Add(f)
		return chain
	
	#Print status information
	def printStatus(self):
		print '[RootFileHandler] Looking for files with naming scheme \'%s\'' % (self.filename)
		if(self.numberOfFiles == 0):
			commandLine.error('Found no matching files!')
		else:
			commandLine.output('Found %d matching files:' % (self.numberOfFiles))
		for filename in self.fileNameList:
			print '[RootFileHandler]\t' + filename
		print
		
	'''
	Get the histogram with the given name from the result files.
	A new histogram is created as a clone from the first histogram,
	and then, the histograms from the other files are added in a loop
	'''
	def getHistogram(self,histoname):
		rootfile = TFile(self.filepath + '/' + self.fileNameList[0],'READ')
		try:
			histNew = rootfile.Get(histoname).Clone()
		except ReferenceError:
			if self.DEBUG: commandLine.warning('Could not get histogram %s' % histoname)
			return None
		histNew.SetDirectory(0)
		for i in range(1,len(self.fileNameList)):
			rootfile = TFile(self.filepath + '/' + self.fileNameList[i],'READ')
			try:
				hist = rootfile.Get(histoname).Clone()
				histNew.Add(hist)
			except ReferenceError:
				if self.DEBUG: commandLine.warning('Could not get histogram %s for every source file' % histoname)
		histNew.SetLineWidth(3)
		return histNew
	
	'''
	Get the graph with the given name from the result files
	The points from the additional files are added to the graph
	from the first file
	'''
	def getGraph(self,graphname,filesToProcess = -1):
		rootfile = TFile(self.fileNameList[0],'READ')
		graph = rootfile.Get(graphname)
		nTotal = 0
		counter = graph.GetN()
		
		#Check whether a number of result files to process is given
		fileRange = filesToProcess if (filesToProcess != -1) else len(self.fileNameList)
		#Then check that we don't try process more files than available
		fileRange = min(len(self.fileNameList), fileRange )
		
		for i in range(0,fileRange):
			rootfile = TFile(self.fileNameList[i],'READ')
			g = rootfile.Get(graphname)
			nTotal += g.GetN()
		commandLine.output('getGraph(%s) found %d points to process' % (graphname,nTotal))
		for i in range(1,fileRange):
			rootfile = TFile(self.fileNameList[i],'READ')
			g2 = rootfile.Get(graphname)
			x = Double(0)
			y = Double(0)
			for j in range(0,g2.GetN()):
				counter += 1
				if (counter % 10000 == 0):
					commandLine.printProgress(counter,nTotal)
				g2.GetPoint(j,x,y)
				graph.SetPoint(graph.GetN(),x,y)
		commandLine.printProgress(counter,nTotal)
		print
		return graph

	def printNEvents(self):
		hEvents = self.getHistogram('hoMuonAnalyzer/count/Events_Count')
		commandLine.warning('Sample contained %d events' % hEvents.GetBinContent(2))
