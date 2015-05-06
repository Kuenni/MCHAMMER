import os,sys
sys.path.append(os.path.abspath("../../../python"))

from ROOT import TCanvas,TH2D

from PlotStyle import setPlotStyle,getTH2D
setPlotStyle()

canvas = TCanvas("canvas","canvas",1200,1200)
hist = getTH2D("hist","Parameter Scan, match by #DeltaR;#DeltaR;E_{Thr}",16,-0.0375,0.3625,16,-0.0375,0.3625)
for filename in os.listdir('./results'):
    if filename[-4:] == '.txt':
        if filename.find('byDeltaR') != -1:
            file = open('./results/' + filename,'r')
            file.readline()
            line 	= file.readline().split()
            deltaR 	= float(line[1])
            eThr 	= float(line[2])
            nCorrect = float(line[3])
            nTotal 	= float(line[4])
            hist.Fill(deltaR,eThr,nCorrect/nTotal*100)
hist.SetStats(0)
hist.Draw('colz')

canvas.Update()

raw_input('-->')