import os,sys
sys.path.append(os.path.abspath("/user/kuensken/ChrisAnelliCode/CMSSW_6_2_0_SLHC11/src/HoMuonTrigger/python"))

from ROOT import TFile, TCanvas, TH1D, TLegend, TPaveText

from plotEnergy import plotEnergyVsEtaPhi
from plotDeltaEtaDeltaPhi import plotDeltaEtaDeltaPhiEnergyProjection,plotDeltaEtaDeltaPhi

DEBUG = 1

import PlotStyle
PlotStyle.setPlotStyle()

def doPlotCutflow(filename='L1MuonHistogram.root'):
	
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
	
	#Counters with energy threshold
	tagThr1 = 'hoMuonAnalyzer/count/L1MuonAboveThr_Count'
	tagThr2 = 'hoMuonAnalyzer/count/L1MuonAboveThrInAcc_Count'
	tagThr3 = 'hoMuonAnalyzer/count/L1MuonAboveThrInAccNotDead_Count'
	
	histEvents = file.Get(tagEvents)
	histL1Muons = file.Get(tagL1Muons)

	histHo1 = file.Get(tagHo1)
	histHo2 = file.Get(tagHo2)
	histHo3 = file.Get(tagHo3)
	
	histThr1 = file.Get(tagThr1)
	histThr2 = file.Get(tagThr2)
	histThr3 = file.Get(tagThr3)

	yValues = [
#			histEvents.GetBinContent(2),
			histL1Muons.GetBinContent(2),
			histHo1.GetBinContent(2),
#			histHo2.GetBinContent(2),
#			histHo3.GetBinContent(2),
			histThr1.GetBinContent(2),
			histThr2.GetBinContent(2),
			histThr3.GetBinContent(2)
			]
	
	xLabels = [
	#		'Event count',
			'L1Muon objects',
			'HO match (No Thr.)',
			'+ HO match > 0.2 GeV',
			'+ HO acceptance'
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
	hist.GetYaxis().SetRangeUser(0.5,1.1
								)	
	hist.Draw("")

	paveText = TPaveText(0.51,0.75,0.9,0.9,'NDC')
	paveText.AddText('%s: %.2f%%' % (xLabels[2],yValues[2]*100))
	paveText.AddText('%s: %.2f%%' % (xLabels[3],yValues[3]*100))
	paveText.SetBorderSize(1)
	paveText.Draw()
	
	c.Update()
	c.SaveAs("cutflow.png")
	c.SaveAs("cutflow.pdf")
	c.SaveAs("cutflow.root")
	
	nTotal = histEvents.GetBinContent(2)
	nL1 = histL1Muons.GetBinContent(2)
	
	nL1AndHo 				= histHo1.GetBinContent(2),
#	nL1AndHoAcc				= histHo2.GetBinContent(2),
#	nL1AndHoAccNotDead		= histHo3.GetBinContent(2),
	nL1AndHoThr				= histThr1.GetBinContent(2),
	nL1AndHoThrAcc			= histThr2.GetBinContent(2),
	nL1AndHoThrAccNotDead	= histThr3.GetBinContent(2)
	
	print 'nEvents:\t%d' % (nTotal)
	print 'nL1:\t%d\t=>\t%.2f%%' % (nL1,nL1/nTotal*100)
	print '%s' % (20*'#')
	print 'L1AndHo:\t%d\t=>\t%.2f%%' % (nL1AndHo,nL1AndHo/nL1*100)
#	print 'L1AndHoAcc:\t%d\t=>\t%.2f%%' % (nL1AndHoAcc,nL1AndHo/nL1*100)
#	print 'L1AndHoAccNotDead:\t%d\t=>\t%.2f%%' % (nL1AndHoAccnotDead,nL1AndHo/nL1*100)
	print '%s' % (20*'#')
	print 'L1AndHoThr:\t%d\t=>\t%.2f%%' % (nL1AndHoThr,nL1AndHo/nL1*100)
	print 'L1AndHoThrAcc:\t%d\t=>\t%.2f%%' % (nL1AndHoThrAcc,nL1AndHo/nL1*100)
	print 'L1AndHoThrAccNotDead:\t%d\t=>\t%.2f%%' % (nL1AndHoThrAccNotDead,nL1AndHo/nL1*100)
											
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
	histoNames = ['L1MuonWithHoMatch_DeltaEtaDeltaPhi',
				'L1MuonWithHoMatchAboveThr_DeltaEtaDeltaPhi',
				'L1MuonWithHoMatchAboveThrFilt_DeltaEtaDeltaPhi',
				'NoSingleMu_DeltaEtaDeltaPhi',
				'NoSingleMuFilt_DeltaEtaDeltaPhi'
				]
	for s in histoNames:
		plotDeltaEtaDeltaPhi('.',sourceHistogram = s)

def doPlotEventCount(filename = 'L1MuonHistogram.root'):
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
	hist.GetYaxis().SetTitle('#')
#	hist.GetYaxis().SetRangeUser(0.5,1.1)	
	hist.Draw("")

	paveText = TPaveText(0.51,0.75,0.9,0.9,'NDC')
	paveText.AddText('%s: %d => %.2f%%' % (xLabels[0],yValues[0],yValues[0]/nEvents*100))
	paveText.AddText('%s: %d => %.2f%%' % (xLabels[1],yValues[1],yValues[1]/yValues[0]*100))
	paveText.SetBorderSize(1)
	paveText.Draw()
	c.Update()

	c.SaveAs("eventCount.png")
	c.SaveAs("eventCount.pdf")
	c.SaveAs("eventCount.root")

	return c,hist

def main(filename = 'L1MuonHistogram.root'):
	doPlotCutflow(filename)
	doPlotDeltaEtaDeltaPhi(filename)
	doPlotDeltaEtaDeltaPhiEnergy(filename)
	doPlotEventCount(filename)
	
if __name__ == '__main__':
	main()