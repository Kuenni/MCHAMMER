from ROOT import ROOT,gROOT,TCanvas,TFile,TH1D,TH2D,TLegend,THStack,TPaveText
import sys
import os
import PlotStyle
import numpy as np

import L1RatePlotter
import EnergyPlotter
import EfficiencyPlotter

PlotStyle.setPlotStyle()

if(len(sys.argv) < 2):
    print 'Error! Filename as first argument needed.'
    sys.exit(1)

if( not os.path.exists('plots')):
    os.mkdir('plots')

filename = sys.argv[1]
print 'Opening file:',filename

#L1RatePlotter.plotL1Rates(filename)
EnergyPlotter.plotEnergy(filename)
#EfficiencyPlotter.plotEfficiency(filename)


file = TFile.Open(filename)

hlt_TrigRate = file.Get("demo/HLT_L1SingleMuOpen_v7_TrigRate")
hltHoMatch_TrigRate = file.Get("demo/HLT_L1SingleMuOpen_v7_hoMatch_TrigRate")
hltHoMatchAboveThr_TrigRate = file.Get("demo/HLT_L1SingleMuOpen_v7_hoMatchAboveThr_TrigRate")
l1Muon_TrigRate = file.Get("demo/L1Muon_TrigRate")

frameHist = TH2D('frame','Pseudo Trigger Rate HLT_L1SingleMuOpen',1,0,100,1,40,2e3)

canv = TCanvas("pseudoTrigRateCanvas",'pseudoTrigRateCanvas')
canv.cd(1).SetLogy()

frameHist.GetXaxis().SetTitle('P_{T} threshold / GeV')
frameHist.GetYaxis().SetTitle('N Entries / 5 GeV')
frameHist.SetStats(0)
#frameHist.Draw()

hlt_TrigRate.SetMarkerStyle(26)
hltHoMatch_TrigRate.SetMarkerStyle(22)
hltHoMatchAboveThr_TrigRate.SetMarkerStyle(25)
l1Muon_TrigRate.SetMarkerStyle(21)
#l1MuwithHoAndGenMatch_TrigRate.SetMarkerStyle(20)

hlt_TrigRate.SetLineColor(ROOT.kBlack)
hltHoMatch_TrigRate.SetLineColor(ROOT.kBlack)
hltHoMatchAboveThr_TrigRate.SetLineColor(ROOT.kBlack)
l1Muon_TrigRate.SetLineColor(ROOT.kBlack)
#l1MuwithHoAndGenMatch_TrigRate.SetLineColor(ROOT.kBlack)


hlt_TrigRate.SetMarkerColor(ROOT.kRed)
hltHoMatch_TrigRate.SetMarkerColor(ROOT.kGreen)
hltHoMatchAboveThr_TrigRate.SetMarkerColor(ROOT.kBlue)
l1Muon_TrigRate.SetMarkerColor(ROOT.kBlack)
#l1MuwithHoAndGenMatch_TrigRate.SetMarkerColor(ROOT.kMagenta)

hlt_TrigRate.Draw('p,e1')
hltHoMatch_TrigRate.Draw('Same,p,e1')
hltHoMatchAboveThr_TrigRate.Draw('same,p,e1')
l1Muon_TrigRate.Draw('same,p,e1')
#l1MuwithHoAndGenMatch_TrigRate.Draw('same,p,e1')

legend = TLegend(0.5,0.65,0.9,0.9)

legend.AddEntry(hlt_TrigRate,'HLT Object','ep')
legend.AddEntry(hltHoMatch_TrigRate,'HLT Object with HO match','ep')
legend.AddEntry(hltHoMatchAboveThr_TrigRate,'HLT Object with HO above Thr. match','ep')
legend.AddEntry(l1Muon_TrigRate,'L1Muon Object','ep')
#legend.AddEntry(l1MuwithHoAndGenMatch_TrigRate,'L1Mu; HO Rec ab. Thres. and Gen Ref match','ep')
legend.Draw()
canv.SaveAs("plots/PseudoTrigRate.png")
canv.SaveAs("plots/PseudoTrigRate.pdf")



l1Muon_TrigRate = file.Get("demo/L1Muon_TrigRate")
l1MuWithHoMatch_TrigRate = file.Get("demo/HORecowithMipMatch_TrigRate")
hltWithL1Match_TrigRate = file.Get("demo/HLT_L1SingleMuOpen_v7L1Match_TrigRate")
hltWithL1MatchAboveThr_TrigRate = file.Get("demo/HLT_L1SingleMuOpen_v7L1MatchHoAboveThr_TrigRate")
hlt_TrigRate = file.Get("demo/HLT_L1SingleMuOpen_v7_TrigRate")
hltMu5_TrigRate = file.Get("demo/HLT_Mu5_v21_TrigRate")
hltMu5L1Match_TrigRate = file.Get("demo/HLT_Mu5_v21L1Match_TrigRate")
hltMu5L1MatchAboveThr_TrigRate = file.Get("demo/HLT_Mu5_v21L1MatchHoAboveThr_TrigRate")

frameHist = TH2D('frame','Pseudo Trigger Rate L1 Muons and HO',1,0,150,1,1,2e3)

canv = TCanvas("pseudoTrigRateCanvasL1HO",'pseudoTrigRateCanvasL1HO')
canv.cd(1).SetLogy()

frameHist.GetXaxis().SetTitle('P_{T} threshold / GeV')
frameHist.GetYaxis().SetTitle('N Entries / 5 GeV')
frameHist.SetStats(0)
#frameHist.Draw()

variableBinArray = [0.5,1,1.5,2,2.5,3,3.5,4,4.5,5,6,7,8,9,10,12,14,16,18,20,25,30,35,40,45,50,60,70,80,100,120,140,180]
variableBinArray = np.array(variableBinArray,dtype=float)

newHist = l1Muon_TrigRate.Rebin(len(variableBinArray)-1,"newTestHist",variableBinArray)


l1Muon_TrigRate.SetMarkerStyle(21)
l1Muon_TrigRate.SetLineColor(ROOT.kBlack)
l1Muon_TrigRate.SetMarkerColor(ROOT.kBlack)
l1Muon_TrigRate.SetStats(0)
l1Muon_TrigRate.GetXaxis().SetRangeUser(0,100)
l1Muon_TrigRate.GetYaxis().SetRangeUser(40,2e4)
l1Muon_TrigRate.Draw('p,e1')

l1MuWithHoMatch_TrigRate.SetMarkerStyle(22)
l1MuWithHoMatch_TrigRate.SetLineColor(ROOT.kBlack)
l1MuWithHoMatch_TrigRate.SetMarkerColor(ROOT.kRed)
l1MuWithHoMatch_TrigRate.Draw('same,p,e1')

hltWithL1Match_TrigRate.SetMarkerStyle(23)
hltWithL1Match_TrigRate.SetLineColor(ROOT.kBlack)
hltWithL1Match_TrigRate.SetMarkerColor(ROOT.kGreen)
hltWithL1Match_TrigRate.Draw('same,p,e1')

hltWithL1MatchAboveThr_TrigRate.SetMarkerStyle(20)
hltWithL1MatchAboveThr_TrigRate.SetLineColor(ROOT.kBlack)
hltWithL1MatchAboveThr_TrigRate.SetMarkerColor(ROOT.kGreen-7)
hltWithL1MatchAboveThr_TrigRate.Draw('same,p,e1')

hlt_TrigRate.SetMarkerStyle(29)
hlt_TrigRate.SetMarkerColor(ROOT.kCyan)
hlt_TrigRate.SetLineColor(ROOT.kBlack)
#hlt_TrigRate.Draw('same,p,e1')

hltMu5_TrigRate.SetMarkerStyle(20)
hltMu5_TrigRate.SetMarkerColor(ROOT.kMagenta)
hltMu5_TrigRate.SetLineColor(ROOT.kBlack)
#hltMu5_TrigRate.Draw('same,p,e1')

hltMu5L1Match_TrigRate.SetMarkerStyle(33)
hltMu5L1Match_TrigRate.SetMarkerColor(ROOT.kOrange)
hltMu5L1Match_TrigRate.SetLineColor(ROOT.kBlack)
hltMu5L1Match_TrigRate.Draw('same,p,e1')

hltMu5L1MatchAboveThr_TrigRate.SetMarkerStyle(34)
hltMu5L1MatchAboveThr_TrigRate.SetMarkerColor(ROOT.kViolet)
hltMu5L1MatchAboveThr_TrigRate.SetLineColor(ROOT.kBlack)
hltMu5L1MatchAboveThr_TrigRate.Draw('same,p,e1')

legend = TLegend(0.5,0.65,0.9,0.9)

legend.AddEntry(l1Muon_TrigRate,'L1Muon Object','ep')
legend.AddEntry(l1MuWithHoMatch_TrigRate,'L1Muon + HO above Thr.','ep')
#legend.AddEntry(hlt_TrigRate,'HLT (Single Mu Open)','ep')
legend.AddEntry(hltWithL1Match_TrigRate,'HLT (Single Mu Open) with L1 match','ep')
legend.AddEntry(hltWithL1MatchAboveThr_TrigRate,'HLT (Single Mu Open) + HO above Thr.','ep')
#legend.AddEntry(hltMu5_TrigRate,'HLT (Single Mu 5)','ep')
legend.AddEntry(hltMu5L1Match_TrigRate,'HLT (Single Mu 5) + L1 match','ep')
legend.AddEntry(hltMu5L1MatchAboveThr_TrigRate,'HLT (Single Mu 5) + HO above Thr. match','ep')

legend.Draw()
canv.SaveAs("plots/PseudoTrigRateL1HO.png")
canv.SaveAs("plots/PseudoTrigRateL1HO.pdf")
f = TFile.Open("plots/PseudoTrigRatePlots.root","RECREATE")
canv.Write()
f.Close()

canv = TCanvas()
newHist.Draw()
canv.SaveAs("plots/binningTest.png")
