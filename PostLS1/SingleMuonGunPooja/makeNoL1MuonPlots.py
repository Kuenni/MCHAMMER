import os,sys
from math import sqrt
sys.path.append(os.path.abspath("../../python"))

from ROOT import TFile, TCanvas, TH1D, TLegend, TPaveText, THStack, TH2D, gStyle

from plotEnergy import plotEnergyVsEtaPhi
from plotDeltaEtaDeltaPhi import plotDeltaEtaDeltaPhiEnergyProjection,plotDeltaEtaDeltaPhi

DEBUG = 1

import PlotStyle
PlotStyle.setPlotStyle()

if( not os.path.exists('plots')):
	os.mkdir('plots')
if( not os.path.exists('plots/cutflow')):
	os.mkdir('plots/cutflow')

def calcSigma(num,denom):
	return sqrt(num/(denom*denom) + num*num/(pow(denom, 3)))

def doPlotCutflow(filename='L1MuonHistogram.root'):
	
	PlotStyle.setPlotStyle()
	
	if(DEBUG):
		print 'Opening file:',filename
	file = TFile.Open(filename)
	if(file == None):
		print 'Error opening file:',filename
	
	#Total event count
	tagEvents = 'hoMuonAnalyzer/count/Events_Count'	
	tagL1Muons = 'hoMuonAnalyzer/count/L1MuonPresent_Count'
	
	#Counters without energy threshold
	tagHo1 = 'hoMuonAnalyzer/count/L1MuonPresentHoMatch_Count'
	tagHo2 = 'hoMuonAnalyzer/count/L1MuonPresentHoMatchInAcc_Count'
	tagHo3 = 'hoMuonAnalyzer/count/L1MuonPresentHoMatchInAccNotDead_Count'
	tagHo4 = 'hoMuonAnalyzer/count/L1MuonPresentHoMatchInAccThr_Count'
	
	#Counters with energy threshold
	tagThr1 = 'hoMuonAnalyzer/count/L1MuonAboveThr_Count'
	tagThr2 = 'hoMuonAnalyzer/count/L1MuonAboveThrInAcc_Count'
	tagThr3 = 'hoMuonAnalyzer/count/L1MuonAboveThrInAccNotDead_Count'
	
	histEvents = file.Get(tagEvents)
	histL1Muons = file.Get(tagL1Muons)

	histHo1 = file.Get(tagHo1)
	histHo2 = file.Get(tagHo2)
	histHo3 = file.Get(tagHo3)
	histHo4 = file.Get(tagHo4)
	
	histThr1 = file.Get(tagThr1)
	histThr2 = file.Get(tagThr2)
	histThr3 = file.Get(tagThr3)

	yValues = [
			histEvents.GetBinContent(2),
			histL1Muons.GetBinContent(2),
			histHo1.GetBinContent(2),
#			histHo2.GetBinContent(2),
#			histHo3.GetBinContent(2),
			histThr1.GetBinContent(2),
			histThr2.GetBinContent(2),
			histThr3.GetBinContent(2)
			]
	
	xLabels = [
			'Event count',
			'L1Muon objects',
			'HO match (No Thr.)',
			'HO match > 0.2 GeV',
	#		'+ HO acceptance'
			]
	
	norm = yValues[0]
	for i,v in enumerate(yValues):
		yValues[i] = v/norm
	
	c = TCanvas('cutflowCanvas','PostLS1 Single #mu gun',1200,1200)

	hist = TH1D("cutflow","PostLS1 Single #mu gun",len(xLabels),0,len(xLabels))
	for i,v in enumerate(xLabels):
		hist.SetBinContent(i+1,yValues[i])
		hist.GetXaxis().SetBinLabel(i+1,str(v))
	
	hist.SetStats(0)
	hist.GetYaxis().SetTitle('rel. Fraction')
	hist.GetYaxis().SetRangeUser(0.7,1.1)
	hist.SetLineColor(PlotStyle.colorRwthDarkBlue)
	hist.SetLabelFont(62)
	hist.SetTitleFont(62)	
	hist.Draw("")

	histTrgCount = file.Get('hoMuonAnalyzer/count/L1_SingleMuOpen_Count')

	hist2 = TH1D("l1TrgCount","PostLS1 Single #mu gun",len(xLabels),0,len(xLabels))
	hist2.SetBinContent(1,histTrgCount.GetBinContent(2)/norm)
	hist2.SetFillStyle(3002)
	hist2.SetFillColor(PlotStyle.colorRwthMagenta)
	hist2.SetLineColor(PlotStyle.colorRwthMagenta)
	hist2.Draw("same")
	
	paveText = TPaveText(0.51,0.75,0.9,0.9,'NDC')
	paveText.AddText('%s: %.2f%% #pm %.2f%%' % (xLabels[1],yValues[1]*100,calcSigma(yValues[1]*norm,norm)*100))
	paveText.AddText('%s: %.2f%% #pm %.2f%%' % (xLabels[2],yValues[2]*100,calcSigma(yValues[2]*norm,norm)*100))
	paveText.AddText('%s: %.2f%% #pm %.2f%%' % (xLabels[3],yValues[3]*100,calcSigma(yValues[3]*norm,norm)*100))
	paveText.SetBorderSize(1)
	paveText.Draw()
	
	legend = TLegend(0.1,0.8,0.45,0.9)
	legend.AddEntry(hist2,"Fraction with L1 Single #mu Trg.","f")
	legend.Draw()
	
	label = PlotStyle.getLabelCmsPrivateSimulation()
	label.Draw()
	
	c.Update()
	c.SaveAs("plots/cutflow/cutflowL1.png")
	c.SaveAs("plots/cutflow/cutflowL1.pdf")
	c.SaveAs("plots/cutflow/cutflowL1.root")
	
	nTotal = histEvents.GetBinContent(2)
	nL1 = histL1Muons.GetBinContent(2)
	
	nL1AndHo 				= histHo1.GetBinContent(2)
	nL1AndHoAcc				= histHo2.GetBinContent(2)
	nL1AndHoAccNotDead		= histHo3.GetBinContent(2)
	nL1AndHoAccThr			= histHo4.GetBinContent(2)
	nL1AndHoThr				= histThr1.GetBinContent(2)
	nL1AndHoThrAcc			= histThr2.GetBinContent(2)
	nL1AndHoThrAccNotDead	= histThr3.GetBinContent(2)
	
	print '%s' % (80*'#')
	print '%s' % (80*'#')
	
	print '%25s%d' % ('nEvents:\t',nTotal)
	print '%25s%d\t=>\t%.2f%% +/- %.2f%%' % ('nL1:\t',nL1,nL1/nTotal*100,calcSigma(nL1, nTotal)*100)
	
	print '%s' % (80*'#')
	
	print '%25s%d\t=>\t%.2f%% +/- %.2f%%' % ('L1AndHo:\t',nL1AndHo,nL1AndHo/nL1*100,calcSigma(nL1AndHo, nL1)*100)
	print '%25s%d\t=>\t%.2f%% +/- %.2f%%' % ('L1AndHoAcc:\t',nL1AndHoAcc,nL1AndHoAcc/nL1*100,calcSigma(nL1AndHoAcc, nL1)*100)
	print '%25s%d\t=>\t%.2f%% +/- %.2f%%' % ('L1AndHoAccNotDead:\t',nL1AndHoAccNotDead,nL1AndHoAccNotDead/nL1*100,calcSigma(nL1AndHoAccNotDead, nL1)*100)
	print '%25s%d\t=>\t%.2f%% +/- %.2f%%' % ('L1AndHoAccThr:\t',nL1AndHoAccThr,nL1AndHoAccThr/nL1*100,calcSigma(nL1AndHoAccThr, nL1)*100)
	
	print '%s' % (80*'#')
	
	print '%25s%d\t=>\t%.2f%% +/- %.2f%%' % ('L1AndHoThr:\t',nL1AndHoThr,nL1AndHoThr/nL1*100,calcSigma(nL1AndHoThr, nL1)*100)
	print '%25s%d\t=>\t%.2f%% +/- %.2f%%' % ('L1AndHoThrAcc:\t',nL1AndHoThrAcc,nL1AndHoThrAcc/nL1*100,calcSigma(nL1AndHoThrAcc,nL1)*100)
	print '%25s%d\t=>\t%.2f%% +/- %.2f%%' % ('L1AndHoThrAccNotDead:\t',nL1AndHoThrAccNotDead,nL1AndHoThrAccNotDead/nL1*100,calcSigma(nL1AndHoThrAccNotDead, nL1)*100)
	
	print '%s' % (80*'#')
	print '%s' % (80*'#')
											
	return c

#Produce plots for different source histograms
def doPlotDeltaEtaDeltaPhiEnergy(filename = 'L1MuonHistogram.root'):
	histoNames = ['NoSingleMu_DeltaEtaDeltaPhiEnergy',
				'NoSingleMuAboveThr_DeltaEtaDeltaPhiEnergy',
				'NoSingleMuFilt_DeltaEtaDeltaPhiEnergy'
				]
	for s in histoNames:
		plotDeltaEtaDeltaPhiEnergyProjection('.',s)

#Produce plots for different source histograms	
def doPlotDeltaEtaDeltaPhi(filename = 'L1MuonHistogram.root'):
	histoNames = [
				'L1MuonWithHoMatch_DeltaEtaDeltaPhi',
				'L1MuonWithHoMatchAboveThr_DeltaEtaDeltaPhi',
				#'L1MuonWithHoMatchAboveThrFilt_DeltaEtaDeltaPhi',
				#'NoSingleMu_DeltaEtaDeltaPhi',
				#'NoSingleMuFilt_DeltaEtaDeltaPhi'
				'NoTrgTdmi_DeltaEtaDeltaPhi',
				'NoTrgTdmiAboveThr_DeltaEtaDeltaPhi'
				]
	for s in histoNames:
		plotDeltaEtaDeltaPhi('.',sourceHistogram = s)

def doPlotCutflowNoL1(filename = 'L1MuonHistogram.root'):
	if(DEBUG):
		print 'Opening file:',filename
	file = TFile.Open(filename)
	if(file == None):
		print 'Error opening file:',filename
	histoNames = [
				'hoMuonAnalyzer/count/NoSingleMu_Count',
				'hoMuonAnalyzer/count/NoSingleMuInGa_Count',
				'hoMuonAnalyzer/count/NoSingleMuInGa5x5_Count',
				'hoMuonAnalyzer/count/NoSingleMuInGa3x3_Count',
				'hoMuonAnalyzer/count/NoSingleMuInGaCentral_Count',
				'hoMuonAnalyzer/count/Events_Count'
				]
	
	histograms = []
	yValues = []
	
	for s in histoNames:
		histograms.append(file.Get(s))
		yValues.append(histograms[-1].GetBinContent(2))
	
	nEvents = histograms[-1].GetEntries()

	xLabels = [
	 		'No Single #mu trigger',
			'TDMI in GA',
			'HO > 0.2 GeV in 5x5',
			'HO > 0.2 GeV in 3x3',
			'HO > 0.2 GeV in Central'
			]
	
	c = TCanvas('eventCountCanvas','PostLS1 Single #mu gun',1200,1200)

	hist = TH1D("eventCount","PostLS1 Single #mu gun",len(xLabels)-1,0,len(xLabels))
	
	paveText = TPaveText(0.51,0.75,0.9,0.9,'NDC')
	paveText.AddText('%s: %d => %.2f%% #pm %.2f%%' % (xLabels[0],yValues[0],yValues[0]/nEvents*100,calcSigma(yValues[0], nEvents)*100))
	paveText.AddText('%s: %d => %.2f%% #pm %.2f%%' % (xLabels[2],yValues[2],yValues[2]/yValues[1]*100,calcSigma(yValues[2], yValues[1])*100))
	paveText.AddText('%s: %d => %.2f%% #pm %.2f%%' % (xLabels[4],yValues[4],yValues[4]/yValues[1]*100,calcSigma(yValues[4], yValues[1])*100))
	paveText.SetBorderSize(1)
	
	print yValues[1]
	
	norm = yValues[1]
	
	for i,v in enumerate(xLabels):
		if(i == 0):
			continue
		hist.SetBinContent(i,yValues[i]/norm)
		hist.GetXaxis().SetBinLabel(i,str(v))
	
	hist.SetStats(0)
	hist.SetLineColor(PlotStyle.colorRwthDarkBlue)
	hist.GetYaxis().SetTitle('#')
#	hist.GetYaxis().SetRangeUser(0.5,1.1)
	hist.SetLabelFont(62)
	hist.SetTitleFont(62)
	hist.SetMinimum(0)
	

	print yValues



	hist.Draw("")
	paveText.Draw()
	label = PlotStyle.getLabelCmsPrivateSimulation()
	label.Draw()
		
	c.Update()

	c.SaveAs("plots/cutflow/cutflowTdmiNoTrg.png")
	c.SaveAs("plots/cutflow/cutflowTdmiNoTrg.pdf")
	c.SaveAs("plots/cutflow/cutflowTdmiNoTrg.root")

	return c,hist

def doPlotGenPt(filename):
	PlotStyle.setPlotStyle()
	
	if(DEBUG):
		print 'Opening file:',filename
	file = TFile.Open(filename)
	if(file == None):
		print 'Error opening file:',filename

	c = TCanvas('genPtCanvas','Gen Pt no Single #mu trg',1200,1200)
	c.cd().SetLeftMargin(0.15)
	genPtHist = file.Get("hoMuonAnalyzer/NoSingleMu_Pt")
	genPtHist.SetLineColor(PlotStyle.colorRwthDarkBlue)
	genPtHist.SetLineWidth(3)
	genPtHist.Rebin(50)
	genPtHist.Sumw2()
	genPtHist.Scale(1/genPtHist.Integral())
	genPtHist.GetXaxis().SetRangeUser(0,200)
	genPtHist.GetYaxis().SetTitle('normalized entries / 5 GeV')
	genPtHist.GetYaxis().SetTitleOffset(2)
	genPtHist.GetXaxis().SetTitle('p_{T} Gen / GeV')
	label = PlotStyle.getLabelCmsPrivateSimulation()
	label.Draw()
	
	genPtHist.Draw("ehist")
	
	c.Update()
	
	stats = genPtHist.GetListOfFunctions().FindObject("stats")
	stats.SetOptStat(10)
	stats.SetX1NDC(.7)
	stats.SetX2NDC(.9)
	stats.SetY1NDC(.85)
	stats.SetY2NDC(.9)
	
	label = PlotStyle.getLabelCmsPrivateSimulation()
	label.Draw()
	
	c.SaveAs('plots/genPtNoSingleMuTrg.png')
	c.SaveAs('plots/genPtNoSingleMuTrg.pdf')
	
	return

def doPlotEtaPtOfFailingMatches():
	file = TFile.Open('L1MuonHistogram.root')
	#Prepare canvas
	canvas = TCanvas("canvasPtEtaHoMatchFail","PtEtaHoMatchFail",1200,1200)
	canvas.cd().Draw()
	#prepare histogram
	hist = file.Get("hoMuonAnalyzer/etaPhi/3D/NoTrgTdmiNotInGA_EtaPhiPt")

	stack = THStack(hist,"zx","2dStack","",1,21,1,201,"zx","")

	#Create new histogram and add the histograms from the stack
	histNew = TH2D("histPtEtaHoMatchFail","p_{T} vs. #eta distribution for events not in HO acceptance;#eta;p_{T} / 5 GeV;#",40,-1.6,1.6,40,0,200)
	histNew.GetYaxis().SetTitleOffset(1.2)
	for i in stack.GetHists():
		histNew.Add(i)

	gStyle.SetPalette(1)
	histNew.SetStats(0)
	histNew.Draw('COLZ')
	canvas.Update()

	palette = histNew.FindObject("palette")
	palette.SetX1NDC(0.9)
	palette.SetX2NDC(0.92)
	#add label
	label = PlotStyle.getLabelCmsPrivateSimulation()
	label.Draw()
	
	canvas.Update()
	canvas.SaveAs('plots/timing/NoL1NotInHoAcceptanceEtaPt.pdf')
	canvas.SaveAs('plots/timing/NoL1NotInHoAcceptanceEtaPt.png')
	return canvas,hist,stack,histNew,label,palette

def doPlotEtaPtOfSuccessfulMatches():
	file = TFile.Open('L1MuonHistogram.root')
	#Prepare canvas
	canvas = TCanvas("canvasPtEtaHoMatch","PtEtaHoMatch",1200,1200)
	canvas.cd().Draw()
	#prepare histogram
	hist = file.Get("hoMuonAnalyzer/etaPhi/3D/NoTrgTdmiAboveThr_EtaPhiPt")

	stack = THStack(hist,"zx","2dStack","",1,21,1,201,"zx","")

	#Create new histogram and add the histograms from the stack
	histNew = TH2D("histPtEtaHoMatch","p_{T} vs. #eta distribution;#eta;p_{T} / 5 GeV;#",40,-1.6,1.6,40,0,200)
	histNew.GetYaxis().SetTitleOffset(1.2)
	for i in stack.GetHists():
		histNew.Add(i)

	gStyle.SetPalette(1)
	histNew.SetStats(0)
	histNew.Draw('COLZ')
	canvas.Update()

	palette = histNew.FindObject("palette")
	palette.SetX1NDC(0.9)
	palette.SetX2NDC(0.92)
	#add label
	label = PlotStyle.getLabelCmsPrivateSimulation()
	label.Draw()
	
	canvas.Update()
	canvas.SaveAs('plots/timing/NoL1HoMatchEtaPt.pdf')
	canvas.SaveAs('plots/timing/NoL1HoMatchEtaPt.png')
	return canvas,hist,stack,histNew,label,palette

filename = 'L1MuonHistogram.root'
doPlotCutflow(filename)
doPlotDeltaEtaDeltaPhi(filename)
#	doPlotDeltaEtaDeltaPhiEnergy(filename)
doPlotCutflowNoL1(filename)
doPlotGenPt(filename)

file = TFile.Open(filename)
hist = file.Get("hoMuonAnalyzer/etaPhi/NoTrgTdmiAboveThr_DeltaEtaDeltaPhi")

nTotal = hist.Integral()
nCentral = hist.GetBinContent(hist.FindBin(0,0))
n3x3 = 0
n5x5 = 0

for i in range(-1,2):
	for j in range(-1,2):
		n3x3 += hist.GetBinContent(hist.FindBin(0.087*i,0.087*j))
		print hist.FindBin(0.087*i,0.087*j),0.087*i,0.087*j
for i in range(-2,3):
	for j in range(-2,3):
		n5x5 += hist.GetBinContent(hist.FindBin(0.087*i,0.087*j))

print '#'*80
print 'No Single Mu Trigger, TDMI Matched to HO > 0.2 GeV'
print 'Total Events:', nTotal
print 'Central bin\t%d ==> %.2f%% +/- %.2f%%' % (nCentral,nCentral/nTotal*100,calcSigma(nCentral, nTotal)*100)
print '3 x 3 bins\t%d ==> %.2f%% +/- %.2f%%' % (n3x3,n3x3/nTotal*100,calcSigma(n3x3, nTotal)*100)
print '5 x 5 bins\t%d ==> %.2f%% +/- %.2f%%' % (n5x5,n5x5/nTotal*100,calcSigma(n5x5, nTotal)*100)
print '#'*80

res = doPlotEtaPtOfFailingMatches()
res2 = doPlotEtaPtOfSuccessfulMatches()
raw_input('--> Enter')