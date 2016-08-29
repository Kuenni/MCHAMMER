#! /usr/bin/env python2
import cesubmit
import os
import logging
import gridlib.ce
import gridlib.se
import glob

logging.basicConfig(level=logging.WARNING)
logger = logging.getLogger(__name__)


class Submitter(gridlib.ce.ProxyDelegator,gridlib.se.GridpackManager):
	
	def __init__(self, site, nJobs):
		# Since both the ProxyDelegator and GridpackManager have the same
		# constructor, it suffices to call one of them.
		super(Submitter, self).__init__(gridlib.se.StorageElement(site))
		self.taskName = os.path.abspath(os.path.curdir).split('/')[-1]
		self.cmsswVersion = 'CMSSW_7_2_2_patch2'
		self.scramArch='slc6_amd64_gcc481'
		self.gridPackName = 'modulegridpack.tar.gz'
		self.nJobs = nJobs
		self.additionalGridPackContents = []

	def addGridPackContent(self,filename):
		self.additionalGridPackContents.append(filename)
	
	def setGridPackName(self,gridPackName):
		self.gridPackName = gridPackName
		
	def createTempExe(self):
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
		return
		
	def cleanup(self):
		for f in glob.glob('./exec*.sh'):
			os.remove(f)
		
	def submit(self):
		print "Preparing task", self.taskName
		
		task = gridlib.ce.Task(
			name = self.taskName,
			storage_element = self.storage_element,
			delegation_id = self.get_delegation_id(),
			directory = '/user/kuensken/tapasTasks/' + self.taskName
		)

		
		task.executable= 'exec.sh'
		task.executable_upload = False

		self.createTempExe()
				
		tarFileUrl = "{0}/{1}.tar.gz".format('gridpacks',self.taskName)
		execTarUrl = "{0}/{1}_exec.tar.gz".format('gridpacks',self.taskName)
		
		cesubmit.createAndUploadGridPack(['../../loader.C','../../hoTriggerAnalyzer'],tarFileUrl)
		cesubmit.createAndUploadGridPack('exec.sh',execTarUrl)
		
		gridPackUrl = os.path.join('/store/user',self.username_cern,tarFileUrl)
		execGridPackUrl = os.path.join('/store/user',self.username_cern,execTarUrl)
		
		task.add_gridpack(gridPackUrl,extract_dir="$CMSSW_BASE/src/HoMuonTrigger")
		task.add_gridpack(execGridPackUrl)

		for i in range(0,self.nJobs):
			job = task.create_job()
			job.arguments.append('parallelConfig' + str(i) + '.py')
			job.inputfiles.append(os.path.abspath('configs/parallelConfig' + str(i) + '.py'))
			job.inputfiles.append(os.path.abspath('sources/sourceList' + str(i)))
			for file in self.additionalGridPackContents:
				job.inputfiles.append(os.path.abspath(file))
			job.outputfiles.append("jobOutput" + str(i) + '.root')
			
		task.submit(6)
		self.cleanup()
		print "[Done]"
		