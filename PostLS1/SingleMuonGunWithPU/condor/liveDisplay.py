import os,sys
sys.path.append(os.path.abspath("../../../python"))
from time import sleep
from ROOT import TCanvas,TH2D

from PlotStyle import setPlotStyle,getTH2D
setPlotStyle()


canvas = TCanvas("canvas","canvas",1200,1200)
canvas.Divide(2,1)
hist = getTH2D("hist","Parameter Scan, match by #DeltaR;#DeltaR;E_{Thr}",16,-0.0375,0.3625,16,-0.0375,0.3625)
hist2 = getTH2D("hist2","Parameter Scan, match by E_{Cone};#DeltaR;E_{Thr}",16,-0.0375,0.3625,16,-0.0375,0.3625)

while True:
	hist.Reset()
	hist2.Reset()
	canvas.cd(1)
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
	hist.SetMinimum(70)
	hist.SetContour(99)
	hist.Draw('colz')
	
	canvas.cd(2)
	for filename in os.listdir('./results'):
	    if filename[-4:] == '.txt':
	        if filename.find('byECone') != -1:
	            file = open('./results/' + filename,'r')
	            file.readline()
	            line 	= file.readline().split()
	            deltaR 	= float(line[1])
	            eThr 	= float(line[2])
	            nCorrect = float(line[3])
	            nTotal 	= float(line[4])
	            if nTotal > 0:
	            	hist2.Fill(deltaR,eThr,nCorrect/nTotal*100)
	hist2.SetStats(0)
	hist2.SetMinimum(75)
	hist2.SetContour(99)
	hist2.Draw('colz')
	
	canvas.Update()
	sleep(5)
raw_input('-->')
