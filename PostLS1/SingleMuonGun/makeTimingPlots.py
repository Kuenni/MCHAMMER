import os,sys
from math import sqrt
sys.path.append(os.path.abspath("../../python"))

from ROOT import TCanvas,ROOT,TFile,TLegend,TF1,TLine,gROOT,TPaveText

DEBUG = 1

gROOT.Reset()

import PlotStyle
PlotStyle.setPlotStyle()

def calcSigma(num,denom):
	return sqrt(num/(denom*denom) + num*num/(pow(denom, 3)))

# Plot the delta timing distribution for Ho
# and the L1MuonObject
filename = 'L1MuonHistogram.root'
if(DEBUG):
	print 'Opening file:',filename
file = TFile.Open(filename)
if(file == None):
	print 'Error opening file:',filename

hDeltaTAllHo = file.Get('hoMuonAnalyzer/L1MuonPresentHoMatch_DeltaTime')
hDeltaTCleanHo = file.Get('hoMuonAnalyzer/L1MuonAboveThrInAccNotDead_DeltaTime')

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

fitFirstMin = TF1("fitFirstMin","[0]+x*[1]+[2]*x**2")
fitSecondMin = TF1("fitsecondMin","[0]+x*[1]+[2]*x**2",10,20)

hDeltaTCleanHo.Fit(fitFirstMin,"+q","",-20,-10)
hDeltaTCleanHo.Fit(fitSecondMin,"R+q","")

hDeltaTAllHo.Draw()
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

legend = TLegend(0.6,0.75,0.9,0.9)
legend.AddEntry(hDeltaTAllHo,"L1Muon matched to any HO","le")
legend.AddEntry(hDeltaTCleanHo,"L1Muon matched to filtered HO","le")
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

PlotStyle.labelCmsPrivateSimulation.Draw()

c.Update()


c.SaveAs("deltaTime.png")
c.SaveAs("deltaTime.pdf")

	