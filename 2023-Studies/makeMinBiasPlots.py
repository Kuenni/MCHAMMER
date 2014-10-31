#!/usr/bin/python
import os,sys

sys.path.append(os.path.abspath("/user/kuensken/ChrisAnelliCode/CMSSW_6_2_0_SLHC11/src/HoMuonTrigger/python"))

from plotEnergy import plotEnergy
from plotDeltaEtaDeltaPhi import plotDeltaEtaDeltaPhi
from plotEtaPhi import plotEtaPhi
from plotL1Rate import plotL1Rates
from plotPhi import plotPhi
from plotEfficiency import plotEfficiency
from plotMultiplicity import plotMultiplicity

toProcess = [
             'crab2023MinBias'
             ]

for s in toProcess:
	print 'Doing Efficiency'
	plotEfficiency(s)