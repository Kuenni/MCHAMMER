from math import sqrt,pi
import sys

class CommandLineHandler:
	#Output function for the progress in a python script
	def getProgressString(self,done,total):
		nHashes = int(done/float(total)*80)
		progressbar = '\r[%s%s] %5.2f%% done.' % (nHashes*'#',(80-nHashes)*' ',done*100/float(total))
		return progressbar

	#Output function for the progress in a python script
	def printProgress(self,done,total):
		s = self.getProgressString(done, total)
		sys.stdout.write(s)
		sys.stdout.flush()
		pass

	#Automatically add prefix to output
	def output(self,outString):
		print self.prefix,outString

	def __init__(self,outputPrefix):
		self.prefix = outputPrefix