import sys
from plotting.RootFileHandler import RootFileHandler
from plotting.PlotStyle import drawLabelCmsPrivateSimulation
from ROOT import TCanvas

fileHandler = RootFileHandler(sys.argv[1])

def plotDeltaPhiVsPt():
	canvas = TCanvas('cDeltaPhiVsPhi','DeltaPhiVsPhi',1200,1200)
	
	hist = fileHandler.getHistogram('hoMuonAnalyzer/correlation/shiftCheckDeltaPhiVsPt')
	
	hist.Draw()
	
	label = drawLabelCmsPrivateSimulation()
	
	canvas.Update()
	
	return canvas,hist,label
	