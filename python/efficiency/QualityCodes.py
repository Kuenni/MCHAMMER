import sys
from ROOT import TCanvas,TLegend
from plotting.RootFileHandler import RootFileHandler
from plotting.PlotStyle import setupAxes,setPlotStyle, colorRwthDarkBlue,\
	drawLabelCmsPrivateSimulation, colorRwthLightBlue, colorRwthGruen,\
	colorRwthTuerkis, colorRwthRot, colorRwthMagenta
fileHandler = RootFileHandler(sys.argv[1])

setPlotStyle()

def plotQualityCodes():
	c = TCanvas('cQualityCodes')
	c.SetLogy()
	qualityCodes = fileHandler.getHistogram('hoMuonAnalyzer/L1MuonQualityCodesCentral_Multiplicity')
	qualityCodesFail = fileHandler.getHistogram('hoMuonAnalyzer/L1MuonQualityCodesCentralFail_Multiplicity')
	
	qualityCodes3x3 = fileHandler.getHistogram('hoMuonAnalyzer/L1MuonQualityCodes3x3_Multiplicity')
	qualityCodes3x3Fail = fileHandler.getHistogram('hoMuonAnalyzer/L1MuonQualityCodes3x3Fail_Multiplicity')
	
	qualityCodes5x5 = fileHandler.getHistogram('hoMuonAnalyzer/L1MuonQualityCodes5x5_Multiplicity')
	qualityCodes5x5Fail = fileHandler.getHistogram('hoMuonAnalyzer/L1MuonQualityCodes5x5Fail_Multiplicity')
	
	setupAxes(qualityCodes)
	qualityCodes.SetTitle('Quality codes for grid matching;Quality code;#')
	qualityCodes.SetLineColor(colorRwthDarkBlue)
	qualityCodes.GetXaxis().SetRangeUser(4,8)
	qualityCodes.SetStats(0)
	qualityCodes.SetLineWidth(3)
	
	setupAxes(qualityCodesFail)
	qualityCodesFail.SetLineWidth(3)
	qualityCodesFail.SetLineColor(colorRwthLightBlue)
	
	setupAxes(qualityCodes3x3)
	qualityCodes3x3.SetLineWidth(3)
	qualityCodes3x3.SetLineColor(colorRwthGruen)
	
	setupAxes(qualityCodes3x3Fail)
	qualityCodes3x3Fail.SetLineWidth(3)
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
	qualityCodes5x5.Draw('same')
	qualityCodes5x5Fail.Draw('same')
	
	legend = TLegend(0.1,0.6,0.3,0.9)
	legend.AddEntry(qualityCodes,"Central","l")
	legend.AddEntry(qualityCodesFail,"Central Fail","l")
	legend.AddEntry(qualityCodes3x3,"3x3","l")
	legend.AddEntry(qualityCodes3x3Fail,"3x3 Fail","l")
	legend.AddEntry(qualityCodes5x5,"5x5","l")
	legend.AddEntry(qualityCodes5x5Fail,"5x5 Fail","l")
	legend.Draw()
	
	label = drawLabelCmsPrivateSimulation()
	c.Update()
	
	return c,qualityCodes,label,qualityCodesFail,qualityCodes3x3,qualityCodes3x3Fail,qualityCodes5x5,qualityCodes5x5Fail,legend