import sys,os
sys.path.append(os.path.abspath("../../python"))

from ROOT import TFile,TCanvas

from PlotStyle import setPlotStyle,getLabelCmsPrivateSimulation
setPlotStyle()

# Plot the efficiency for matching L1 to both, GEN and HO Rec Hits
def plotHoMatchEfficiency():
	c = TCanvas("cHoEff","hoEff",1800,900)
	c.Divide(2,1)
	
	fileVaried = TFile.Open('condor/HoEff.root')
	if(fileVaried.IsZombie()):
		print 'Error opening file: condor/HoEff.root'
		sys.exit(1)
		
	fileFixed = TFile.Open('condorFixedGenDeltaR/HoEff.root')
	if(fileFixed.IsZombie()):
		print 'Error opening file: condorFixedGenDeltaR/HoEff.root'
		sys.exit(1)
		
	fileNL1Varied = TFile.Open('condor/Histtotal.root')
	fileNL1Fixed = TFile.Open('condorFixedGenDeltaR/Histtotal.root')
	
	histNL1Varied = fileNL1Varied.Get('histTotalTruth')
	histNL1Varied.SetName('histTotalTruthVaried')
	histNL1Fixed = fileNL1Fixed.Get('histTotalTruth')
	histNL1Fixed.SetName('histTotalTruthFixed')

	hVaried = fileVaried.Get('histEff')
	hVaried.SetName('histEffVaried')
	hFixed = fileFixed.Get('histEff')
	hFixed.SetName('histEffFixed')

	min = 18
	max = 100

	label = getLabelCmsPrivateSimulation()
	
	c.cd(1)
	hVaried.SetMinimum(min)
	hVaried.SetMaximum(max)
	hVaried.SetTitle('HO matched to "true" L1, GEN cone varied')
	hVaried.Draw('colz')
	label.Draw()
#	histNL1Varied.Draw('Same,box')
	c.cd(2)
	hFixed.SetMinimum(min)
	hFixed.SetMaximum(max)
	hFixed.SetTitle('HO matched to "true" L1, GEN cone fixed')
	hFixed.Draw('colz')
#	histNL1Fixed.Draw('same,box')

	label.Draw()

	c.Update()

	c.SaveAs('hoMatchEfficiency.png')
	c.SaveAs('hoMatchEfficiency.pdf')

	return c,hFixed,hVaried,fileFixed,fileVaried,histNL1Varied,histNL1Fixed,fileNL1Fixed,fileNL1Varied,label

# Plot the efficiency for L1 to GEN matching
def plotL1MatchEfficiency():
	c = TCanvas("cL1Eff","L1Eff",1800,900)
	c.Divide(2,1)
	
	fileVaried = TFile.Open('condor/L1Eff.root')
	if(fileVaried.IsZombie()):
		print 'Error opening file: condor/L1Eff.root'
		sys.exit(1)
		
	fileFixed = TFile.Open('condorFixedGenDeltaR/L1Eff.root')
	if(fileFixed.IsZombie()):
		print 'Error opening file: condorFixedGenDeltaR/L1Eff.root'
		sys.exit(1)
		
	hVaried = fileVaried.Get('histL1Eff')
	hVaried.SetName('histL1EffVaried')
	hFixed = fileFixed.Get('histL1Eff')
	
	min = 0
	max = 100

	label = getLabelCmsPrivateSimulation()
	
	c.cd(1)
	hVaried.SetMinimum(min)
	hVaried.SetMaximum(max)
	hVaried.SetTitle('L1 matched to GEN, GEN cone varied')
	hVaried.Draw('colz')
	label.Draw()
	c.cd(2)
	hFixed.SetMinimum(min)
	hFixed.SetMaximum(max)
	hFixed.SetTitle('L1 matched to GEN, GEN cone fixed')
	hFixed.Draw('colz')

	label.Draw()
	
	c.Update()

	c.SaveAs('L1MatchEfficiency.png')
	c.SaveAs('L1MatchEfficiency.pdf')
	
	return c,hFixed,hVaried,fileFixed,fileVaried,label

#Plot the fraction of HO Rec hits inside time window
def plotFractionInTimeWindow():
	c = TCanvas("cFraction","Fraction in Time Window",900,900)
	
	fileVaried = TFile.Open('condor/FractionTimeWindow.root')
	if(fileVaried.IsZombie()):
		print 'Error opening file: condor/FractionTimeWindow.root'
		sys.exit(1)
		
	hVaried = fileVaried.Get('hist')

	min = 94
	max = 99.6

	c.cd(1)
	hVaried.SetMinimum(min)
	hVaried.SetMaximum(max)
	hVaried.SetTitle('Fraction of HO Rec Hits in [-12.5,12.5], GEN cone varied')
	hVaried.Draw('colz')

	label = getLabelCmsPrivateSimulation()
	label.Draw()

	c.Update()

	c.SaveAs('fractionInTimeWindow.pdf')
	c.SaveAs('fractionInTimeWindow.png')
	
	return fileVaried,c,hVaried,label

def plotProduct():
	c = TCanvas("cProduct","product",1800,900)
	c.Divide(2,1)
	
	fileVaried = TFile.Open('condor/product.root')
	if(fileVaried.IsZombie()):
		print 'Error opening file: condor/product.root'
		sys.exit(1)
		
	fileFixed = TFile.Open('condorFixedGenDeltaR/product.root')
	if(fileFixed.IsZombie()):
		print 'Error opening file: condorFixedGenDeltaR/product.root'
		sys.exit(1)
	
	hVaried = fileVaried.Get('histEffp')
	hVaried.SetName('histEffpVaried')
	hFixed = fileFixed.Get('histEffp')
	
	min = 15
	max = 97

	label = getLabelCmsPrivateSimulation()
	
	c.cd(1)
	hVaried.SetMinimum(min)
	hVaried.SetMaximum(max)
	hVaried.SetTitle('Fraction in TimeWindow #times HO matched to "true" L1, GEN cone varied')
	hVaried.Draw('colz')
	label.Draw()
	c.cd(2)
	hFixed.SetMinimum(min)
	hFixed.SetMaximum(max)
	hFixed.SetTitle('Fraction in TimeWindow #times HO matched to "true" L1, GEN cone fixed')
	hFixed.Draw('colz')

	label.Draw()
	
	c.Update()
	
	c.SaveAs('productTimeWindowAndEfficiency.png')
	c.SaveAs('productTimeWindowAndEfficiency.pdf')
		
	return c,hVaried,hFixed,fileFixed,fileVaried,label

res2 	= plotL1MatchEfficiency()
res 	= plotHoMatchEfficiency()
res3 	= plotFractionInTimeWindow()
res4 	= plotProduct()

raw_input('-->')