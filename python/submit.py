#! /usr/bin/env python2
import cesubmit
import os
import time
import glob
import subprocess
import logging
logging.basicConfig(level=logging.WARNING)
logger = logging.getLogger(__name__)
import ConfigParser
import argparse

class Submitter:
	
	def __init__(self,nJobs):
		self.taskName = "muonAnalyzerTask"
		self.cmsswVersion = 'CMSSW_7_2_2_patch2'
		self.scramArch='slc6_amd64_gcc481'
		self.gridPackName = 'modulegridpack.tar.gz'
		self.nJobs = nJobs
		self.additionalGridPackContents = []

	def addGridPackContent(self,filename):
		self.additionalGridPackContents.append(filename)
	
	def setGridPackName(self,gridPackName):
		self.gridPackName = gridPackName
		
	def submit(self):
		print "Preparing task", self.taskName
		task=cesubmit.Task(self.taskName,cmsswVersion=self.cmsswVersion, scramArch=self.scramArch)
	  	tempExe = '''
	cmsRun $1
	RET=$?
	if [ $RET -eq 0 ]; then
		echo "Finished execution";
	else
		exit $RET;
	fi
	'''
		tempFile = open('exec.sh','w')
		tempFile.write(tempExe)
		tempFile.close()
		task.executable=os.path.abspath('exec.sh')
		uploadurl = cesubmit.createAndUploadGridPack(['../../loader.C','../../hoTriggerAnalyzer'],self.gridPackName)
		task.addGridPack(uploadurl,extractdir="$CMSSW_BASE/src/HoMuonTrigger")
		for i in range(0,self.nJobs):
			job=cesubmit.Job()
			job.arguments.append('parallelConfig' + str(i) + '.py')
			job.inputfiles.append(os.path.abspath('configs/parallelConfig' + str(i) + '.py'))
			job.inputfiles.append(os.path.abspath('sources/sourceList' + str(i)))
			for file in self.additionalGridPackContents:
				job.inputfiles.append(os.path.abspath(file))
			job.outputfiles.append("jobOutput" + str(i) + '.root')
			task.addJob(job)
		task.submit(6)
		print "[Done]"
