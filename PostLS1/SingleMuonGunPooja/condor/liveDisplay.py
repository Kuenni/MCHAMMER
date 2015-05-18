import os,sys
sys.path.append(os.path.abspath("../../../python"))
from time import sleep
from ROOT import TCanvas,TH2D,TPaveText

from PlotStyle import setPlotStyle,getTH2D,getLabelCmsPrivateSimulation
setPlotStyle()

def testResults():
	instances = []
	for filename in os.listdir('./log/'):
		if(filename.startswith('err')):
			if(os.path.getsize('./log/'+filename) > 0):
				cluster = filename.split('_')[-1]
				for logfile in os.listdir('./log/'):
					if(logfile.endswith(cluster + '_0.log')):
						instance = logfile.split('_')[1]
						instances.append(int(instance))
	instances.sort(cmp=None, key=None, reverse=False)
	for i in instances:
		for filename in os.listdir('./log/'):
			if filename.find('INSTANCE_' + str(i) + '.log') != -1 :
				foundErrorLine = False
				logfile = open('./log/' + filename)
				for line in logfile.readlines():
					if line.find('Error occured during script execution') != -1:
						foundErrorLine = True
				print 'File %s --> %s' % (filename,'OK' if foundErrorLine else 'NO ERROR')
	print instances

def plotResults():	
	canvas = TCanvas("canvas","canvas",1200,1200)
	hist = getTH2D("hist","Parameter Scan;#DeltaR;E_{Thr}",16,-0.0375,0.3625,16,-0.0375,0.3625)
	histCorrect = getTH2D("histCorrect","Parameter Scan in abs(12.5)ns;#DeltaR;E_{Thr}",16,-0.0375,0.3625,16,-0.0375,0.3625)
	histTotal = getTH2D("histTotal","Parameter Scan Total events;#DeltaR;E_{Thr}",16,-0.0375,0.3625,16,-0.0375,0.3625)
	
	l1Total = 0
	
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
				l1Total += nTotal
				if(nTotal > 0):
					histCorrect.SetBinContent(histCorrect.FindBin(deltaR,eThr),histCorrect.GetBinContent(histCorrect.FindBin(deltaR,eThr)) + nCorrect)
					histTotal.SetBinContent(histTotal.FindBin(deltaR,eThr),histTotal.GetBinContent(histCorrect.FindBin(deltaR,eThr)) + nTotal)
	
	hist.SetStats(0)
	for i in range(0,hist.GetNbinsX()):
		for j in range (0,hist.GetNbinsY()):
			if histTotal.GetBinContent(i,j) > 0:
				hist.SetBinContent(i,j,histCorrect.GetBinContent(i,j)/histTotal.GetBinContent(i,j)*100)
	hist.SetMinimum(93)
	hist.SetContour(100)
	hist.SetTitle('Parameter Scan, Single #mu Gun, No PU')
	hist.GetYaxis().SetTitleOffset(1.45)
	hist.GetZaxis().SetTitle('Fraction within |12.5| ns / %')
	hist.Draw('colz')
	
	canvas.Update()
	pal = hist.GetListOfFunctions().FindObject("palette")
	pal.SetX2NDC(0.92)
	
	label = getLabelCmsPrivateSimulation()
	label.Draw()
	
	canvas.Update()
	return canvas,hist,label

res = plotResults()
testResults()

raw_input('-->')
