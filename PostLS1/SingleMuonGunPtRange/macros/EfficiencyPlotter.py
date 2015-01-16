from ROOT import TEfficiency,TCanvas
import ROOT

import math


#counter variable for the root object naming
efficiencyCounter = 0
def getEfficiencyForPtCut(listMatchedPairs,ptCut):
	global efficiencyCounter
	efficiencyCounter += 1
	effObj = TEfficiency("efficiency" + str(efficiencyCounter),"Efficiency for p_{T,cut} = " + str(ptCut) + " GeV",251,-0.5,250.5)
	ROOT.SetOwnership(effObj,False)
	truePtValues = range(0,200)
	countPassed = [0]*200
	countTotal = [0]*200
	yVal = [0]*200
	xErr = [0.5]*200
	yErr = [0]*200
	
	for event in listMatchedPairs:
		for pair in event:
			effObj.Fill(pair[0].pt >= ptCut,pair[1].pt)
			
			countTotal[int(pair[1].pt)] += 1
			if(pair[0].pt >= ptCut):
				countPassed[int(pair[1].pt)] += 1
	
	
	for i,val in enumerate(countPassed):
		if(countTotal[i] > 0):
			yVal[i]=float(countPassed[i]/countTotal[i])
			yErr[i]=float(math.sqrt(yVal[i]*(1-yVal[i])/countTotal[i]))
	#print countPassed
	#print countTotal
	c = TCanvas("can","vas",1200,1200)
	#effObj.Draw()
	return c,effObj
	#return [truePtValues,yVal,xErr,yErr]
	
