from ROOT import ROOT,gROOT,TCanvas,TFile,TH1D,TH2D,TLegend,THStack,TPaveText
import sys
import PlotStyle
import numpy as np

def plotL1Rates(filename):
    
    file = TFile.Open(filename)
    
    ho = file.Get("demo/horeco_Energy")
    hoAboveThr = file.Get("demo/horecoAboveThreshold_Energy")
    L1MuonAndHoMatch = file.Get('demo/L1MuonAndHoAboveThr_Energy')
    
    canv = TCanvas("energieCanvas",'EnergieCanvas')
    canv.cd(1).SetLogy()
    
    ho.SetStats(0)
    ho.GetXaxis().SetTitle('Energie / GeV')
    ho.GetYaxis().SetTitle('Anzahl Eintr#ddot{a}ge')
    ho.SetRangeUser(0,100)
    
    ho.SetLineColor(ROOT.kBlack)
   # hoAboveThr.SetLineColor(ROOT.kBlue)
   # L1MuonAndHoMatch.SetLineColor(ROOT.kRed)
   
    ho.Draw()
   # hoAboveThr.Draw('same')
   # L1MuonAndHoMatch.Draw('same')
    
    legend = TLegend(0.5,0.65,0.9,0.9)
    legend.AddEntry(ho,'Alle HO Hits','l')
   # legend.AddEntry(hoAboveThr,'HO Hits > 0.2 GeV','ep')
   # legend.AddEntry(L1MuonAndHoMatch,'L1 Objekte mit HO-Match','ep')
    legend.Draw()
    
    canv.SaveAs("plots/Energieverteilung.png")
    canv.SaveAs("plots/Energieverteilung.pdf")
    
    f = TFile.Open("plots/Energieverteilung.root","RECREATE")
    canv.Write()
    f.Close()
    