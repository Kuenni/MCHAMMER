#!/usr/bin/python

import sys,os
sys.path.append(os.path.abspath("../../python"))

from optparse import OptionParser

parser = OptionParser()
parser.add_option("--eThr", dest="eThr", help="Set fix E thr value",type="float",default = -1)
parser.add_option("--deltaR", dest="deltaR",help="Set fix delta R value",type="float",default = -1)
parser.add_option("--byDeltaR", dest="byDeltaR",help="Select this to do the matching by best delta R value",action="store_true",default=False)
parser.add_option("--byECone", dest="byECone",help="Select this to do the matching by the highest energy in cone",action="store_true",default=False)

(options, args) = parser.parse_args()

if not options.byDeltaR ^ options.byECone:
    parser.error("Exactly one of the options --byDeltaR and --byECone has to be set")

info = '# The Analysis will be performed using matching by %s #' % ('best delta R' if options.byDeltaR else 'highest E in cone.')
print len(info)*'#'
print info
print len(info)*'#'

import numpy as np

from ROOT import TFile,gROOT,std,TCanvas
gROOT.SetBatch()
gROOT.ProcessLine("gErrorIgnoreLevel = 3000;")
gROOT.ProcessLine(".L ./loader.C+");

from matchingLibrary import calculateDeltaR, findBestHoMatchByEnergy, findBestHoMatchByDeltaR

from PlotStyle import setPlotStyle,getTH1D
setPlotStyle()

if( not os.path.exists('results')):
	os.mkdir('results')
if( not os.path.exists('results/plots')):
	os.mkdir('results/plots')

file = TFile.Open('L1MuonHistogram.root')
if(file == None):
	print 'Error opening file: L1MuonHistogram.root'
	sys.exit(1)
	
tree = file.Get('hoMuonAnalyzer/dataTree')

DELTA_R_START = 0
DELTA_R_END = 0.35
E_THR_START = 0
E_THR_END = 0.3

STEPSIZE_DELTA_R = 0.025
STEPSIZE_E_THR = STEPSIZE_DELTA_R

def analyzeByECone(deltaR = -1, eThr = -1):
	deltaTimes = []
	eventCounter = 0
	
	header = '| E Thr = %3.2f GeV. Delta R = %4.3f |' % (eThr,deltaR)
	
	print len(header)*'-'
	print header
	print len(header)*'-'
	
	for event in tree:
		#Tell us about the progress
		eventCounter += 1
		if(eventCounter%1000 == 0):
			sys.stdout.write( '\rprocessing event %7d ==> %6.2f%% done.' % (eventCounter,eventCounter/float(tree.GetEntriesFast())*100))
			sys.stdout.flush()
		l1DataVector = event.l1MuonData
		for l1Object in l1DataVector:
			hoMatch = findBestHoMatchByEnergy(l1Object,event.hoRecHitData,deltaR)
			if(hoMatch != None):
				deltaTimes.append(l1Object.bx*25. - hoMatch.time)
	print
	
	histDeltaTime = getTH1D("histDeltaTime","#DeltaTime;#DeltaR;#DeltaTime / ns", 200,-100,100)
	
	for deltaTime in deltaTimes:
		histDeltaTime.Fill(deltaTime)
	canvas = TCanvas('canvasDeltaTimes','Delta Time',1200,1200)
	histDeltaTime.SetStats(0)
	histDeltaTime.Draw()
	
	canvas.Update()

	print
	print 'Done.'
	
	filenameTrunk = 'results/plots/deltaTimeVsDeltaR_%s-DeltaR%01d_%03d-EThr%01d_%03d' % ('byDeltaR' if options.byDeltaR else 'byECone',
												int(options.deltaR),int(options.deltaR*1000),
												int(options.eThr),int(options.eThr*1000))
	
	canvas.SaveAs(filenameTrunk + '.png')
	canvas.SaveAs(filenameTrunk + '.pdf')
	canvas.SaveAs(filenameTrunk + '.root')
	
	return deltaTimes,deltaR,eThr
	

def analyzeByDeltaR(deltaR = -1, eThr = -1):

	deltaTimes = []
	eventCounter = 0
	
	header = '| Delta R = %4.3f. E Thr = %4.3fGeV |' % (deltaR,eThr)
	
	print len(header)*'-'
	print header
	print len(header)*'-'
	
	for event in tree:
		#Tell us about the progress
		eventCounter += 1
		if(eventCounter%1000 == 0):
			sys.stdout.write( '\rprocessing event %7d ==> %6.2f%% done.' % (eventCounter,eventCounter/float(tree.GetEntriesFast())*100))
			sys.stdout.flush()
		l1DataVector = event.l1MuonData
		for l1Object in l1DataVector:
			hoMatch = findBestHoMatchByDeltaR(l1Object,event.hoRecHitData,eThr)
			if(hoMatch != None):
				deltaTimes.append(l1Object.bx*25. - hoMatch.time)
	print
	
	histDeltaTime = getTH1D("histDeltaTimes","#DeltaTime;E_{Thr} / GeV;#DeltaTime / ns", 200,-100,100)
	
	for deltaTime in deltaTimes:
			histDeltaTime.Fill(deltaTime)
	canvas = TCanvas('canvasDeltaTimesEThr','Delta Time vs. E_{Thr}',1200,1200)
	histDeltaTime.SetStats(0)
	histDeltaTime.Draw()
	
	canvas.Update()
	
	print 'Done.'
	
	filenameTrunk = 'results/plots/deltaTimeVsEThr_%s-DeltaR%01d_%03d-EThr%01d_%03d' % ('byDeltaR' if options.byDeltaR else 'byECone',
												int(options.deltaR),int(options.deltaR*1000),
												int(options.eThr),int(options.eThr*1000))
	
	canvas.SaveAs(filenameTrunk + '.png')
	canvas.SaveAs(filenameTrunk + '.pdf')
	canvas.SaveAs(filenameTrunk + '.root')
	
	return deltaTimes,deltaR,eThr
	
deltaTimesArray = thresholdsArray = fixParameter = None

if(options.byECone):
	deltaTimes,deltaR,eThr = analyzeByECone(options.deltaR,options.eThr)
else:
	deltaTimes,deltaR,eThr = analyzeByDeltaR(options.deltaR,options.eThr)

nInsideTimeWindow = 0

for deltaTime in deltaTimes:
	if abs(deltaTime) < 12.5:
		nInsideTimeWindow += 1

resultHeader = "Matching\tdeltaR\tEThr\tnInside\tnTotal\n"
resultString = "%s\t%f\t%f\t%d\t%d\n" % ("byDeltaR" if options.byDeltaR else "byECone",
										options.deltaR,options.eThr,nInsideTimeWindow,len(deltaTimes))

filename = 'results/%s-DeltaR%01d_%03d-EThr%01d_%03d.txt' % ('byDeltaR' if options.byDeltaR else 'byECone',
												int(options.deltaR),int(options.deltaR*1000),
												int(options.eThr),int(options.eThr*1000))

f = open(filename,'w')
f.write(resultHeader)
f.write(resultString)
f.close()

#raw_input('-->')
