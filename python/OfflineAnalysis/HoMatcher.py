from matchingLibrary import calculateDeltaEta,calculateDeltaPhi
from numpy import math
from plotting.OutputModule import CommandLineHandler
from ROOT import gROOT
HO_BIN = math.pi/36.
E_THR = 0.2 
	
commandLine = CommandLineHandler('[HoMatcher] ')
gROOT.ProcessLine(".L $HOMUONTRIGGER_BASE/python/loader.C+");

from ROOT import HoRecHitData,L1MuonData

def isEtaPhiInGrid(l1Eta,l1Phi,hoEta,hoPhi,gridSize):
	deltaEta = calculateDeltaEta(l1Eta,hoEta)
	deltaPhi = calculateDeltaPhi(l1Phi,hoPhi)
		
	deltaIEta = 0
	deltaIPhi = 0
	
	if(deltaEta > HO_BIN/2.):
		deltaIEta = 1 + int((deltaEta - HO_BIN/2.)/HO_BIN)
	elif(deltaEta < -HO_BIN/2.):
		deltaIEta = -1 + int((deltaEta + HO_BIN/2.)/HO_BIN)

	if(deltaPhi > HO_BIN/2.):
		deltaIPhi = 1 + int((deltaPhi - HO_BIN/2.)/HO_BIN)
	elif(deltaPhi < -HO_BIN/2.):
		deltaIPhi = -1 + int((deltaPhi + HO_BIN/2.)/HO_BIN)
	
	if abs(deltaIEta) > gridSize or abs(deltaIPhi) > gridSize:
		return False
	return True	
	
def isHoHitInGrid(l1Data,hoData,gridSize):
	l1Eta = l1Data.eta
	l1Phi = l1Data.phi
	hoEta = hoData.eta
	hoPhi = hoData.phi
	return isEtaPhiInGrid(l1Eta,l1Phi,hoEta,hoPhi,gridSize)
	
def getEMaxHoHitInGrid(l1Data,hoDataVector,gridSize):
	l1Eta = l1Data.eta
	l1Phi = l1Data.phi
	bestE = -999.
	bestHoMatch = None
	for hoData in hoDataVector:
		hoPhi = hoData.phi
		hoEta = hoData.eta
		if isEtaPhiInGrid(l1Eta, l1Phi, hoEta, hoPhi, gridSize):
			if hoData.energy >= E_THR:
				if hoData.energy > bestE:
					bestE = hoData.energy
					bestHoMatch = hoData
	return bestHoMatch

def getEMaxMatches(dataChain):
	matchesByEmax = []
	eventCounter = 0
	nEvents = dataChain.GetEntries()
	for event in dataChain:
		eventCounter += 1
		if not eventCounter % 1000:
			commandLine.printProgress(eventCounter, nEvents)
		if(eventCounter == nEvents):
			commandLine.printProgress(nEvents,nEvents)
		for l1 in event.l1MuonData:
			eMaxhit = getEMaxHoHitInGrid(l1, event.hoRecHitData, 2)
			if eMaxhit != None:
				matchesByEmax.append((L1MuonData(l1),HoRecHitData(eMaxhit)))
	print
	return matchesByEmax