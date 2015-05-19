#!/usr/bin/python

# Creates job descriptions and submits them to condor
#
# copy this file into a subdir of the directory where the CMSSW analyzer was run.
# The script assumes that the result file is called L1MuonHistogram.root
#

import sys,os
import numpy as np
from subprocess import call
from shutil import copy

# Prepare options from CLI
from optparse import OptionParser

#Callback for the option list
def get_comma_separated_args(option, opt, value, parser):
    setattr(parser.values, option.dest, [int(i) for i in value.replace(' ','').split(',')])

parser = OptionParser()
parser.add_option("--instance", dest="instance", help="Process only the given sample.",type="str",default = -1)
parser.add_option("--dryRun", dest="dryRun",help="Run the script but do not actually submit to condor.",action="store_true",default=False)
parser.add_option('--instanceList',type='string',action='callback',callback=get_comma_separated_args,dest = 'instanceList')
(options, args) = parser.parse_args()
if options.instance != -1:
	print 'Processing instance: %s' % options.instance
elif options.instanceList != None:
	print 'Processing instances:'
	print options.instanceList
else:
	print 'Processing all'

progressCounter = 0

#First gather somenecessary files from the top level directories
if( not os.path.exists('additionalFiles')):
	os.mkdir('additionalFiles')
if( not os.path.exists('additionalFiles/headers')):
	os.mkdir('additionalFiles/headers')
if( not os.path.exists('additionalFiles/data')):
	os.mkdir('additionalFiles/data')
	
print 'Copy PlotStyle.py'
copy('../../../python/PlotStyle.py','additionalFiles')
print 'Copy matchingLibrary.py'
copy('../../../python/matchingLibrary.py','additionalFiles')
print 'Copy headers for structs in ROOT'
copy('../../../hoTriggerAnalyzer/interface/GenMuonData.h','additionalFiles/headers')
copy('../../../hoTriggerAnalyzer/interface/L1MuonData.h','additionalFiles/headers')
copy('../../../hoTriggerAnalyzer/interface/HoRecHitData.h','additionalFiles/headers')
print 'Copy loader.C'
copy('/user/kuensken/CMSSW/CMSSW_7_2_2_patch2/src/HoMuonTrigger/condorBase/loader.C','additionalFiles')
print 'Copy analyzeFull.py'
copy('/user/kuensken/CMSSW/CMSSW_7_2_2_patch2/src/HoMuonTrigger/condorBase/analyzeFull.py','.')
print 'Copy liveDisplay.py'
copy('/user/kuensken/CMSSW/CMSSW_7_2_2_patch2/src/HoMuonTrigger/condorBase/liveDisplay.py','.')
print 'Copy treeSplitter'
copy('/user/kuensken/CMSSW/CMSSW_7_2_2_patch2/src/HoMuonTrigger/condorBase/treeSplitter','.')


print 'Do you want to copy L1MuonHistogram.root?'
while(True):
	input = raw_input('Y/N?')
	if input == 'Y' or input == 'y':
		try:
			copy('../L1MuonHistogram.root','additionalFiles')
		except IOError,e:
			print "Unable to copy file. %s" % e
			sys.exit(1)
		else:
			print 'OK'
		break
	else:
		break
print
print 'Do you want to re-split L1MuonHistogram?'
print
while(True):
	input = raw_input('Y/N?')
	if input == 'Y' or input == 'y':
		print 'Splitting L1MuonHistogram.root'
		ret = call("./treeSplitter", shell=True)
		if ret != 0:
			print 'Error while splitting tree!'
			sys.exit(1)
		break
	else:
		break
N_FILES = len(os.listdir('additionalFiles/data'))

print
print 'Creating job descriptions%s:' % ( ' and submitting condor jobs' if not options.dryRun else '' )

if( not os.path.exists('jdlFiles')):
	os.mkdir('jdlFiles')

if( not os.path.exists('log')):
	os.mkdir('log')

#Set the range of instances
instanceRange = range(0,N_FILES)
if options.instanceList != None:
	instanceRange = options.instanceList
	N_FILES = len(instanceRange)
	
for i in instanceRange:
	progressCounter += 1
	if(options.instance != -1):
		i = int(options.instance)
	infile = open('/user/kuensken/CMSSW/CMSSW_7_2_2_patch2/src/HoMuonTrigger/condorBase/jobDescriptionTemplate.jdl','r')
	filename = 'jdlFiles/analyzeDeltaTime_%d.jdl' % (i)
	outfile = open(filename,'w')
	#Generate jdl file
	for line in infile.readlines():
		line = line.replace('%INSTANCE%', str(i))
		outfile.write(line)
	outfile.close()
	infile.close()
	submitCommand = 'condor_submit ' + filename
	if not options.dryRun:
		ret = call(submitCommand, shell=True, stdout=open("condor_submit.out", 'a'),stderr=open("condor_submit.err", 'a'))
		if ret != 0:
			print
			print 'Something went wrong on submitting. Abort!'
			sys.exit(1)
	#If a single instance was requested, submit only that one
	if options.instance != -1:
		break
	nHashes = progressCounter*100/N_FILES*80/100
	progressbar = '\r[%s%s] %5.2f%% done.' % (nHashes*'#',(80-nHashes)*' ',progressCounter*100/float(N_FILES))
	sys.stdout.write(progressbar)
	sys.stdout.flush()
	
print
if options.instance == -1:
	print 'Submitted %d condor jobs.' % (N_FILES)
else:
	print 'Submitted condor job with instance %s' % options.instance
	