from ROOT import TEfficiency

def getEfficiencyForPtCut(listMatchedPairs,ptCut):
	truePtValues = range(0,200+1)
	countPassed = [0]*200
	countTotal = [0]*200
	
	for event in listMatchedPairs:
		for pair in event:
			countTotal[int(pair[1].pt)] += 1
			if(pair[0].pt >= ptCut):
				countPassed[int(pair[1].pt)] += 1
	
	
	print countPassed
	print countTotal