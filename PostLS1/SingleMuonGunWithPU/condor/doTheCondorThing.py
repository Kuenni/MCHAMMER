#!/usr/bin/python

# Creates job descriptions and submits them to condor
# The delta R and e thr ranges and step sizes have to be set here

import sys,os
import numpy as np
from subprocess import call
from shutil import copy

DELTA_R_START=0
DELTA_R_END=0.35
DELTA_R_STEPSIZE=0.025

E_THR_START = 0
E_THR_END = 0.35
E_THR_STEPSIZE = DELTA_R_STEPSIZE

matchTypes 	= ["byDeltaR","byECone"]
deltaRList 	= np.arange(DELTA_R_START,DELTA_R_END,DELTA_R_STEPSIZE)
eThrList 	= np.arange(E_THR_START,E_THR_END,E_THR_STEPSIZE)


# Prepare options from CLI
from optparse import OptionParser

parser = OptionParser()
parser.add_option("--parameters", dest="parameters", help="Give a combination of parameters. Only this combination will be sent to condor."\
				"The keys have to be deltaR,eThr and match. E.g. \"deltaR:<val>,eThr:<val>,match:<val>\""
				,type="str",default = -1)
parser.add_option("--dryRun", dest="dryRun",help="Run the script but do not actually submit to condor.",action="store_true",default=False)

(options, args) = parser.parse_args()
if options.parameters != -1:
	parameterDict = dict((key,value) for key,value in( item.split(':') for item in options.parameters.split(',')))
	print 'Using these parameters:'
	print parameterDict
	matchTypes = [parameterDict["match"]]
	deltaRList = [float(parameterDict["deltaR"])]
	eThrList = [float(parameterDict["eThr"])]
else:
	print 'Processing all'

progressCounter = 0
totalActionsCounter = len(matchTypes)*len(deltaRList)*len(eThrList)


#First gather some necessary files from the top level directories

if( not os.path.exists('additionalFiles')):
	os.mkdir('additionalFiles')
if( not os.path.exists('additionalFiles/headers')):
	os.mkdir('additionalFiles/headers')

print 'Copy PlotStyle.py'
copy('../../../python/PlotStyle.py','additionalFiles')
print 'Copy matchingLibrary.py'
copy('../../../python/matchingLibrary.py','additionalFiles')
print 'Copy headers for structs in ROOT'
copy('../../../hoTriggerAnalyzer/interface/GenMuonData.h','additionalFiles/headers')
copy('../../../hoTriggerAnalyzer/interface/L1MuonData.h','additionalFiles/headers')
copy('../../../hoTriggerAnalyzer/interface/HoRecHitData.h','additionalFiles/headers')
print 'Copy L1MuonHistogram.root'
copy('../L1MuonHistogram.root','additionalFiles')

print
print 'Create loader.C'
loaderC = open('../loader.C','r')
newLoaderC = open('additionalFiles/loader.C','w')
for line in loaderC:
	if line.find('GenMuonData.h') != -1:
		newLoaderC.write('#include "headers/GenMuonData.h"\n')
	elif line.find('L1MuonData.h') != -1:
		newLoaderC.write('#include "headers/L1MuonData.h"\n')
	elif line.find('HoRecHitData.h') != -1:
		newLoaderC.write('#include "headers/HoRecHitData.h"\n')
	else:
		newLoaderC.write(line)
print
print 'Creating job descriptions%s:' % ( ' and submitting condor jobs' if not options.dryRun else '' )

if( not os.path.exists('jdlFiles')):
	os.mkdir('jdlFiles')

if( not os.path.exists('log')):
	os.mkdir('log')

for matchType in matchTypes:
	for deltaR in deltaRList:
		for eThr in eThrList:
			progressCounter += 1
			replaceDict = {
						"@DELTA_R@":str(deltaR),
						"@E_THR@":str(eThr),
						"@MATCH_TYPE@":str(matchType)
			}
			infile = open('jobDescriptionTemplate.jdl','r')
			filename = 'jdlFiles/%s-DeltaR%1d_%03d-EThr%1d_%03d.jdl' % (matchType,int(deltaR),int(deltaR*1000),int(eThr),int(eThr*1000))
			outfile = open(filename,'w')
			for line in infile.readlines():
				for src, target in replaceDict.iteritems():
					line = line.replace(src, target)
				outfile.write(line)
			infile.close()
			outfile.close()
			submitCommand = 'condor_submit ' + filename
			if not options.dryRun:
				ret = call(submitCommand, shell=True, stdout=open(os.devnull, 'wb'),stderr=open(os.devnull, 'wb'))
				if ret != 0:
					print
					print 'Something went wrong on submitting. Abort!'
					sys.exit(1)
			nHashes = progressCounter*100/totalActionsCounter*80/100
			progressbar = '\r[%s%s] %5.2f%% done.' % (nHashes*'#',(80-nHashes)*' ',progressCounter*100/float(totalActionsCounter))
			sys.stdout.write(progressbar)
			sys.stdout.flush()
print
print 'Submitted %d condor jobs.' % (totalActionsCounter)