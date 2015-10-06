import sys
from ROOT import TCanvas,TLegend,THStack,TLegend
from plotting.RootFileHandler import RootFileHandler
from plotting.PlotStyle import setupAxes,setPlotStyle, colorRwthDarkBlue,\
	drawLabelCmsPrivateSimulation, colorRwthLightBlue, colorRwthGruen,\
	colorRwthTuerkis, colorRwthRot, colorRwthMagenta, setupPalette
from plotting.OutputModule import CommandLineHandler,CliColors
fileHandler = RootFileHandler(sys.argv[1])

setPlotStyle()
cli = CommandLineHandler('[QualityCodes] ')

qualityCodeDict = {
				1:'Halo Muon',
				2:'Very low qual. Type 1',
				3:'Very low qual. Type 2',
				4:'Very low qual. Type 3',
				5:'unmatched RPC',
				6:'unmatched DT or CSC',
				7:'matched DT-RPC or CSC-RPC'
				}

gridSizeDict = {
			0:'Central',
			1:'3x3',
			2:'5x5'}

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
	qualityCodes.GetXaxis().SetRangeUser(0,8)
	qualityCodes.SetStats(0)
	qualityCodes.SetLineWidth(3)
	
	c.cd().SetBottomMargin(0.15)
	#Label the bins with the meaning of the quality code
	for i in range(1,8):
		qualityCodes.GetXaxis().SetBinLabel(qualityCodes.FindBin(i),qualityCodeDict.get(i))
	
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

def plotQualityCodesStacked(gridSize):
	gridString = gridSizeDict.get(gridSize)
	c = TCanvas('cQualityCodes' + gridString + 'Stacked','Stacked QC ' + gridString,600,0,800,600)
	c.SetLogy()
	c.cd().SetBottomMargin(0.15)
	c.cd().SetRightMargin(0.20)
	qualityCodes = fileHandler.getHistogram('hoMuonAnalyzer/multiplicity/L1MuonQualityCodes' + gridString + '_Multiplicity')
	qualityCodesFail = fileHandler.getHistogram('hoMuonAnalyzer/multiplicity/L1MuonQualityCodes' + gridString + 'Fail_Multiplicity')
	
	countQualityCodes = fileHandler.getHistogram('hoMuonAnalyzer/multiplicity/L1MuonAllQualityCodes_Multiplicity')
	countQualityCodesTruth = fileHandler.getHistogram('hoMuonAnalyzer/multiplicity/L1MuonTruthAllQualityCodes_Multiplicity')
	
	print
	cli.output('Sanity check for quality code counts')
	for i in range(1,8):
		nTotalHistogram = countQualityCodes.GetBinContent(countQualityCodes.FindBin(i))
		nFail = qualityCodesFail.GetBinContent(qualityCodesFail.FindBin(i))
		nPass = qualityCodes.GetBinContent(qualityCodes.FindBin(i))
		nSummed = nFail + nPass
		print
		cli.output('NTotal: %d\t\tNSummed: %d' % (nTotalHistogram,nSummed))
		cli.output('Sanity check: %s'% (CliColors.OKBLUE + 'OK' + CliColors.ENDC if nTotalHistogram == nSummed else CliColors.FAIL + 'FAIL' + CliColors.ENDC) )
		print
		if nTotalHistogram:
			qualityCodes.SetBinContent(qualityCodes.FindBin(i),nPass/float(nTotalHistogram))
			qualityCodesFail.SetBinContent(qualityCodesFail.FindBin(i),nFail/float(nTotalHistogram))
	
	stack = THStack("hstack","Fractions of rejected and accepted quality codes (" + gridString + ");;rel. fraction")
	
	qualityCodes.SetLineColor(colorRwthDarkBlue)
	qualityCodes.SetFillColor(colorRwthDarkBlue)
	qualityCodes.SetFillStyle(3002)

	qualityCodesFail.SetFillColor(colorRwthMagenta)
	qualityCodesFail.SetLineColor(colorRwthMagenta)
	qualityCodesFail.SetFillStyle(3002)

	stack.Add(qualityCodes)
	stack.Add(qualityCodesFail)
	
	stack.Draw()
	stack.GetXaxis().SetRangeUser(0,8)
		#Label the bins with the meaning of the quality code
	for i in range(1,8):
		stack.GetXaxis().SetBinLabel(stack.GetXaxis().FindBin(i),qualityCodeDict.get(i))
		
	legend = TLegend(0.82,0.75,0.99,0.9)
	legend.AddEntry(qualityCodes,"Passed","f")
	legend.AddEntry(qualityCodesFail,"Failed","f")
	legend.Draw()
	
	label = drawLabelCmsPrivateSimulation(x1ndc=0.5,y1ndc=0.9,x2ndc=0.8,y2ndc=0.93)
	
	setupAxes(stack)
		
	c.Update()
	
	c.SaveAs('plots/efficiency/qualityCodesStacked' + gridString + '.pdf')
	
	return stack,c,qualityCodes,qualityCodesFail,legend,label

def createPlotPtVsQualityCode(gridSize):
	sourceHistogramsForGrid = {
		1:'hoMuonAnalyzer/correlation/L1MuonpTvsQCCentralFail',
		2:'hoMuonAnalyzer/correlation/L1MuonpTvsQC3x3Fail',
		3:'hoMuonAnalyzer/correlation/L1MuonpTvsQC5x5Fail'
	}
	histogramTitleDict = {
		1:'Central',
		2:'3x3',
		3:'5x5'
	}
	histogram = fileHandler.getHistogram(sourceHistogramsForGrid.get(gridSize))
	title = 'p_{T} vs. rejected QC (' + histogramTitleDict.get(gridSize) + ')'
	canvasTitle = 'cPtVsQualityCodes' + histogramTitleDict.get(gridSize)
	
	canvas = TCanvas(canvasTitle,'cPtVsQualityCodes' + histogramTitleDict.get(gridSize),800,0,800,600)
	canvas.SetLogz()
		
	histogram.GetXaxis().SetRangeUser(0,8)
	histogram.GetYaxis().SetRangeUser(-1,160)
	histogram.SetStats(0)
	histogram.SetTitle(title)
	
	histogram.Scale(1,'width')
	
	histogram.Draw('colz')
	
	label = drawLabelCmsPrivateSimulation()
	canvas.Update()
	
	setupPalette(histogram)
	canvas.Update()
	
	fileNameTrunk = 'plots/efficiency/ptVsQualityCode' + histogramTitleDict.get(gridSize) + 'Fail'
	
	canvas.SaveAs(fileNameTrunk + '.png')
	canvas.SaveAs(fileNameTrunk + '.pdf')
	
	histogram.Draw('lego2')
	canvas.Update()		
		
	canvas.SaveAs(fileNameTrunk + '3D.png')
	canvas.SaveAs(fileNameTrunk + '3D.pdf')
	
	return canvas,label,histogram

def plotQualityCodesVsPt():
	allPlots = []

	allPlots.append(createPlotPtVsQualityCode(1))
	allPlots.append(createPlotPtVsQualityCode(2))
	allPlots.append(createPlotPtVsQualityCode(3))
	
	canvas = TCanvas('allQCCodes',"All QC")
	canvas.SetLogy()
	canvas.cd().SetBottomMargin(0.15)

	histAllCodes = fileHandler.getHistogram('hoMuonAnalyzer/multiplicity/L1MuonAllQualityCodes_Multiplicity')
	histAllCodesTruth = fileHandler.getHistogram('hoMuonAnalyzer/multiplicity/L1MuonTruthAllQualityCodes_Multiplicity')

	setupAxes(histAllCodes)

	histAllCodes.SetLineWidth(3)
	histAllCodesTruth.SetLineWidth(3)
	histAllCodes.SetLineColor(colorRwthDarkBlue)
	histAllCodes.Scale(1/histAllCodes.Integral())
	histAllCodes.GetXaxis().SetRangeUser(0,8)	
	histAllCodes.SetStats(0)
	histAllCodes.SetTitle('L1 muon quality codes;;rel. fraction')
	#Label the bins with the meaning of the quality code
	for i in range(1,8):
		histAllCodes.GetXaxis().SetBinLabel(histAllCodes.GetXaxis().FindBin(i),qualityCodeDict.get(i))
	
	histAllCodes.Draw()
	
	histAllCodesTruth.Scale(1/histAllCodesTruth.Integral())
	histAllCodesTruth.SetLineColor(colorRwthMagenta)
	histAllCodesTruth.Draw('Same')
	
	label = drawLabelCmsPrivateSimulation()
	
	legend = TLegend(0.1,0.75,0.3,0.9)
	legend.AddEntry(histAllCodes,"All L1","l")
	legend.AddEntry(histAllCodesTruth,"L1 Truth","l")
	legend.Draw()
	
	canvas.Update()
	canvas.SaveAs('plots/efficiency/allQualityCodes.pdf')
	
	allPlots.append([histAllCodes,histAllCodesTruth,canvas,legend,label])
	
	return allPlots
