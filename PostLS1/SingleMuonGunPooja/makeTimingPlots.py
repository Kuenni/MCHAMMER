import os,sys
from math import sqrt
sys.path.append(os.path.abspath("../../python"))

from ROOT import TCanvas,ROOT,TFile,TLegend,TF1,TLine,gROOT,TPaveText,TH1D,THStack,Double

DEBUG = 1

gROOT.Reset()

import PlotStyle
PlotStyle.setPlotStyle()

def calcSigma(num,denom):
	return sqrt(num/(denom*denom) + num*num/(pow(denom, 3)))

if( not os.path.exists('plots')):
	os.mkdir('plots')
if( not os.path.exists('plots/timing')):
	os.mkdir('plots/timing')

# Plot the delta timing distribution for Ho
# and the L1MuonObject
filename = 'L1MuonHistogram.root'
if(DEBUG):
	print 'Opening file:',filename
file = TFile.Open(filename)
if(file == None):
	print 'Error opening file:',filename

hDeltaTAllHo = file.Get('hoMuonAnalyzer/L1MuonPresentHoMatch_DeltaTime')
hDeltaTCleanHo = file.Get('hoMuonAnalyzer/L1MuonAboveThr_DeltaTime')

c = TCanvas("c","Delta Time",1200,1200)
c.SetLogy()

hDeltaTAllHo.SetLineColor(ROOT.kBlue)
hDeltaTAllHo.SetLineWidth(3)
hDeltaTAllHo.SetFillColor(ROOT.kBlue)
hDeltaTAllHo.SetFillStyle(3017)
hDeltaTAllHo.SetTitle("#Delta time")
hDeltaTAllHo.SetStats(0)

hDeltaTCleanHo.SetLineColor(8)
hDeltaTCleanHo.SetFillColor(8)
hDeltaTCleanHo.SetLineWidth(3)
hDeltaTCleanHo.SetFillStyle(3002)

#hDeltaTAllHo.Scale(1/hDeltaTAllHo.Integral())
#hDeltaTCleanHo.Scale(1/hDeltaTCleanHo.Integral())

print hDeltaTCleanHo.Integral(),hDeltaTAllHo.Integral()

fitFirstMin = TF1("fitFirstMin","[0]+x*[1]+[2]*x**2")
fitSecondMin = TF1("fitsecondMin","[0]+x*[1]+[2]*x**2",10,20)

hDeltaTCleanHo.Fit(fitFirstMin,"+q","",-20,-10)
hDeltaTCleanHo.Fit(fitSecondMin,"R+q","")

hDeltaTAllHo.Draw()
legend = TLegend(0.6,0.75,0.9,0.9)
legend.AddEntry(hDeltaTAllHo,"L1Muon matched to any HO","le")
legend.Draw()

label = PlotStyle.getLabelCmsPrivateSimulation()
label.Draw()
c.Update()

c.SaveAs("plots/timing/deltaTimeAllHo.png")
c.SaveAs("plots/timing/deltaTimeAllHo.pdf")

hDeltaTCleanHo.Draw('same')

fitFirstMin.SetRange(-50,50)
fitSecondMin.SetRange(-50,50)

#fitFirstMin.Draw('lSame')
#fitSecondMin.Draw('lSame')

lineFirstMin = TLine(fitFirstMin.GetMinimumX(-20,-10),hDeltaTAllHo.GetMinimum(),fitFirstMin.GetMinimumX(-20,-10),hDeltaTAllHo.GetMaximum())
lineFirstMin.SetLineWidth(3)
lineFirstMin.SetLineColor(ROOT.kRed)
lineFirstMin.Draw()

lineSecondMin = TLine(fitSecondMin.GetMinimumX(10,20),hDeltaTAllHo.GetMinimum(),fitSecondMin.GetMinimumX(10,20),hDeltaTAllHo.GetMaximum())
lineSecondMin.SetLineWidth(3)
lineSecondMin.SetLineColor(ROOT.kRed)
lineSecondMin.Draw()


legend.AddEntry(hDeltaTCleanHo,"L1Muon matched to HO > 0.2 GeV","le")
legend.AddEntry(lineFirstMin,"Integral boundaries","e")
legend.Draw()

integralCenter = hDeltaTCleanHo.Integral(hDeltaTCleanHo.FindBin(fitFirstMin.GetMinimumX(-20,-10)),hDeltaTCleanHo.FindBin(fitSecondMin.GetMinimumX(10,20)))
integralCenterAll = hDeltaTAllHo.Integral(hDeltaTAllHo.FindBin(fitFirstMin.GetMinimumX(-20,-10)),hDeltaTAllHo.FindBin(fitSecondMin.GetMinimumX(10,20)))
print 80*'#'
print 'Integral of center area in clean histogram :',integralCenter
print '==> %.2f%% +/- %.2f%%' % (integralCenter/hDeltaTCleanHo.Integral()*100,calcSigma(integralCenter, hDeltaTCleanHo.Integral())*100)
print 'Integral of center area in all matched HO events:',integralCenterAll
print '==> %.2f%% +/- %.2f%%' % (integralCenterAll/hDeltaTAllHo.Integral()*100,calcSigma(integralCenterAll, hDeltaTAllHo.Integral())*100)
print 80*'#'

paveText = TPaveText(0.6,0.7,0.9,0.75,'NDC')
paveText.AddText('%s' % ('Central peak contains (filtered hist.)'))
paveText.AddText('%.2f%% +/- %.2f%%' % (integralCenter/hDeltaTCleanHo.Integral()*100,calcSigma(integralCenter, hDeltaTCleanHo.Integral())*100))
paveText.SetBorderSize(1)
paveText.Draw()

label = PlotStyle.getLabelCmsPrivateSimulation()
label.Draw()
c.Update()


c.SaveAs("plots/timing/deltaTime.png")
c.SaveAs("plots/timing/deltaTime.pdf")

c2 = TCanvas("c2","BX ID",1200,1200)
c2.SetLogy()

hBxId = file.Get('hoMuonAnalyzer/L1MuonPresent_BxId')
hBxIdAboveThr = file.Get('hoMuonAnalyzer/L1MuonAboveThr_BxId')
hBxId.SetLineColor(PlotStyle.colorRwthDarkBlue)
hBxId.SetLineWidth(3)
hBxId.SetStats(0)
hBxId.SetTitle("BX ID distribution")
hBxId.GetXaxis().SetRangeUser(-2,5)
#hBxId.SetFillColor(PlotStyle.colorRwthDarkBlue)
#hBxId.SetFillStyle(3017)
hBxIdAboveThr.SetFillStyle(3002)
hBxIdAboveThr.SetFillColor(PlotStyle.colorRwthMagenta)
hBxIdAboveThr.SetLineColor(PlotStyle.colorRwthMagenta)
hBxIdAboveThr.SetLineWidth(2)

hBxId.Scale(1/hBxId.Integral())
hBxIdAboveThr.Scale(1/hBxIdAboveThr.Integral())

hBxId.GetYaxis().SetTitle("rel. fraction")

hBxId.Draw()
#hBxIdAboveThr.Draw("same")

legend2 = TLegend(0.45,0.8,0.9,0.9)
legend2.AddEntry(hBxId,"L1Muon","f")
#legend2.AddEntry(hBxIdAboveThr,"L1Muon matched to HO > 0.2 GeV","f")
legend2.Draw()

label = PlotStyle.getLabelCmsPrivateSimulation()
label.Draw()

c2.SaveAs("plots/timing/bxId.png")
c2.SaveAs("plots/timing/bxId.pdf")


c3 = TCanvas("c3","HO Time",1200,1200)
c3.Divide(1,2)
c3.cd(1)
hHoTime = file.Get('hoMuonAnalyzer/hoRecHits_Time')
hHoTimeAboveThr = file.Get('hoMuonAnalyzer/hoRecHitsAboveThr_Time')

hHoTime.SetStats(0)
hHoTime.SetTitle("Time distribution for all HO Rec Hits")
hHoTime.SetLineColor(PlotStyle.colorRwthDarkBlue)
hHoTime.SetLineWidth(3)
hHoTime.Draw()
label = PlotStyle.getLabelCmsPrivateSimulation()
label.Draw()

c3.cd(2)
hHoTimeAboveThr.SetStats(0)
hHoTimeAboveThr.SetTitle("Time distribution for HO Rec Hits > 0.2 GeV")
hHoTimeAboveThr.SetLineColor(PlotStyle.colorRwthDarkBlue)
hHoTimeAboveThr.SetLineWidth(3)
hHoTimeAboveThr.Draw()
label = PlotStyle.getLabelCmsPrivateSimulation()
label.Draw()

print 80*'#'
print 'Integral of HO > 0.2 GeV time histogram:'
print hHoTimeAboveThr.Integral()
print 80*'#'

fit = TF1("fit","gaus",-10,10)
hHoTimeAboveThr.Fit(fit)

pText = TPaveText(0.7,0.8,0.9,0.9,'NDC')
pText.AddText('Mean: %.2f ns' % (fit.GetParameter(1)))
pText.AddText('#sigma: %.2f ns' % (fit.GetParameter(2)))
pText.SetBorderSize(1)
pText.Draw()

c3.Update()
c3.SaveAs("plots/timing/hoTime.png")
c3.SaveAs("plots/timing/hoTime.pdf")

c4 = TCanvas("c4","BX L1Muon in ns",1200,1200)
c4.SetLogy()
hL1InNs = TH1D("hL1InNs","L1 Muon time in ns;time / ns;#",201,-100.5,100.5)
for i in range(0,hBxId.GetNbinsX()):
	x = hBxId.GetBinCenter(i)*25
	y = hBxId.GetBinContent(i)
	hL1InNs.SetBinContent(hL1InNs.FindBin(x),y)
hL1InNs.SetStats(0)
hL1InNs.Draw()
c4.SaveAs("plots/timing/timeL1Only.pdf")

##BX right plotting pt
canvasBxRightPt = TCanvas("cBxRightPt","cBxRightPt",1200,1200)
canvasBxRightPt.cd().SetLeftMargin(0.15)
hBxRightPt = file.Get('hoMuonAnalyzer/BxRightGenPt_Pt').Clone()
PlotStyle.setPlotStyle()
hBxRightPt.Rebin(50)
hBxRightPt.GetXaxis().SetRangeUser(0,200)
hBxRightPt.GetYaxis().SetTitle("normalized Entries / 5 GeV")
hBxRightPt.GetXaxis().SetTitle("p_{T} Gen")
hBxRightPt.GetYaxis().SetTitleOffset(2)
hBxRightPt.SetTitle("Events with right BX ID vs. p_{T}")
hBxRightPt.SetStats(0)
hBxRightPt.SetLineWidth(2)
hBxRightPt.Scale(1/hBxRightPt.Integral())
hBxRightPt.Draw()
label = PlotStyle.getLabelCmsPrivateSimulation()
label.Draw()
canvasBxRightPt.SaveAs('plots/timing/bxRightPt.pdf')

##BX wrong plotting pt
canvasBxWrongPt = TCanvas("cBxWrongPt","cBxWrongPt",1200,1200)
canvasBxWrongPt.cd().SetLeftMargin(0.15)
hBxWrongPt = file.Get('hoMuonAnalyzer/BxWrongGenPt_Pt').Clone()
PlotStyle.setPlotStyle()
hBxWrongPt.Rebin(50)
hBxWrongPt.GetXaxis().SetRangeUser(0,200)
hBxWrongPt.GetYaxis().SetTitle("normalized Entries / 5 GeV")
hBxWrongPt.GetXaxis().SetTitle("p_{T} Gen")
hBxWrongPt.GetYaxis().SetTitleOffset(2)
hBxWrongPt.SetTitle("Events with wrong BX ID vs. p_{T}")
hBxWrongPt.SetStats(0)
hBxWrongPt.SetLineWidth(2)
hBxWrongPt.Scale(1/hBxWrongPt.Integral())
hBxWrongPt.DrawCopy()
label = PlotStyle.getLabelCmsPrivateSimulation()
label.Draw()
canvasBxWrongPt.SaveAs('plots/timing/bxWrongPt.pdf')

#Plot the histogram stack
canvasStack = TCanvas("cStacked","cStacked",1200,1200)
canvasStack.cd().SetLeftMargin(0.15)
hWrong = file.Get('hoMuonAnalyzer/BxWrongGenPt_Pt')
hRight = file.Get('hoMuonAnalyzer/BxRightGenPt_Pt')
hRightFraction = TH1D('hRightFraction','',100,0,500)
hWrongFraction = TH1D('hWrongFraction','',100,0,500)
hWrong.Rebin(50)
hRight.Rebin(50)
#Fill the histograms with the bin wise fractions
for i in range(0,hRight.GetNbinsX()):
	nRight = hRight.GetBinContent(i+1)
	nWrong = hWrong.GetBinContent(i+1)
	if(nRight + nWrong == 0):
		continue
	hRightFraction.SetBinContent(i+1,nRight/(nRight+nWrong))
	hWrongFraction.SetBinContent(i+1,nWrong/(nRight+nWrong))

#Create the stack
stack = THStack("hstack","Fractions of events for BX ID correct and wrong")
nRight = hRight.Integral()
nWrong = hWrong.Integral()
nTotal = nRight + nWrong
hRightFraction.SetLineColor(PlotStyle.colorRwthDarkBlue)
hRightFraction.SetFillColor(PlotStyle.colorRwthDarkBlue)
hRightFraction.SetFillStyle(3002)
hWrongFraction.SetLineColor(PlotStyle.colorRwthMagenta)
hWrongFraction.SetFillColor(PlotStyle.colorRwthMagenta)
hWrongFraction.SetFillStyle(3002)
stack.Add(hRightFraction)
stack.Add(hWrongFraction)
stack.Draw()
stack.GetXaxis().SetRangeUser(0,201)
stack.GetYaxis().SetTitle('rel. fraction / 5 GeV')
stack.GetYaxis().SetTitleOffset(2)
stack.GetXaxis().SetTitle('p_{T} Gen')
stack.SetMinimum(0.9)
stack.SetMaximum(1)
legend = TLegend(0.6,0.75,0.9,0.9)
legend.AddEntry(hRightFraction,"BX ID right","f")
legend.AddEntry(hWrongFraction,"BX ID wrong","f")
legend.Draw()
label = PlotStyle.getLabelCmsPrivateSimulation()
label.Draw()
canvasStack.Update()
canvasStack.SaveAs('plots/timing/bxStacked.pdf')
canvasStack.SaveAs('plots/timing/bxStacked.root')

#Plot eta and phi of wrong bx ids
canvasEtaPhiBxWrong = TCanvas("canvasEtaPhiBxWrong","canvasEtaPhiBxWrong",1200,1200)

etaPhiBxWrongNC = file.Get("hoMuonAnalyzer/graphs/BxWrongGen")
etaPhiBxWrong = PlotStyle.convertToHcalCoords(etaPhiBxWrongNC)
etaPhiBxWrong.GetXaxis().SetTitle("i#eta / a.u.")
etaPhiBxWrong.GetYaxis().SetTitle("i#phi / a.u.")
etaPhiBxWrong.SetMarkerStyle(6)
etaPhiBxWrong.SetMarkerColor(PlotStyle.colorRwthDarkBlue)
etaPhiBxWrong.SetTitle("#eta #phi plot of events with BX ID wrong")
etaPhiBxWrong.Draw("AP")

pText = TPaveText(0.7,0.85,0.9,0.9,'NDC')
pText.AddText('Events with L1 objects: %d' % (nRight + nWrong))
pText.AddText('Events in Plot: %d' % (etaPhiBxWrong.GetN()))
pText.SetBorderSize(1)
pText.Draw()

chimney1Converted = PlotStyle.convertToHcalCoords(PlotStyle.chimney1)
chimney2Converted = PlotStyle.convertToHcalCoords(PlotStyle.chimney2)
chimney1Converted.SetLineColor(PlotStyle.colorRwthMagenta)
chimney2Converted.SetLineColor(PlotStyle.colorRwthMagenta)
chimney1Converted.Draw("same,l")
chimney2Converted.Draw("same,l")

labelCmsPrivateSimulation = PlotStyle.getLabelCmsPrivateSimulation()
labelCmsPrivateSimulation.Draw()

legend = TLegend(0.1,0.87,0.3,0.9)
legend.AddEntry(chimney2Converted,"chimney","l")
legend.Draw()

canvasEtaPhiBxWrong.Update()
canvasEtaPhiBxWrong.SaveAs("plots/timing/bxWrongEtaPhi.pdf")

#Make eta histogram of the graph before
canvasEtaBxWrong = TCanvas("canvasEtaBxWrong","canvasEtaBxWrong",1200,1200)
histEtaBxWrong = TH1D("histEtaBxWrong","histEtaBxWrong;p_{t} Gen;# Events",20,-0.8,0.8)
x = Double(0)
y = Double(0)
for i in range(0,etaPhiBxWrong.GetN()):
	etaPhiBxWrongNC.GetPoint(i,x,y)
	histEtaBxWrong.Fill(x)
histEtaBxWrong.Draw()
canvasEtaBxWrong.Update()
canvasEtaBxWrong.SaveAs("plots/timing/bxWrongEta.pdf")

raw_input('-->')
