#! /usr/bin/env python2
import cesubmit
import os,sys,math
import time
import glob
import subprocess
import logging
logging.basicConfig(level=logging.WARNING)
logger = logging.getLogger(__name__)
import ConfigParser
import argparse

import gridlib.ce
import gridlib.se

class Submitter(gridlib.ce.ProxyDelegator,gridlib.se.GridpackManager):
	
	def __init__(self, site, nJobs, batchNumber = 1):
		# Since both the ProxyDelegator and GridpackManager have the same
		# constructor, it suffices to call one of them.
		super(Submitter, self).__init__(gridlib.se.StorageElement(site))
		self.taskName = os.path.abspath(os.path.curdir).split('/')[-1]
		self.cmsswVersion = 'CMSSW_7_4_15'
		self.scramArch='slc6_amd64_gcc491'
		self.nJobs = nJobs
		self.gridPackName = 'muMinusPuProduction.tar.gz'
		self.additionalGridPackContents = []
		#Adds possibility to split up production in several batches
		self.batchNumber = batchNumber

	def addGridPackContent(self,filename):
		self.additionalGridPackContents.append(filename)
	
	def setGridPackName(self,gridPackName):
		self.gridPackName = gridPackName
		
	def getStatus(self):
		taskDir = '/user/kuensken/tapasTasks/'
		for dir in os.listdir(taskDir):
			if not dir.startswith(self.taskName):
				continue
			print '\ttaskDirs: ',dir
		#	task=cesubmit.Task(dir,directory = '/user/kuensken/tapasTasks/' + dir,cmsswVersion=self.cmsswVersion, scramArch=self.scramArch)
		#	task.getStatus()
		
	def createTempExe(self):
		tempExe = '''
	cmsRun $1
	RET=$?
	if [ $RET -eq 0 ]; then
		uberftp grid-srm "cd /pnfs/physik.rwth-aachen.de/cms/store/user/akunsken/SingleMuPU52-VtxZero; put $2" 
		echo "Finished execution";
	else
		exit $RET;
	fi
	'''
		tempFile = open('exec.sh','w')
		tempFile.write(tempExe)
		tempFile.close()
		
	def submit(self):
		print "Preparing task", self.taskName
		
		if not os.path.exists('configs'):
			os.mkdir('configs')		

		for j in range(0, 10):
			globalTaskId = j + self.batchNumber*10
			task = gridlib.ce.Task(
				name = self.taskName + str(globalTaskId),
				storage_element = self.storage_element,
				delegation_id = self.get_delegation_id(),
				directory = '/user/kuensken/tapasTasks/' + self.taskName + str(globalTaskId)
				)
			
			self.createTempExe()
			task.executable='exec.sh'
			task.executable_upload = False

			for i in range(1,self.nJobs+1):
				globalJobId =  globalTaskId*self.nJobs+i
				job=task.create_job()
				createRunConfig(globalJobId)
				job.arguments.append('runConfigProductionWithPu_' + str(globalJobId) + '.py')
				job.arguments.append('SingleMuWithPu52_' + str(globalJobId) + '.root')
				job.inputfiles = [os.path.abspath(os.path.curdir) + '/configs/runConfigProductionWithPu_' + str(globalJobId) + '.py',
								os.path.abspath('exec.sh')]
			task.submit(6)
		print "[Done]"

#create the cms run cfgs
def createRunConfig(instance):
	outfileName = 'configs/runConfigProductionWithPu_' + str(instance) + '.py'
	#Use a dedicated cfg template if given
	configTemplate = 'runConfigProductionWithPu_template.py'
	with open(configTemplate) as infile:
		with open(outfileName,'w') as outfile:
			for line in infile.readlines():
				line = line.replace('%INSTANCE%', str(instance))
				outfile.write(line)
		outfile.close()
	infile.close()
	print 'Created config', outfileName
