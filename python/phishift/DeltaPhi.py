import sys
from plotting.RootFileHandler import RootFileHandler
from plotting.PlotStyle import drawLabelCmsPrivateSimulation, setupAxes,\
	setupPalette
from plotting.Utils import setupEAvplot,fillGraphIn2DHist
from ROOT import TCanvas,TLine,TLegend,Double,TH2D
import math,os


if( not os.path.exists('plots')):
	os.mkdir('plots')
if( not os.path.exists('plots/averageEnergy')):
	os.mkdir('plots/averageEnergy')
	
L1_BIN = math.pi/72.

fileHandler = RootFileHandler(sys.argv[1])
fileHandler.printStatus()
def plotDeltaPhiVsL1Pt():
	canvas = TCanvas('cDeltaPhiVsL1Pt','DeltaPhiVsL1Pt',1200,1200)
	hist = fileHandler.getHistogram('hoMuonAnalyzer/correlation/shiftCheckDeltaPhiVsL1Pt')
	hist.Scale(1,'width')
	hist.Draw('colz')
	label = drawLabelCmsPrivateSimulation()
	canvas.Update()
	
	return canvas,hist,label

def plotDeltaPhiVsGenPt():
	canvas = TCanvas('cDeltaPhiVsGenPt','DeltaPhiVsGenPt',1200,1200)
	hist = fileHandler.getHistogram('hoMuonAnalyzer/correlation/shiftCheckDeltaPhiVsGenPt')
	hist.GetYaxis().SetRangeUser(-0.6,0.6)
	hist.Draw('colz')
	canvas.Update()
	
	setupPalette(hist)
	setupAxes(hist)
	
	label = drawLabelCmsPrivateSimulation()
	canvas.Update()
	
	return canvas,hist,label

def plotDeltaPhiVsL1Phi():
	canvas = TCanvas('cDeltaPhiVsL1Phi','DeltaPhiVsL1Phi',1200,1200)
	hist = fileHandler.getHistogram('hoMuonAnalyzer/correlation/shiftCheckDeltaPhiVsPhi')
	hist.GetYaxis().SetRangeUser(-1,1)
	hist.GetXaxis().SetRangeUser(-.5,.5)
	hist.GetXaxis().SetTitle('L1 #phi')
	hist.GetZaxis().SetTitle('#')
	hist.SetStats(0)
	hist.SetTitle('#Delta#phi vs. L1#phi')
	setupAxes(hist)

	hist.Draw('colz')
	phiBorderLines = []
	
	HO_BIN = math.pi/36.
	
	for i in range(-31,32):
		line = TLine(HO_BIN*i - HO_BIN/2.,-.6, HO_BIN*i - HO_BIN/2.,.6)
		line.SetLineWidth(2)
	#	line.Draw()
		phiBorderLines.append(line)
		
	legend = TLegend(0.6,0.8,0.9,0.85)
	legend.AddEntry(phiBorderLines[0],"HO Tile center","e")
	#legend.Draw()
	
	label = drawLabelCmsPrivateSimulation()
	canvas.Update()
	
	setupPalette(hist)
	
	canvas.Update()
	canvas.SaveAs('plots/deltaPhiVsL1Phi.pdf')
	
	return canvas,hist,label,phiBorderLines,legend
	
def plotDeltaPhiVsL1Eta():
	canvas = TCanvas('cDeltaPhiVsL1Eta','DeltaPhiVsL1Eta',1200,1200)
	hist = fileHandler.getHistogram('hoMuonAnalyzer/correlation/shiftCheckDeltaPhiVsL1Eta')
	hist.GetYaxis().SetRangeUser(-1,1)
	hist.GetXaxis().SetRangeUser(-.5,.5)
	hist.GetXaxis().SetTitle('L1 #eta')
	hist.GetZaxis().SetTitle('#')
	hist.SetStats(0)
	hist.SetTitle('#Delta#phi vs. L1#eta')
	hist.Draw('colz')
	
	label = drawLabelCmsPrivateSimulation()
	canvas.Update()
	
	setupAxes(hist)
	setupPalette(hist)
	
	canvas.Update()
	canvas.SaveAs('plots/deltaPhiVsL1Eta.pdf')
	
	return canvas,hist,label#,phiBorderLines,legend

def plotL1PhiVsHoPhi():
	canvas = TCanvas('cL1PhiVsHoPhi','L1PhiVsHoPhi',1200,1200)
	canvas.Divide(1,2)
	canvas.cd(1)
	graph = fileHandler.getGraph('hoMuonAnalyzer/correlation/l1PhiVsHoPhi')
	graph.SetTitle('L1 #phi vs. HO #phi;HO #phi;L1 #phi')
	graph.SetMarkerStyle(2)
	setupAxes(graph)
	graph.Draw('AP')
	canvas.Update()
	
	canvas.cd(2)
	halfbinwidth = L1_BIN/2.
	hist = TH2D('hL1PhiVsHoPhi','L1 Phi vs. iPhi',289, -math.pi - halfbinwidth,math.pi + halfbinwidth
			,289, -math.pi - halfbinwidth,math.pi + halfbinwidth)
	hist = fillGraphIn2DHist(graph, hist)
	hist.Draw('colz')
	canvas.Update()
	setupPalette(hist)
	canvas.Update()
	
	return canvas,graph,hist

def plotL1PhiVsHoIPhi():
	canvas = TCanvas('cL1PhiVsHoIPhi','L1PhiVsHoIPhi',1200,1200)
	canvas.Divide(1,2)
	canvas.cd(1)
	graph = fileHandler.getGraph('hoMuonAnalyzer/correlation/l1PhiVsHoIPhi')
	graph.SetTitle('L1 #phi vs. HO i#phi;HO i#phi;L1 #phi')
	graph.SetMarkerStyle(2)
	setupAxes(graph)
	graph.Draw('AP')
	canvas.Update()
	
	canvas.cd(2)
	
	halfbinwidth = L1_BIN/2.
	
	hist = TH2D('hL1PhiVsHoIPhi','L1 Phi vs. iPhi',73,0.5,72.5,289, -math.pi - halfbinwidth,math.pi + halfbinwidth)
	hist = fillGraphIn2DHist(graph, hist)
	hist.Draw('colz')
	
	canvas.Update()
	
	return canvas,graph,hist
	
def plotHoPhiVsHoIPhi():
	canvas = TCanvas('cHoPhiVsHoIPhi','HoPhiVsHoIPhi',1200,1200)
	graph = fileHandler.getGraph('hoMuonAnalyzer/correlation/hoPhiVsHoIPhi')
	graph.SetTitle('HO #phi vs. HO i#phi;HO i#phi;HO #phi')
	graph.SetMarkerStyle(2)
	setupAxes(graph)
	graph.Draw('AP')
	
	canvas.Update()
	
	return canvas,graph

def plotDeltaPhiHistogram():
	canvas = TCanvas('cDeltaPhi','Delta Phi',1200,1200)
	hist = fileHandler.getHistogram('hoMuonAnalyzer/histograms1D/deltaPhi')
	hist.Draw()
	
	label = drawLabelCmsPrivateSimulation()
	
	return hist,canvas,label

def plotEAveragePerWheel():
	canvas = TCanvas('cEAvPerWheel',"E Average per Wheel",1800,800)
	canvas.Divide(3,1)

	hM1Energy = fileHandler.getHistogram('hoMuonAnalyzer/averageEnergy/wh1m/averageEnergyAroundPoint_wh-1SummedEnergy')
	hM1Counter = fileHandler.getHistogram('hoMuonAnalyzer/averageEnergy/wh1m/averageEnergyAroundPoint_wh-1Counter')
	hM1Energy = setupEAvplot(hM1Energy, hM1Counter)
	hM1Energy.SetStats(0)

	h0Energy = fileHandler.getHistogram('hoMuonAnalyzer/averageEnergy/wh0/averageEnergyAroundPoint_wh0SummedEnergy')
	h0Counter = fileHandler.getHistogram('hoMuonAnalyzer/averageEnergy/wh0/averageEnergyAroundPoint_wh0Counter')
	h0Energy = setupEAvplot(h0Energy, h0Counter)
	h0Energy.SetStats(0)

	hP1Energy = fileHandler.getHistogram('hoMuonAnalyzer/averageEnergy/wh1p/averageEnergyAroundPoint_wh1SummedEnergy')
	hP1Counter = fileHandler.getHistogram('hoMuonAnalyzer/averageEnergy/wh1p/averageEnergyAroundPoint_wh1Counter')
	hP1Energy = setupEAvplot(hP1Energy, hP1Counter)
	hP1Energy.SetStats(0)

	canvas.cd(1).SetLogz()
	setupAxes(hM1Energy)
	hM1Energy.SetMaximum(1.2)
	hM1Energy.SetMinimum(5e-3)
	hM1Energy.Draw('colz')
	canvas.Update()
	setupPalette(hM1Energy)
	
	canvas.cd(2).SetLogz()
	setupAxes(h0Energy)
	h0Energy.SetMaximum(1.2)
	h0Energy.SetMinimum(5e-3)
	h0Energy.Draw('colz')
	#h0Counter.Draw('same,text')
	canvas.Update()
	setupPalette(h0Energy)
	
	canvas.cd(3).SetLogz()
	setupAxes(hP1Energy)
	hP1Energy.SetMaximum(1.2)
	hP1Energy.SetMinimum(5e-3)
	hP1Energy.Draw('colz')
	canvas.Update()
	setupPalette(hP1Energy)

	canvas.Update()
	
	canvas.SaveAs('plots/averageEnergy/eAveragePerWheel.pdf')
	
	return hM1Energy,canvas,h0Energy,hP1Energy,h0Counter

	
def plotEtaPhiForDeltaPhiOne():
	canvas = TCanvas("cEtaPhiDeltaPhiOne","Eta Phi For DPhi 1",1200,1200)
	graph = fileHandler.getGraph('hoMuonAnalyzer/graphs/averageEnergyDeltaPhi1')
		
	halfbinwidth = L1_BIN/2.
	hist = TH2D('hEtaPhiDeltaPhi1',"#eta#phi of #Delta#phi=1 evts.",93,-46*L1_BIN - halfbinwidth
			,46*L1_BIN + halfbinwidth,289, -math.pi - halfbinwidth,math.pi + halfbinwidth)
	
	x = Double(0)
	y = Double(0)
	
	for i in range(0,graph.GetN()):
		graph.GetPoint(i,x,y)
		hist.Fill(x,y)
	
	hist.SetStats(0)
	hist.GetXaxis().SetRangeUser(-1,1)
	hist.SetTitle(hist.GetTitle() + ';#eta;#phi;Entries')
	setupAxes(hist)
	hist.Draw('colz')
	canvas.Update()
	
	setupPalette(hist)
	
	canvas.Update()
	
	canvas.SaveAs('plots/etaPhiForDeltaPhiOne.pdf')
	
	return canvas,hist

def plotEtaPhiForAllL1():
	canvas = TCanvas("cEtaPhi","Eta Phi",1200,1200)
	canvas.Divide(2,1)
	graphAll = fileHandler.getGraph('hoMuonAnalyzer/graphs/L1Muon')
	graphWithHo = fileHandler.getGraph('hoMuonAnalyzer/graphs/L1Muon3x3')
			
	halfbinwidth = L1_BIN/2.
	histAll = TH2D('hEtaPhiAll',"#eta#phi for all L1",93,-46*L1_BIN - halfbinwidth
			,46*L1_BIN + halfbinwidth,289, -math.pi - halfbinwidth,math.pi + halfbinwidth)
	histWithHo = TH2D('hEtaPhiWithHO',"#eta#phi L1 + HO (3x3)",93,-46*L1_BIN - halfbinwidth
			,46*L1_BIN + halfbinwidth,289, -math.pi - halfbinwidth,math.pi + halfbinwidth)
	
	x = Double(0)
	y = Double(0)
	
	for i in range(0,graphAll.GetN()):
		graphAll.GetPoint(i,x,y)
		histAll.Fill(x,y)
		
	for i in range(0,graphWithHo.GetN()):
		graphWithHo.GetPoint(i,x,y)
		histWithHo.Fill(x,y)
	
	canvas.cd(1)
	histAll.SetStats(0)
	histAll.GetXaxis().SetRangeUser(-1,1)
	histAll.SetTitle(histAll.GetTitle() + ';#eta;#phi;Entries')
	setupAxes(histAll)
	histAll.Draw('colz')
	label1 = drawLabelCmsPrivateSimulation()
	canvas.Update()
	
	setupPalette(histAll)
	
	canvas.cd(2)
	histWithHo.SetStats(0)
	histWithHo.GetXaxis().SetRangeUser(-1,1)
	histWithHo.SetTitle(histWithHo.GetTitle() + ';#eta;#phi;Entries')
	setupAxes(histWithHo)
	histWithHo.Draw('colz')
	label2 = drawLabelCmsPrivateSimulation()
	
	canvas.Update()
	setupPalette(histWithHo)
	
	canvas.Update()
	
	canvas.SaveAs('plots/etaPhiForAllL1.pdf')
	
	return canvas,histAll,histWithHo,label1,label2

	