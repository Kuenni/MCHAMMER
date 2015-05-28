import os,sys
from math import sqrt
sys.path.append(os.path.abspath("../../python"))

from ROOT import TCanvas,ROOT,TFile,TLegend,TF1,TLine,gROOT,TPaveText,TH1D,Double,TH2D,THStack,gStyle

DEBUG = 1

gROOT.Reset()

from PlotStyle import setPlotStyle,colorRwthDarkBlue,getLabelCmsPrivateSimulation,colorRwthTuerkis,colorRwthMagenta,setupAxes
setPlotStyle()

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
	canvas = TCanvas("canvasBxId","BXID",1200,1200)
	canvas.SetLogy()
	histBx = file.Get("hoMuonAnalyzer/hoDigi_BxId")
	histBx.GetXaxis().SetRangeUser(-3,3)
	histBx.SetLineWidth(3)
	histBx.Scale(1/histBx.Integral())
	histBx.SetStats(0)
	histBx.SetLineColor(colorRwthDarkBlue)
	
	
	histBx.Draw('')	

	#Add label
	label = getLabelCmsPrivateSimulation()
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
	histAdcSum.SetLineColor(colorRwthDarkBlue)
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
	histAdcTS4.SetLineColor(colorRwthDarkBlue)
	histAdcTS4.Draw()
	canvasTS4.Update()
	canvasTS4.SaveAs('plots/timing/digiAdcTs4.pdf')
	canvasTS4.SaveAs('plots/timing/digiAdcTs4.png')

	print histAdcSum.Integral(histAdcSum.FindBin(17),histAdcSum.FindBin(500))

	return canvas, histBx,label,canvasAdcSum,histAdcSum,canvasTS4,histAdcTS4
	
#Make the plots for the simple Digi time reconstruction
def plotDigiTime():
	canvas = TCanvas("canvasDigiSimpleTime","Simple Digi Time",1200,1200)
	canvas.SetLogy()
	
	histHoTime = file.Get('hoMuonAnalyzer/hoTimeFromDigi_Time')
	setupAxes(histHoTime)
	histHoTime.GetXaxis().SetTitle('time / ns')
	histHoTime.SetLineColor(colorRwthDarkBlue)
	histHoTime.SetStats(0)
	histHoTime.SetFillStyle(3004)
	histHoTime.SetFillColor(colorRwthDarkBlue)
	histHoTime.SetLineWidth(3)
	histHoTime.SetTitle('Simple time reconstruction from HO digi')
	histHoTime.Draw()
	
	#Label for CMS private
	label = getLabelCmsPrivateSimulation()
	label.Draw()

 	#Add legend
 	legend = TLegend(0.65,0.75,0.9,0.9)
 	legend.AddEntry(histHoTime,"All Digi times","f")
 	legend.Draw()

	canvas.Update()
	canvas.SaveAs('plots/timing/digiTimeAllHo.pdf')
	canvas.SaveAs('plots/timing/digiTimeAllHo.png')

	#Now add next plot
	histHoTimeAboveThr = file.Get('hoMuonAnalyzer/hoTimeFromDigiAboveThr_Time')
	histHoTimeAboveThr.SetLineColor(colorRwthTuerkis)
	histHoTimeAboveThr.SetStats(0)
	histHoTimeAboveThr.SetLineWidth(3)
	histHoTimeAboveThr.SetFillStyle(3005)
	histHoTimeAboveThr.SetFillColor(colorRwthTuerkis)
	histHoTimeAboveThr.Draw('same')
	
 	legend.AddEntry(histHoTimeAboveThr,"4 TS sum > E_{Thr}","f")
 	legend.Draw()
	
	canvas.Update()
	canvas.SaveAs('plots/timing/digiTimePlusThr.pdf')
	canvas.SaveAs('plots/timing/digiTimePlusThr.png')
	
	#Now add Ho rec hit time plot
	histHoRecHitTime = file.Get('hoMuonAnalyzer/hoRecHitsAboveThr_Time')
	histHoRecHitTime.SetLineColor(colorRwthMagenta)
	histHoRecHitTime.SetStats(0)
	histHoRecHitTime.SetLineWidth(3)

	histHoRecHitTime.Draw('same')
	
 	legend.AddEntry(histHoRecHitTime,"HO Rec Hit Time > E_{Thr}","l")
 	legend.Draw()
	
	canvas.Update()
	canvas.SaveAs('plots/timing/digiTimePlusRecHits.pdf')
	canvas.SaveAs('plots/timing/digiTimePlusRecHits.png')
	
	return canvas,label,histHoTime,legend,histHoTimeAboveThr,histHoRecHitTime

def plotDigiDeltaTime():
	canvas = TCanvas("canvasDigiDeltaTime","Simple Digi Delta Time",1200,1200)
	canvas.SetLogy()
	
	histHoTime = file.Get('hoMuonAnalyzer/hoTimeFromDigi_DeltaTime')
	setupAxes(histHoTime)
	histHoTime.GetXaxis().SetTitle('#Deltatime / ns')
	histHoTime.SetLineColor(colorRwthDarkBlue)
	histHoTime.SetStats(0)
	histHoTime.SetLineWidth(3)
	histHoTime.SetTitle('#DeltaTime of L1 and simple time reconstruction from HO digi')

	histHoTime.Draw()

	#Label for CMS private
	label = getLabelCmsPrivateSimulation()
	label.Draw()
	
	#Add legend
 	legend = TLegend(0.65,0.75,0.9,0.9)
 	legend.AddEntry(histHoTime,"L1 - Digi time","l")
 	legend.Draw()
	
	canvas.Update()
	canvas.SaveAs('plots/timing/digiTimeDeltaTime.pdf')
	canvas.SaveAs('plots/timing/digiTimeDeltaTime.png')
	
	histRecHitTime = file.Get('hoMuonAnalyzer/L1MuonAboveThr_DeltaTime')
	histRecHitTime.SetLineColor(colorRwthMagenta)
	histRecHitTime.SetLineWidth(3)
	histRecHitTime.Draw('same')
	
 	legend.AddEntry(histRecHitTime,"L1 - RecHit time","l")
 	legend.Draw()
	
	canvas.Update()
	canvas.SaveAs('plots/timing/digiTimeDeltaTimePlusRecHit.pdf')
	canvas.SaveAs('plots/timing/digiTimeDeltaTimePlusRecHit.png')
		
	return canvas,label, histHoTime,histRecHitTime,legend

# Study digi time vs eta
def plotDigiVsEta():

	canvas = TCanvas("canvasDigiEta","Simple Digi Eta",1200,1200)

	hoDigiTime = file.Get('hoMuonAnalyzer/correlation/hoTimeFromDigiEta')
	setupAxes(hoDigiTime)
	hoDigiTime.GetXaxis().SetTitle('#eta')
	hoDigiTime.GetYaxis().SetTitle('time / ns')
	hoDigiTime.GetYaxis().SetTitleOffset(1.4)
	hoDigiTime.SetMarkerStyle(5)
	hoDigiTime.SetMarkerColor(colorRwthDarkBlue)
	hoDigiTime.SetTitle('Simple time reco vs. #eta')
	hoDigiTime.Draw('ap')

	#Label for CMS private
	label = getLabelCmsPrivateSimulation()
	label.Draw()

	canvas.Update()
	
	canvas.SaveAs('plots/timing/digiTimeVsEta.png')
	
	return canvas,hoDigiTime,label

# Study digi time vs phi
def plotDigiVsPhi():

	canvas = TCanvas("canvasDigiPhi","Simple Digi Phi",1200,1200)

	hoDigiTime = file.Get('hoMuonAnalyzer/correlation/hoTimeFromDigiPhi')
	setupAxes(hoDigiTime)
	hoDigiTime.GetXaxis().SetTitle('#phi')
	hoDigiTime.GetYaxis().SetTitle('time / ns')
	hoDigiTime.GetYaxis().SetTitleOffset(1.4)
	hoDigiTime.SetMarkerStyle(5)
	hoDigiTime.SetMarkerColor(colorRwthDarkBlue)
	hoDigiTime.SetTitle('Simple time reco vs. #phi')
	hoDigiTime.Draw('ap')

	#Label for CMS private
	label = getLabelCmsPrivateSimulation()
	label.Draw()

	canvas.Update()
	
	canvas.SaveAs('plots/timing/digiTimeVsphi.png')
	
	return canvas,hoDigiTime,label

def plotRecHitVsDigiTime():
	canvas = TCanvas("canvasRecHitVsDigi","RecHitTime Vs Simple Digi",1200,1200)

	hoDigiTime = file.Get('hoMuonAnalyzer/correlation/hoTimeRecHitVsDigi')
	setupAxes(hoDigiTime)

	hoDigiTime.GetXaxis().SetTitle('digi time / ns')
	hoDigiTime.GetYaxis().SetTitle('rec hit time / ns')
	hoDigiTime.GetYaxis().SetTitleOffset(1.2)
	hoDigiTime.SetMarkerStyle(6)
	hoDigiTime.SetMarkerColor(colorRwthDarkBlue)
	hoDigiTime.SetTitle('HORecHit time vs. simple digi time estimation')
	hoDigiTime.Draw('ap')

	#Label for CMS private
	label = getLabelCmsPrivateSimulation()
	label.Draw()

	canvas.Update()
	
	canvas.SaveAs('plots/timing/digiTimeVsRecHitTime.png')

	return canvas, label, hoDigiTime

#res = plotDigiTest()
#res = plotDigiTime()
#res2 = plotDigiDeltaTime()
#res3 = plotDigiVsEta()
#res4 = plotDigiVsPhi()
res5 = plotRecHitVsDigiTime()
raw_input('-->')
