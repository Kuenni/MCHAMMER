#!/usr/bin/python
import os,sys
from math import sqrt
from ROOT import TCanvas,ROOT,TFile,TLegend,TF1,TLine,gROOT,TPaveText,TH1D,Double,TH2D,THStack,gStyle

DEBUG = 1

gROOT.Reset()

from plotting.PlotStyle import setPlotStyle,getLabelCmsPrivateSimulation,getTH2D,calcSigma,setupAxes
setPlotStyle()

from plotting.RootFileHandler import RootFileHandler

if( not os.path.exists('plots')):
	os.mkdir('plots')
if( not os.path.exists('plots/timeCorrelation')):
	os.mkdir('plots/timeCorrelation')

if len(sys.argv) < 2:
	print 'First argument has to be the file name scheme!'
fileHandler = RootFileHandler(sys.argv[1])
fileHandler.printStatus()


#plot the timing correlation between HO and L1 in general
def plotHoL1Correlation():
	#Select whether matching to all HO should also be plotted
	plotBoth = True
	histAll = fileHandler.getHistogram('hoMuonAnalyzer/correlation/L1MuonPresentHoMatch_TimeCorrelation')
	histAboveThr = fileHandler.getHistogram('hoMuonAnalyzer/correlation/L1MuonAboveThr_TimeCorrelation')

	label = getLabelCmsPrivateSimulation()
	
	canvas = TCanvas("canvasHoL1Correlation","canvasHoL1Correlation",1600,1200)
	
	if(plotBoth):
		canvas.Divide(2,1)
		canvas.cd(1).SetLogz()
		
		histNew = getTH2D("histNew","Correlation between L1 BX ID and HO;HO time / ns;L1 / BX ID",5,-37.5,87.5#24,-56.25,93.75
						,5,-2.5,2.5)
		
		xAxis = histAll.GetXaxis()
		yAxis = histAll.GetYaxis()
		nBinsX = xAxis.GetNbins()
		nBinsY = yAxis.GetNbins()
		
		#Fill new histogram with fewer bins
		for i in range( 1 , nBinsX + 1 ):
			for j in range( 1 , nBinsY + 1 ):
				histNew.Fill(xAxis.GetBinCenter(i),yAxis.GetBinCenter(j)/25.,histAll.GetBinContent(i,j))
		histNew.SetStats(0)
		histNew.Draw('colz')
			
		canvas.Update()
		pal = histNew.GetListOfFunctions().FindObject("palette")
		pal.SetX2NDC(0.92)
		
		#Calcualte fraction at (0,0)
		nCentral = histNew.GetBinContent(histNew.FindBin(0,0))
		nTotal = histNew.Integral()

		fraction = nCentral/float(nTotal)
		fractionUncert = calcSigma(nCentral,nTotal)
		
		sliceFraction = 0
		for i in range(0,5):
			sliceFraction += histNew.GetBinContent(histNew.FindBin(0,-2.5+i))
		
		sliceFractionUncert = calcSigma(sliceFraction,nTotal)
		sliceFraction /= nTotal
		
		paveText = TPaveText(0.1,0.8,0.5,0.9,'NDC')
		paveText.AddText('Fraction at (0,0): %5.2f%% #pm %5.2f%%' % (fraction*100, fractionUncert*100))
		paveText.AddText('Fraction at (0,x): %5.2f%% #pm %5.2f%%' % (sliceFraction*100, sliceFractionUncert*100))
		paveText.SetBorderSize(1)
		paveText.Draw()
			
		label.Draw()
		
	canvas.cd(2).SetLogz()
	histAboveThr.SetStats(0)
	
	xAxis = histAboveThr.GetXaxis()
	yAxis = histAboveThr.GetYaxis()
	nBinsX = xAxis.GetNbins()
	nBinsY = yAxis.GetNbins()
	
	histNewAboveThr = getTH2D("histNewAboveThr","Correlation between L1 BX ID and HO > E_{Thr};HO time / ns;L1 / BX ID",5,-37.5,87.5#,12,-56.25,93.75
							,5,-2.5,2.5)
	for i in range( 1 , nBinsX + 1 ):
		for j in range( 1 , nBinsY + 1 ):
			histNewAboveThr.Fill(xAxis.GetBinCenter(i),yAxis.GetBinCenter(j)/25.,histAboveThr.GetBinContent(i,j))
	histNewAboveThr.SetStats(0)
	histNewAboveThr.Draw('colz')
	
	canvas.Update()
	pal = histNewAboveThr.GetListOfFunctions().FindObject("palette")
	pal.SetX2NDC(0.92)
	
	#Calcualte fraction at (0,0)
	nCentral = histNewAboveThr.GetBinContent(histNewAboveThr.FindBin(0,0))
	nTotal = histNewAboveThr.Integral()

	fraction = nCentral/float(nTotal)
	fractionUncert = calcSigma(nCentral,nTotal)

	sliceFraction = 0
	for i in range(0,5):
		sliceFraction += histNewAboveThr.GetBinContent(histNewAboveThr.FindBin(0,-2.5+i))
	
	sliceFractionUncert = calcSigma(sliceFraction,nTotal)
	sliceFraction /= nTotal
	
	paveTextAboveThr = TPaveText(0.1,0.8,0.5,0.9,'NDC')
	paveTextAboveThr.AddText('Fraction at (0,0): %5.2f%% #pm %5.2f%%' % (fraction*100, fractionUncert*100))
	paveTextAboveThr.AddText('Fraction at (0,x): %5.2f%% #pm %5.2f%%' % (sliceFraction*100, sliceFractionUncert*100))
	paveTextAboveThr.SetBorderSize(1)
	paveTextAboveThr.Draw()
	
	label.Draw()
	canvas.Update()
	
	canvas.SaveAs('plots/timeCorrelation/l1AndHoCorrelation.pdf')
	canvas.SaveAs('plots/timeCorrelation/l1AndHoCorrelation.png')

	return canvas,histAll,histAboveThr,label,histNewAboveThr, histNew,paveTextAboveThr

#Plot the correlation between Time slice and ADC value
def plotAdcTimeSliceCorrelation():
	hist = fileHandler.getHistogram('hoDigiAnalyzer/correlation/MaxTimeSliceVsAdc_Correlation')
	canvas = TCanvas('canvasTSvsADC',"ADC vs. TS",1200,1200)
	canvas.cd().SetLogz()
	hist.GetXaxis().SetRangeUser(-1,11)
	hist.GetYaxis().SetRangeUser(10,130)
	hist.SetTitle("Max ADC Value vs. Time Slice;Time slice ID;ADC")
	hist.SetStats(0)
	setupAxes(hist)
	hist.Draw('colz')
	
	canvas.Update()
	
	pal = hist.GetListOfFunctions().FindObject("palette")
	pal.SetX2NDC(0.92)
	
	label = getLabelCmsPrivateSimulation()
	label.Draw()
	
	canvas.SaveAs('plots/timeCorrelation/adcVsTs.pdf')
	canvas.SaveAs('plots/timeCorrelation/adcVsTs.png')
	
	return hist,canvas,label

def plotDtVsHo():
	hist =fileHandler.getHistogram('hoMuonAnalyzer/correlation/DtHoAboveThr_TimeCorrelation')
	canvas = TCanvas('canvasDtVsHo',"DT vs. HO",1200,1200)
	canvas.cd().SetLogz()

	histNew = getTH2D("histDtVsHo","DT BX ID vs. HO > E_{Thr};HO time / ns;BX ID",5,-37.5,87.5#24,-56.25,93.75
						,5,-2.5,2.5)
		
	xAxis = hist.GetXaxis()
	yAxis = hist.GetYaxis()
	nBinsX = xAxis.GetNbins()
	nBinsY = yAxis.GetNbins()
		
	#Fill new histogram with fewer bins
	for i in range( 1 , nBinsX + 1 ):
		for j in range( 1 , nBinsY + 1 ):
			histNew.Fill(xAxis.GetBinCenter(i),yAxis.GetBinCenter(j)/25.,hist.GetBinContent(i,j))

	histNew.SetStats(0)
	histNew.Draw('colz')
	
	canvas.Update()
	
	pal = histNew.GetListOfFunctions().FindObject("palette")
	pal.SetX2NDC(0.92)
	
	#Calcualte fraction at (0,0)
	nCentral = histNew.GetBinContent(histNew.FindBin(0,0))
	nTotal = histNew.Integral()

	fraction = nCentral/float(nTotal)
	fractionUncert = calcSigma(nCentral,nTotal)
	
	sliceFraction = 0
	for i in range(0,5):
		sliceFraction += histNew.GetBinContent(histNew.FindBin(0,-2.5+i))
	
	sliceFractionUncert = calcSigma(sliceFraction,nTotal)
	sliceFraction /= nTotal
	
	paveTextAboveThr = TPaveText(0.1,0.8,0.5,0.9,'NDC')
	paveTextAboveThr.AddText('Fraction at (0,0): %5.2f%% #pm %5.2f%%' % (fraction*100, fractionUncert*100))
	paveTextAboveThr.AddText('Fraction at (0,x): %5.2f%% #pm %5.2f%%' % (sliceFraction*100, sliceFractionUncert*100))
	paveTextAboveThr.SetBorderSize(1)
	paveTextAboveThr.Draw()
	
	label = getLabelCmsPrivateSimulation()
	label.Draw()
	
	canvas.SaveAs('plots/timeCorrelation/dtVsHo.pdf')
	canvas.SaveAs('plots/timeCorrelation/dtVsHo.png')
	
	return hist,canvas,paveTextAboveThr,label

def plotRpcVsHo():
	hist =fileHandler.getHistogram('hoMuonAnalyzer/correlation/RpcHoAboveThr_TimeCorrelation')
	canvas = TCanvas('canvasRpcVsHo',"RPC vs. HO",1200,1200)
	canvas.cd().SetLogz()

	histNew = getTH2D("histRpcVsHo","RPC BX ID vs. HO > E_{Thr};HO time / ns;BX ID",5,-37.5,87.5#24,-56.25,93.75
						,5,-2.5,2.5)
		
	xAxis = hist.GetXaxis()
	yAxis = hist.GetYaxis()
	nBinsX = xAxis.GetNbins()
	nBinsY = yAxis.GetNbins()
		
	#Fill new histogram with fewer bins
	for i in range( 1 , nBinsX + 1 ):
		for j in range( 1 , nBinsY + 1 ):
			histNew.Fill(xAxis.GetBinCenter(i),yAxis.GetBinCenter(j)/25.,hist.GetBinContent(i,j))

	histNew.SetStats(0)
	histNew.Draw('colz')
	
	canvas.Update()
	
	pal = histNew.GetListOfFunctions().FindObject("palette")
	pal.SetX2NDC(0.92)
	
	#Calcualte fraction at (0,0)
	nCentral = histNew.GetBinContent(histNew.FindBin(0,0))
	nTotal = histNew.Integral()

	fraction = nCentral/float(nTotal)
	fractionUncert = calcSigma(nCentral,nTotal)
	
	sliceFraction = 0
	for i in range(0,5):
		sliceFraction += histNew.GetBinContent(histNew.FindBin(0,-2.5+i))
	
	sliceFractionUncert = calcSigma(sliceFraction,nTotal)
	sliceFraction /= nTotal
	
	paveTextAboveThr = TPaveText(0.1,0.8,0.5,0.9,'NDC')
	paveTextAboveThr.AddText('Fraction at (0,0): %5.2f%% #pm %5.2f%%' % (fraction*100, fractionUncert*100))
	paveTextAboveThr.AddText('Fraction at (0,x): %5.2f%% #pm %5.2f%%' % (sliceFraction*100, sliceFractionUncert*100))
	paveTextAboveThr.SetBorderSize(1)
	paveTextAboveThr.Draw()
	
	label = getLabelCmsPrivateSimulation()
	label.Draw()
	
	canvas.SaveAs('plots/timeCorrelation/rpcVsHo.pdf')
	canvas.SaveAs('plots/timeCorrelation/rpcVsHo.png')
	
	return hist,canvas,paveTextAboveThr,label

def plotDigiEnergyVsTime():
	canvas = TCanvas()
	graph = fileHandler.getGraph('hoDigiAnalyzer/correlation/digiTimeVs4TSSum')
	graph.GetXaxis().SetTitle('Time / ns')
	graph.GetYaxis().SetTitle('ADC')
	graph.GetYaxis().SetRangeUser(0,200)
	graph.GetXaxis().SetRangeUser(-100,140)
	graph.SetMarkerStyle(2)
	graph.Draw('ap')
	canvas.Update()
	canvas.SaveAs('plots/timeCorrelation/adcVsTime.pdf')
	return graph,canvas

res = plotHoL1Correlation()
res2 = plotAdcTimeSliceCorrelation()
res3 = plotDtVsHo()
res4 = plotRpcVsHo()
res5 = plotDigiEnergyVsTime()

raw_input('-->')
