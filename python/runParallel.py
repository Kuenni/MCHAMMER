#! /usr/bin/python

import os,sys,math
from subprocess import call
import argparse
'''
Creates the run configs with the different subsets of samples
as well as the files with the subsets

Uses the TAPAS library from Aachen 3A Music

The input file for the event sources is a file "cmsswSourceFiles" which is
created by the script fileRetriever.py

The script takes as a parameter the number of jobs to prepare with the
paths to the samples

Created: 24. 06. 2015
Author: Andreas Kuensken <kuensken@physik.rwth-aachen.de>

'''

cmsswSourceFiles = 'cmsswSourceFiles'
outputFileTrunk = 'sourceList'

print 

prefix = '[runParallel]'
def output(outString):
	print prefix,outString

def printProgress(done,total):
	nHashes = done/total*80
	progressbar = '\r[%s%s] %5.2f%% done.' % (nHashes*'#',(80-nHashes)*' ',done*100/float(total))
	sys.stdout.write(progressbar)
	sys.stdout.flush()

configTemplate = os.environ['HOMUONTRIGGER_BASE'] + '/python/runConfig_template.py'
	
parser = argparse.ArgumentParser()

parser.add_argument('--nJobs','-n'
					,dest='nJobs'
					,type=int
					,default = 10
					,help='Create N jobs')

parser.add_argument('--test'
					,dest='test'
					,action="store_true",default=False
					,help='Only submit one job for testing')

args = parser.parse_args()

if not args.nJobs and not args.test:
	output('If no test run is requested, the number of jobs has to be set!')
	parser.print_help()
	sys.exit(1)

#Get the number of lines in a file
def getLineCount(filename):
	with open(filename) as f:
		for i, l in enumerate(f):
			pass
	return i + 1

#Create the necessary output dirs
def createDirectories():
	if not os.path.exists('configs'):
		output('Creating folder "configs"')
		os.mkdir('configs')
	if not os.path.exists('sources'):
		output('Creating folder "sources"')
		os.mkdir('sources')
		
#call the other script
def createSourceLists():
	if not os.path.exists(cmsswSourceFiles):
		output('Error! File %s does not exist!' % (cmsswSourceFiles))
		sys.exit(1)
	nSourceFiles = getLineCount(cmsswSourceFiles)
	#round the number
	nSourcesPerFile = math.ceil(nSourceFiles/args.nJobs)
	output('Creating %d source files' % (args.nJobs))
	output('Found %d sample files in total.' % nSourceFiles)
	output('\t=> %d sources per file' % nSourcesPerFile)
	
	#loop over sources and create the new files
	with open(cmsswSourceFiles,'r') as f:
		outFile = None
		iterationCounter = 0
		for i,line in enumerate(f):
			if i % nSourcesPerFile == 0:
				if outFile != None:
					outFile.close()
				outFile = open('sources/' + outputFileTrunk + str(iterationCounter),'w')
				iterationCounter += 1
			outFile.write(line)
			if args.test:
				break
	outFile.close()

#create the cms run cfgs
def createRunConfigs():
	for i in range(0,args.nJobs):
		outfileName = 'configs/parallelConfig%d.py' % (i)
		with open(configTemplate) as infile:
			with open(outfileName,'w') as outfile:
				for line in infile.readlines():
					line = line.replace('%INSTANCE%', str(i))
					outfile.write(line)
				outfile.close()
				infile.close()
	output('Created configs')
	pass

#Eventually send the jobs
def sendJobs():
	ret = call(['submit.py','--nJobs',str(1 if args.test else args.nJobs)]			)
	if ret:
		output('Something went wrong while creating the sample file lists!')
	sys.exit(1)

def main():
	createDirectories()
	createSourceLists()
	createRunConfigs()
	sendJobs()

if __name__=="__main__":
	main()
