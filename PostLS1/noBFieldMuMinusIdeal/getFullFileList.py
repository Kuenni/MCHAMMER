#!/usr/bin/python
from subprocess import call

server = "srmls srm://grid-srm.physik.rwth-aachen.de:8443/pnfs/physik.rwth-aachen.de/cms"

lsResults = open('dcacheFiles','w+')

cmd = server + '/store/user/akunsken/SingleMuMinus/CRAB_PrivateMC/crab_noBMuMinusIdeal_DESIGN72_V5/151211_092300/0000'
call(cmd, shell=True, stdout=lsResults, stderr=open('/dev/null'))
	
lsResults.seek(0)
cmsswRunSources = open('cmsswSourceFiles','w+')

XROOTPREFIX = 'root://xrootd.unl.edu/'

for line in lsResults:
	lineStr = str(line)
	if lineStr.count('.root'):
		fileName = lineStr.split(' ')[-1].rstrip('\n')
		fileName = 'file://' + fileName
		fileName = fileName[fileName.index('/store'):]
		cmsswRunSources.write(XROOTPREFIX + fileName + '\n')


