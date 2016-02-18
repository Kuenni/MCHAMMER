from ROOT import gROOT,gStyle, TColor, TPaveText, TGraph, ROOT, Double, TBox, TH2D, TH1D, TEfficiency
from math import sqrt,pi
import matplotlib.pyplot as plt
import sys

colorRwthMagenta 	= TColor.GetColor("#E30066")
colorRwthLightBlue 	= TColor.GetColor("#8EBAE5")
colorRwthDarkBlue 	= TColor.GetColor("#00549F")
colorRwthTuerkis	= TColor.GetColor("#0098A1")
colorRwthGruen		= TColor.GetColor("#57AB27")
colorRwthRot		= TColor.GetColor("#CC071E")
colorRwthOrange 	= TColor.GetColor("#F6A800")
colorRwthViolett	= TColor.GetColor("#612158")
colorRwthLila		= TColor.GetColor("#7A6FAC")

def getLabelCmsPrivateSimulation( x1ndc = 0.6, y1ndc = 0.90, x2ndc = 0.9, y2ndc = 0.93):
	labelCmsPrivateSimulation = TPaveText(x1ndc,y1ndc,x2ndc,y2ndc,"NDC")
	labelCmsPrivateSimulation.AddText("#font[62]{CMS private}, #font[72]{simulation}")
	labelCmsPrivateSimulation.SetBorderSize(1)
	labelCmsPrivateSimulation.SetFillColor(0) # 0 == White
	return labelCmsPrivateSimulation

def drawLabelCmsPrivateSimulation( x1ndc = 0.6, y1ndc = 0.90, x2ndc = 0.9, y2ndc = 0.93):
	label = getLabelCmsPrivateSimulation(x1ndc,y1ndc,x2ndc,y2ndc)
	label.Draw()
	return label

def getLabelCmsPrivateData( x1ndc = 0.6, y1ndc = 0.90, x2ndc = 0.9, y2ndc = 0.93):
	labelCmsPrivateSimulation = TPaveText(x1ndc,y1ndc,x2ndc,y2ndc,"NDC")
	labelCmsPrivateSimulation.AddText("#font[62]{CMS private}, #font[72]{2015 data}")
	labelCmsPrivateSimulation.SetBorderSize(1)
	labelCmsPrivateSimulation.SetFillColor(0) # 0 == White
	return labelCmsPrivateSimulation

def drawLabelCmsPrivateData( x1ndc = 0.6, y1ndc = 0.90, x2ndc = 0.9, y2ndc = 0.93):
	label = getLabelCmsPrivateData(x1ndc,y1ndc,x2ndc,y2ndc)
	label.Draw()
	return label

chimney1 = TGraph()
chimney1.SetPoint(0,.3425,1.48)
chimney1.SetPoint(1,.3425,1.65)
chimney1.SetPoint(2,.435,1.65)
chimney1.SetPoint(3,.435,1.48)
chimney1.SetPoint(4,.3425,1.48)
chimney1.SetLineColor(colorRwthMagenta)
chimney1.SetLineWidth(2)

chimney2 = TGraph()
chimney2.SetPoint(0,-.3425,0.87)
chimney2.SetPoint(1,-.3425,1.22)
chimney2.SetPoint(2,-.435,1.22)
chimney2.SetPoint(3,-.435,0.87)
chimney2.SetPoint(4,-.3425,0.87)
chimney2.SetLineColor(colorRwthMagenta)
chimney2.SetLineWidth(2)

#Converts a graph in eta and phi to hcal coordinates with ieta and iphi
def convertToHcalCoords(inputGraph):
	gConvertedToiEtaiPhi = TGraph()
	gConvertedToiEtaiPhi.SetMarkerStyle(6)
	for i in range(0, inputGraph.GetN()):
		x = Double(0)
		y = Double(0)
		inputGraph.GetPoint(i,x,y)
		if( y < 0 ):
			y += 2*pi
		if( y > 2*pi ):
			y -= 2*pi
		xIEta = x/0.087 + ( 0.5 if x > 0 else -0.5 )
		yIPhi = y/0.087 + 1
		gConvertedToiEtaiPhi.SetPoint(i,xIEta,yIPhi)
	gConvertedToiEtaiPhi.GetXaxis().SetTitle("i#eta")
	gConvertedToiEtaiPhi.GetYaxis().SetTitle("i#phi")
	return gConvertedToiEtaiPhi

def drawHcalBoxesHcalCoords(canvas):
	canvas.cd()
	boxes = []
	for i in range(-15,15):
		for j in range(0,72):
			box = TBox(i,j,(i+1),(j+1))
			box.SetFillStyle(0)
			box.SetLineColor(colorRwthMagenta)
			box.SetLineWidth(2)
			box.Draw()
			boxes.append(box)
	return boxes

def drawHoBoxes(canvas):
	canvas.cd()
	boxes = []
	for i in range(-1,2):
		for j in range(-1,2):
			box = TBox(i*0.087 - 0.0435,j*0.087 - 0.0435,(i*0.087+0.0435),(j*0.087+0.0435))
			box.SetFillStyle(0)
			box.SetLineColor(colorRwthMagenta)
			box.SetLineWidth(3)
			box.Draw()
			boxes.append(box)
	return boxes

def setPlotStyle():
	gStyle.SetPadGridX(1)
	gStyle.SetPadGridY(1)
	gStyle.SetOptStat(1110)
	gStyle.SetLineWidth(2)
	gStyle.SetHistLineWidth(3)
	gStyle.SetPadTickX(1)
	gStyle.SetPadTickY(1)
	gStyle.SetTextFont(62)
	gStyle.SetLabelFont(62)
	gStyle.SetTitleFont(62)
	gStyle.SetLegendBorderSize(1)
	gStyle.SetLegendFont(62)
#	gStyle.SetFillColor(0)
	gStyle.SetPalette(1)

#Set all Axes to bold font
def setupAxes(plot):
	
	if plot.__class__ == TEfficiency:
		plot = plot.GetPaintedGraph()
	plot.GetXaxis().SetTitleFont(62)
	plot.GetYaxis().SetTitleFont(62)
	plot.GetXaxis().SetLabelFont(62)
	plot.GetYaxis().SetLabelFont(62)
	# Check for the function. Otherwise it crashes with TGraphs
	if hasattr(plot, 'GetZaxis'):
		plot.GetZaxis().SetTitleFont(62)
		plot.GetZaxis().SetLabelFont(62)

#Set the stat box display Options
def setStatBoxOptions(plot,option):
	stats = plot.GetListOfFunctions().FindObject("stats")
	stats.SetOptStat(option)

#Set the stat box position
def setStatBoxPosition(plot,x1 = 0.7, x2 = 0.9, y1 = 0.75, y2 = 0.9):
	stats = plot.GetListOfFunctions().FindObject("stats")
	stats.SetX1NDC(x1)
	stats.SetX2NDC(x2)
	stats.SetY1NDC(y1)
	stats.SetY2NDC(y2)

def setupPalette(plot):
	#Set as many color palette divisions as possible
	plot.SetContour(99)
	#make the palette as small as possible
	pal = plot.GetListOfFunctions().FindObject("palette")
	pal.SetX2NDC(0.92)

#Function that returns a new TH2D with the axes already set up
def getTH2D(name,title,nBinsX,xLow,xHigh,nBinsY,yLow,yHigh):
	hist = TH2D(name,title,nBinsX,xLow,xHigh,nBinsY,yLow,yHigh)
	setupAxes(hist)
	return hist

#Function that returns a new TH2D with the axes already set up
def getTH1D(name,title,nBinsX,xLow,xHigh):
	hist = TH1D(name,title,nBinsX,xLow,xHigh)
	setupAxes(hist)
	return hist

def calcSigma(num,denom):
	return sqrt(num/float(denom*denom) + num*num/float(pow(denom, 3)))

#Output function for the progress in a python script
def printProgress(done,total):
	s = getProgressString(done, total)
	sys.stdout.write(s)
	sys.stdout.flush()
	pass

#Output function for the progress in a python script
def getProgressString(done,total):
	nHashes = int(done/float(total)*80)
	progressbar = '\r[%s%s] %5.2f%% done.' % (nHashes*'#',(80-nHashes)*' ',done*100/float(total))
	return progressbar

def pyplotCmsPrivateLabel(ax,x=0.995,y=0.945):
	plt.text(x, y, r'$\mathbf{CMS}$ private, $\mathit{simulation}$',
        horizontalalignment='right',
        verticalalignment='bottom',
        transform=ax.transAxes,
        bbox=dict(facecolor='white'))