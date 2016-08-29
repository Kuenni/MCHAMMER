from plotting.Plot import Plot
from plotting.PlotStyle import setupAxes,setupPalette
from plotting.Utils import fillGraphIn2DHist,L1_PHI_BIN,L1_ETA_BIN
from ROOT import TCanvas,TLine,TLegend,Double,TH2D
import math

class DeltaPhi(Plot):

	def __init__(self,filename,data = False,debug = False):
		Plot.__init__(self,filename,data,debug)
		self.createPlotSubdir('averageEnergy')
	
	def plotDeltaPhiVsL1Pt(self):
		canvas = TCanvas('cDeltaPhiVsL1Pt','DeltaPhiVsL1Pt',1200,1200)
		canvas.cd().SetLogz()
		hist = self.fileHandler.getHistogram('correlation/shiftCheckDeltaPhiVsL1PtL1MuonPresent')
		hist.Scale(1,'width')
		hist.SetStats(0)
		hist.GetYaxis().SetRangeUser(-0.6,.6)
		hist.GetZaxis().SetTitle('# entries')
		hist.Draw('colz')
		label = self.drawLabel()
		setupAxes(hist)
		canvas.Update()
		setupPalette(hist)
		canvas.Update()
		self.storeCanvas(canvas,'deltaPhiVsPt')
		return canvas,hist,label
	
	def plotDeltaPhiVsL1TightPt(self):
		canvas = TCanvas('cDeltaPhiVsL1TightPt','DeltaPhiVsL1TightPt',1200,1200)
		canvas.cd().SetLogz()
		hist = self.fileHandler.getHistogram('correlation/shiftCheckDeltaPhiVsL1PtpatTightToL1Muons')
		hist.Scale(1,'width')
		hist.SetTitle('#Delta#phi shift check, tight muons')
		hist.SetStats(0)
		hist.GetYaxis().SetRangeUser(-0.6,.6)
		hist.GetZaxis().SetTitle('# entries')
		hist.Draw('colz')
		label = self.drawLabel()
		setupAxes(hist)
		canvas.Update()
		setupPalette(hist)
		canvas.Update()
		self.storeCanvas(canvas,'deltaPhiVsPtL1Tight')
		return canvas,hist,label
	
	def plotDeltaPhiVsGenPt(self):
		canvas = TCanvas('cDeltaPhiVsGenPt','DeltaPhiVsGenPt',1200,1200)
		hist = self.fileHandler.getHistogram('correlation/shiftCheckDeltaPhiVsGenPt')
		hist.GetYaxis().SetRangeUser(-0.6,0.6)
		hist.Draw('colz')
		canvas.Update()
		
		setupPalette(hist)
		setupAxes(hist)
		
		label = self.drawLabel()
		canvas.Update()
		
		return canvas,hist,label
	
	def plotDeltaPhiVsL1Phi(self):
		canvas = TCanvas('cDeltaPhiVsL1Phi','DeltaPhiVsL1Phi',1200,1200)
		hist = self.fileHandler.getHistogram('correlation/shiftCheckDeltaPhiVsPhi')
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
		
		label = self.drawLabel()
		canvas.Update()
		
		setupPalette(hist)
		
		canvas.Update()
		canvas.SaveAs('plots/deltaPhiVsL1Phi.pdf')
		
		return canvas,hist,label,phiBorderLines,legend
		
	def plotDeltaPhiVsL1Eta(self):
		canvas = TCanvas('cDeltaPhiVsL1Eta','DeltaPhiVsL1Eta',1200,1200)
		hist = self.fileHandler.getHistogram('correlation/shiftCheckDeltaPhiVsL1Eta' + self.key)
		hist.GetYaxis().SetRangeUser(-1,1)
	#	hist.GetXaxis().SetRangeUser(-.5,.5)
		hist.GetXaxis().SetTitle('L1 #eta')
		hist.GetZaxis().SetTitle('#')
		hist.SetStats(0)
		hist.SetTitle('#Delta#phi vs. L1#eta')
		hist.Draw('colz')
		
		label = self.drawLabel()
		canvas.Update()
		
		setupAxes(hist)
		setupPalette(hist)
		
		canvas.Update()
		canvas.SaveAs('plots/deltaPhiVsL1Eta.pdf')
		
		return canvas,hist,label#,phiBorderLines,legend
	
	def plotL1PhiVsHoPhi(self):
		canvas = TCanvas('cL1PhiVsHoPhi','L1PhiVsHoPhi',1200,1200)
		canvas.Divide(1,2)
		canvas.cd(1)
		graph = self.fileHandler.getGraph('correlation/l1PhiVsHoPhi')
		graph.SetTitle('L1 #phi vs. HO #phi;HO #phi;L1 #phi')
		graph.SetMarkerStyle(2)
		setupAxes(graph)
		graph.Draw('AP')
		canvas.Update()
		
		canvas.cd(2)
		halfbinwidth = L1_PHI_BIN/2.
		hist = TH2D('hL1PhiVsHoPhi','L1 Phi vs. iPhi',289, -math.pi - halfbinwidth,math.pi + halfbinwidth
				,289, -math.pi - halfbinwidth,math.pi + halfbinwidth)
		hist = fillGraphIn2DHist(graph, hist)
		hist.Draw('colz')
		canvas.Update()
		setupPalette(hist)
		canvas.Update()
		
		return canvas,graph,hist
	
	def plotL1PhiVsHoIPhi(self):
		canvas = TCanvas('cL1PhiVsHoIPhi','L1PhiVsHoIPhi',1200,1200)
		canvas.Divide(1,2)
		canvas.cd(1)
		graph = self.fileHandler.getGraph('correlation/l1PhiVsHoIPhi')
		graph.SetTitle('L1 #phi vs. HO i#phi;HO i#phi;L1 #phi')
		graph.SetMarkerStyle(2)
		setupAxes(graph)
		graph.Draw('AP')
		canvas.Update()
		
		canvas.cd(2)
		
		halfbinwidth = L1_PHI_BIN/2.
		
		hist = TH2D('hL1PhiVsHoIPhi','L1 Phi vs. iPhi',73,0.5,72.5,289, -math.pi - halfbinwidth,math.pi + halfbinwidth)
		hist = fillGraphIn2DHist(graph, hist)
		hist.Draw('colz')
		
		canvas.Update()
		
		return canvas,graph,hist
		
	def plotHoPhiVsHoIPhi(self):
		canvas = TCanvas('cHoPhiVsHoIPhi','HoPhiVsHoIPhi',1200,1200)
		graph = self.fileHandler.getGraph('correlation/hoPhiVsHoIPhi')
		graph.SetTitle('HO #phi vs. HO i#phi;HO i#phi;HO #phi')
		graph.SetMarkerStyle(2)
		setupAxes(graph)
		graph.Draw('AP')
		
		canvas.Update()
		
		return canvas,graph
	
	def plotDeltaPhiHistogram(self):
		canvas = TCanvas('cDeltaPhi','Delta Phi',1200,1200)
		hist = self.fileHandler.getHistogram('histograms1D/deltaPhi' + self.key)
		hist.Draw()
		
		label = self.drawLabel()
		
		return hist,canvas,label
		
	def plotEtaPhiForDeltaPhiOne(self):
		canvas = TCanvas("cEtaPhiDeltaPhiOne","Eta Phi For DPhi 1",1200,1200)
		graph = self.fileHandler.getGraph('graphs/averageEnergyDeltaPhi1')
			
		halfbinwidth = L1_PHI_BIN/2.
		hist = TH2D('hEtaPhiDeltaPhi1',"#eta#phi of #Delta#phi=1 evts.",30,-15*L1_ETA_BIN	,15*L1_ETA_BIN,
				289, -math.pi - halfbinwidth,math.pi + halfbinwidth)
		
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
		
		label = self.drawLabel()
		
		canvas.Update()
		
		self.storeCanvas(canvas, 'etaPhiForDeltaPhiOne')
		canvas.SaveAs('plots/etaPhiForDeltaPhiOne.pdf')
		
		return canvas,hist,label
	
	def plotEtaPhiForAllL1(self):
		canvas = TCanvas("cEtaPhi","Eta Phi",1200,1200)
		canvas.Divide(2,1)
		graphAll = self.fileHandler.getGraph('graphs/L1MuonPresent')
		graphWithHo = self.fileHandler.getGraph('graphs/L1Muon3x3')
				
		halfPhiBinwidth = L1_PHI_BIN/2.
		halfEtaBinwidth = L1_ETA_BIN/2.
		
		histAll = TH2D('hEtaPhiAll',"#eta#phi for all L1",30,-15*L1_ETA_BIN	,15*L1_ETA_BIN,
					289, -math.pi - halfPhiBinwidth,math.pi + halfPhiBinwidth)
		histWithHo = TH2D('hEtaPhiWithHO',"#eta#phi L1 + HO (3x3)",30,-15*L1_ETA_BIN,15*L1_ETA_BIN,
					289, -math.pi - halfPhiBinwidth,math.pi + halfPhiBinwidth)
		
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
		label1 = self.drawLabel()
		canvas.Update()
		
		setupPalette(histAll)
		
		canvas.cd(2)
		histWithHo.SetStats(0)
		histWithHo.GetXaxis().SetRangeUser(-1,1)
		histWithHo.SetTitle(histWithHo.GetTitle() + ';#eta;#phi;Entries')
		setupAxes(histWithHo)
		histWithHo.Draw('colz')
		label2 = self.drawLabel()
		
		canvas.Update()
		setupPalette(histWithHo)
		
		canvas.Update()
		
		canvas.SaveAs('plots/etaPhiForAllL1.pdf')
		
		return canvas,histAll,histWithHo,label1,label2
	
		