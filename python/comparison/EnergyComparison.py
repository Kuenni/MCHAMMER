from ROOT import TFile,TCanvas
from plotting.PlotStyle import colorRwthDarkBlue, colorRwthMagenta,\
	drawLabelCmsPrivateData, setPlotStyle, setupAxes
from plotting.Utils import getLegend
from plotting.Plot import Plot

SIMULATION_FILE_SCHEME = '/user/kuensken/CMSSW/CMSSW_7_2_2_patch2/src/HoMuonTrigger/PostLS1/SingleMuonGunPooja/NoPUAnalyzed'
DATA_FILE_SCHEME = '/user/kuensken/CMSSW/CMSSW_7_4_15/src/HoMuonTrigger/PostLS1/collisionData2015/SingleMuon2015D'

class EnergyComparison(Plot):
	#Initialize
	def __init__(self,data):
		Plot.__init__(self,data = data)
		self.createPlotSubdir('energyComparison')
		self.fileHandlerSimulation = self.createFileHandler(SIMULATION_FILE_SCHEME)
		self.fileHandlerData = self.createFileHandler(DATA_FILE_SCHEME)
	
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
			
			hSimHo.Draw()
			hSimMatch.Draw('same')
			hDataHo.Draw('same')
			hDataMatch.Draw('same')
			
			legend = getLegend(y1 =.6,y2=.9)
			legend.AddEntry(hSimHo,'Sim, HO Only','l').SetTextFont(62)
			legend.AddEntry(hSimMatch,'Sim, HO matched','l').SetTextFont(62)
			legend.AddEntry(hDataHo,'Data, HO Only','l').SetTextFont(62)
			legend.AddEntry(hDataMatch,'Data HO Matched','l').SetTextFont(62)
			legend.Draw()
			
			label = drawLabelCmsPrivateData()
			
			objectStorage.append([hSimHo,hSimMatch,hDataHo,hDataMatch,legend,label])
		
		canvas.Update()
		canvas.SaveAs('energyPerWheelDataAndSimNormed.gif')
	
		return canvas,objectStorage
	
	def compareEnergyAbsolute(self):
		
		canvas = TCanvas('cEnergyTogether')
		canvas.cd().SetLogy()
		
		hSimHo = self.fileHandlerSimulation.getHistogram('hoMuonAnalyzer/energy/horeco_Energy')
		hSimMatched = self.fileHandlerSimulation.getHistogram('hoMuonAnalyzer/energy/L1MuonWithHoMatchAboveThr_Energy')
		hDataHo = self.fileHandlerData.getHistogram('hoMuonAnalyzer/energy/horeco_Energy')
		hDataMatched = self.fileHandlerData.getHistogram('hoMuonAnalyzer/energy/L1MuonWithHoMatchAboveThr_Energy')
		
		hSimHo.SetLineColor(colorRwthDarkBlue)
		hSimHo.SetStats(0)
		hSimHo.GetXaxis().SetRangeUser(-1,6)
		hSimHo.SetTitle('Distribution of HO Energy;E_{HO} / a.u.;# entries')
		hSimMatched.SetLineColor(colorRwthDarkBlue)
		hSimMatched.SetLineStyle(7)
		hDataHo.SetLineColor(colorRwthMagenta)
		hDataMatched.SetLineColor(colorRwthMagenta)
		hDataMatched.SetLineStyle(7)
		
		hSimHo.Draw()
		hSimMatched.Draw('same')
		hDataHo.Draw('same')
		hDataMatched.Draw('same')
		
		label = drawLabelCmsPrivateData()

		legend = getLegend(y1 = 0.65,y2=.9)
		legend.AddEntry(hSimHo,'Sim No PU, HO only','l')
		legend.AddEntry(hSimMatched,'Sim No PU, L1 + HO','l')
		legend.AddEntry(hDataHo,'Data, HO only','l')
		legend.AddEntry(hDataMatched,'Data, L1 + HO','l')
		legend.Draw()
		
		setupAxes(hSimHo)
		canvas.Update()
		
		canvas.SaveAs('energyComparison/energyAbsolute.gif')
		
		return canvas, hSimHo,hSimMatched,hDataHo,hDataMatched, legend, label

	def compareEnergyNormalizedToIntegral(self):
		objectList = self.compareEnergyAbsolute()
		objectList[1].Scale(1/objectList[1].Integral())
		objectList[2].Scale(1/objectList[2].Integral())
		objectList[3].Scale(1/objectList[3].Integral())
		objectList[4].Scale(1/objectList[4].Integral())
		
		objectList[1].SetTitle('Distribution of HO Energy, normalized')
		objectList[1].GetYaxis().SetTitle('rel. fraction')
		objectList[1].Draw()
		objectList[2].Draw('same')
		objectList[3].Draw('same')
		objectList[4].Draw('same')
		
		objectList[-2].Draw()
		objectList[-1].Draw()
		
		objectList[0].Update()
		
		
		return objectList
		