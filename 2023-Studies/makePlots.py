#!/usr/bin/python
import os,sys
sys.path.append(os.path.abspath("/user/kuensken/ChrisAnelliCode/CMSSW_6_2_0_SLHC11/src/HoMuonTrigger/python"))

from plotEnergy import plotEnergy
from plotDeltaEtaDeltaPhi import plotDeltaEtaDeltaPhi
from plotEtaPhi import plotEtaPhi
from plotL1Rate import plotL1Rates

toProcess = [
             'crabSiPMCalib',
             'crabSiPMNoExtraCalib'
             ]

for s in toProcess:
	print 'Doing energy...'
	plotEnergy(s)
	print 'Doing Delta Eta Delta Phi...'
	plotDeltaEtaDeltaPhi(s)
	print 'Doing Eta Phi...'
	plotEtaPhi(s)
	print 'Doing L1Rates...'
	plotL1Rates(s)

print "Say Hello" 
