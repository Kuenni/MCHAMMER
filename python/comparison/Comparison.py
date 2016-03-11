from ROOT import TFile,TCanvas,TH1F,TPad
from plotting.PlotStyle import colorRwthDarkBlue, colorRwthMagenta,\
	drawLabelCmsPrivateData, setupAxes, colorRwthTuerkis,\
	colorRwthLila, colorRwthOrange
from plotting.Utils import getLegend,makeResidualsPad
from plotting.Plot import Plot

SIMULATION_FILE_SCHEME = '/user/kuensken/CMSSW/CMSSW_7_2_2_patch2/src/HoMuonTrigger/PostLS1/SingleMuonGunPooja/NoPUAnalyzed'
SIMULATION_PU_FILE_SCHEME = '/user/kuensken/CMSSW/CMSSW_7_2_2_patch2/src/HoMuonTrigger/PostLS1/SingleMuonGunWithPU/PU52Analyzed'
DATA_FILE_SCHEME = '/user/kuensken/CMSSW/CMSSW_7_4_15/src/HoMuonTrigger/PostLS1/collisionData2015/SingleMuon2015D'

class Comparison(Plot):
	#Initialize
	def __init__(self,data):
		Plot.__init__(self,data = data)
		self.createPlotSubdir('energyComparison')
		self.createPlotSubdir('l1CountComparison')
		self.fileHandlerSimulation = self.createFileHandler(SIMULATION_FILE_SCHEME)
		self.fileHandlerData = self.createFileHandler(DATA_FILE_SCHEME)
		self.fileHandlerSimulationPu = self.createFileHandler(SIMULATION_PU_FILE_SCHEME)
	
	def compareEnergyPerWheel(self):	

		namesHo = [
				'hoMuonAnalyzer/energy/perWheel/horeco_Energy_M1',
				'hoMuonAnalyzer/energy/perWheel/horeco_Energy_M0',
				'hoMuonAnalyzer/energy/perWheel/horeco_Energy_P0',
				'hoMuonAnalyzer/energy/perWheel/horeco_Energy_P1'
				]
		
		namesMatched = [
				'hoMuonAnalyzer/energy/perWheel/L1MuonWithHoMatchAboveThr_Energy_M1',
				'hoMuonAnalyzer/energy/perWheel/L1MuonWithHoMatchAboveThr_Energy_M0',
				'hoMuonAnalyzer/energy/perWheel/L1MuonWithHoMatchAboveThr_Energy_P0',
				'hoMuonAnalyzer/energy/perWheel/L1MuonWithHoMatchAboveThr_Energy_P1'
				]
				
		canvas = TCanvas('compareCanvas','comparison',1800,500)
		canvas.Divide(4,1)
		
		objectStorage = []
		
		for i in range (0,4):
			canvas.cd(i+1).SetLogy()
			
			hSimHo = self.fileHandlerSimulation.getHistogram(namesHo[i])
			hSimHo.SetLineColor(colorRwthDarkBlue)
			
			hSimMatch = self.fileHandlerSimulation.getHistogram(namesMatched[i])
			hSimMatch.SetLineColor(colorRwthDarkBlue)
			hSimMatch.SetLineStyle(7)
		
			hDataHo = self.fileHandlerData.getHistogram(namesHo[i])
			hDataHo.SetLineColor(colorRwthMagenta)
			
			hDataMatch = self.fileHandlerData.getHistogram(namesMatched[i])
			hDataMatch.SetLineColor(colorRwthMagenta)
			hDataMatch.SetLineStyle(7)
			
			hSimPuHo = self.fileHandlerSimulationPu.getHistogram(namesHo[i])
			hSimPuHo.SetLineColor(colorRwthTuerkis)
			
			hSimPuMatch = self.fileHandlerSimulationPu.getHistogram(namesMatched[i])
			hSimPuMatch.SetLineColor(colorRwthTuerkis)
			hSimPuMatch.SetLineStyle(7)
			
			hSimHo.Draw()
			hSimMatch.Draw('same')
			hDataHo.Draw('same')
			hDataMatch.Draw('same')
			hSimPuHo.Draw('same')
			hSimPuMatch.Draw('same')
			
			legend = getLegend(y1 =.6,y2=.9)
			legend.AddEntry(hSimHo,'Sim, HO Only','l').SetTextFont(62)
			legend.AddEntry(hSimMatch,'Sim, HO matched','l').SetTextFont(62)
			legend.AddEntry(hDataHo,'Data, HO Only','l').SetTextFont(62)
			legend.AddEntry(hDataMatch,'Data HO Matched','l').SetTextFont(62)
			legend.AddEntry(hSimPuHo,'Sim PU52, HO Only','l').SetTextFont(62)
			legend.AddEntry(hSimPuMatch,'Sim PU52 HO Matched','l').SetTextFont(62)
			legend.Draw()
			
			label = drawLabelCmsPrivateData()
			
			objectStorage.append([hSimHo,hSimMatch,hDataHo,hDataMatch,hSimPuHo,hSimPuMatch,legend,label])
		
		canvas.Update()
		canvas.SaveAs('plots/energyComparison/energyPerWheelDataAndSimNormed.gif')
	
		return canvas,objectStorage
	
	def buildTripleCanvasWithResiduals(self,hSimHo, hSimPuHo, hDataHo,canvasName = 'cTripleCanvas',legendPostix = 'HO Only',ylabel = '# entries'):
		canvas = TCanvas(canvasName,canvasName,1800,1000)
		canvas.Divide(3,1)
		##
		#	Sim No PU and Data
		##
		hSimHo.SetLineColor(colorRwthDarkBlue)
		hSimHo.SetStats(0)
		hSimHo.SetTitle('No PU and Data compared;E_{HO} / a.u.;' + ylabel)
		
		hDataHo.SetLineColor(colorRwthMagenta)
		hSimPuHo.SetLineColor(colorRwthTuerkis)
		
		pad1 = makeResidualsPad(canvas.cd(1))
		pad1.cd(1).SetLogy()
		pad1.cd(2).SetLogy()
		pad1.cd(1)
		hSimHo.Draw()
		hDataHo.DrawCopy('same')
		
		label = drawLabelCmsPrivateData()

		legend = getLegend(x1=.5,y1 = 0.75,y2=.9)
		legend.AddEntry(hSimHo,'Sim No PU, ' + legendPostix,'l')
		legend.AddEntry(hDataHo,'Data, ' + legendPostix,'l')
		legend.Draw()
		
		setupAxes(hSimHo)

		##
		#	Sim PU52 and Data
		##		
		pad2 = makeResidualsPad(canvas.cd(2))
		pad2.cd(1).SetLogy()
		pad2.cd(2).SetLogy()
		pad2.cd(1)
		setupAxes(hSimPuHo)
		hSimPuHo.SetStats(0)
		hSimPuHo.SetTitle('PU52 and Data compared;E_{HO} / a.u.;' + ylabel)
		hSimPuHo.DrawCopy('')
		hDataHo.DrawCopy('same')
		
		label2 = drawLabelCmsPrivateData()

		legend2 = getLegend(x1=.5,y1 = 0.75,y2=.9)
		legend2.AddEntry(hSimPuHo,'Sim PU52, ' + legendPostix,'l')
		legend2.AddEntry(hDataHo,'Data, ' + legendPostix,'l')
		legend2.Draw()
		
		##
		#	Sim No PU and Sim PU 52
		##
		pad3 = makeResidualsPad(canvas.cd(3))
		pad3.cd(1).SetLogy()
		pad3.cd(2).SetLogy()
		pad3.cd(1)
		hSimPuHo.SetStats(0)
		setupAxes(hSimPuHo)
		hSimPuHo.SetTitle('PU52 and No PU Simulation compared;E_{HO} / a.u.;' + ylabel)
		hSimPuHo.Draw('')
		hSimHo.DrawCopy('same')
		
		label3 = drawLabelCmsPrivateData()

		legend3 = getLegend(x1=.5,y1 = 0.75,y2=.9)
		legend3.AddEntry(hSimPuHo,'Sim PU52, ' + legendPostix,'l')
		legend3.AddEntry(hSimHo,'Sim No PU, ' + legendPostix,'l')
		legend3.Draw()
				
		#Do the ratio
		pad1.cd(2)
		cloneData = hSimHo.Clone('cloneData')
		cloneData.SetTitle(';E_{HO} / a.u.;Sim/Data')
		cloneData.Sumw2()
		setupAxes(cloneData)
		cloneData.GetYaxis().SetTitleSize(0.05)
		cloneData.GetYaxis().SetLabelSize(0.05)
		cloneData.GetXaxis().SetTitleSize(0.05)
		cloneData.GetXaxis().SetLabelSize(0.05)
		cloneData.GetYaxis().CenterTitle()
		cloneData.Divide(hDataHo)
		cloneData.SetLineWidth(1)
		cloneData.SetMarkerStyle(6)
		cloneData.SetMarkerColor(colorRwthMagenta)
		cloneData.SetLineColor(colorRwthMagenta)
		cloneData.Draw('ep')
		
		pad2.cd(2)
		clonePuAndData = hSimPuHo.Clone('clonePuAndData')
		setupAxes(clonePuAndData)
		clonePuAndData.GetYaxis().SetTitleSize(0.05)
		clonePuAndData.GetYaxis().SetLabelSize(0.05)
		clonePuAndData.GetXaxis().SetTitleSize(0.05)
		clonePuAndData.GetXaxis().SetLabelSize(0.05)
		clonePuAndData.GetYaxis().CenterTitle()
		clonePuAndData.SetTitle(';E_{HO} / a.u.;Sim/Data')
		clonePuAndData.Sumw2()
		clonePuAndData.Divide(hDataHo)
		clonePuAndData.SetLineWidth(1)
		clonePuAndData.SetMarkerStyle(6)
		clonePuAndData.SetMarkerColor(colorRwthTuerkis)
		clonePuAndData.SetLineColor(colorRwthTuerkis)
		clonePuAndData.Draw('ep')
		
		pad3.cd(2)
		clonePuAndNoPu = hSimHo.Clone('clonePuAndNoPu')
		setupAxes(clonePuAndNoPu)
		clonePuAndNoPu.GetYaxis().SetTitleSize(0.05)
		clonePuAndNoPu.GetYaxis().SetLabelSize(0.05)
		clonePuAndNoPu.GetXaxis().SetTitleSize(0.05)
		clonePuAndNoPu.GetXaxis().SetLabelSize(0.05)
		clonePuAndNoPu.GetYaxis().CenterTitle()
		clonePuAndNoPu.SetTitle(';E_{HO} / a.u.;Sim No PU/Sim PU52')
		clonePuAndNoPu.Sumw2()
		clonePuAndNoPu.Divide(hSimPuHo)
		clonePuAndNoPu.SetLineWidth(1)
		clonePuAndNoPu.SetMarkerStyle(6)
		clonePuAndNoPu.SetMarkerColor(colorRwthDarkBlue)
		clonePuAndNoPu.SetLineColor(colorRwthDarkBlue)
		clonePuAndNoPu.Draw('ep')
		return canvas, hSimHo,hDataHo,hSimPuHo,cloneData,clonePuAndData,clonePuAndNoPu, legend,legend2,legend3, label2, label3 ,label
		
	def compareEnergyAbsolute(self):
		
		hSimHo = self.fileHandlerSimulation.getHistogram('hoMuonAnalyzer/energy/horeco_Energy')
		hDataHo = self.fileHandlerData.getHistogram('hoMuonAnalyzer/energy/horeco_Energy')
		hSimPuHo = self.fileHandlerSimulationPu.getHistogram('hoMuonAnalyzer/energy/horeco_Energy')
		
		res = self.buildTripleCanvasWithResiduals(hSimHo,hSimPuHo,hDataHo,'cHoOnlycompared')
		
		res[0].Update()
		res[0].SaveAs('plots/energyComparison/energyAbsoluteHoOnly.gif')
		return res

	def compareEnergyAbsoluteHoMatched(self):
		hSimMatched = self.fileHandlerSimulation.getHistogram('hoMuonAnalyzer/energy/L1MuonWithHoMatchAboveThr_Energy')
		hDataMatched = self.fileHandlerData.getHistogram('hoMuonAnalyzer/energy/L1MuonWithHoMatchAboveThr_Energy')
		hSimPuHo = self.fileHandlerSimulationPu.getHistogram('hoMuonAnalyzer/energy/L1MuonWithHoMatchAboveThr_Energy')
				
		res = self.buildTripleCanvasWithResiduals(hSimMatched,hSimPuHo,hDataMatched,'cL1AndHoCompared',legendPostix='L1 + HO')
		
		res[0].Update()
		res[0].SaveAs('plots/energyComparison/energyAbsoluteL1AndHo.gif')
		return res
	
	def compareEnergyNormalizedToIntegral(self):
		hSimMatched = self.fileHandlerSimulation.getHistogram('hoMuonAnalyzer/energy/L1MuonWithHoMatchAboveThr_Energy')
		hDataMatched = self.fileHandlerData.getHistogram('hoMuonAnalyzer/energy/L1MuonWithHoMatchAboveThr_Energy')
		hSimPuHo = self.fileHandlerSimulationPu.getHistogram('hoMuonAnalyzer/energy/L1MuonWithHoMatchAboveThr_Energy')
		
		hSimMatched.Sumw2()
		hDataMatched.Sumw2()
		hSimPuHo.Sumw2()
		
		hSimMatched.Scale(1/hSimMatched.Integral())
		hDataMatched.Scale(1/hDataMatched.Integral())
		hSimPuHo.Scale(1/hSimPuHo.Integral())
				
		res = self.buildTripleCanvasWithResiduals(hSimMatched,hSimPuHo,hDataMatched,'cL1AndHoComparedNorm',legendPostix='L1 + HO',ylabel = 'rel. fraction')
		
		res[0].Update()
		res[0].SaveAs('plots/energyComparison/energyAbsoluteL1AndHoNorm.gif')
		return res
	
	def createResidualsPlot(self,canvas, h1, h2):
		pad = makeResidualsPad(canvas.cd())
		pad.cd(1).SetLogy()
		pad.cd(2).SetLogy()
		pad.cd(1)
		setupAxes(h1)
		h1.SetStats(0)
		h1.DrawCopy()
		h2.DrawCopy('same')
		pad.cd(2)
		hDataClone = h2.Clone()
		setupAxes(hDataClone)
		hDataClone.SetStats(0)
		hDataClone.SetTitle(';E_{HO} / a.u.;Tight / Not Tight')
		hDataClone.Divide(h1)
		hDataClone.GetYaxis().SetTitleSize(0.07)
		hDataClone.GetYaxis().SetLabelSize(0.07)
		hDataClone.GetYaxis().SetTitleOffset(0.4)
		hDataClone.GetXaxis().SetTitleSize(0.07)
		hDataClone.GetXaxis().SetLabelSize(0.07)
		hDataClone.GetYaxis().CenterTitle()
		
		hDataClone.Draw('ep')
		return hDataClone
	
	def compareEnergyTightNormalizedToIntegral(self):
		hSimMatched = self.fileHandlerSimulation.getHistogram('hoMuonAnalyzer/energy/L1RecoHoTight_Energy')
		hDataMatched = self.fileHandlerData.getHistogram('hoMuonAnalyzer/energy/L1RecoHoTight_Energy')
		hSimPuMatched = self.fileHandlerSimulationPu.getHistogram('hoMuonAnalyzer/energy/L1RecoHoTight_Energy')
		hDataMatchedNotTight = self.fileHandlerData.getHistogram('hoMuonAnalyzer/energy/L1MuonWithHoMatchAboveThr_Energy')
		hSimNoPuMatchedNotTight = self.fileHandlerData.getHistogram('hoMuonAnalyzer/energy/L1MuonWithHoMatchAboveThr_Energy')
		hSimPuMatchedNotTight = self.fileHandlerData.getHistogram('hoMuonAnalyzer/energy/L1MuonWithHoMatchAboveThr_Energy')
		
		hSimMatched.Sumw2()
		hDataMatched.Sumw2()
		hSimPuMatched.Sumw2()
		hDataMatchedNotTight.Sumw2()
		hSimNoPuMatchedNotTight.Sumw2()
		hSimPuMatchedNotTight.Sumw2()
		
		hSimMatched.Scale(1/hSimMatched.Integral())
		hDataMatched.Scale(1/hDataMatched.Integral())
		hSimPuMatched.Scale(1/hSimPuMatched.Integral())
		hDataMatchedNotTight.Scale(1/hDataMatchedNotTight.Integral())
		hSimNoPuMatchedNotTight.Scale(1/hSimNoPuMatchedNotTight.Integral())
		hSimPuMatchedNotTight.Scale(1/hSimPuMatchedNotTight.Integral())

				
		res = self.buildTripleCanvasWithResiduals(hSimMatched,hSimPuMatched,hDataMatched,'cL1TightAndHoComparedNorm',legendPostix='L1 + HO',ylabel = 'rel. fraction')
		
		res[0].Update()
		res[0].SaveAs('plots/energyComparison/energyAbsoluteL1TightAndHoNorm.gif')
		
		##
		# Data
		##
		c = TCanvas('cTightAndNotTight','Data tight and not tight',1800,1000)
		hDataMatchedNotTight.SetTitle('L1 Tight and L1 compared;E_{HO} / a.u.;rel. fraction')
		
		hDataClone = self.createResidualsPlot(c, hDataMatchedNotTight, hDataMatched)
		c.cd(1).cd(1)
		label = self.drawLabel()
		legend = getLegend(x1=0.7,y2=.9)
		legend.AddEntry(hDataMatchedNotTight,'Data, L1 + HO','l')
		legend.AddEntry(hDataMatched,'Data, L1 Tight + HO','l')
		legend.Draw()
		
		c.Update()
		c.SaveAs('plots/energyComparison/energyDataL1AndL1TightCompared.gif')
		
		##
		# No PU
		##
		c2 = TCanvas('cTightAndNotTightNoPu','Sim No PU tight and not tight',1800,1000)
		hSimNoPuMatchedNotTight.SetTitle('L1 Tight and L1 compared;E_{HO} / a.u.;rel. fraction')
		
		hSimNoPuClone = self.createResidualsPlot(c2, hSimNoPuMatchedNotTight, hSimMatched)
		c2.cd(1).cd(1)
		label2 = self.drawLabel()
		legend2 = getLegend(x1=0.7,y2=.9)
		legend2.AddEntry(hSimNoPuMatchedNotTight,'Sim No PU, L1 + HO','l')
		legend2.AddEntry(hSimMatched,'Sim No PU, L1 Tight + HO','l')
		legend2.Draw()
		
		c2.Update()
		c2.SaveAs('plots/energyComparison/energySimNoPuL1AndL1TightCompared.gif')
		
		##
		# PU 52
		##
		c3 = TCanvas('cTightAndNotTightPu','Sim PU tight and not tight',1800,1000)
		hSimPuMatchedNotTight.SetTitle('L1 Tight and L1 compared;E_{HO} / a.u.;rel. fraction')
		
		hSimPuClone = self.createResidualsPlot(c3, hSimPuMatchedNotTight, hSimPuMatched)
		c3.cd(1).cd(1)
		label3 = self.drawLabel()
		legend3 = getLegend(x1=0.7,y2=.9)
		legend3.AddEntry(hSimPuMatchedNotTight,'Sim PU 52, L1 + HO','l')
		legend3.AddEntry(hSimPuMatched,'Sim PU 52, L1 Tight + HO','l')
		legend3.Draw()
		
		c3.Update()
		c3.SaveAs('plots/energyComparison/energySimPu52L1AndL1TightCompared.gif')
		
		return res,c,c2,c3,hDataClone,hSimNoPuClone,hSimPuClone,legend,legend2,legend3,label,label2,label3
		
	
	def compareL1Count(self):
		hSim = self.fileHandlerSimulation.getHistogram('hoMuonAnalyzer/L1MuonPresent_Pt')
		hSimPu = self.fileHandlerSimulationPu.getHistogram('hoMuonAnalyzer/L1MuonPresent_Pt')
		hData = self.fileHandlerData.getHistogram('hoMuonAnalyzer/L1MuonPresent_Pt')
		
	#	hSimPu.Sumw2()
	#	hSim.Sumw2()

		hSim.Scale(1/hSim.Integral(),'width')
		hSimPu.Scale(1/hSimPu.Integral(),'width')
		hData.Scale(1/hData.Integral(),'width')
		
		c = TCanvas('cNvsPt','Nvs pt')
		
		hSim.SetMarkerStyle(20)
		hSim.SetMarkerColor(colorRwthLila)
		hSim.SetLineColor(colorRwthLila)
		hSim.GetYaxis().SetRangeUser(0,0.03)
		
		
		hSimPu.SetMarkerStyle(21)
		hSimPu.SetMarkerColor(colorRwthOrange)
		hSimPu.SetLineColor(colorRwthOrange)
		hSimPu.SetTitle('Normalized distribution of p_{T};p_{T,L1};normalized fraction / binwidth')
		hSimPu.SetStats(0)
		hSimPu.GetXaxis().SetRangeUser(0,20)
		hSimPu.Draw('lp')
		hSim.Draw('same,lp')		
		setupAxes(hSimPu)

		hSimPu.GetYaxis().SetTitleOffset(1.35)

		hData.SetMarkerStyle(22)
		hData.SetMarkerColor(colorRwthTuerkis)
#		hData.Draw('same,p')
		
		legend = getLegend(y1 = 0.65,y2=.9)
		legend.AddEntry(hSim,'Sim','lp')
		legend.AddEntry(hSimPu,'Sim, PU52','lp')
#		legend.AddEntry(hData,'Data','ep')
		legend.Draw()
		
		label = self.drawLabel()
		
		c.Update()
		c.SaveAs('plots/l1CountComparison/l1CountNormalized.gif')
		
		return hSim,c,hSimPu,hData,legend,label
