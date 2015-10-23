from plotting import OutputModule
from plotting.PlotStyle import setupAxes

commandLine = OutputModule.CommandLineHandler('[Utils.py] ')

def average2DHistogramBinwise(histWeights,histCounter):
	for i in range(0,histWeights.GetNbinsX()):
		for j in range(0,histWeights.GetNbinsY()):
			if histCounter.GetBinContent(histCounter.GetBin(i,j)) != 0:
				histWeights.SetBinContent(histWeights.GetBin(i,j),histWeights.GetBinContent(histWeights.GetBin(i,j))
										/histCounter.GetBinContent(histCounter.GetBin(i,j)))
	return histWeights

def setupEAvplot(histE,histC = None,xmin = -0.4, xmax = 0.4, ymin = -0.4, ymax = 0.4,same = False, borderAll = None):
	if histC != None:
		histE = average2DHistogramBinwise(histE,histC)
	if same:
		if borderAll == None:
			commandLine.output('WARNING: Requested same histogram borders for all ranges but '
							'did not give borderAll parameter. Using default values instead!')
		else:
			xmin = ymin = -borderAll
			xmax = ymax = borderAll
	histE.GetXaxis().SetRangeUser(xmin,xmax)
	histE.GetYaxis().SetRangeUser(ymin,ymax)
	histE.SetStats(0)
	histE.GetXaxis().SetTitle('#Delta#eta')
	histE.GetYaxis().SetTitle('#Delta#phi')
	histE.GetZaxis().SetTitle('Reconstructed Energy / GeV')
	setupAxes(histE)
	return histE