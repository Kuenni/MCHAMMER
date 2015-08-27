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

globalTags = {
			'noPU':'autoCond[\'run2_mc\']',
			'pu52':'\'PHYS14_25_V1::All\''
			}

print 

prefix = '[runParallel]'
def output(outString):
	print prefix,outString

def printProgress(done,total):
	s = getProgressString(done, total)
	sys.stdout.write(s)
	sys.stdout.flush()
	pass
	
def getProgressString(done,total):
	nHashes = int(done/float(total)*80)
	progressbar = '\r[%s%s] %5.2f%% done.' % (nHashes*'#',(80-nHashes)*' ',done*100/float(total))
	return progressbar

configTemplate = os.environ['HOMUONTRIGGER_BASE'] + '/python/runConfig_template.py'
	
parser = argparse.ArgumentParser()

parser.add_argument('--nJobs','-n'
					,dest='nJobs'
					,type=int
					,help='Create N jobs')

parser.add_argument('--test'
					,dest='test'
					,action="store_true",default=False
					,help='Only submit one job for testing')

parser.add_argument('--collect','-c'
				,dest='collect'
				,action='store_true',default=False
				,help='Gather the results from running on CEs')

parser.add_argument('--dir','-d'
				,dest='dir'
				,help='Set the name of the directory to process on collecting the events (should be the same as the task name)')

parser.add_argument('--outfile','-o'
				,dest='outfile'
				,type = str
				,default='L1MuonHistogram.root'
				,help='Set the name of the output file when collecting the results')

parser.add_argument('--split-every','-s'
				,dest='split'
				,type = int
				,default= 25
				,help='Set the number of files after whose merging to create a new root file')

parser.add_argument('--gridpackname','-g'
				,dest='gridpackname'
				,type = str
				,default='modulegridpack.tar.gz'
				,help='Set the name of the gridpack file')

parser.add_argument('--no-submit'
				,dest='noSubmit'
				,action="store_true",default=False
				,help='Do not submit jobs to CE')

parser.add_argument('--no-pu'
				,dest='noPu'
				,action="store_true",default=False
				,help='Use no pileup case')

parser.add_argument('--pu'
				,dest='withPu'
				,action="store_true",default=False
				,help='Use PU 52 case')


args = parser.parse_args()

if not args.nJobs and not args.test and not args.collect:
	output('If no test run is requested, the number of jobs has to be set!')
	parser.print_help()
	sys.exit(1)

def hasJobFailed(resultsPath):
	errFile = open(os.path.abspath(resultsPath) + '/out.txt')
	for line in errFile.readlines():
		if line.find('Finished execution') != -1:
			return False
	return True

def collectOutput():
	fileBatches = []
	filesToProcess = []
	if not args.dir:
		output('You have to provide the task directory')
		sys.exit(1)
	for sourceFile in os.listdir(args.dir):
		if len(filesToProcess) == args.split:
			fileBatches.append(filesToProcess)
			filesToProcess = []
		if sourceFile.startswith('grid'):
			sourceFile = os.path.abspath(args.dir + '/' + sourceFile)
			if not hasJobFailed(sourceFile):
				for result in os.listdir(sourceFile):
					if result.endswith('.root'):
						filesToProcess.append(sourceFile + '/' + result)
	if(len(filesToProcess) != 0):
		fileBatches.append(filesToProcess)
	filenameTrunk = args.outfile[0:args.outfile.rfind('.root')]
	for i,batch in enumerate(fileBatches):
		filename = '%s%d.root' % (filenameTrunk,i)
		output('Merging into file %s' % filename)
		cmd = ['hadd',filename]
		cmd.extend(batch)
		ret = call(cmd)
		if ret != 0:
			output('Error on merging root files')
			sys.exit(1)
		else:
			output('All files merged')
			output(getProgressString(i+1, len(fileBatches)))
	
	
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
	gt = None
	if args.noPu:
		gt = globalTags['noPU']
	elif args.withPu:
		gt = globalTags['pu52']
	else:
		output('ERROR! Don\'t know which globaltag to use')
		sys.exit(-1)
	for i in range(0,args.nJobs):
		outfileName = 'configs/parallelConfig%d.py' % (i)
		with open(configTemplate) as infile:
			with open(outfileName,'w') as outfile:
				for line in infile.readlines():
					line = line.replace('%INSTANCE%', str(i))
					line = line.replace('%GLOBALTAG%',gt)
					outfile.write(line)
				outfile.close()
				infile.close()
	output('Created configs')
	pass

#Eventually send the jobs
def sendJobs():
	cmdList = ['submit.py','--nJobs',str(1 if args.test else args.nJobs)]
	if args.gridpackname != None:
		cmdList.extend(['--gridpackname',args.gridpackname])
	ret = call(cmdList)
	if ret:
		output('Something went wrong while creating the sample file lists!')
	sys.exit(1)

def main():
	if args.nJobs or args.test:
		createDirectories()
		createSourceLists()
		createRunConfigs()
		if not args.noSubmit:
			sendJobs()
		else:
			output('As requested, no jobs were submitted.')
	else:
		collectOutput()

if __name__=="__main__":
	main()
