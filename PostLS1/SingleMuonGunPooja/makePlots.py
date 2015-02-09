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

from ROOT import TH2D,TH2F

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

#c1 = None
#c2 = None
#c3 = None
#cPhi1 = None
#cPhi2 = None
#cPhi3 = None

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

histoNames = ['tdmiHoMatch_DeltaEtaDeltaPhi',
			'tdmiHoAboveThr_DeltaEtaDeltaPhi',
			'L1MuonWithHoMatch_DeltaEtaDeltaPhi',
			'L1MuonWithHoMatchAboveThr_DeltaEtaDeltaPhi'
			]

histograms = []

for s in histoNames:
	histograms.append(plotDeltaEtaDeltaPhi('.',sourceHistogram = s,storeSubdir='tdmiDeltaEtaDeltaPhi'))


from ROOT import TCanvas
'''
c1 = TCanvas("c1","No Thr",1200,600)
c1.Divide(2,1)
c1.cd(1)
histograms[2][0].Draw('colz')
c1.cd(2)
histograms[0][0].Draw('colz')
c1.SaveAs("c1.pdf")
c1.SaveAs("c1.root")
c1.Update()


c2 = TCanvas("c2","Above Thr",1200,600)
c2.Divide(2,1)
c2.cd(1)
histograms[3][0].Draw('colz')
c2.cd(2)
histograms[1][0].Draw('colz')
c2.SaveAs("c2.pdf")
c2.SaveAs("c2.root")
c2.Update()
cCombEff = plotCombinedEfficiency()
print cCombEff

c = TCanvas("c","Above Thr",1200,600)
histograms[2][0].Draw()
'''
cCombEff = plotCombinedEfficiency()
