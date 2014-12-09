from ROOT import gROOT,gStyle

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