import math

#Calculate delta phi in CMS
def calculateDeltaPhi(phi1,phi2):
	delta = phi1 - phi2
	if delta < -math.pi:
		return delta + 2*math.pi
	if delta > math.pi:
		return 2*math.pi - delta
	return delta

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

