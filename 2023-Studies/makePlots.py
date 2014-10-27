#!/usr/bin/python
import os,sys

sys.path.append(os.path.abspath("/user/kuensken/ChrisAnelliCode/CMSSW_6_2_0_SLHC11/src/HoMuonTrigger/python"))

from plotEnergy import plotEnergy, plotEnergyVsEta, plotEnergyVsPhi
from plotDeltaEtaDeltaPhi import plotDeltaEtaDeltaPhi
from plotEtaPhi import plotEtaPhi
from plotL1Rate import plotL1Rates
from plotPhi import plotPhi
from plotEfficiency import plotEfficiency
from plotMultiplicity import plotMultiplicity
from plotPtCorrelation import plotPtCorrelation

print len(sys.argv)

filename = 'L1MuonHistogram.root'

if(len(sys.argv) > 1 ):
	filename = sys.argv[1]

toProcess = [
             'crabSiPMCalib'
   #         ,'crab2023MinBias'
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
	print 'Doing Phi...'
	plotPhi(s)
	print 'Doing Efficiency...'
	plotEfficiency(s)
	print 'Doing Multiplicity...'
	plotMultiplicity(s)
	print 'Doing Energy Vs Eta...'
	plotEnergyVsEta(s,filename)
	print 'Doing Energy Vs Phi...'
	plotEnergyVsPhi(s,filename)
print 'All done.'