import math

#Calculate delta phi in CMS
def calculateDeltaPhi(phi1,phi2):
	delta = phi2 - phi1
	if delta < -math.pi:
		return delta + 2*math.pi
	if delta > math.pi:
		return 2*math.pi - delta
	return delta

def calculateDeltaEta(eta1,eta2):
	return eta2 - eta1

def getDeltaPhiList(pairList):
	deltaPhiList = []
	for pair in pairList:
		deltaPhiList.append(calculateDeltaPhi(pair[0].phi,pair[1].phi))
	return deltaPhiList

def getDeltaEtaList(pairList):
	deltaEtaList = []
	for pair in pairList:
		deltaEtaList.append(calculateDeltaEta(pair[0].eta,pair[1].eta))
	return deltaEtaList

#Calculate delta R
def calculateDeltaR(eta1,phi1,eta2,phi2):
	deltaEta = eta1 - eta2
	deltaPhi = calculateDeltaPhi(phi1, phi2)
	return math.sqrt( math.pow(deltaEta,2) + math.pow(deltaPhi,2) )

#Takes the given L1 object data and searches for the best HO match by Delta R
def findBestHoMatchByDeltaR(l1Data,hoDataVector, eMin = -1. ):
	bestDeltaR = 999.
	bestHoData = None
	for i in range(0,len(hoDataVector)):
		hoEta = hoDataVector[i].eta
		hoPhi = hoDataVector[i].phi
		deltaR = calculateDeltaR(l1Data.eta, l1Data.phi, hoEta, hoPhi)
		#Check for energy threshold if given, else check only Delta R
		if ( deltaR < bestDeltaR ) and ( ( hoDataVector[i].energy > eMin ) if eMin >= 0 else True ):
			bestDeltaR = deltaR
			bestHoData = hoDataVector[i]
	return bestHoData

#Takes the given L1 object data and searches for the best HO match by EMax
def findBestHoMatchByEnergy(l1Data,hoDataVector, deltaRMax = -1. ):
	bestE = -1.
	bestHoData = None
	for i in range(0,len(hoDataVector)):
		hoEta = hoDataVector[i].eta
		hoPhi = hoDataVector[i].phi
		deltaR = calculateDeltaR(l1Data.eta, l1Data.phi, hoEta, hoPhi)
		#Check for energy threshold if given, else check only Delta R
		if ( hoDataVector[i].energy > bestE ) and ( ( deltaR < deltaRMax ) if deltaRMax >= 0 else True ):
			bestE = hoDataVector[i].energy
			bestHoData = hoDataVector[i]
	return bestHoData

#Find the best Ho match when testing both energy and delta R
def findBestHoMatch(l1Data,hoDataVector, deltaRMax, eMin):
	bestDeltaR = 999.
	bestE = -1.
	bestHoData = None
	for i in range(0,len(hoDataVector)):
		hoEta = hoDataVector[i].eta
		hoPhi = hoDataVector[i].phi
		deltaR = calculateDeltaR(l1Data.eta, l1Data.phi, hoEta, hoPhi)
		if hoDataVector[i].energy > bestE and deltaR < deltaRMax and deltaR < bestDeltaR and hoDataVector[i].energy > eMin:
			bestE = hoDataVector[i].energy
			bestDeltaR = deltaR
			bestHoData = hoDataVector[i]
	return bestHoData

#Find the best L1Match for a given gen particle
def findBestL1Match(genData,l1DataVector,deltaRMax):
	bestDeltaR = 999.
	bestL1Data = None
	for i in range(0,len(l1DataVector)):
		l1Eta = l1DataVector[i].eta
		l1Phi = l1DataVector[i].phi
		deltaR = calculateDeltaR(genData.eta, genData.phi, l1Eta, l1Phi)
		#Check for energy threshold if given, else check only Delta R
		if deltaR < deltaRMax and deltaR < bestDeltaR :
			bestDeltaR = deltaR
			bestL1Data = l1DataVector[i]
	return bestL1Data