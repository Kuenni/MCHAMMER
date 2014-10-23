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

toProcess = [
             'crabSiPMCalib'
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
	plotEnergyVsEta(s,'L1MuonHistogram_Full.root')
	print 'Doing Energy Vs Phi...'
	plotEnergyVsPhi(s,'L1MuonHistogram_Full.root')
print 'All done.'