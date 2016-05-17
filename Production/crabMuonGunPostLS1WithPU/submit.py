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

class Submitter:
    
    def __init__(self,nJobs):
        self.taskName = os.path.abspath(os.path.curdir).split('/')[-1]
	print 'TaskName: ',self.taskName
        self.cmsswVersion = 'CMSSW_7_4_15'
        self.scramArch='slc6_amd64_gcc491'
        self.gridPackName = 'muMinusPu52Production.tar.gz'
        self.nJobs = nJobs
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
	#	task=cesubmit.Task(dir,directory = '/user/kuensken/tapasTasks/' + dir,cmsswVersion=self.cmsswVersion, scramArch=self.scramArch)
	#	task.getStatus()
        
    def submit(self):
        print "Preparing task", self.taskName
	if not os.path.exists('configs'):
		os.mkdir('configs')        
	#ls -hl
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
        
        #uploadurl = cesubmit.createAndUploadGridPack(['./','./'],self.gridPackName)
        #task.addGridPack(uploadurl,extractdir="$CMSSW_BASE/src/SimMuon")
        for j in range(0, 25):
#            output = './RunOutput' + str(j)
            task=cesubmit.Task(self.taskName + str(j),directory = '/user/kuensken/tapasTasks/' + self.taskName + str(j),cmsswVersion=self.cmsswVersion, scramArch=self.scramArch)
            task.executable=os.path.abspath('exec.sh')
            #uploadurl = cesubmit.createAndUploadGridPack(['./GenFiles','./GenFiles'],self.gridPackName)
            #task.addGridPack(uploadurl,extractdir="$CMSSW_BASE/src/SimMuon")
            for i in range(1,self.nJobs+1): 
                job=cesubmit.Job()
		createRunConfig(j*self.nJobs+i)
                job.arguments.append('runConfigProductionWithPu_' + str(j*self.nJobs+i) + '.py')
                job.arguments.append('SingleMuWithPu52_' + str(j*self.nJobs+i) + '.root')
                job.inputfiles = [os.path.abspath(os.path.curdir) + '/configs/runConfigProductionWithPu_' + str(j*self.nJobs+i) + '.py']
#		job.outputfiles.append(output)
                task.addJob(job)
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
