import os
from ROOT import TChain,TFile,SetOwnership
class RootFileHandler:
	#Look, how many files with the given name trunk in filename exist in the directory
	def getNumberOfFiles(self):
		fileCounter = 0
		self.fileNameList = []
		for f in os.listdir('.'):
			if f.find(self.filename) != -1:
				fileCounter += 1
				self.fileNameList.append(f)
		self.numberOfFiles = fileCounter
		pass
	
	#Initialize object
	def __init__(self,filename):
		self.filename = filename
		self.getNumberOfFiles()
		pass
	
	#Get a tChain for the dataTree in the result root files
	def getTChain(self):
		chain = TChain('hoMuonAnalyzer/dataTree')
		for f in self.fileNameList:
			chain.Add(f)
			pass
		return chain
	
	#Print status information
	def printStatus(self):
		print '[RootFileHandler] Looking for files with naming scheme \'%s\'' % (self.filename)
		print '[RootFileHandler] Found %d matching files' % (self.numberOfFiles)
		
	'''
	Get the histogram with the given name from the result files.
	A new histogram is created as a clone from the first histogram,
	and then, the histograms from the other files are added in a loop
	'''
	def getHistogram(self,histoname):
		histNew = None
		file = TFile(self.fileNameList[0])
		histNew = file.Get(histoname).Clone()
		histNew.SetDirectory(0)
		for i in range(1,len(self.fileNameList)):
			file = TFile(self.fileNameList[i])
			histNew.Add(file.Get(histoname))
		return histNew