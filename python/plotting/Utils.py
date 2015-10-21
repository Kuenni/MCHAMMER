def average2DHistogramBinwise(histWeights,histCounter):
	for i in range(0,histWeights.GetNbinsX()):
		for j in range(0,histWeights.GetNbinsY()):
			if histCounter.GetBinContent(histCounter.GetBin(i,j)) != 0:
				histWeights.SetBinContent(histWeights.GetBin(i,j),histWeights.GetBinContent(histWeights.GetBin(i,j))
										/histCounter.GetBinContent(histCounter.GetBin(i,j)))
	return histWeights