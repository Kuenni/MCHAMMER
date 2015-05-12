import os,sys
sys.path.append(os.path.abspath("../../../python"))
from time import sleep
from ROOT import TCanvas,TH2D

from PlotStyle import setPlotStyle,getTH2D
setPlotStyle()


canvas = TCanvas("canvas","canvas",1200,1200)
hist = getTH2D("hist","Parameter Scan;#DeltaR;E_{Thr}",16,-0.0375,0.3625,16,-0.0375,0.3625)
histCorrect = getTH2D("histCorrect","Parameter Scan in abs(12.5)ns;#DeltaR;E_{Thr}",16,-0.0375,0.3625,16,-0.0375,0.3625)
histTotal = getTH2D("histTotal","Parameter Scan Total events;#DeltaR;E_{Thr}",16,-0.0375,0.3625,16,-0.0375,0.3625)

for filename in os.listdir('./results'):
	if filename[-4:] == '.txt':
		file = open('./results/' + filename,'r')
		for line in file.readlines():
			if line.find('deltaR') != -1:
				continue
			lineParts = line.split('\t')
			deltaR 	= float(lineParts[0])
			eThr 	= float(lineParts[1])
			nCorrect = float(lineParts[2])
			nTotal 	= float(lineParts[3])
			print lineParts
			
			if(nTotal > 0):
				histCorrect.SetBinContent(histCorrect.FindBin(deltaR,eThr),histCorrect.GetBinContent(histCorrect.FindBin(deltaR,eThr)) + nCorrect)
				histTotal.SetBinContent(histTotal.FindBin(deltaR,eThr),histTotal.GetBinContent(histCorrect.FindBin(deltaR,eThr)) + nTotal)

hist.SetStats(0)
for i in range(0,hist.GetNbinsX()):
	for j in range (0,hist.GetNbinsY()):
		if histTotal.GetBinContent(i,j) > 0:
			hist.SetBinContent(i,j,histCorrect.GetBinContent(i,j)/histTotal.GetBinContent(i,j)*100)
hist.SetMinimum(88)
hist.SetContour(99)
hist.Draw('colz')

canvas.Update()
raw_input('-->')
