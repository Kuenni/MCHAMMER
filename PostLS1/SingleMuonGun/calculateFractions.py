#!/usr/bin/python
import os,sys

from ROOT import TFile

sys.path.append(os.path.abspath("/user/kuensken/ChrisAnelliCode/CMSSW_6_2_0_SLHC11/src/HoMuonTrigger/python"))

print 'Calculate bin fractions'

f = TFile.Open('plots/NoSingleMu_DeltaEtaDeltaPhi.root')
c = f.Get('canvasDeltaEtaDeltaPhi')
h = c.GetListOfPrimitives().FindObject('NoSingleMu_DeltaEtaDeltaPhi')

nTotal = h.GetEntries()

central = h.GetBinContent(h.FindBin(0,0))
threeTimesThree = 0

for i in range(0,3):
	for j in range (0,3):
		threeTimesThree += h.GetBinContent(h.FindBin(-0.087 + j*0.087, 0.087 - i*0.087))
	#	print i,j,h.FindBin(-0.087 + j*0.087, 0.087 - i*0.087)
		
print 'Events in central bin:\t%d\t=>\t%.2f%%' % (central,central/nTotal*100)
print 'Events in 3x3 bins:\t%d\t=>\t%.2f%%' % (threeTimesThree,threeTimesThree/nTotal*100)

print '%s' % (20*'#')
print 'Events with L1 muon match'
f = TFile.Open('plots/L1MuonWithHoMatchAboveThr_DeltaEtaDeltaPhi.root')
c = f.Get('canvasDeltaEtaDeltaPhi')
h = c.GetListOfPrimitives().FindObject('L1MuonWithHoMatchAboveThr_DeltaEtaDeltaPhi')
nTotal = h.GetEntries()
central = h.GetBinContent(h.FindBin(0,0))

threeTimesThree = 0
for i in range(0,3):
	for j in range (0,3):
		threeTimesThree += h.GetBinContent(h.FindBin(-0.087 + j*0.087, 0.087 - i*0.087))
		
		

print 'Events in central bin:\t%d\t=>\t%.2f%%' % (central,central/nTotal*100)
print 'Events in 3x3 bins:\t%d\t=>\t%.2f%%' % (threeTimesThree,threeTimesThree/nTotal*100)
