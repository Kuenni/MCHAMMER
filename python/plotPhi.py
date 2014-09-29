#!/usr/bin/python
from ROOT import ROOT,gROOT,gStyle,TCanvas,TFile,TH1D,TH2D,TLegend,THStack,TPaveText,TBox
import sys
import os
import PlotStyle
import numpy as np

PlotStyle.setPlotStyle()
gStyle.SetPalette(1)

if(len(sys.argv) < 2):
    print 'Error! Filename as first argument needed.'
    sys.exit(1)

if( not os.path.exists('plots')):
    os.mkdir('plots')

filename = sys.argv[1]
print 'Opening file:',filename

file = TFile.Open(filename)

h1phi = file.Get("hoMuonAnalyzer/etaPhi/horeco_Phi")
h1MatchedPhiHo = file.Get("hoMuonAnalyzer/etaPhi/L1MuonWithHoMatch_Phi")
h1MatchedPhiHoAbThr = file.Get("hoMuonAnalyzer/etaPhi/L1MuonwithHoMatch_HO_Phi")

canv = TCanvas("canvasPhi",'canvasPhi',1200,1200)
canv.SetLogy()

h1phi.GetXaxis().SetTitle("#phi")
h1phi.GetYaxis().SetTitle("N")
#h1phi.Rebin(4)
h1phi.GetYaxis().SetRangeUser(0.1,2e5)
h1phi.Draw()

h1MatchedPhiHo.SetLineColor(ROOT.kRed)
#h1MatchedPhiHo.Rebin(4)
h1MatchedPhiHo.Draw('Same')

h1MatchedPhiHoAbThr.SetLineColor(ROOT.kBlack)
#h1MatchedPhiHoAbThr.Rebin(4)
h1MatchedPhiHoAbThr.Draw('Same')

canv.Update()

stats = h1phi.GetListOfFunctions().FindObject("stats")
#stats.SetX1NDC(.1)
#stats.SetX2NDC(.3)
#stats.SetY1NDC(.8)
#stats.SetY2NDC(.9)

canv.SaveAs("plots/phi.png")
canv.SaveAs("plots/phi.pdf")

f = TFile.Open("plots/eta.root","RECREATE")
canv.Write()
f.Close()
