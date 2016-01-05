from plotting.Plot import Plot

from ROOT import TCanvas
from plotting.Utils import getTGraphErrors
import math

class HoThresholdScan(Plot):
	
	def __init__(self,filename,data = False):
		Plot.__init__(self,filename,data)
		self.createPlotSubdir('hoThresholdScan')
		
	def plotHoThresholdScan(self):
		canvas = TCanvas('cThresholdScan')
		xVals = []
		yVals = []
		yErr = []
		for i in range(0,199):
			hist = self.fileHandler.getHistogram('hoMuonAnalyzer/multiplicity/recHitThrScan%d_Multiplicity' % i)
			hist.GetXaxis().SetRangeUser(0,50)
			hist.Draw()
			canvas.SaveAs('plots/hoThresholdScan/hist%fGeV.gif' % ((i+1)*0.025))
			yVals.append(hist.GetBinCenter(hist.GetMaximumBin()))
			yErr.append(math.sqrt(yVals[-1]))
			xVals.append((i+1)*0.025)
 		graph = getTGraphErrors(xVals, yVals, ey=yErr)
 		graph.Draw('ap')
 		return canvas, graph