'''
	Analyzer script for root trees containing data from L1 muon objects, Gen muon objects
	and Ho rec hit objects stored in vectors for each event
	
	Created on 12. Jan 2015
	Andreas Kuensken <kuensken@physik.rwth-aachen.de>
'''
import sys,os
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.colors import LogNorm
import numpy as np
import math

sys.path.append(os.path.abspath("../../../python"))
import PlotStyle
PlotStyle.setPlotStyle()

from ROOT import TTree,TFile,gROOT,vector,gSystem,std
gROOT.ProcessLine('.L ./loader.C+')
from ROOT import L1MuonData,GenMuonData,HoRecHitData

# Define a switch to enable debug mode. In this mode only a fraction of the 
# total event data is processed to enable a fast check on any implemented
# changes
DEBUG = False
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

def create2dHistogram(ax,dataX,dataY, binwidth, axisRange = [[0,0],[0,0]],centerBins = False,norm = None,parameterDict = {'label':'2D hist'}):
	binStartX = int(min(dataX)/binwidth[0])*binwidth[0]
	binStartY = int(min(dataY)/binwidth[1])*binwidth[1]
	binEndX = int(max(dataX)/binwidth[0])*binwidth[0]
	binEndY = int(max(dataY)/binwidth[1])*binwidth[1]
	if(axisRange != [[0,0],[0,0]]):
		binStartX = int(axisRange[0][0]/binwidth[0])*binwidth[0]
		binStartY = int(axisRange[1][0]/binwidth[1])*binwidth[1]
		binEndX = int(axisRange[0][1]/binwidth[0])*binwidth[0]
		binEndY = int(axisRange[1][1]/binwidth[1])*binwidth[1]
	if(centerBins):
		binStartX -= binwidth[0]/2.
		binStartY -= binwidth[1]/2.
		binEndX += binwidth[0]/2.
		binEndY += binwidth[1]/2.
		
	binsX=np.arange(binStartX, binEndX, binwidth[0])
	binsY=np.arange(binStartY, binEndY, binwidth[1])
	
	out = ax.hist2d(dataX,dataY,[binsX,binsY],norm=norm ,**parameterDict)
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

#FIXME: Can this be removed?
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

hoRecHitsAboveThr = filterListByEnergy(hoRecHits, EMIN)

matchedL1AndHoAboveThr 	= getListOfMatchedPairs(l1Muons, hoRecHitsAboveThr)
matchedL1AndHo 			= getListOfMatchedPairs(l1Muons, hoRecHits)
matchedL1AndGen 		= getListOfMatchedPairs(l1Muons, genMuons)
matchedGenAndHo 		= getListOfMatchedPairs(genMuons, hoRecHits)
matchedGenAndHoAboveThr = getListOfMatchedPairs(genMuons, hoRecHitsAboveThr)


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
fig.canvas.set_window_title('HO energy')
hoEnergy = []
hoEnergyAboveThr = []

for event in hoRecHits:
	for data in event:
		hoEnergy.append(data.energy)
for event in hoRecHitsAboveThr:
	for data in event:
		hoEnergyAboveThr.append(data.energy)
plt.title("HO energy")
ax1 = plt.subplot(2,1,1)
ax1.set_yscale('log')
ax1.set_xlim(-0.5,6)
createSimpleHistogram(ax1, hoEnergy, binwidth=0.05, parameterDict={'facecolor':'blue','label':'HO Rec Hits'})
plt.xlabel('Reconstructed energy / GeV')
plt.ylabel('# entries')
plt.legend()
ax2 = plt.subplot(2,1,2)
ax2.set_yscale('log')
ax2.set_xlim(-0.5,6)
createSimpleHistogram(ax2, hoEnergyAboveThr, binwidth = 0.05,axisRange=[min(hoEnergy),max(hoEnergy)], parameterDict={'facecolor':'red','label':'HO Rec Hits > 0.2 GeV'})
plt.xlabel('Reconstructed energy / GeV')
plt.ylabel('# entries')
plt.legend()

print 'Done'

############
# Plot delta timing
############

print 'Creating timing plots'

#delta time for l1 and ho above thr
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
					parameterDict={'color':'blue','histtype':'step','lw':3,'label':r'$\Delta$Time L1$_{BX=0}$ matched to HO'})
plt.title('L1 Muons matched to HO > 0.2 GeV')
plt.ylabel('# entries')
plt.xlabel(r'$\Delta$time / ns')
plt.legend(loc=2)

#delta time for l1 and all ho
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
					parameterDict={'color':'blue','histtype':'step','lw':3,'label':r'$\Delta$Time L1$_{BX=0}$ matched to HO'})
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
					parameterDict={'color':'blue','histtype':'step','lw':3,'label':r'$\Delta$Time L1 matched to HO > 0.2 GeV'})
plt.title('Delta Time')
plt.ylabel('# entries')
plt.xlabel(r'$\Delta$time / ns')
plt.legend(loc=2)

# Plot of bx for all L1 and L1 matched to HO Above Thr
fig = plt.figure()
fig.canvas.set_window_title('BX ID')
ax = plt.subplot(1,1,1)

countBxId0 = 0
countBxId0WithHo = 0
countBxIdM1 = 0
countBxIdM1WithHo = 0


l1Bx = []
l1MatchedBx = []

for event in l1Muons:
	for data in event:
		l1Bx.append(data.bx)
		if(data.bx == 0):
			countBxId0 += 1
		if(data.bx == -1):
			countBxIdM1 += 1

for event in matchedL1AndHoAboveThr:
	for pair in event:
		l1MatchedBx.append(pair[0].bx)
		if(pair[0].bx == 0):
			countBxId0WithHo += 1
		if(pair[0].bx == -1):
			countBxIdM1WithHo += 1

print countBxIdM1,countBxIdM1WithHo

ax.set_yscale('log')		
createSimpleHistogram(ax, l1Bx, binwidth = 1,axisRange=[-5,5],parameterDict={'color':'blue','label':'All L1 Muons'})
createSimpleHistogram(ax, l1MatchedBx, binwidth = 1,axisRange=[-5,5],
					parameterDict={'histtype':'step','color':'red','lw':2,'label':'L1Muon matched to HO'})

ax.text(0.01, 0.5, r'With HO in BX$_0$: %.2f%%' % (countBxId0WithHo/float(countBxId0)*100),
        verticalalignment='bottom', horizontalalignment='left',
        transform=ax.transAxes,
        fontsize=15)
ax.text(0.01, 0.4, r'With HO in BX$_{-1}$: %.2f%%' % (countBxIdM1WithHo/float(countBxIdM1)*100),
        verticalalignment='bottom', horizontalalignment='left',
        transform=ax.transAxes,
        fontsize=15)
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

createSimpleHistogram(ax2, hoTime, binwidth = 1,parameterDict={'label':'All HO Rec Hits','color':'blue'})
plt.ylabel('# entries')
plt.xlabel('time / ns')
plt.legend()

# time of ho hits above thr
plt.figure()
ax2 = plt.subplot(1,1,1)
createSimpleHistogram(ax2, hoTimeAboveThr, binwidth = 1, axisRange=[min(hoTime),max(hoTime)],
					parameterDict={'color':'red','histtype':'step','lw':2,'label':'HO Rec Hits > 0.2 GeV'})

plt.ylabel('# entries')
plt.xlabel('time / ns')
plt.legend()
ax2.set_xlim(-20,20)
print 'Done'

############
# Create the efficiency plots and turn on curves
############

from EfficiencyPlotter import getEfficiencyForPtCut
res = getEfficiencyForPtCut(matchedL1AndGen,ptCut = 15)

res[-1].Draw()
res[0].Update()

############
# Create delta eta delta phi plots
############

deltaEtaData = []
deltaPhiData = []
for event in matchedL1AndHoAboveThr:
	for pair in event:
		l1Eta = pair[0].eta
		l1Phi = pair[0].phi
		hoEta = pair[1].eta
		hoPhi = pair[1].phi
		deltaEtaData.append(l1Eta - hoEta)
		deltaPhiData.append(computeDeltaPhi(l1Phi,hoPhi))

fig = plt.figure()
fig.canvas.set_window_title("Delta eta Delta phi above thr")
ax = plt.subplot(1,1,1)
img = create2dHistogram(ax, deltaEtaData, deltaPhiData, binwidth = [0.087,0.087],axisRange=[[-0.35,0.35],[-0.35,0.35]],centerBins=True, norm=LogNorm())
plt.xlabel(r'$\Delta\eta$')
plt.ylabel(r'$\Delta\phi$')
plt.title(r'$\Delta\eta$ $\Delta\phi$ for L1 matched to HO > 0.2 GeV')


# Make an axis for the colorbar on the right side
cax = fig.add_axes([0.9, 0.1, 0.03, 0.8])
fig.colorbar(img[3], cax=cax)
plt.draw()

######
## Plot delta eta delta phi for all ho 
######

deltaEtaData = []
deltaPhiData = []
for event in matchedL1AndHo:
	for pair in event:
		l1Eta = pair[0].eta
		l1Phi = pair[0].phi
		hoEta = pair[1].eta
		hoPhi = pair[1].phi
		if(isInsideDeltaR(l1Eta, hoEta, l1Phi, hoPhi,deltaRMax=0.3)):
			deltaEtaData.append(l1Eta - hoEta)
			deltaPhiData.append(computeDeltaPhi(l1Phi,hoPhi))

fig = plt.figure()
fig.canvas.set_window_title("Delta eta Delta phi")
ax = plt.subplot(1,1,1)
img = create2dHistogram(ax, deltaEtaData, deltaPhiData, binwidth = [0.087,0.087],axisRange=[[-0.35,0.35],[-0.35,0.35]],centerBins=True,norm=LogNorm())
plt.xlabel(r'$\Delta\eta$')
plt.ylabel(r'$\Delta\phi$')
plt.title(r'$\Delta\eta$ $\Delta\phi$ for L1 matched to any HO')


# Make an axis for the colorbar on the right side
cax = fig.add_axes([0.9, 0.1, 0.03, 0.8])
fig.colorbar(img[3], cax=cax)
plt.draw()

###########################
## All done. But keep the plots open...
###########################

print 'Finished'
print
print 'The Tree contained %d entries' % (t.GetEntries())
print
import matplotlib
print 'Ran on matplotlib version',matplotlib.__version__
plt.show(block=True)
raw_input('-->')