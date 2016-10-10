'''
Created on Oct 5, 2016

@author: kuensken
'''
from plotting.Plot import Plot

from dataQuality.EvsEtaPhi import EvsEtaPhi
from plotting.PlotStyle import drawHoBoxes

class NoL1Muon(Plot):
	'''
	classdocs
	'''


	def __init__(self,filename,data = False,debug=False):
		'''
		Constructor
		'''
		Plot.__init__(self,filename,data,debug = debug)
		self.createPlotSubdir('noL1Muon')
		
	def plotEMaxNoL1Muon(self):
		eVsEtaPhiLib = EvsEtaPhi(self.filename, self.data, self.DEBUG)
		libStuff = eVsEtaPhiLib.makeEmaxPlot('_NoL1_Tdmi')
		boxes = drawHoBoxes(libStuff[0])
		return [libStuff,boxes]