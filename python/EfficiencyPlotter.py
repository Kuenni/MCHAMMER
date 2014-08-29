from ROOT import ROOT,gROOT,TCanvas,TFile,TH1D,TH2D,TLegend,THStack,TPaveText
import sys
import PlotStyle

def plotEfficiency(filename):
    
    file = TFile.Open(filename)
    
    l1Muon = file.Get("demo/L1Muon_Efficiency")
    hoAboveThr = file.Get("demo/horecoAboveThreshold_Efficiency")
    
    canv = TCanvas("efficiencyCanvas",'efficiencyCanvas')
    
    frame = TH2D('frame','L1 Efficiency',1,5,50,1,0,1.1)
    frame.SetStats(0)
    frame.GetXaxis().SetTitle('P_{T}-Schwelle / GeV')
    frame.GetYaxis().SetTitle('Effizienz')
    frame.Draw()

    l1Muon.SetMarkerStyle(2)
    hoAboveThr.SetMarkerStyle(2)
    
    l1Muon.SetMarkerColor(ROOT.kBlack)
    hoAboveThr.SetMarkerColor(ROOT.kRed)   
    
    l1Muon.SetLineColor(ROOT.kBlack)
    hoAboveThr.SetLineColor(ROOT.kRed)
   
    l1Muon.Draw('same')
    hoAboveThr.Draw('same')
    
    legend = TLegend(0.5,0.1,0.9,0.35)
    legend.AddEntry(l1Muon,'L1 Effizienz','ep')
    legend.AddEntry(hoAboveThr,'L1 + HO Hits > 0.2 GeV','ep')
    legend.Draw()
    
    canv.SaveAs("plots/Effizienz.png")
    canv.SaveAs("plots/Effizienz.pdf")
    
    f = TFile.Open("plots/Effizienz.root","RECREATE")
    canv.Write()
    f.Close()
    