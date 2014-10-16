#!/usr/bin/python
import os,sys
sys.path.append(os.path.abspath("/user/kuensken/ChrisAnelliCode/CMSSW_6_2_0_SLHC11/src/HoMuonTrigger/python"))

from plotEnergy import plotEnergy

toProcess = [
             'crabSiPMCalib',
             'crabSiPMNoExtraCalib'
             ]

for s in toProcess:
    plotEnergy(s)

print "Say Hello" 
