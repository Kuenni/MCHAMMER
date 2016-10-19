'''
Created on Oct 5, 2016

@author: kuensken
'''
from plotting.Plot import Plot

from dataQuality.EvsEtaPhi import EvsEtaPhi
from plotting.PlotStyle import drawHoBoxes
from plotting.Utils import calcSigma

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
		boxes = None

		eVsEtaPhiLib = EvsEtaPhi(self.filename, self.data, self.DEBUG)
		libStuff = eVsEtaPhiLib.makeEmaxPlot('_NoL1_Tdmi','# of E_{Max} in HO tiles around extrapolated muon position')
		#boxes = drawHoBoxes(libStuff[0])
		return [libStuff,boxes]
	
	def printNoL1Info(self):
		hEventCount = self.fileHandler.getHistogram('count/Events_Count')
		nEvents = hEventCount.GetBinContent(2)
		
		hNoL1Count = self.fileHandler.getHistogram('count/NoL1Muon_Count')
		nNoL1Events = hNoL1Count.GetBinContent(2)
		
		hNoL1Ho = self.fileHandler.getHistogram('deltaEtaDeltaPhiEnergy/averageEMaxAroundPoint_NoL1_Tdmi_2dCounter')
		nNoL1HoEvents = hNoL1Ho.Integral()
		
		self.debug(60*'#')
		self.debug('%15s %7d' % ('N Events',nEvents))
		self.debug('%15s %7d %5.2f%% +/- %5.2f%%' % ('N No L1',nNoL1Events,nNoL1Events/nEvents*100,calcSigma(nNoL1Events,nEvents)*100))
		self.debug('%15s %7d %5.2f%% +/- %5.2f%%' % ('N No L1 + HO',nNoL1HoEvents,nNoL1HoEvents/nEvents*100,calcSigma(nNoL1HoEvents,nEvents)*100))
		self.debug(60*'#')