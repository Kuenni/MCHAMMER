#!/usr/bin/python
import os,sys

sys.path.append(os.path.abspath("../../python"))

from plotEnergy import plotEnergy, plotEnergyVsEta, plotEnergyVsPhi
from plotDeltaEtaDeltaPhi import plotDeltaEtaDeltaPhi
from plotEtaPhi import plotEtaPhi
from plotL1Rate import plotL1Rates
from plotPhi import plotPhi
from plotEfficiency import plotEfficiency,plotCombinedEfficiency
from plotMultiplicity import plotMultiplicity
from plotPtCorrelation import plotPtCorrelation

print 'File crabSiPMCalibPlots'

filename = 'L1MuonHistogram.root'

if(len(sys.argv) > 1 ):
	filename = sys.argv[1]

toProcess = [
    #         '.'
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
# 	print 'Doing Phi...'
# 	plotPhi(s)
	print 'Doing Efficiency...'
	plotEfficiency(s)
	print 'Doing Multiplicity...'
	plotMultiplicity(s)

print 'All done.'

"""
c1 = plotEnergyVsEta('.','L1MuonWithHoMatch_EnergyVsEta')
c1.SetName('c1')
c1.SaveAs('energyVsEta_L1MuonAndHo.png')
c2 = plotEnergyVsEta('.','L1MuonWithHoMatchAboveThr_EnergyVsEta')
c2.SetName('c2')
c2.SaveAs('energyVsEta_L1MuonAndHoAboveThr.png')
c3 = plotEnergyVsEta('.','L1MuonWithHoMatchAboveThrFilt_EnergyVsEta')
c3.SetName('c3')
c3.SaveAs('energyVsEta_L1MuonAndHoAboveThrFilt.png')
cPhi1 = plotEnergyVsPhi('.','L1MuonWithHoMatch_EnergyVsPhi')
cPhi1.SetName('cPhi1')
cPhi1.SaveAs('energyVsPhi_L1MuonAndHo.png')
cPhi2 = plotEnergyVsPhi('.','L1MuonWithHoMatchAboveThr_EnergyVsPhi')
cPhi2.SetName('cPhi2')
cPhi2.SaveAs('energyVsPhi_L1MuonAndHoAboveThr.png')
cPhi3 = plotEnergyVsPhi('.','L1MuonWithHoMatchAboveThrFilt_EnergyVsPhi')
cPhi3.SetName('cPhi2')
cPhi3.SaveAs('energyVsPhi_L1MuonAndHoAboveThrFilt.png')
"""

c1 = None
c2 = None
c3 = None
cPhi1 = None
cPhi2 = None
cPhi3 = None

cCombEff = plotCombinedEfficiency()
