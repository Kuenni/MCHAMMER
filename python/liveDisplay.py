#!/usr/bin/python
import os,sys
sys.path.append(os.path.abspath("../../../python"))
from time import sleep
from ROOT import TCanvas,TH2D,TPaveText

from PlotStyle import setPlotStyle,getTH2D,getLabelCmsPrivateSimulation
setPlotStyle()
'''
Colums in the analysis results file:

deltaR	EThr	nTimeInside	nTimeTotal	nMatchedTruth	nTruthTotal	nEvents

deltaR, EThr	-> The analysed parameter set
nTimeInside 	-> The number of HO Rec Hits matched to L1 with a reconstructed Time in [-12.5,12.5] ns
nTimeTotal		-> The total number of HO Rec Hits matched to an L1 object
nMatchedTruth	-> The number of successfully matched L1 to both, GEN and HO Rec Hit
nTruthTotal		-> The number of successfully matched L1 to GEN
nEvents			-> The number of processed events in this file 

'''

def testResults():
	instances = []
	for filename in os.listdir('./log/'):
		if(filename.startswith('err')):
			if(os.path.getsize('./log/'+filename) > 0):
				cluster = filename.split('_')[-1]
				for logfile in os.listdir('./log/'):
					if(logfile.endswith(cluster + '_0.log')):
						instance = logfile.split('_')[1]
						instances.append(int(instance))
	instances.sort(cmp=None, key=None, reverse=False)
	for i in instances:
		for filename in os.listdir('./log/'):
			if filename.find('INSTANCE_' + str(i) + '.log') != -1 :
				foundErrorLine = False
				logfile = open('./log/' + filename)
				for line in logfile.readlines():
					if line.find('Error occured during script execution') != -1:
						foundErrorLine = True
				print 'File %s --> %s' % (filename,'OK' if foundErrorLine else 'NO ERROR')
	print instances

def plotTimeFraction():	
	canvas = TCanvas("canvas","canvas",1200,1200)
	hist = getTH2D("hist","Parameter Scan;#DeltaR;E_{Thr}",16,-0.0375,0.3625,16,-0.0375,0.3625)
	histCorrect = getTH2D("histCorrect","Parameter Scan in abs(12.5)ns;#DeltaR;E_{Thr}",16,-0.0375,0.3625,16,-0.0375,0.3625)
	histTotal = getTH2D("histTotal","Parameter Scan Total events;#DeltaR;E_{Thr}",16,-0.0375,0.3625,16,-0.0375,0.3625)
	
	l1Total = 0
	
	for filename in os.listdir('./results'):
		if filename[-4:] == '.txt':
			file = open('./results/' + filename,'r')
			for line in file.readlines():
				if line.find('deltaR') != -1:
					continue
				lineParts = line.split('\t')
				deltaR 	= float(lineParts[0])
				eThr 	= float(lineParts[1])
				nCorrect = float(lineParts[2])
				nTotal 	= float(lineParts[3])
				l1Total += nTotal
				if(nTotal > 0):
					histCorrect.SetBinContent(histCorrect.FindBin(deltaR,eThr),histCorrect.GetBinContent(histCorrect.FindBin(deltaR,eThr)) + nCorrect)
					histTotal.SetBinContent(histTotal.FindBin(deltaR,eThr),histTotal.GetBinContent(histCorrect.FindBin(deltaR,eThr)) + nTotal)
	
	hist.SetStats(0)
	minimum = 100
	for i in range(0,hist.GetNbinsX()):
		for j in range (0,hist.GetNbinsY()):
			if histTotal.GetBinContent(i,j) > 0:
				fraction = histCorrect.GetBinContent(i,j)/histTotal.GetBinContent(i,j)*100
				hist.SetBinContent(i,j,fraction)
				if fraction < minimum:
					minimum = fraction
					
	hist.SetMinimum(minimum)
	hist.SetContour(100)
	hist.SetTitle('Parameter Scan, Single #mu Gun,XYZ')
	hist.GetYaxis().SetTitleOffset(1.45)
	hist.GetZaxis().SetTitle('Fraction within |12.5| ns / %')
	hist.Draw('colz')
	
	canvas.Update()
	pal = hist.GetListOfFunctions().FindObject("palette")
	pal.SetX2NDC(0.92)
	
	label = getLabelCmsPrivateSimulation()
	label.Draw()
	
	hist.SaveAs('FractionTimeWindow.root')
	
	canvas.Update()
	return canvas,hist,label

# Plot the fraction of the L1 Objects, that were matched to
# a gen muon and successfully matched to an HO rec hit
def plotEfficiency():
	canvas = TCanvas("canvas2","canvas2",1200,1200)
	hist = getTH2D("histEff","HO matched to L1 Matched to GEN;#DeltaR;E_{Thr}",16,-0.0375,0.3625,16,-0.0375,0.3625)
	histCorrect = getTH2D("histMatchedTruth","Parameter Scan in abs(12.5)ns;#DeltaR;E_{Thr}",16,-0.0375,0.3625,16,-0.0375,0.3625)
	histTotal = getTH2D("histTotalTruth","Parameter Scan n  L1 Matched;#DeltaR;E_{Thr}",16,-0.0375,0.3625,16,-0.0375,0.3625)
	for filename in os.listdir('./results'):
		if filename[-4:] == '.txt':
			file = open('./results/' + filename,'r')
			for line in file.readlines():
				if line.find('deltaR') != -1:
					continue
				lineParts = line.split('\t')
				deltaR 	= float(lineParts[0])
				eThr 	= float(lineParts[1])
#				nCorrect = float(lineParts[2])
#				nTotal 	= float(lineParts[3])
				nMatched = float(lineParts[4])
				nTruth = float(lineParts[5])
				if(nTruth > 0):
					histCorrect.SetBinContent(histCorrect.FindBin(deltaR,eThr),histCorrect.GetBinContent(histCorrect.FindBin(deltaR,eThr)) + nMatched)
					histTotal.SetBinContent(histTotal.FindBin(deltaR,eThr),histTotal.GetBinContent(histTotal.FindBin(deltaR,eThr)) + nTruth)
	
	hist.SetStats(0)
	minimum = 100
	for i in range(0,hist.GetNbinsX()):
		for j in range (0,hist.GetNbinsY()):
			if histTotal.GetBinContent(i,j) > 0:
				fraction = histCorrect.GetBinContent(i,j)/histTotal.GetBinContent(i,j)*100
				hist.SetBinContent(i,j,fraction)
				if fraction < minimum:
					minimum = fraction
					
	hist.SetMinimum(minimum)
	hist.SetContour(100)
	hist.GetYaxis().SetTitleOffset(1.45)
	hist.GetZaxis().SetTitle('Efficiency / %')
	hist.Draw('colz')
	
	canvas.Update()
	pal = hist.GetListOfFunctions().FindObject("palette")
	pal.SetX2NDC(0.92)
	
	label = getLabelCmsPrivateSimulation()
	label.Draw()
	
	canvas.Update()
	hist.SaveAs('HoEff.root')
	histTotal.SaveAs('Histtotal.root')
	return canvas,hist,label
	
# Plot the fraction of the L1 Objects, that were matched to
# a gen muon
def plotL1Efficiency():
	canvas = TCanvas("canvas2L1Eff","L1Eff",1200,1200)
	hist = getTH2D("histL1Eff","HO matched to L1 Matched to GEN;#DeltaR;E_{Thr}",16,-0.0375,0.3625,16,-0.0375,0.3625)
	histTotal = getTH2D("histTotalTruth","Parameter Scan n  L1 Matched;#DeltaR;E_{Thr}",16,-0.0375,0.3625,16,-0.0375,0.3625)
	histEvents  = getTH2D("histEvents","Parameter Scan Total events;#DeltaR;E_{Thr}",16,-0.0375,0.3625,16,-0.0375,0.3625)
	for filename in os.listdir('./results'):
		if filename[-4:] == '.txt':
			file = open('./results/' + filename,'r')
			for line in file.readlines():
				if line.find('deltaR') != -1:
					continue
				lineParts = line.split('\t')
				deltaR 	= float(lineParts[0])
				eThr 	= float(lineParts[1])
#				nCorrect = float(lineParts[2])
#				nTotal 	= float(lineParts[3])
				nMatched = float(lineParts[4])
				nTruth = float(lineParts[5])
				nEvents = float(lineParts[6])
				if(nTruth > 0):
					histTotal.SetBinContent(histTotal.FindBin(deltaR,eThr),histTotal.GetBinContent(histTotal.FindBin(deltaR,eThr)) + nTruth)
					histEvents.SetBinContent(histEvents.FindBin(deltaR,eThr),histEvents.GetBinContent(histEvents.FindBin(deltaR,eThr)) + nEvents)
	
	hist.SetStats(0)
	minimum = 100
	for i in range(0,hist.GetNbinsX()):
		for j in range (0,hist.GetNbinsY()):
			if histEvents.GetBinContent(i,j) > 0:
				fraction = histTotal.GetBinContent(i,j)/histEvents.GetBinContent(i,j)*100
				hist.SetBinContent(i,j,fraction)
				if fraction < minimum:
					minimum = fraction
					
	hist.SetMinimum(minimum)
	hist.SetContour(100)
	hist.GetYaxis().SetTitleOffset(1.45)
	hist.GetZaxis().SetTitle('L1 Efficiency / %')
	hist.Draw('colz')
	
	canvas.Update()
	pal = hist.GetListOfFunctions().FindObject("palette")
	pal.SetX2NDC(0.92)
	
	label = getLabelCmsPrivateSimulation()
	label.Draw()
	
	canvas.Update()
	hist.SaveAs('L1Eff.root')
	histEvents.SaveAs('nEvents.root')
	return canvas,hist,label
	
#Plot the product of efficiency and fraction in right time window
def plotProduct():
	canvas = TCanvas("canvas2p","canvas2p",1200,1200)
	hist = getTH2D("histEffp","L1 Matched to GEN and HO;#DeltaR;E_{Thr}",16,-0.0375,0.3625,16,-0.0375,0.3625)
	histCorrect = getTH2D("histMatchedTruthp","Parameter Scan in abs(12.5)ns;#DeltaR;E_{Thr}",16,-0.0375,0.3625,16,-0.0375,0.3625)
	histTotal = getTH2D("histTotalTruthp","Parameter Scan Total events;#DeltaR;E_{Thr}",16,-0.0375,0.3625,16,-0.0375,0.3625)
	histCorrectTime = getTH2D("histCorrectp","Parameter Scan in abs(12.5)ns;#DeltaR;E_{Thr}",16,-0.0375,0.3625,16,-0.0375,0.3625)
	histTotalTime = getTH2D("histTotalp","Parameter Scan Total events;#DeltaR;E_{Thr}",16,-0.0375,0.3625,16,-0.0375,0.3625)
	for filename in os.listdir('./results'):
		if filename[-4:] == '.txt':
			file = open('./results/' + filename,'r')
			for line in file.readlines():
				if line.find('deltaR') != -1:
					continue
				lineParts = line.split('\t')
				deltaR 	= float(lineParts[0])
				eThr 	= float(lineParts[1])
				nCorrect = float(lineParts[2])
				nTotal 	= float(lineParts[3])
				nMatched = float(lineParts[4])
				nTruth = float(lineParts[5])
				if(nTruth > 0 and nTotal > 0):
					histCorrect.SetBinContent(histCorrect.FindBin(deltaR,eThr),histCorrect.GetBinContent(histCorrect.FindBin(deltaR,eThr)) + nMatched)
					histTotal.SetBinContent(histTotal.FindBin(deltaR,eThr),histTotal.GetBinContent(histCorrect.FindBin(deltaR,eThr)) + nTruth)
					histCorrectTime.SetBinContent(histCorrectTime.FindBin(deltaR,eThr),histCorrectTime.GetBinContent(histCorrectTime.FindBin(deltaR,eThr)) + nCorrect)
					histTotalTime.SetBinContent(histTotalTime.FindBin(deltaR,eThr),histTotalTime.GetBinContent(histTotalTime.FindBin(deltaR,eThr)) + nTotal)
					
	hist.SetStats(0)
	minimum = 100
	for i in range(0,hist.GetNbinsX()):
		for j in range (0,hist.GetNbinsY()):
			if histTotal.GetBinContent(i,j) > 0:
				fraction = histCorrect.GetBinContent(i,j)/histTotal.GetBinContent(i,j)*histCorrectTime.GetBinContent(i,j)/histTotalTime.GetBinContent(i,j)*100
				hist.SetBinContent(i,j,fraction)
				if fraction < minimum:
					minimum = fraction
					
	hist.SetMinimum(minimum)
	hist.SetContour(100)
	hist.GetYaxis().SetTitleOffset(1.45)
	hist.GetZaxis().SetTitle('Efficiency #times Time fraction / %')
	hist.Draw('colz')
	
	canvas.Update()
	pal = hist.GetListOfFunctions().FindObject("palette")
	pal.SetX2NDC(0.92)
	
	label = getLabelCmsPrivateSimulation()
	label.Draw()
	
	hist.SaveAs('product.root')
	
	canvas.Update()	
	return canvas,hist,label

res = plotTimeFraction()
testResults()

res2 = plotEfficiency()
res3 = plotProduct()
res4 = plotL1Efficiency()

raw_input('-->')
