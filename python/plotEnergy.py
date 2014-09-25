#!/usr/bin/python
from ROOT import ROOT,gROOT,TCanvas,TFile,TH1D,TH2D,TLegend,THStack,TPaveText
import sys,os
import PlotStyle
import numpy as np

if(len(sys.argv) < 2):
    print 'Error! Filename as first argument needed.'
    sys.exit(1)

if( not os.path.exists('plots')):
    os.mkdir('plots')

filename = sys.argv[1]
print 'Opening file:',filename
file = TFile.Open(filename)


#Set plot style
PlotStyle.setPlotStyle()

ho = file.Get("hoMuonAnalyzer/energy/horeco_Energy")
L1MuonAndHoMatch = file.Get('hoMuonAnalyzer/energy/L1MuonWithHoMatch_Energy')
L1MuonAndHoMatchAboveThr = file.Get('hoMuonAnalyzer/energy/L1MuonWithHoMatchAboveThr_Energy')

canv = TCanvas("energieCanvas",'Energy canvas',1200,1200)
canv.SetLogy()

ho.SetStats(0)
ho.SetTitle('Energy distribution of HO hits')
ho.GetXaxis().SetTitle('Reconstructed HO energy / GeV')
ho.GetYaxis().SetTitle('N')
ho.GetXaxis().SetRangeUser(-0.2,4)

ho.SetLineColor(ROOT.kBlack)
L1MuonAndHoMatch.SetLineColor(ROOT.kBlue)
L1MuonAndHoMatchAboveThr.SetLineColor(ROOT.kRed)

ho.SetLineWidth(3)
L1MuonAndHoMatch.SetLineWidth(3)
L1MuonAndHoMatchAboveThr.SetLineWidth(3)

ho.Draw()
L1MuonAndHoMatch.Draw('same')
L1MuonAndHoMatchAboveThr.Draw('same')

legend = TLegend(0.5,0.65,0.9,0.9)
legend.AddEntry(ho,'All HO hits','l')
legend.AddEntry(L1MuonAndHoMatch,'L1 + HO match','l')
legend.AddEntry(L1MuonAndHoMatchAboveThr,'L1 + HO match > 0.2 GeV','l')
legend.Draw()

canv.SaveAs("plots/Energieverteilung.png")
canv.SaveAs("plots/Energieverteilung.pdf")

f = TFile.Open("plots/Energieverteilung.root","RECREATE")
canv.Write()
f.Close()
