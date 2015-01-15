'''
	Analyzer script for root trees containing data from L1 muon objects, Gen muon objects
	and Ho rec hit objects stored in vectors for each event
	
	Created on 12. Jan 2015
	Andreas Kuensken <kuensken@physik.rwth-aachen.de>
'''
import sys,os
import matplotlib.pyplot as plt
import numpy as np
import math

from ROOT import TTree,TFile,gROOT,vector,gSystem,std
gROOT.ProcessLine('.L ./loader.C+')
from ROOT import L1MuonData,GenMuonData,HoRecHitData

# Define a switch to enable debug mode. In this mode only a fraction of the 
# total event data is processed to enable a fast check on any implemented
# changes
DEBUG = True
EVENTLIMIT = 1000

EMIN = 0.2 #GeV

#Define global variables for the root file and the tree
f = TFile.Open("../L1MuonHistogram.root")
t = f.Get("hoMuonAnalyzer/dataTree")

###########################################################################
##		Functions for analysis
###########################################################################

'''
	Compute the delta phi between two phi values in CMS
'''
def computeDeltaPhi(phi1, phi2):
	delta_phi = phi1 - phi2;	
	if(delta_phi < -math.pi):
	  return (2*math.pi + delta_phi);	
	if(delta_phi > math.pi):
	  return (delta_phi - 2*math.pi);
	
	return delta_phi;

'''
	Evaluate whether a given set of coordinates is inside a delta R cone
	with the delta R max parameter
'''
def isInsideDeltaR(eta1,eta2,phi1,phi2,deltaRMax):
	deltaEta = eta1 - eta2;
	deltaPhi = computeDeltaPhi(phi1,phi2); # Finds difference in phi
	if(pow(deltaEta,2)+pow(deltaPhi,2) <= pow(deltaRMax,2)):
		return True;
	return False;


'''
	Find in a list the element with the largest energy inside a given delta
	R cone. The elements in the list must have a member energy
'''
def matchByEMaxDeltaR(eta,phi,maxDeltaR,matchList):
	bestMatch = None
	
	for element in matchList:
		if(isInsideDeltaR(eta, element.eta, phi, element.phi, maxDeltaR)):
			if(bestMatch == None):
				bestMatch = element
			else:
				if(bestMatch.energy < element.energy):
					bestMatch = element
	return bestMatch

'''
	Return a list of elements in the given list, that have a larger energy than
	eMin. The elements in the parameter "list" must have the member "energy"
'''
def filterListByEnergy(list, eMin):
	filteredList = []
	for event in list:
		filteredEvent = []
		for data in event:
			if(data.energy >= eMin):
				filteredEvent.append(data)
		filteredList.append(filteredEvent)
	return filteredList

'''
	Return a list of pairs with two objects matched to each other by the given criteria
'''
def getListOfMatchedPairs(listObjects, listToMatch, maxDeltaR = 0.3):
	pairList = []
	for i,event in enumerate(listObjects):
		eventPairs = []
		for object in event:
			matched = matchByEMaxDeltaR(object.eta, object.phi, maxDeltaR, listToMatch[i])
			if(matched != None):
				eventPairs.append([object,matched])
		pairList.append(eventPairs)
	return pairList
		
###########################################################################
##		Functions for creating plots with pyplot
###########################################################################

def createSimpleHistogram( ax, data , binwidth , axisRange = [0,0] , parameterDict = {'facecolor':'green'}):
	bins=np.arange(min(data), max(data) + binwidth, binwidth)
	if(axisRange != [0,0]):
		bins = np.arange(axisRange[0],axisRange[1],binwidth)
	out = ax.hist(data,bins,**parameterDict)
	return out

###########################################################################
##		Functions for getting the raw event data from the tree
###########################################################################

#Get the vectors with the L1 Muons from the Tree
def getL1Muons():
	counter = 0
	print "Getting L1 muons from the tree..."
	fullList = []
	for event in t:
		eventData = []
		for data in event.l1MuonData:
			eventData.append(L1MuonData(data))
		fullList.append(eventData)
		if(DEBUG):
			counter += 1
			if(counter == EVENTLIMIT):
				break
	print "Done."
	return fullList

#Get the vectors with the gen Muons from the Tree
def getGenMuons():
	counter = 0
	print "Getting Gen muons from the tree..."
	fullList = []
	for event in t:
		eventData = []
		for data in event.genMuonData:
			eventData.append(GenMuonData(data))
		fullList.append(eventData)
		if(DEBUG):
			counter += 1
			if(counter == EVENTLIMIT):
				break
	print "Done."
	return fullList

#Get the vectors with the Ho rec hits from the Tree
def getHoRecHits():
	counter = 0
	print "Getting Ho Rec hits from the tree..."
	fullList = []
	N = t.GetEntries()
#	vec = ROOT.vector<HoRecHitData>()
	for i in range(N):
		t.GetEntry(i)
		eventData = []
		for data in t.hoRecHitData:
			eventData.append(HoRecHitData(data))
		fullList.append(eventData)
		if(DEBUG):
			counter += 1
			if(counter == EVENTLIMIT):
				break
	print "Done."
	return fullList

#FIXME: remove getting figure in function
def plotL1Pt():
	for event in t:
		for l1Data in event.l1MuonData:
			ptL1Muons.append(l1Data.pt)
	fig = plt.figure()
	bins = sorted(set(ptL1Muons))
	plt.hist(ptL1Muons,bins)

def plotHoTime():
	xVal = []
	for event in t:
		for hoData in event.hoRecHitData:
			xVal.append(hoData.time)

###########################################################################
###########################################################################
###########################################################################

l1Muons = getL1Muons()
genMuons = getGenMuons()
hoRecHits = getHoRecHits()

l1Phi = []
eventCounter = 0
innerLoopCounter =0
for l1Data in l1Muons:
	eventCounter += 1
	for e in l1Data:
		l1Phi.append(e.phi)
		innerLoopCounter += 1

print 'Creating L1 Phi histogram'
fig = plt.figure()
plt.ion()
ax = plt.subplot(1,1,1)
res = createSimpleHistogram(ax, l1Phi, binwidth=0.5)

print 'creating L1 p_T distribution'
ptL1Muons = []
for vect in l1Muons:
	for e in vect:
		ptL1Muons.append(e.pt)
fig = plt.figure()

##Enable interactive mode
#plt.ion()


ax = plt.subplot(1,1,1)
res = createSimpleHistogram(ax, ptL1Muons, binwidth=0.5)

############
# Plot Ho energy
############
print 'Creating plots with HO energy'
fig = plt.figure()
hoEnergy = []
hoEnergyAboveThr = []

for event in hoRecHits:
	for data in event:
		hoEnergy.append(data.energy)
hoRecHitsAboveThr = filterListByEnergy(hoRecHits, EMIN)
for event in hoRecHitsAboveThr:
	for data in event:
		hoEnergyAboveThr.append(data.energy)
		
ax1 = plt.subplot(2,1,1)
ax1.set_yscale('log')
createSimpleHistogram(ax1, hoEnergy, binwidth=0.05, parameterDict={'facecolor':'blue'})
plt.xlabel('Reconstructed energy / GeV')
plt.ylabel('# entries')
ax2 = plt.subplot(2,1,2)
ax2.set_yscale('log')
createSimpleHistogram(ax2, hoEnergyAboveThr, binwidth = 0.05,axisRange=[min(hoEnergy),max(hoEnergy)], parameterDict={'facecolor':'red'})
plt.xlabel('Reconstructed energy / GeV')
plt.ylabel('# entries')

print 'Done'

############
# Plot delta timing
############

print 'Creating timing plots'

#delta time for l1 and ho above thr
matchedL1AndHoAboveThr = getListOfMatchedPairs(l1Muons, hoRecHitsAboveThr)
deltaTimes = []
deltaTimesBx0 = []
for event in matchedL1AndHoAboveThr:
	for pair in event:
		deltaTimes.append(pair[0].bx*25 - pair[1].time)
		if(pair[0].bx == 0):
			deltaTimesBx0.append(pair[0].bx*25 - pair[1].time)
fig = plt.figure()
fig.canvas.set_window_title("L1 to HO above Thr.")
ax = plt.subplot(1,1,1)
createSimpleHistogram(ax, deltaTimes, binwidth=1, parameterDict={'facecolor':'red','label':r'$\Delta$Time L1 matched to HO'})
createSimpleHistogram(ax, deltaTimesBx0, binwidth=1, axisRange=[min(deltaTimes),max(deltaTimes)],
					parameterDict={'color':'blue','alpha':0.4,'histtype':'step','lw':3,'label':r'$\Delta$Time L1$_{BX=0}$ matched to HO'})
plt.title('L1 Muons matched to HO > 0.2 GeV')
plt.ylabel('# entries')
plt.xlabel(r'$\Delta$time / ns')
plt.legend(loc=2)

#delta time for l1 and all ho
matchedL1AndHo = getListOfMatchedPairs(l1Muons, hoRecHits)
deltaTimes = []
deltaTimesBx0 = []
for event in matchedL1AndHo:
	for pair in event:
		deltaTimes.append(pair[0].bx*25 - pair[1].time)
		if(pair[0].bx == 0):
			deltaTimesBx0.append(pair[0].bx*25 - pair[1].time)
fig = plt.figure()
fig.canvas.set_window_title("L1 to any HO")
ax = plt.subplot(1,1,1)
createSimpleHistogram(ax, deltaTimes, binwidth=1, parameterDict={'facecolor':'red','label':r'$\Delta$Time L1 matched to HO'})
createSimpleHistogram(ax, deltaTimesBx0, binwidth=1, axisRange=[min(deltaTimes),max(deltaTimes)],
					parameterDict={'color':'blue','alpha':0.4,'histtype':'step','lw':3,'label':r'$\Delta$Time L1$_{BX=0}$ matched to HO'})
plt.title('L1 Muons matched to any HO')
plt.ylabel('# entries')
plt.xlabel(r'$\Delta$time / ns')
plt.legend(loc=2)

#delta time for l1 to any ho and to ho > 0.2

deltaTimesAny = []
deltaTimesAboveThr = []
for event in matchedL1AndHo:
	for pair in event:
		deltaTimesAny.append(pair[0].bx*25 - pair[1].time)

for event in matchedL1AndHoAboveThr:
	for pair in event:
		deltaTimesAboveThr.append(pair[0].bx*25 - pair[1].time)
		
fig = plt.figure()
fig.canvas.set_window_title("Delta Time")
ax = plt.subplot(1,1,1)
createSimpleHistogram(ax, deltaTimesAny, binwidth=1, parameterDict={'facecolor':'red','label':r'$\Delta$Time L1 matched to any HO'})
createSimpleHistogram(ax, deltaTimesAboveThr, binwidth=1, axisRange=[min(deltaTimesAny),max(deltaTimesAny)],
					parameterDict={'color':'blue','alpha':0.4,'histtype':'step','lw':3,'label':r'$\Delta$Time L1 matched to HO > 0.2 GeV'})
plt.title('Delta Time')
plt.ylabel('# entries')
plt.xlabel(r'$\Delta$time / ns')
plt.legend(loc=2)

# Plot of bx for all L1 and L1 matched to HO Above Thr
plt.figure()
ax = plt.subplot(1,1,1)

l1Bx = []
l1MatchedBx = []

for event in l1Muons:
	for data in event:
		l1Bx.append(data.bx)

for event in matchedL1AndHoAboveThr:
	for pair in event:
		l1MatchedBx.append(pair[0].bx)

ax.set_yscale('log')		
createSimpleHistogram(ax, l1Bx, binwidth = 1,axisRange=[-5,5],parameterDict={'color':'blue','label':'All L1 Muons'})
createSimpleHistogram(ax, l1MatchedBx, binwidth = 1,axisRange=[-5,5],
					parameterDict={'histtype':'step','color':'red','lw':2,'alpha':0.2,'label':'L1Muon matched to HO'})

plt.ylabel('# entries')
plt.xlabel('BX ID')
plt.legend(loc=2)

# Plot of all ho time 
plt.figure()
ax2 = plt.subplot(1,1,1)
hoTime = []
for event in hoRecHits:
	for data in event:
		hoTime.append(data.time)

hoTimeAboveThr = []
for event in hoRecHitsAboveThr:
	for data in event:
		hoTimeAboveThr.append(data.time)

createSimpleHistogram(ax2, hoTime, binwidth = 0.1,parameterDict={'label':'All HO Rec Hits','color':'blue'})
plt.ylabel('# entries')
plt.xlabel('time / ns')
plt.legend()

# time of ho hits above thr
plt.figure()
ax2 = plt.subplot(1,1,1)
createSimpleHistogram(ax2, hoTimeAboveThr, binwidth = 1, axisRange=[min(hoTime),max(hoTime)],
					parameterDict={'color':'red','alpha':0.4,'histtype':'step','lw':2,'label':'HO Rec Hits > 0.2 GeV'})

plt.ylabel('# entries')
plt.xlabel('time / ns')
plt.legend()
ax2.set_xlim(-20,20)
print 'Done'

plt.show()
plt.subplots()

print 'Finished'
