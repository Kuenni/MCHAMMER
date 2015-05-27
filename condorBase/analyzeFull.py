#!/usr/bin/python

import sys,os
sys.path.append(os.path.abspath("../../python"))

from optparse import OptionParser

parser = OptionParser()
parser.add_option("--instance", dest="instance", help="The index of this process. Handles opening of files and naming stuff.",type="str",default = "")

(options, args) = parser.parse_args()

filename = 'L1MuonHistogram_' + options.instance + '.root'

info = '# The Analysis will be performed using file L1MuonHistogram_%s.root #' % (options.instance)
print len(info)*'#'
print info
print len(info)*'#'

import numpy as np

from ROOT import TFile,gROOT,std,TCanvas
gROOT.SetBatch()
gROOT.ProcessLine("gErrorIgnoreLevel = 3000;")
gROOT.ProcessLine(".L ./loader.C+");

from matchingLibrary import calculateDeltaR, findBestHoMatchByEnergy, findBestHoMatchByDeltaR, findBestHoMatch,findBestL1Match

from PlotStyle import setPlotStyle,getTH1D
setPlotStyle()

if( not os.path.exists('results')):
	os.mkdir('results')
if( not os.path.exists('results/plots')):
	os.mkdir('results/plots')

file = TFile(filename,'READ')
if(file.IsZombie()):
	print 'Error opening file: %s' % filename
	sys.exit(1)
	
tree = file.Get('dataTree')

#Prepare the loop over parameters
DELTA_R_START=0
DELTA_R_END=0.35
DELTA_R_STEPSIZE=0.025

E_THR_START = 0
E_THR_END = 0.35
E_THR_STEPSIZE = DELTA_R_STEPSIZE

matchTypes 	= ["byDeltaR","byECone"]
deltaRList 	= np.arange(DELTA_R_START,DELTA_R_END,DELTA_R_STEPSIZE)
eThrList 	= np.arange(E_THR_START,E_THR_END,E_THR_STEPSIZE)

#Prepare file for results
resultFilename = 'results/analyzeFullResults_%s.txt' % (options.instance)
resultHeader = "deltaR\tEThr\tnTimeInside\tnTimeTotal\tnMatchedTruth\tnTruthTotal\tnEvents\n"
resultFile = open(resultFilename,'w')
resultFile.write(resultHeader)

#analyze timing for matching done by the best delta R 
def analyze(deltaR = -1, eThr = -1):

	deltaTimes = []
	eventCounter = 0
	print 'Delta time analysis:'
	for event in file.dataTree:
		#Tell us about the progress
		eventCounter += 1
		if(eventCounter%1000 == 0):
			sys.stdout.write( '\rprocessing event %7d ==> %6.2f%% done.' % (eventCounter,eventCounter/float(tree.GetEntriesFast())*100))
			sys.stdout.flush()
		l1DataVector = event.l1MuonData
		for l1Object in l1DataVector:
			hoMatch = findBestHoMatch(l1Object,event.hoRecHitData,deltaR,eThr)
			if(hoMatch != None):
				deltaTimes.append(l1Object.bx*25. - hoMatch.time)
	print
	
# 	histDeltaTime = getTH1D("histDeltaTimes","#DeltaTime;#DeltaTime / ns;#", 200,-100,100)
	
# 	for deltaTime in deltaTimes:
# 			histDeltaTime.Fill(deltaTime)
# 	canvas = TCanvas('canvasDeltaTimesEThr','Delta Time vs. E_{Thr}',1200,1200)
# 	histDeltaTime.SetStats(0)
# 	histDeltaTime.Draw()
# 	
# 	canvas.Update()
	
	print 'Done.'
	
# 	filenameTrunk = 'results/plots/analyzeFull-DeltaR%01d_%03d-EThr%01d_%03d_%s' % (int(deltaR),int(deltaR*1000),
# 												int(eThr),int(eThr*1000),options.instance)
	
# 	canvas.SaveAs(filenameTrunk + '.png')
# 	canvas.SaveAs(filenameTrunk + '.pdf')
# 	canvas.SaveAs(filenameTrunk + '.root')
	
	return deltaTimes

#Determine the number of successfully matched L1 and HO for the L1 associated to GEN
def calculateEfficiency(deltaR = -1, eThr = -1):
	nMatches = 0
	nTotal = 0
	eventCounter = 0
	print 'Efficiency analysis:'
	for event in file.dataTree:
		#Tell us about the progress
		eventCounter += 1
		if(eventCounter%1000 == 0):
			sys.stdout.write( '\rprocessing event %7d ==> %6.2f%% done.' % (eventCounter,eventCounter/float(tree.GetEntriesFast())*100))
			sys.stdout.flush()
		l1DataVector = event.l1MuonData
		genDataVector = event.genMuonData
		for genObject in genDataVector:
			l1Match = findBestL1Match(genObject, l1DataVector,0.3)
			if l1Match != None:
				nTotal += 1
				hoMatch = findBestHoMatch(l1Match,event.hoRecHitData,deltaR,eThr)
				if(hoMatch != None):
					nMatches += 1
	print
	print 'Done.'
	return nMatches, nTotal,eventCounter

#Run the full parameter loop
progressCounter = 0
totalActionsCounter = len(deltaRList)*len(eThrList)
for deltaR in deltaRList:
	for eThr in eThrList:
		progressCounter += 1
		header = '| Delta R = %4.3f. E Thr = %4.3fGeV |' % (deltaR,eThr)
		print len(header)*'-'
		print header
		print len(header)*'-'
		deltaTimes = analyze(deltaR, eThr)
		nMatchedTruth, nTotal,nEvents = calculateEfficiency(deltaR, eThr)
		nInsideTimeWindow = 0
		
		for deltaTime in deltaTimes:
			if abs(deltaTime) < 12.5:
				nInsideTimeWindow += 1
				
		resultString = "%f\t%f\t%d\t%d\t%d\t%d\t%d\n" % (deltaR,eThr,nInsideTimeWindow,len(deltaTimes),nMatchedTruth,nTotal,nEvents)
		resultFile.write(resultString)
		
		print 'Overall progress: %5.2f%%' % (progressCounter/float(totalActionsCounter)*100)

resultFile.close()

#raw_input('-->')
