import sys
import os
sys.path.append(os.path.abspath("../../python"))

import PlotStyle
from PlotStyle import calcSigma

from ROOT import TFile,TCanvas,gStyle,TH2D,TPaveText,TH1D,TLegend

from plotDeltaEtaDeltaPhi import plotDeltaEtaDeltaPhi

if( not os.path.exists('plots')):
	os.mkdir('plots')
if( not os.path.exists('plots/cutflow')):
	os.mkdir('plots/cutflow')

PlotStyle.setPlotStyle()

gStyle.SetPalette(1)
file = TFile.Open("./L1MuonHistogram.root")

countHistPrefix = 'hoMuonAnalyzer/count/'

hEvents = file.Get(countHistPrefix + 'Events_Count')
print hEvents
hL1Present = file.Get(countHistPrefix + 'L1MuonPresent_Count')
print hL1Present
hL1InGA = file.Get(countHistPrefix + 'L1MuonInGA_L1Dir_Count')
print hL1InGA
hL13x3 = file.Get(countHistPrefix + 'L1Muon3x3_Count')
print hL13x3
hL1Central = file.Get(countHistPrefix + 'L1MuonCentral_Count')
print hL1Central

histList = [#hEvents,
		hL1Present,hL1InGA,hL13x3,hL1Central]

yValues = []

for hist in histList:
	yValues.append(hist.GetBinContent(2))
	
xLabels = [
#		'Events',
		'L1 Present',
		'In GA',
		'Hit in 3x3',
		'Hit in Central'
		]

norm = yValues[0]
for i,v in enumerate(yValues):
		yValues[i] = v/norm

c = TCanvas('cutflowCanvas','PostLS1 Single #mu gun',1200,1200)

hist = TH1D("cutflow","PostLS1 Single #mu gun, L1 object information",len(xLabels),0,len(xLabels))
for i,v in enumerate(xLabels):
	hist.SetBinContent(i+1,yValues[i])
	hist.GetXaxis().SetBinLabel(i+1,str(v))
	
hist.SetStats(0)
hist.GetYaxis().SetTitle('rel. Fraction')
hist.GetYaxis().SetRangeUser(0,1.1)
hist.SetLineColor(PlotStyle.colorRwthDarkBlue)
hist.SetLabelFont(62)
hist.SetTitleFont(62)	
hist.Draw("")


histTrgCount = file.Get('hoMuonAnalyzer/count/L1_SingleMu3_Count')
hist2 = TH1D("l1TrgCount","PostLS1 Single #mu gun using L1",len(xLabels),0,len(xLabels))
hist2.SetBinContent(1,histTrgCount.GetBinContent(2)/norm)
hist2.SetFillStyle(3002)
hist2.SetFillColor(PlotStyle.colorRwthMagenta)
hist2.SetLineColor(PlotStyle.colorRwthMagenta)
hist2.Draw("same")

paveText = TPaveText(0.51,0.1,0.9,0.3,'NDC')
paveText.AddText('%s: %.2f%% #pm %.2f%%' % (xLabels[1],yValues[1]*100,calcSigma(yValues[1]*norm,norm)*100))
paveText.AddText('%s: %.2f%% #pm %.2f%%' % (xLabels[2],yValues[2]*100,calcSigma(yValues[2]*norm,norm)*100))
paveText.AddText('%s: %.2f%% #pm %.2f%%' % (xLabels[3],yValues[3]*100,calcSigma(yValues[3]*norm,norm)*100))
#paveText.AddText('%s: %.2f%% #pm %.2f%%' % (xLabels[4],yValues[4]*100,calcSigma(yValues[4]*norm,norm)*100))
paveText.SetBorderSize(1)
paveText.Draw()

paveText2 = TPaveText(0.51,0.3,0.9,0.4,'NDC')
paveText2.AddText('Total Events: %d' % (hEvents.GetBinContent(2)))
paveText2.AddText('Events with L1 in GA: %d' % (hL1InGA.GetBinContent(2)))
paveText2.SetBorderSize(1)
paveText2.Draw()

legend = TLegend(0.51,0.85,0.9,0.9)
legend.AddEntry(hist2,"Fraction with L1 Single #mu Trg.","f")
legend.Draw()

PlotStyle.labelCmsPrivateSimulation.Draw()


c.SaveAs("plots/cutflow/cutflowL1Info.pdf")

canv = TCanvas()
histPt = file.Get('hoMuonAnalyzer/L1MuonPresent_Pt')

histPt.Scale(1/histPt.Integral(),"width")
histPt.GetYaxis().SetTitle('')
histPt.Draw()

from plotEfficiency import plotEfficiencyPerHoTiles
c2 = plotEfficiencyPerHoTiles('L1Muon',0)
raw_input('--> Enter')
