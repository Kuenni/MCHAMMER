from ROOT import gROOT,gStyle, TColor, TPaveText, TGraph, ROOT, Double, TBox
from math import sqrt,pi

colorRwthMagenta 	= TColor.GetColor("#E30066")
colorRwthLightBlue 	= TColor.GetColor("#8EBAE5")
colorRwthDarkBlue 	= TColor.GetColor("#00549F")

def getLabelCmsPrivateSimulation( x1ndc = 0.6, y1ndc = 0.90, x2ndc = 0.9, y2ndc = 0.93):
	labelCmsPrivateSimulation = TPaveText(x1ndc,y1ndc,x2ndc,y2ndc,"NDC")
	labelCmsPrivateSimulation.AddText("#font[62]{CMS private}, #font[72]{simulation}")
	labelCmsPrivateSimulation.SetBorderSize(1)
	labelCmsPrivateSimulation.SetFillColor(0) # 0 == White
	return labelCmsPrivateSimulation

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

def calcSigma(num,denom):
	return sqrt(num/(denom*denom) + num*num/(pow(denom, 3)))
