from plotting.Plot import Plot

from ROOT import TCanvas,TFile
from plotting.Utils import getLegend
from plotting.PlotStyle import colorRwthDarkBlue, colorRwthTuerkis, colorRwthRot,\
	colorRwthGruen

class Energy(Plot):
	#Initialize
	def __init__(self,filename,data):
		Plot.__init__(self,filename,data)
		self.createPlotSubdir('energy')
			
	def plotEnergyNormalized(self):

		ho = self.fileHandler.getHistogram("hoMuonAnalyzer/energy/horeco_Energy")
		L1MuonAndHoMatch = self.fileHandler.getHistogram('hoMuonAnalyzer/energy/L1MuonWithHoMatch_Energy')
		L1MuonAndHoMatchAboveThr = self.fileHandler.getHistogram('hoMuonAnalyzer/energy/L1MuonWithHoMatchAboveThr_Energy')
		L1MuonAndHoMatchAboveThrFilt = self.fileHandler.getHistogram('hoMuonAnalyzer/energy/L1MuonWithHoMatchAboveThrFilt_Energy')
	
		canv = TCanvas("energieNormCanvas",'Energy Norm canvas',1200,1200)
		canv.SetLogy()
	
		ho.SetStats(0)
		ho.SetTitle('Normalized energy distribution of HO hits')
		ho.GetXaxis().SetTitle('Reconstructed HO energy / GeV')
		ho.GetYaxis().SetTitle('rel. fraction')
		ho.GetXaxis().SetRangeUser(-2,6)
	
		ho.SetLineColor(colorRwthDarkBlue)
		ho.SetLineWidth(3)
		ho.Scale(1/ho.Integral())
		ho.Draw()
		
		label = self.drawLabel()
		
		legend = getLegend(0.5,0.65,0.9,0.9)
		legend.AddEntry(ho,'All HO hits','l')
		legend.Draw()
	
		if(L1MuonAndHoMatch):
			L1MuonAndHoMatch.SetLineColor(colorRwthTuerkis)
			L1MuonAndHoMatch.SetLineWidth(3)
			L1MuonAndHoMatch.Scale(1/L1MuonAndHoMatch.Integral())
			L1MuonAndHoMatch.Draw('same')
			legend.AddEntry(L1MuonAndHoMatch,'L1Muon + HO match','l')
			
		if(L1MuonAndHoMatchAboveThr):
			L1MuonAndHoMatchAboveThr.SetLineColor(colorRwthRot)
			L1MuonAndHoMatchAboveThr.SetLineWidth(3)
			L1MuonAndHoMatchAboveThr.Scale(1/L1MuonAndHoMatchAboveThr.Integral())
			L1MuonAndHoMatchAboveThr.Draw('same')
			legend.AddEntry(L1MuonAndHoMatchAboveThr,'L1Muon + HO match > 0.2 GeV','l')
	
	
		if(L1MuonAndHoMatchAboveThrFilt):
			L1MuonAndHoMatchAboveThrFilt.SetLineColor(colorRwthGruen)
			L1MuonAndHoMatchAboveThrFilt.SetLineWidth(3)
			L1MuonAndHoMatchAboveThrFilt.Scale(1/L1MuonAndHoMatchAboveThrFilt.Integral())
			L1MuonAndHoMatchAboveThrFilt.Draw('same')
			legend.AddEntry(L1MuonAndHoMatchAboveThrFilt,'L1Muon + HO match > 0.2 GeV (In Ho Geom.)','l')
	
		
	
		canv.SaveAs("plots/energy/energyNorm.png")
		canv.SaveAs("plots/energy/energyNorm.pdf")
	
		f = TFile.Open("plots/energy/energyNorm.root","RECREATE")
		canv.Write()
		f.Close()
		return [canv,ho,L1MuonAndHoMatch, L1MuonAndHoMatchAboveThr,L1MuonAndHoMatchAboveThrFilt,label]
	
	def plotEnergy(self):

		ho = self.fileHandler.getHistogram("hoMuonAnalyzer/energy/horeco_Energy")
		L1MuonAndHoMatch = self.fileHandler.getHistogram('hoMuonAnalyzer/energy/L1MuonWithHoMatch_Energy')
		L1MuonAndHoMatchAboveThr = self.fileHandler.getHistogram('hoMuonAnalyzer/energy/L1MuonWithHoMatchAboveThr_Energy')
		L1MuonAndHoMatchAboveThrFilt = self.fileHandler.getHistogram('hoMuonAnalyzer/energy/L1MuonWithHoMatchAboveThrFilt_Energy')
	
		canv = TCanvas("energieCanvas",'Energy canvas',1200,1200)
		canv.SetLogy()
	
		ho.SetStats(0)
		ho.SetTitle('Energy distribution of HO hits')
		ho.GetXaxis().SetTitle('Reconstructed HO energy / GeV')
		ho.GetYaxis().SetTitle('N')
		ho.GetXaxis().SetRangeUser(-2,6)
	
		ho.SetLineColor(colorRwthDarkBlue)
		ho.SetLineWidth(3)
		ho.Draw()
		
		label = self.drawLabel()
		
		legend = getLegend(0.5,0.65,0.9,0.9)
		legend.AddEntry(ho,'All HO hits','l')
		legend.Draw()
	
		if(L1MuonAndHoMatch):
			L1MuonAndHoMatch.SetLineColor(colorRwthTuerkis)
			L1MuonAndHoMatch.SetLineWidth(3)
			L1MuonAndHoMatch.Draw('same')
			legend.AddEntry(L1MuonAndHoMatch,'L1Muon + HO match','l')
			
		if(L1MuonAndHoMatchAboveThr):
			L1MuonAndHoMatchAboveThr.SetLineColor(colorRwthRot)
			L1MuonAndHoMatchAboveThr.SetLineWidth(3)
			L1MuonAndHoMatchAboveThr.Draw('same')
			legend.AddEntry(L1MuonAndHoMatchAboveThr,'L1Muon + HO match > 0.2 GeV','l')
	
	
		if(L1MuonAndHoMatchAboveThrFilt):
			L1MuonAndHoMatchAboveThrFilt.SetLineColor(colorRwthGruen)
			L1MuonAndHoMatchAboveThrFilt.SetLineWidth(3)
			L1MuonAndHoMatchAboveThrFilt.Draw('same')
			legend.AddEntry(L1MuonAndHoMatchAboveThrFilt,'L1Muon + HO match > 0.2 GeV (In Ho Geom.)','l')
	
		
	
		canv.SaveAs("plots/energy/energy.png")
		canv.SaveAs("plots/energy/energy.pdf")
	
		f = TFile.Open("plots/energy/energy.root","RECREATE")
		canv.Write()
		f.Close()
		return [canv,ho,L1MuonAndHoMatch, L1MuonAndHoMatchAboveThr,L1MuonAndHoMatchAboveThrFilt,label]
	
	def plotEnergyVsEta(self,sourceHistogram = 'L1MuonWithHoMatch_EnergyVsEta'):
	
		canv = TCanvas("energieCanvas",'Energy canvas',1200,1200)
	
		energyVsEta = self.fileHandler.getHistogram("hoMuonAnalyzer/energy/" + sourceHistogram)
		energyVsEta.Rebin2D(10,1)
		energyVsEta.GetXaxis().SetRangeUser(-1.1,1.1)
		energyVsEta.GetYaxis().SetRangeUser(0,2.5)
		energyVsEta.SetStats(0)
	
		energyVsEta.GetZaxis().SetTitle('Entries / 0.05 GeV')
		
		energyVsEta.Draw('colz')
		
		canv.Update()
		pal = energyVsEta.GetListOfFunctions().FindObject("palette")
		pal.SetX2NDC(0.92)
		
		canv.SaveAs("plots/energy/energyVsEta.png")
		canv.SaveAs("plots/energy/energyVsEta.pdf")
	
		f = TFile.Open("plots/energy/energyVsEta.root","RECREATE")
		canv.Write()
		f.Close()
		return canv
	
	def plotEnergyVsPhi(self,sourceHistogram = 'L1MuonWithHoMatch_EnergyVsPhi'):
	
		canv = TCanvas("energieCanvas",'Energy canvas',1200,1200)
	
		energyVsEta = self.fileHandler.getHistogram("hoMuonAnalyzer/energy/" + sourceHistogram)
		energyVsEta.Rebin2D(10,1)
		energyVsEta.GetXaxis().SetRangeUser(-3.17,3.17)
		energyVsEta.GetYaxis().SetRangeUser(0,2.5)
		energyVsEta.SetStats(0)
	
		energyVsEta.GetZaxis().SetTitle('Entries / 0.05 GeV')
		
		energyVsEta.Draw('colz')
		
		canv.Update()
		pal = energyVsEta.GetListOfFunctions().FindObject("palette")
		pal.SetX2NDC(0.92)
		
		canv.SaveAs("plots/energy/energyVsPhi.png")
		canv.SaveAs("plots/energy/energyVsPhi.pdf")
	
		f = TFile.Open("plots/energy/energyVsPhi.root","RECREATE")
		canv.Write()
		f.Close()
		return canv
	
	# Generate the plot based on the energy vs eta and phin histogram
	def plotEnergyVsEtaPhi(self,sourceHistogram = 'L1MuonWithHoMatch_EnergyVsEtaPhi'):

		canv = TCanvas("energieVsPositionCanvas",'Energy canvas',1200,1200)

		energyVsPos = self.fileHandler.getHistogram("hoMuonAnalyzer/energy/" + sourceHistogram)
		projection = energyVsPos.Project3DProfile()
		projection.GetXaxis().SetTitle(energyVsPos.GetXaxis().GetTitle())
		projection.GetYaxis().SetTitle(energyVsPos.GetYaxis().GetTitle())
		projection.GetZaxis().SetTitle(energyVsPos.GetZaxis().GetTitle())
		projection.Draw('colz')
		
		canv.Update()
		pal = projection.GetListOfFunctions().FindObject("palette")
		pal.SetX2NDC(0.92)
		
		stats = projection.GetListOfFunctions().FindObject("stats")
		stats.SetX1NDC(.1)
		stats.SetX2NDC(.3)
		stats.SetY1NDC(.7)
		stats.SetY2NDC(.9)
		
		canv.SaveAs("plots/energy/energyVsPosition.png")
		canv.SaveAs("plots/energy/energyVsPosition.pdf")
	
		f = TFile.Open("plots/energy/energyVsPosition.root","RECREATE")
		canv.Write()
		f.Close()
		return canv
	