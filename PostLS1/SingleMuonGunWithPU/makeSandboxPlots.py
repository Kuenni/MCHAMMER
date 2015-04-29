import os,sys
from math import sqrt
sys.path.append(os.path.abspath("../../python"))

from ROOT import TCanvas,ROOT,TFile,TLegend,TF1,TLine,gROOT,TPaveText,TH1D,Double,TH2D,THStack,gStyle

DEBUG = 1

gROOT.Reset()

import PlotStyle
PlotStyle.setPlotStyle()

def calcSigma(num,denom):
	return sqrt(num/float(denom*denom) + num*num/float(pow(denom, 3)))

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

def plotDigiTest():
	#Prepare canvas
	PlotStyle.setPlotStyle()
	canvas = TCanvas("canvasBxId","BXID",1200,1200)
	canvas.SetLogy()
	histBx = file.Get("hoMuonAnalyzer/hoDigi_BxId")
	histBx.GetXaxis().SetRangeUser(-3,3)
	histBx.SetLineWidth(3)
	histBx.Scale(1/histBx.Integral())
	histBx.SetStats(0)
	histBx.SetLineColor(PlotStyle.colorRwthDarkBlue)
	
	
	histBx.Draw('')	

	#Add label
	label = PlotStyle.getLabelCmsPrivateSimulation()
	label.Draw()
	
# 	#Add legend
# 	legend = TLegend(0.7,0.65,0.9,0.8)
# 	legend.AddEntry(histBx,"DT Only","l")
# 	legend.AddEntry(histNew,"DT shifted with HO","l")
# 	legend.SetBorderSize(1)
# 	legend.Draw()
	
# 	#Add text object
# 	pText = TPaveText(0.52,0.8,0.9,0.9,'NDC')
# 	pText.AddText('Fraction in BX ID 0: %6.3f%% #pm %6.3f%%' % (dtBx0/float(dtBxTotal)*100,calcSigma(dtBx0, dtBxTotal)))
# 	pText.AddText('Fraction in BX ID 0 (HO corr.): %6.3f%% #pm %6.3f%%' % (correctedRightFraction*100,calcSigma(correctedBxId0, correctedTotal)))
# 	pText.SetBorderSize(1)
# 	pText.SetFillColor(0)
# 	pText.Draw()
# 	
 	pText2 = TPaveText(0.7,0.85,0.9,0.9,'NDC')
 	pText2.AddText('Entries: %d' % (histBx.GetEntries()))
 	pText2.SetBorderSize(1)
 	pText2.SetFillColor(0)
 	pText2.Draw()
	
	canvas.Update()
	canvas.SaveAs('plots/timing/digiBxId.pdf')
	canvas.SaveAs('plots/timing/digiBxId.png')

	canvasAdcSum = TCanvas("cavasAdcSum","ADC Sum",1200,1200)
	canvasAdcSum.SetLogy()
	histAdcSum = file.Get("hoMuonAnalyzer/hoDigiAdcSum_Multiplicity")
	histAdcSum.GetXaxis().SetRangeUser(-0.5,500)
	histAdcSum.GetXaxis().SetTitle('ADC counts')
	histAdcSum.GetYaxis().SetTitle('#')
	histAdcSum.SetLineWidth(3)
	histAdcSum.SetStats(0)
	histAdcSum.SetLineColor(PlotStyle.colorRwthDarkBlue)
	histAdcSum.Draw()
	canvasAdcSum.Update()
	canvasAdcSum.SaveAs('plots/timing/digiAdcSum.pdf')
	canvasAdcSum.SaveAs('plots/timing/digiAdcSum.png')

	canvasTS4 = TCanvas("cavasTS4","TS4",1200,1200)
	canvasTS4.SetLogy()
	histAdcTS4 = file.Get("hoMuonAnalyzer/hoDigiAdcTS4_Multiplicity")
	histAdcTS4.GetXaxis().SetRangeUser(-0.5,500)
	histAdcTS4.GetXaxis().SetTitle('ADC counts')
	histAdcTS4.GetYaxis().SetTitle('#')
	histAdcTS4.SetLineWidth(3)
	histAdcTS4.SetStats(0)
	histAdcTS4.SetLineColor(PlotStyle.colorRwthDarkBlue)
	histAdcTS4.Draw()
	canvasTS4.Update()
	canvasTS4.SaveAs('plots/timing/digiAdcTs4.pdf')
	canvasTS4.SaveAs('plots/timing/digiAdcTs4.png')

	print histAdcSum.Integral(histAdcSum.FindBin(17),histAdcSum.FindBin(500))

	return canvas, histBx,label,canvasAdcSum,histAdcSum,canvasTS4,histAdcTS4
	
res = plotDigiTest()

raw_input('-->')
