#!/usr/bin/python
import os,sys
from math import sqrt
from ROOT import TCanvas,ROOT,TFile,TLegend,TF1,TLine,gROOT,TPaveText,TH1D,Double,TH2D,THStack,gStyle
from plotting.PlotStyle import setPlotStyle,calcSigma,getLabelCmsPrivateSimulation,colorRwthDarkBlue
from plotting.PlotStyle import colorRwthMagenta,setupAxes,convertToHcalCoords,chimney1,chimney2,printProgress
from plotting.RootFileHandler import RootFileHandler
from matchingLibrary import findBestL1Match

setPlotStyle()

prefix = '[makeEvsEtaPhiPlot] '
def output(outString):
	print prefix,outString

if len(sys.argv) < 2:
	print 'First argument has to be the file name scheme!'
fileHandler = RootFileHandler(sys.argv[1])
fileHandler.printStatus()

if( not os.path.exists('plots')):
	os.mkdir('plots')
if( not os.path.exists('plots/controlPlots')):
	os.mkdir('plots/controlPlots')

'''
Control Plot that shows the number of matches in Det Ids for a given RecHit Det id
'''
def plotHoDigiMatchesPerDetId():
	canvas = TCanvas('canvasDigiMatchesMultiplicity')
	digiMatches = fileHandler.getHistogram('hoMuonAnalyzer/hoDigiMatchesPerDetId_Multiplicity')
	setupAxes(digiMatches)
	digiMatches.SetTitle('Number of matches between RecHit and Digi for a given DetId')
	digiMatches.GetXaxis().SetRangeUser(0,5)
	digiMatches.GetXaxis().SetTitle('Number of matches per DetId')
	digiMatches.GetYaxis().SetTitle('#')
	canvas.cd().SetLogy()
	digiMatches.SetLineWidth(3)
	digiMatches.SetLineColor(colorRwthDarkBlue)
	digiMatches.Draw()
	
	label = getLabelCmsPrivateSimulation()
	label.Draw()
	
	canvas.Update()
	
	stats = digiMatches.GetListOfFunctions().FindObject("stats")
	stats.SetX1NDC(.7)
	stats.SetX2NDC(.9)
	stats.SetY1NDC(.75)
	stats.SetY2NDC(.9)
	
	canvas.Update()
	
	canvas.SaveAs('plots/controlPlots/digiMatchesPerDetId.pdf')
	canvas.SaveAs('plots/controlPlots/digiMatchesPerDetId.png')
	
	return canvas,digiMatches,label

output('Plotting digi matches per det id')
res = plotHoDigiMatchesPerDetId()
	
raw_input('-->')
