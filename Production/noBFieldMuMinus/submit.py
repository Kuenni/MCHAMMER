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
   
	def __init__(self, site, nJobs):
		# Since both the ProxyDelegator and GridpackManager have the same
		# constructor, it suffices to call one of them.
		super(Submitter, self).__init__(gridlib.se.StorageElement(site))
		self.taskName = os.path.abspath(os.path.curdir).split('/')[-1]
		self.cmsswVersion = 'CMSSW_7_4_15'
		self.scramArch='slc6_amd64_gcc491'
		self.nJobs = nJobs
		self.gridPackName = 'muMinusNoBProduction.tar.gz'
		self.additionalGridPackContents = []
 
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

	def createTempExe(self):
		tempExe = '''
	cmsRun $1
	RET=$?
	if [ $RET -eq 0 ]; then
		uberftp grid-srm "cd /pnfs/physik.rwth-aachen.de/cms/store/user/akunsken/SingleMuMinusNoBFieldFixed; put $2" 
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

		for j in range(0, 25):
			task = gridlib.ce.Task(
				name = self.taskName + str(j),
				storage_element = self.storage_element,
				delegation_id = self.get_delegation_id(),
				directory = '/user/kuensken/tapasTasks/' + self.taskName + str(j)
				)
			
			self.createTempExe()
			task.executable='exec.sh'
			task.executable_upload = False

			for i in range(1,self.nJobs+1): 
				job=task.create_job()
				createRunConfig(j*self.nJobs+i)
				job.arguments.append('runConfigProduction_' + str(j*self.nJobs+i) + '.py')
				job.arguments.append('SingleMuPt1to200_noBField_' + str(j*self.nJobs+i) + '.root')
				job.inputfiles = [os.path.abspath(os.path.curdir) + '/configs/runConfigProduction_' + str(j*self.nJobs+i) + '.py',
								os.path.abspath('exec.sh')]
			task.submit(6)
		print "[Done]"

#create the cms run cfgs
def createRunConfig(instance):
	outfileName = 'configs/runConfigProduction_' + str(instance) + '.py'
	#Use a dedicated cfg template if given
	configTemplate = 'runConfigProduction_template.py'
	with open(configTemplate) as infile:
		with open(outfileName,'w') as outfile:
			for line in infile.readlines():
				line = line.replace('%INSTANCE%', str(instance))
				outfile.write(line)
		outfile.close()
	infile.close()
	print 'Created config', outfileName
