import os,sys
from math import sqrt
sys.path.append(os.path.abspath("../../python"))
import PlotStyle

from ROOT import TFile, TCanvas, TH1D, TLegend, TPaveText

DEBUG = 1

if( not os.path.exists('plots')):
	os.mkdir('plots')
if( not os.path.exists('plots/cutflow')):
	os.mkdir('plots/cutflow')

def calcSigma(num,denom):
	return sqrt(num/(denom*denom) + num*num/(pow(denom, 3)))

def doPlotCutflowTdmi(filename='L1MuonHistogram.root'):
	
	PlotStyle.setPlotStyle()
	
	if(DEBUG):
		print 'Opening file:',filename
	file = TFile.Open(filename)
	if(file == None):
		print 'Error opening file:',filename
	
	#Total event count
	tagEvents 	= 'hoMuonAnalyzer/count/Events_Count'	
	tagL1Muons 	= 'hoMuonAnalyzer/count/L1MuonPresent_Count'
	
	tagTdmiInGa 	= 'hoMuonAnalyzer/count/TdmiInGA_TdmiDir_Count'
	tagMatchIn3x3 = 'hoMuonAnalyzer/count/Tdmi3x3_Count'
	tagMatchInCentral = 'hoMuonAnalyzer/count/TdmiCentral_Count'
#	tagAboveThr		= 'hoMuonAnalyzer/count/SMuTrgL1AndHoAboveThr_Count'
	
	histEvents = file.Get(tagEvents)
	histL1Muons = file.Get(tagL1Muons)

	histTdmiInGa = file.Get(tagTdmiInGa)
	histFoundL1Match = file.Get(tagMatchIn3x3)
	histFoundHoMatch = file.Get(tagMatchInCentral)
#	histAboveThr = file.Get(tagAboveThr)

	yValues = [
#			histEvents.GetBinContent(2),
			histTdmiInGa.GetBinContent(2),
			histFoundL1Match.GetBinContent(2),
			histFoundHoMatch.GetBinContent(2),
#			histAboveThr.GetBinContent(2),
			]
	
	xLabels = [
#			'Event count',
			'Events with TDMI in Geom Acc.',
			'Hit in 3x3',
			'Hit in Central',
	#		'HO > 0.2 GeV'
			]
	
	norm = yValues[0]
	for i,v in enumerate(yValues):
		yValues[i] = v/norm
	
	c = TCanvas('cutflowCanvas','PostLS1 Single #mu gun',1200,1200)

	hist = TH1D("cutflow","PostLS1 Single #mu gun, using TDMI",len(xLabels),0,len(xLabels))
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

	hist2 = TH1D("l1TrgCount","PostLS1 Single #mu gun, using TDMI",len(xLabels),0,len(xLabels))
	hist2.SetBinContent(1,histTrgCount.GetBinContent(2)/norm)
	hist2.SetFillStyle(3002)
	hist2.SetFillColor(PlotStyle.colorRwthMagenta)
	hist2.SetLineColor(PlotStyle.colorRwthMagenta)
#	hist2.Draw("same")
	
	paveText = TPaveText(0.51,0.1,0.9,0.2,'NDC')
	paveText.AddText('%s: %.2f%% #pm %.2f%%' % (xLabels[1],yValues[1]*100,calcSigma(yValues[1]*norm,norm)*100))
	paveText.AddText('%s: %.2f%% #pm %.2f%%' % (xLabels[2],yValues[2]*100,calcSigma(yValues[2]*norm,norm)*100))
#	paveText.AddText('%s: %.2f%% #pm %.2f%%' % (xLabels[3],yValues[3]*100,calcSigma(yValues[3]*norm,norm)*100))
	paveText.SetBorderSize(1)
	paveText.Draw()
	
	paveText2 = TPaveText(0.51,0.2,0.9,0.3,'NDC')
	paveText2.AddText('Total Events: %d' % (histEvents.GetBinContent(2)))
	paveText2.AddText('Events in GA: %d' % (histTdmiInGa.GetBinContent(2)))
	paveText2.SetBorderSize(1)
	paveText2.Draw()
	
	legend = TLegend(0.51,0.85,0.9,0.9)
	legend.AddEntry(hist2,"Fraction with L1 Single #mu Trg.","f")
#	legend.Draw()
	
	PlotStyle.labelCmsPrivateSimulation.Draw()
	
	c.Update()
	c.SaveAs("plots/cutflow/cutflowTdmi.png")
	c.SaveAs("plots/cutflow/cutflowTdmi.pdf")
	c.SaveAs("plots/cutflow/cutflowTdmi.root")
	
	nTotal = histEvents.GetBinContent(2)
	nL1 = histL1Muons.GetBinContent(2)
	
# 	nL1AndHo 				= histHo1.GetBinContent(2)
# 	nL1AndHoAcc				= histHo2.GetBinContent(2)
# 	nL1AndHoAccNotDead		= histHo3.GetBinContent(2)
# 	nL1AndHoAccThr			= histHo4.GetBinContent(2)
# 	nL1AndHoThr				= histThr1.GetBinContent(2)
# 	nL1AndHoThrAcc			= histThr2.GetBinContent(2)
# 	nL1AndHoThrAccNotDead	= histThr3.GetBinContent(2)
# 	
# 	print '%s' % (80*'#')
# 	print '%s' % (80*'#')
# 	
# 	print '%25s%d' % ('nEvents:\t',nTotal)
# 	print '%25s%d\t=>\t%.2f%% +/- %.2f%%' % ('nL1:\t',nL1,nL1/nTotal*100,calcSigma(nL1, nTotal)*100)
# 	
# 	print '%s' % (80*'#')
# 	
# 	print '%25s%d\t=>\t%.2f%% +/- %.2f%%' % ('L1AndHo:\t',nL1AndHo,nL1AndHo/nL1*100,calcSigma(nL1AndHo, nL1)*100)
# 	print '%25s%d\t=>\t%.2f%% +/- %.2f%%' % ('L1AndHoAcc:\t',nL1AndHoAcc,nL1AndHoAcc/nL1*100,calcSigma(nL1AndHoAcc, nL1)*100)
# 	print '%25s%d\t=>\t%.2f%% +/- %.2f%%' % ('L1AndHoAccNotDead:\t',nL1AndHoAccNotDead,nL1AndHoAccNotDead/nL1*100,calcSigma(nL1AndHoAccNotDead, nL1)*100)
# 	print '%25s%d\t=>\t%.2f%% +/- %.2f%%' % ('L1AndHoAccThr:\t',nL1AndHoAccThr,nL1AndHoAccThr/nL1*100,calcSigma(nL1AndHoAccThr, nL1)*100)
# 	
# 	print '%s' % (80*'#')
# 	
# 	print '%25s%d\t=>\t%.2f%% +/- %.2f%%' % ('L1AndHoThr:\t',nL1AndHoThr,nL1AndHoThr/nL1*100,calcSigma(nL1AndHoThr, nL1)*100)
# 	print '%25s%d\t=>\t%.2f%% +/- %.2f%%' % ('L1AndHoThrAcc:\t',nL1AndHoThrAcc,nL1AndHoThrAcc/nL1*100,calcSigma(nL1AndHoThrAcc,nL1)*100)
# 	print '%25s%d\t=>\t%.2f%% +/- %.2f%%' % ('L1AndHoThrAccNotDead:\t',nL1AndHoThrAccNotDead,nL1AndHoThrAccNotDead/nL1*100,calcSigma(nL1AndHoThrAccNotDead, nL1)*100)
# 	
# 	print '%s' % (80*'#')
# 	print '%s' % (80*'#')
											
	return c,hist,hist2,legend,paveText,paveText2

def doPlotEventCountTdmi(filename = 'L1MuonHistogram.root'):
	if(DEBUG):
		print 'Opening file:',filename
	file = TFile.Open(filename)
	if(file == None):
		print 'Error opening file:',filename
	histoNames = [
				'hoMuonAnalyzer/L1_SingleMu3_Trig',
				'hoMuonAnalyzer/etaPhi/NoSingleMu_DeltaEtaDeltaPhi',
				'hoMuonAnalyzer/count/Events_Count'
				]
	
	histograms = []
	
	for s in histoNames:
		histograms.append(file.Get(s))

	yValues = []
	yValues.append(histograms[0].GetBinContent(1))
	yValues.append(histograms[1].GetEntries())

	nEvents = histograms[2].GetEntries()

	xLabels = [
			'No Single #mu trigger',
			'HO > 0.2 GeV matched to Gen'
			]
	
	c = TCanvas('eventCountCanvas','PostLS1 Single #mu gun',1200,1200)

	hist = TH1D("eventCount","PostLS1 Single #mu gun",len(xLabels),0,len(xLabels))
	for i,v in enumerate(xLabels):
		hist.SetBinContent(i+1,yValues[i])
		hist.GetXaxis().SetBinLabel(i+1,str(v))
	
	hist.SetStats(0)
	hist.SetLineColor(PlotStyle.colorRwthDarkBlue)
	hist.GetYaxis().SetTitle('#')
#	hist.GetYaxis().SetRangeUser(0.5,1.1)
	hist.SetLabelFont(62)
	hist.SetTitleFont(62)
	hist.SetMinimum(0)
	hist.Draw("")

	paveText = TPaveText(0.51,0.75,0.9,0.9,'NDC')
	paveText.AddText('%s: %d => %.2f%% #pm %.2f%%' % (xLabels[0],yValues[0],yValues[0]/nEvents*100,calcSigma(yValues[0], nEvents)*100))
	paveText.AddText('%s: %d => %.2f%% #pm %.2f%%' % (xLabels[1],yValues[1],yValues[1]/yValues[0]*100,calcSigma(yValues[1], yValues[0])*100))
	paveText.SetBorderSize(1)
	paveText.Draw()
	
	PlotStyle.labelCmsPrivateSimulation.Draw()
	
	c.Update()

	c.SaveAs("eventCount.png")
	c.SaveAs("eventCount.pdf")
	c.SaveAs("eventCount.root")

	return c,hist

def main(filename = 'L1MuonHistogram.root'):
	returnList = []
	returnList.append( doPlotCutflowTdmi(filename))
	returnList.append( doPlotEventCountTdmi(filename) )
	return returnList

if __name__ == '__main__':
	m = main()
	raw_input('--> Enter')