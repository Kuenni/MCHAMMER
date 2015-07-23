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

parser = argparse.ArgumentParser()

parser.add_argument('--nJobs'
                    ,dest='nJobs'
                    ,type=int
                    ,required=True
                    ,help='Set the number of Jobs in the task')

parser.add_argument('--gridpackname','-g'
				,dest='gridpackname'
				,type = str
				,default='modulegridpack.tar.gz'
				,help='Set the name of the gridpack file')

args = parser.parse_args()

def main():
	name = "muonAnalyzerTask"
	print "Preparing task", name
	task=cesubmit.Task(name,cmsswVersion='CMSSW_7_2_2_patch2', scramArch='slc6_amd64_gcc481')
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
	uploadurl = cesubmit.createAndUploadGridPack(['../../loader.C','../../hoTriggerAnalyzer'],
												args.gridpackname if args.gridpackname != None else 'modulegridpack.tar.gz')
	task.addGridPack(uploadurl,extractdir="$CMSSW_BASE/src/HoMuonTrigger")
	for i in range(0,args.nJobs):
		job=cesubmit.Job()
		job.arguments.append('parallelConfig' + str(i) + '.py')
		job.inputfiles.append(os.path.abspath('configs/parallelConfig' + str(i) + '.py'))
		job.inputfiles.append(os.path.abspath('sources/sourceList' + str(i)))
		job.outputfiles.append("L1MuonHistogramPooja" + str(i) + '.root')
		task.addJob(job)
	task.submit(6)
	print "[Done]"

if __name__=="__main__":
    main()
