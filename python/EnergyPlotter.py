from ROOT import ROOT,gROOT,TCanvas,TFile,TH1D,TH2D,TLegend,THStack,TPaveText
import sys
import PlotStyle
import numpy as np

def plotEnergy(filename):
    
    file = TFile.Open(filename)
    
    ho = file.Get("demo/horeco_Energy")
    hoAboveThr = file.Get("demo/horecoAboveThreshold_Energy")
    L1MuonAndHoMatch = file.Get('demo/HORecowithMipMatch'
                                #L1MuonAndHoAboveThr
                                '_Energy')
    
    canv = TCanvas("energieCanvas",'EnergieCanvas')
    canv.SetLogy()
    
    ho.SetStats(0)
    ho.SetTitle('Energie der HO-Treffer')
    ho.GetXaxis().SetTitle('Rekonstruierte Energie / GeV')
    ho.GetYaxis().SetTitle('Anzahl Eintr#ddot{a}ge')
    ho.GetXaxis().SetRangeUser(-0.2,4)
    
    ho.SetLineColor(ROOT.kBlack)
    hoAboveThr.SetLineColor(ROOT.kBlue)
    L1MuonAndHoMatch.SetLineColor(ROOT.kRed)
    
    ho.SetLineWidth(3)
    hoAboveThr.SetLineWidth(3)
    L1MuonAndHoMatch.SetLineWidth(3)
   
    ho.Draw()
    hoAboveThr.Draw('same')
    L1MuonAndHoMatch.Draw('same')
    
    legend = TLegend(0.5,0.65,0.9,0.9)
    legend.AddEntry(ho,'Alle HO Hits','l')
    legend.AddEntry(hoAboveThr,'HO Hits > 0.2 GeV','l')
    legend.AddEntry(L1MuonAndHoMatch,'L1 Objekte mit HO-Match > 0.2 GeV','l')
    legend.Draw()
    
    canv.SaveAs("plots/Energieverteilung.png")
    canv.SaveAs("plots/Energieverteilung.pdf")
    
    f = TFile.Open("plots/Energieverteilung.root","RECREATE")
    canv.Write()
    f.Close()
    