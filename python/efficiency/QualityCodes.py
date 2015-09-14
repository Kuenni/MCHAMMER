import sys
from ROOT import TCanvas,TLegend
from plotting.RootFileHandler import RootFileHandler
from plotting.PlotStyle import setupAxes,setPlotStyle, colorRwthDarkBlue,\
	drawLabelCmsPrivateSimulation, colorRwthLightBlue, colorRwthGruen,\
	colorRwthTuerkis, colorRwthRot, colorRwthMagenta, setupPalette
fileHandler = RootFileHandler(sys.argv[1])

setPlotStyle()

def plotQualityCodes():
	c = TCanvas('cQualityCodes')
	c.SetLogy()
	qualityCodes = fileHandler.getHistogram('hoMuonAnalyzer/multiplicity/L1MuonQualityCodesCentral_Multiplicity')
	qualityCodesFail = fileHandler.getHistogram('hoMuonAnalyzer/multiplicity/L1MuonQualityCodesCentralFail_Multiplicity')
	
	qualityCodes3x3 = fileHandler.getHistogram('hoMuonAnalyzer/multiplicity/L1MuonQualityCodes3x3_Multiplicity')
	qualityCodes3x3Fail = fileHandler.getHistogram('hoMuonAnalyzer/multiplicity/L1MuonQualityCodes3x3Fail_Multiplicity')
	
	qualityCodes5x5 = fileHandler.getHistogram('hoMuonAnalyzer/multiplicity/L1MuonQualityCodes5x5_Multiplicity')
	qualityCodes5x5Fail = fileHandler.getHistogram('hoMuonAnalyzer/multiplicity/L1MuonQualityCodes5x5Fail_Multiplicity')
	
	setupAxes(qualityCodes)
	qualityCodes.SetTitle('Quality codes for grid matching;;#')
	qualityCodes.SetLineColor(colorRwthDarkBlue)
	qualityCodes.GetXaxis().SetRangeUser(4,8)
	qualityCodes.SetStats(0)
	qualityCodes.SetLineWidth(3)
	
	c.cd().SetBottomMargin(0.15)
	#Label the bins with the meaning of the quality code
	qualityCodes.GetXaxis().SetBinLabel(qualityCodes.FindBin(5),'unmatched RPC')
	qualityCodes.GetXaxis().SetBinLabel(qualityCodes.FindBin(6),'unmatched DT or CSC')
	qualityCodes.GetXaxis().SetBinLabel(qualityCodes.FindBin(7),'matched DT-RPC or CSC-RPC')
	
	setupAxes(qualityCodesFail)
	qualityCodesFail.SetLineWidth(3)
	qualityCodesFail.SetLineStyle(7)
	qualityCodesFail.SetLineColor(colorRwthLightBlue)
	
	setupAxes(qualityCodes3x3)
	qualityCodes3x3.SetLineWidth(3)
	qualityCodes3x3.SetLineStyle(10)
	qualityCodes3x3.SetLineColor(colorRwthGruen)
	
	setupAxes(qualityCodes3x3Fail)
	qualityCodes3x3Fail.SetLineWidth(3)
	qualityCodes3x3Fail.SetLineStyle(8)
	qualityCodes3x3Fail.SetLineColor(colorRwthTuerkis)
	
	setupAxes(qualityCodes5x5)
	qualityCodes5x5.SetLineWidth(3)
	qualityCodes5x5.SetLineColor(colorRwthRot)
	
	setupAxes(qualityCodes5x5Fail)
	qualityCodes5x5Fail.SetLineWidth(3)
	qualityCodes5x5Fail.SetLineColor(colorRwthMagenta)
	
	qualityCodes.Scale(1/qualityCodes.Integral())
	qualityCodes3x3.Scale(1/qualityCodes3x3.Integral())
	qualityCodes3x3Fail.Scale(1/qualityCodes3x3Fail.Integral())
	qualityCodes5x5.Scale(1/qualityCodes5x5.Integral())
	qualityCodes5x5Fail.Scale(1/qualityCodes5x5Fail.Integral())
	qualityCodesFail.Scale(1/qualityCodesFail.Integral())
	
	qualityCodes.Draw()
	qualityCodesFail.Draw('same')
	qualityCodes3x3.Draw('same')
	qualityCodes3x3Fail.Draw('same')
#	qualityCodes5x5.Draw('same')
#	qualityCodes5x5Fail.Draw('same')
	
	legend = TLegend(0.1,0.6,0.3,0.9)
	legend.AddEntry(qualityCodes,"Central","l")
	legend.AddEntry(qualityCodesFail,"Central Fail","l")
	legend.AddEntry(qualityCodes3x3,"3x3","l")
	legend.AddEntry(qualityCodes3x3Fail,"3x3 Fail","l")
	legend.SetFillColor(0)
#	legend.AddEntry(qualityCodes5x5,"5x5","l")
#	legend.AddEntry(qualityCodes5x5Fail,"5x5 Fail","l")
	legend.Draw()
	
	label = drawLabelCmsPrivateSimulation()
	c.Update()
	
	c.SaveAs('plots/efficiency/qualityCodes.pdf')
	
	return c,qualityCodes,label,qualityCodesFail,qualityCodes3x3,qualityCodes3x3Fail,qualityCodes5x5,qualityCodes5x5Fail,legend

def plotQualityCodesVsPt():
	canvas = TCanvas('cQualityCodesVsPtCentral','cQualityCodesVsPtCentral',800,0,800,600)
	canvas.SetLogz()
	qualityCentralFail = fileHandler.getHistogram('hoMuonAnalyzer/correlation/L1MuonpTvsQCCentralFail')
	quality3x3Fail = fileHandler.getHistogram('hoMuonAnalyzer/correlation/L1MuonpTvsQC3x3Fail')
	quality5x5Fail = fileHandler.getHistogram('hoMuonAnalyzer/correlation/L1MuonpTvsQC5x5Fail')

	setupAxes(qualityCentralFail)
	qualityCentralFail.GetXaxis().SetRangeUser(4,8)
	qualityCentralFail.GetYaxis().SetRangeUser(-1,160)
	qualityCentralFail.SetStats(0)
	qualityCentralFail.Draw('colz')
	
	label = drawLabelCmsPrivateSimulation()
	canvas.Update()
	
	setupPalette(qualityCentralFail)
	canvas.Update()
	
	canvas.SaveAs('plots/efficiency/ptVsQualityCodeCentralFail.png')
	canvas.SaveAs('plots/efficiency/ptVsQualityCodeCentralFail.pdf')
	
	raw_input('wait')
	
	qualityCentralFail.Draw('lego2')
	canvas.Update()
	
	canvas.SaveAs('plots/efficiency/ptVsQualityCodeCentral3DFail.png')
	canvas.SaveAs('plots/efficiency/ptVsQualityCodeCentral3DFail.pdf')
	
	return qualityCentralFail,label,canvas