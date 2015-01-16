from ROOT import gROOT,gStyle, TColor, TPaveText

colorRwthMagenta 	= TColor.GetColor("#E30066")
colorRwthLightBlue 	= TColor.GetColor("#8EBAE5")
colorRwthDarkBlue 	= TColor.GetColor("#00549F")

labelCmsPrivateSimulation = TPaveText(0.1,0.901,0.4,0.93,"NDC")
labelCmsPrivateSimulation.AddText("#font[62]{CMS private}, #font[72]{simulation}")
labelCmsPrivateSimulation.SetBorderSize(1)
labelCmsPrivateSimulation.SetFillColor(0) # 0 == White

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