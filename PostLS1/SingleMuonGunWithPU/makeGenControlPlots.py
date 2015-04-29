from ROOT import TCanvas,TFile,ROOT,TPaveText,TGraph,TLegend,TMarker,TH1D,Double
import os,sys
sys.path.append(os.path.abspath("../../python"))

import PlotStyle

file = TFile.Open('L1MuonHistogram.root')

if( not os.path.exists('plots')):
	os.mkdir('plots')
if( not os.path.exists('plots/genControlPlots')):
	os.mkdir('plots/genControlPlots')

hTotalEvents = file.Get('hoMuonAnalyzer/count/Events_Count')
totalEvents = hTotalEvents.GetBinContent(2)

PlotStyle.setPlotStyle()

#make control plots of gen eta and phi
def plotGenEtaPhi():
	c = TCanvas("canvasGenEtaPhi","canvas Gen Eta Phi",1200,1200)
	graph = file.Get('hoMuonAnalyzer/graphs/gen')
	
	graph.SetMarkerColor(PlotStyle.colorRwthDarkBlue)
	graph.SetMarkerStyle(2)
	graph.GetXaxis().SetTitleFont(62)
	graph.GetYaxis().SetTitleFont(62)
	graph.GetYaxis().SetLabelFont(62)
	graph.GetYaxis().SetTitle('#phi')
	graph.GetXaxis().SetTitle('#eta')
	graph.SetTitle('#eta #phi distribution for GEN')
	graph.Draw('AP')
	
	#CMS label
	label = PlotStyle.getLabelCmsPrivateSimulation()
	label.Draw()

	pText = TPaveText(0.7,0.85,0.9,0.9,'NDC')
	pText.SetBorderSize(1)
	pText.AddText('Total Events: %d' % (totalEvents))
	pText.Draw()

	c.SaveAs('plots/genControlPlots/genEtaPhi.pdf')
	c.SaveAs('plots/genControlPlots/genEtaPhi.png')

	#Prepare histograms for eta and phi alone
	histPhi = TH1D('histGenPhi',"#phi GEN;#phi;#",80,-3.48,3.48)
	histEta = TH1D('histGenEta',"#eta GEN;#eta;#",40,-1.74,1.74)

	#Get the data from the graph
	x = Double(0)
	y = Double(0)
	for i in range(0,graph.GetN()):
		graph.GetPoint(i,x,y)
		histPhi.Fill(y)
		histEta.Fill(x)
		
	#Draw phi histogram
	cPhi = TCanvas("canvasGenPhi","canvas Gen Phi",1200,1200)
	histPhi.SetStats(0)
	histPhi.Draw()
	label.Draw()
	cPhi.SaveAs('plots/genControlPlots/genPhi.pdf')
	cPhi.SaveAs('plots/genControlPlots/genPhi.pdf')
	
	#Draw eta histogram
	cEta = TCanvas("canvasGenEta","canvas Gen Eta",1200,1200)
	histEta.SetStats(0)
	histEta.Draw()
	label.Draw()
	cEta.SaveAs('plots/genControlPlots/genEta.pdf')
	cEta.SaveAs('plots/genControlPlots/genEta.pdf')
	
	return c,graph,label,histEta,histPhi,cEta,cPhi,pText


def plotAllEventsInAcceptance():
	c = TCanvas("c","c",1200,1200)
	gTdmiInGa = file.Get("hoMuonAnalyzer/graphs/tdmiInGA")
	gTdmiInGa = PlotStyle.convertToHcalCoords(gTdmiInGa)
	gTdmiInGa.GetXaxis().SetTitle("i#eta / a.u.")
	gTdmiInGa.GetYaxis().SetTitle("i#phi / a.u.")
	gTdmiInGa.SetMarkerStyle(6)
	gTdmiInGa.SetMarkerColor(PlotStyle.colorRwthDarkBlue)
	gTdmiInGa.Draw("AP")
	
	pText = TPaveText(0.7,0.85,0.9,0.9,'NDC')
	pText.AddText('Total Events: %d' % (totalEvents))
	pText.AddText('Events in Plot: %d' % (gTdmiInGa.GetN()))
	pText.SetBorderSize(1)
	pText.Draw()
	
	chimney1 = PlotStyle.chimney1
	chimney2 = PlotStyle.chimney2
	
	chimney1Converted = PlotStyle.convertToHcalCoords(chimney1)
	chimney2Converted = PlotStyle.convertToHcalCoords(chimney2)
	chimney1Converted.SetLineColor(PlotStyle.colorRwthMagenta)
	chimney2Converted.SetLineColor(PlotStyle.colorRwthMagenta)
	chimney1Converted.Draw("same,l")
	chimney2Converted.Draw("same,l")
	
	labelCmsPrivateSimulation = PlotStyle.getLabelCmsPrivateSimulation()
	labelCmsPrivateSimulation.Draw()
	
	legend = TLegend(0.1,0.87,0.3,0.9)
	legend.AddEntry(chimney2Converted,"chimney","l")
	legend.Draw()
	
	c.Update()
	
	c.SaveAs("plots/graphsEtaPhi/gTdmiInGa.pdf")
	c.SaveAs("plots/graphsEtaPhi/gTdmiInGa.png")
	return c,chimney1Converted,chimney2Converted,gTdmiInGa,pText

def plotHoMatchFail():
	c2 = TCanvas("c2","c2",1200,1200)
	
	gNoTrgNoL1TdmiInGa = file.Get("hoMuonAnalyzer/graphs/NoTrgNoL1TdmiInGA")
	gNoTrgNoL1TdmiInGa.GetXaxis().SetTitle("#eta")
	gNoTrgNoL1TdmiInGa.GetYaxis().SetTitle("#phi")
	gNoTrgNoL1TdmiInGa.SetMarkerStyle(6)
	gNoTrgNoL1TdmiInGa.Draw("AP")
	chimney1 = PlotStyle.chimney1
	chimney2 = PlotStyle.chimney2
	chimney1.Draw("same,l")
	chimney2.Draw("same,l")
	pText3 = TPaveText(0.7,0.85,0.9,0.9,'NDC')
	pText3.AddText('Total Events: %d' % (totalEvents))
	pText3.AddText('Events in Plot: %d' % (gNoTrgNoL1TdmiInGa.GetN()))
	pText3.SetBorderSize(1)
	pText3.Draw()
	
	c2.SaveAs("plots/graphsEtaPhi/gNoTrgNoL1TdmiInGa.pdf")
	return c2,chimney1,chimney2,gNoTrgNoL1TdmiInGa,pText3

def plotHoMatchFailInHoCoords():
	c3 = TCanvas("c3","c3",1200,1200)
	  
	gHoMatchFail = file.Get("hoMuonAnalyzer/graphs/NoTrgHoMatchFail")
	gHoMatchFail.GetXaxis().SetTitle("#eta")
	gHoMatchFail.GetYaxis().SetTitle("#phi")
	gHoMatchFail.SetMarkerStyle(6)
	gHoMatchFail.Draw("AP")
	chimney1.Draw("same,l")
	chimney2.Draw("same,l")
	labelCmsPrivateSimulation.Draw()
	pText2 = TPaveText(0.7,0.85,0.9,0.9,'NDC')
	pText2.AddText('Total Events: %d' % (totalEvents))
	pText2.AddText('Events in Plot: %d' % (gHoMatchFail.GetN()))
	pText2.SetBorderSize(1)
	pText2.Draw()
	
	c3.SaveAs("plots/graphsEtaPhi/gHoMatchFail.pdf")

def plotNoL1AndTdmiInAcceptance():
	c4 = TCanvas("c4","c4",1200,1200)
	gNoTrgNoL1TdmiInGa = file.Get("hoMuonAnalyzer/graphs/NoTrgNoL1TdmiInGA")
	gConvertedToiEtaiPhi = PlotStyle.convertToHcalCoords(gNoTrgNoL1TdmiInGa)
	gConvertedToiEtaiPhi.SetTitle('No Single #mu Trg, in HO Acceptance')
	gConvertedToiEtaiPhi.SetMarkerColor(PlotStyle.colorRwthDarkBlue)
	gConvertedToiEtaiPhi.Draw("AP")
	chimney1 = PlotStyle.chimney1
	chimney2 = PlotStyle.chimney2
	chimney1Converted = PlotStyle.convertToHcalCoords(chimney1)
	chimney2Converted = PlotStyle.convertToHcalCoords(chimney2)
	chimney1Converted.SetLineColor(PlotStyle.colorRwthMagenta)
	chimney2Converted.SetLineColor(PlotStyle.colorRwthMagenta)
	chimney1Converted.Draw('Same,l')
	chimney2Converted.Draw('Same,l')
	legend = TLegend(0.7,0.85,0.9,0.9)
	legend.AddEntry(chimney2Converted,"chimneys","le")
	legend.Draw()
	
	label = PlotStyle.getLabelCmsPrivateSimulation()
	label.Draw()
	c4.Update()
	#boxes = PlotStyle.drawHcalBoxesHcalCoords(c4)
	c4.SaveAs("plots/graphsEtaPhi/gNoTrgNoL1TdmiInGaHocoords.pdf")
	c4.SaveAs("plots/graphsEtaPhi/gNoTrgNoL1TdmiInGaHocoords.png")
	return c4,legend,chimney1Converted,chimney2Converted,gConvertedToiEtaiPhi

    
def plotEventsInAcceptance():
	c = TCanvas("c","c",1200,1200)
	
	gTdmiInGaNotConverted = file.Get("hoMuonAnalyzer/graphs/tdmiInGaNotDead")
	gTdmiInGa = PlotStyle.convertToHcalCoords(gTdmiInGaNotConverted)
	gTdmiInGa.GetXaxis().SetTitle("i#eta")
	gTdmiInGa.GetYaxis().SetTitle("i#phi")
	gTdmiInGa.SetMarkerStyle(6)
	gTdmiInGa.SetMarkerColor(PlotStyle.colorRwthDarkBlue)
	gTdmiInGa.SetTitle("#eta #phi plot of HO geom. Acceptance and not dead channels")
	gTdmiInGa.Draw("AP")
	
	pText = TPaveText(0.7,0.85,0.9,0.9,'NDC')
	pText.AddText('Total Events: %d' % (totalEvents))
	pText.AddText('Events in Plot: %d' % (gTdmiInGa.GetN()))
	pText.SetBorderSize(1)
	pText.Draw()
	
	#Make chimneys and label
	chimney1 = PlotStyle.chimney1
	chimney2 = PlotStyle.chimney2
	chimney1Converted = PlotStyle.convertToHcalCoords(PlotStyle.chimney1)
	chimney2Converted = PlotStyle.convertToHcalCoords(PlotStyle.chimney2)
	chimney1Converted.SetLineColor(PlotStyle.colorRwthMagenta)
	chimney2Converted.SetLineColor(PlotStyle.colorRwthMagenta)
	labelCmsPrivateSimulation = PlotStyle.getLabelCmsPrivateSimulation()
	chimney1Converted.Draw("same,l")
	chimney2Converted.Draw("same,l")
	labelCmsPrivateSimulation.Draw()
	legend = TLegend(0.1,0.87,0.3,0.9)
	legend.AddEntry(chimney2Converted,"chimney","l")
	legend.Draw()
	c.Update()
	c.SaveAs("plots/graphsEtaPhi/gTdmiInGaNotDead.png")
	return c,legend,chimney1Converted,chimney2Converted,pText,gTdmiInGa

#####
# HO > 0.2 GeV; No Single Muon Trigger
#####
def plotHoAboveThr():
	c5 = TCanvas("c5","c5",1200,1200)
	
	noTrgTdmiAboveThrNotConverted = file.Get("hoMuonAnalyzer/graphs/NoTrgTdmiAboveThr")
	noTrgTdmiAboveThr = PlotStyle.convertToHcalCoords(noTrgTdmiAboveThrNotConverted)
	noTrgTdmiAboveThr.GetXaxis().SetTitle("i#eta / a.u.")
	noTrgTdmiAboveThr.GetYaxis().SetTitle("i#phi / a.u.")
	noTrgTdmiAboveThr.SetMarkerStyle(6)
	noTrgTdmiAboveThr.SetMarkerColor(PlotStyle.colorRwthDarkBlue)
	noTrgTdmiAboveThr.SetTitle("#eta #phi plot of HO > 0.2 GeV in no Single #mu Trg. events")
	noTrgTdmiAboveThr.Draw("AP")
	
	pText = TPaveText(0.7,0.85,0.9,0.9,'NDC')
	pText.AddText('No Single #mu in GA: %d' % (noSingleMuEventsInGa))
	pText.AddText('Events in Plot: %d' % (noTrgTdmiAboveThr.GetN()))
	pText.SetBorderSize(1)
	pText.Draw()
	
	#Get chimneys
	chimney1 = PlotStyle.chimney1
	chimney2 = PlotStyle.chimney2
	chimney1Converted = PlotStyle.convertToHcalCoords(PlotStyle.chimney1)
	chimney2Converted = PlotStyle.convertToHcalCoords(PlotStyle.chimney2)
	chimney1Converted.SetLineColor(PlotStyle.colorRwthMagenta)
	chimney2Converted.SetLineColor(PlotStyle.colorRwthMagenta)
	
	#Add label
	labelCmsPrivateSimulation = PlotStyle.getLabelCmsPrivateSimulation()
	chimney1Converted.Draw("same,l")
	chimney2Converted.Draw("same,l")
	labelCmsPrivateSimulation.Draw()
	legend = TLegend(0.1,0.87,0.3,0.9)
	legend.AddEntry(chimney2Converted,"chimney","l")
	legend.Draw()
	#c5.SetGridY(0)
	#c5.SetGridX(0)
	c5.Update()
	c5.SaveAs("plots/graphsEtaPhi/gNoTrgTdmiHoAboveThr.png")
	return c5, legend,chimney1Converted,chimney2Converted,pText,noTrgTdmiAboveThr

def plotFailedHoMatchesNoTrg():
	c = TCanvas("cFailedHoMatchesNoTrg","cFailedHoMatchesNoTrg",1200,1200)
	c.cd().SetRightMargin(0.25)
	c.cd().SetLeftMargin(0.08)
	
	#legend
	legend = TLegend(0.75,0.8,0.99,0.9)
	
	#Graph for in events not in geometric acceptance
	grNotInGaNC = file.Get("hoMuonAnalyzer/graphs/NoTrgTdmiNotInGA")
	grNotInGa = PlotStyle.convertToHcalCoords(grNotInGaNC)
	grNotInGa.GetYaxis().SetTitle("i#phi / a.u.")
	grNotInGa.GetXaxis().SetTitle("i#eta / a.u.")
	grNotInGa.GetYaxis().SetTitleFont(62)
	grNotInGa.GetYaxis().SetLabelFont(62)
	grNotInGa.SetMarkerStyle(6)
	grNotInGa.SetMarkerColor(PlotStyle.colorRwthDarkBlue)
	grNotInGa.SetTitle("#eta #phi plot failed HO matches in no Single #mu Trg. events")
	grNotInGa.Draw("AP")
	
	#Graph of events with HO match below threshold
	grHoBelowThrNC = file.Get("hoMuonAnalyzer/graphs/NoTrgTdmiBelowThr")
	grHoBelowThr = PlotStyle.convertToHcalCoords(grHoBelowThrNC)
	grHoBelowThr.SetMarkerStyle(20)
	grHoBelowThr.SetMarkerSize(1.2)
	grHoBelowThr.SetMarkerColor( PlotStyle.colorRwthGruen )
	grHoBelowThr.Draw("samep")
	
	#Graph for events where HO matching failed
	grHoMatchFailNC = file.Get("hoMuonAnalyzer/graphs/NoTrgHoMatchFail")
	grHoMatchFail = None
	nNotMatching = 0
	if not grHoMatchFailNC == None:
		grHoMatchFail = PlotStyle.convertToHcalCoords(grHoMatchFailNC)
		grHoMatchFail.SetMarkerStyle(21)
		grHoMatchFail.SetMarkerSize(1)
		grHoMatchFail.SetMarkerColor( PlotStyle.colorRwthRot )
		grHoMatchFail.Draw("samep")
		legend.AddEntry(grHoMatchFail,'HO match fail','p')
		nNotMatching = grHoMatchFail.GetN()
	
	#Draw chimneys
	chimney1Converted = PlotStyle.convertToHcalCoords(PlotStyle.chimney1)
	chimney2Converted = PlotStyle.convertToHcalCoords(PlotStyle.chimney2)
	chimney1Converted.SetLineColor(PlotStyle.colorRwthMagenta)
	chimney2Converted.SetLineColor(PlotStyle.colorRwthMagenta)
	chimney1Converted.Draw('same')
	chimney2Converted.Draw('same')
	
	#cms private label
	label = TPaveText(PlotStyle.getLabelCmsPrivateSimulation(x1ndc=0.5,x2ndc=0.75))
	label.Draw()
	
	#create extra marker for the legend
	marker = TMarker(1,1,2)
	marker.SetMarkerSize(3)
	marker.SetMarkerColor(PlotStyle.colorRwthDarkBlue)

	legend.AddEntry(chimney2Converted,"chimney","l")
	legend.AddEntry(marker,'Not in GA','p')		
	legend.AddEntry(grHoBelowThr,'HO match < 0.2 GeV','p')
	legend.Draw()
	
	nNotInGa = grNotInGa.GetN()
	nBelowThr = grHoBelowThr.GetN()
	nTotal = nNotMatching + nNotInGa + nBelowThr
	
	print 80*'#'
	print 'Not Matching:\t%5d/%d\t=> %5.2f%% +- %f%%' % (nNotMatching,nTotal,nNotMatching/float(nTotal)*100,PlotStyle.calcSigma(nNotMatching,float(nTotal)))
	print 'Not in GA:\t%5d/%d\t=> %5.2f%% +- %f%%' % (nNotInGa,nTotal,nNotInGa/float(nTotal)*100,PlotStyle.calcSigma(nNotInGa,float(nTotal)))
	print 'Below Thr:\t%5d/%d\t=> %5.2f%% +- %f%%' % (nBelowThr,nTotal,nBelowThr/float(nTotal)*100,PlotStyle.calcSigma(nBelowThr,float(nTotal)))
	print 80*'#'
	
	c.Update()
	c.SaveAs('plots/graphsEtaPhi/gNoTrgHoMatchingFailed.png')
	c.SaveAs('plots/graphsEtaPhi/gNoTrgHoMatchingFailed.pdf')
	return c,grNotInGa,label,chimney1Converted,chimney2Converted,legend,grHoMatchFail,grHoBelowThr


res = plotGenEtaPhi()


raw_input('--> Enter')
