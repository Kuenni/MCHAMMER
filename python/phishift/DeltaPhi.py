import sys
from plotting.RootFileHandler import RootFileHandler
from plotting.PlotStyle import drawLabelCmsPrivateSimulation, setupAxes
from ROOT import TCanvas,TLine
from cmath import pi

fileHandler = RootFileHandler(sys.argv[1])

def plotDeltaPhiVsL1Pt():
	canvas = TCanvas('cDeltaPhiVsL1Pt','DeltaPhiVsL1Pt',1200,1200)
	hist = fileHandler.getHistogram('hoMuonAnalyzer/correlation/shiftCheckDeltaPhiVsL1Pt')
	hist.Scale(1,'width')
	hist.Draw('colz')
	label = drawLabelCmsPrivateSimulation()
	canvas.Update()
	
	return canvas,hist,label

def plotDeltaPhiVsGenPt():
	canvas = TCanvas('cDeltaPhiVsGenPt','DeltaPhiVsGenPt',1200,1200)
	hist = fileHandler.getHistogram('hoMuonAnalyzer/correlation/shiftCheckDeltaPhiVsGenPt')
	hist.Draw('colz')
	label = drawLabelCmsPrivateSimulation()
	canvas.Update()
	
	return canvas,hist,label

def plotDeltaPhiVsL1Phi():
	canvas = TCanvas('cDeltaPhiVsL1Phi','DeltaPhiVsL1Phi',1200,1200)
	hist = fileHandler.getHistogram('hoMuonAnalyzer/correlation/shiftCheckDeltaPhiVsPhi')
	hist.GetYaxis().SetRangeUser(-.6,.6)
	hist.Draw('colz')
	phiBorderLines = []
	
	for i in range(72):
		line = TLine(-pi+0.087*i,-.6,-pi+0.087*i,.6)
		line.Draw()
		phiBorderLines.append(line)
		
	label = drawLabelCmsPrivateSimulation()
	canvas.Update()
	
	return canvas,hist,label,phiBorderLines
	
def plotL1PhiVsHoPhi():
	canvas = TCanvas('cL1PhiVsHoPhi','L1PhiVsHoPhi',1200,1200)
	fileHandlerLocal = RootFileHandler('L1MuonHistogramPooja')
	graph = fileHandlerLocal.getGraph('hoMuonAnalyzer/correlation/l1PhiVsHoPhi')
	graph.SetTitle('L1 #phi vs. HO #phi;HO #phi;L1 #phi')
	graph.SetMarkerStyle(2)
	setupAxes(graph)
	graph.Draw('AP')
	canvas.Update()
	
	return canvas,graph

def plotL1PhiVsHoIPhi():
	canvas = TCanvas('cL1PhiVsHoIPhi','L1PhiVsHoIPhi',1200,1200)
	fileHandlerLocal = RootFileHandler('L1MuonHistogramPooja')
	graph = fileHandlerLocal.getGraph('hoMuonAnalyzer/correlation/l1PhiVsHoIPhi')
	graph.SetTitle('L1 #phi vs. HO i#phi;HO i#phi;L1 #phi')
	graph.SetMarkerStyle(2)
	setupAxes(graph)
	graph.Draw('AP')
	canvas.Update()
	
	return canvas,graph
	
def plotHoPhiVsHoIPhi():
	canvas = TCanvas('cHoPhiVsHoIPhi','HoPhiVsHoIPhi',1200,1200)
	fileHandlerLocal = RootFileHandler('L1MuonHistogramPooja')
	graph = fileHandlerLocal.getGraph('hoMuonAnalyzer/correlation/hoPhiVsHoIPhi')
	graph.SetTitle('HO #phi vs. HO i#phi;HO i#phi;HO #phi')
	graph.SetMarkerStyle(2)
	setupAxes(graph)
	graph.Draw('AP')
	
	canvas.Update()
	
	return canvas,graph
