#!/usr/bin/python

import re
import sys,os
import argparse
from subprocess import call

#Initialize the argparser module
parser = argparse.ArgumentParser(description='Tool for copying files from dCache, merging to one root file and moving to net_scratch.')
parser.add_argument('--copy'
                    ,dest='copy'
                    ,action='store_true'
                    ,help='Copy files from dCache.')
parser.add_argument('--dcache-dir'
                    ,dest='dCacheDir'
                    ,type=str
                    ,help='Manually provide the dCache directory containing the data')
parser.add_argument('--desy'
                    ,dest='useDesy'
                    ,action='store_true'
                    ,help='Use a different server for copying to access data on DESY T2')
parser.add_argument('--rwth'
                    ,dest='useRwth'
                    ,action='store_true'
                    ,help='Use a different server for copying to access data on RWTH T2')
parser.add_argument('--net-scratch'
                    ,dest='useNetScratch'
                    ,action='store_true'
                    ,help='Use local /net/scratch dir as source folder')
parser.add_argument('--merge'
                    ,dest='merge'
                    ,action='store_true'
                    ,help='Merge files to one edm root file.')
parser.add_argument('--remove-originals'
                    ,dest='removeOriginals'
                    ,action='store_true'
                    ,help='If --merge option is given, remove the source files after merging.')
parser.add_argument('--merge-root-files'
                    ,dest='mergeRootFiles'
                    ,action='store_true'
                    ,help='If --merge option is given, use hadd for merging instead of edmCopyPickMerge.')
parser.add_argument('--merge-list'
                    ,dest='mergeList'
                    ,help='Give a list of files that are used for merging instead of using the default list.')
parser.add_argument('--move'
                    ,dest='move'
                    ,action='store_true'
                    ,help='Move files to directory under net_scratch')
parser.add_argument('--all'
                    ,dest='all'
                    ,action='store_true'
                    ,help='Enable all of the options')
parser.add_argument('-N'
                    ,dest='nFilesToCopy'
                    ,type=int
                    ,help='Copy only n files from dest. dir')
parser.add_argument('--target-dir'
                    ,dest='targetDir'
                    ,type=str
                    ,help='Give a target dir for the copy operation. Merging will probably not work with this')
parser.add_argument('--create-file-list'
                    ,dest='createFileList'
                    ,action='store_true'
                    ,help='Create a text file with dcache content that can be processed by a CMSSW run config')
args = parser.parse_args()


#local variables for storing arg switches and variables
copy = args.copy
dCacheDir = args.dCacheDir

merge = args.merge
removeOriginals = args.removeOriginals
mergeList = args.mergeList
mergeRootFiles = args.mergeRootFiles

nFilesToCopy = args.nFilesToCopy
targetDir = args.targetDir
useDesy = args.useDesy
useRwth = args.useRwth
useNetScratch = args.useNetScratch

createFileList = args.createFileList

move = args.move

all = args.all

if all:
    copy = True
    merge = True
    move = True
else:
    if not (copy or merge or move or createFileList):
        print 'Error! Program requires at least one parameter!'
        parser.print_help()
        sys.exit(3)

#define prefix for lcg copy from desy
DESYSERVER = 'srm://dcache-se-cms.desy.de:8443'
DESYT2PREFIX = 'srm://dcache-se-cms.desy.de:8443/srm/managerv2?SFN=/pnfs/desy.de/cms/tier2'
RWTHSERVER = 'srm://grid-srm.physik.rwth-aachen.de:8443'
RWTHT2PREFIX = 'srm://grid-srm.physik.rwth-aachen.de:8443/pnfs/physik.rwth-aachen.de/cms'
#Get dev null for call later on
DEVNULL = open(os.devnull, 'wb')

#Give java more memory. Otherwise srmls fails on large lists of files
os.environ['SRM_JAVA_OPTIONS'] = '-Xms256m -Xmx256m'

#Find out, where the script is running
sampleName = ''
if(dCacheDir != None):
    sampleName = dCacheDir
    print 'Manual dCacheDir given: ' + sampleName

else:
    curDir = str(os.getcwd())
    curDirParts = curDir.split('/')
    sampleName = curDirParts[-1]
    print 'Found program running in directory: ' + sampleName


def createFileList():
    print 'Creating filelist'
    server = ''
    if useDesy:
        server = DESYT2PREFIX
    elif useNetScratch:
    	server=''
    else:
        server = RWTHT2PREFIX
    
    sourceDir = server + sampleName
        
    #Build command to check for dir on T2
    print 'Testing whether sample name directory exists on dcache...'
    print 'Directory:',sourceDir
    cmd = "srmls " + sourceDir
    if useNetScratch:
    	cmd = 'find ' + sourceDir + ' -name \"*.root\"'
        
    #Get the list of files in the source directory
    lsResults = open('dcacheFiles','w+')
    ret = call(cmd, shell=True, stdout=lsResults, stderr=DEVNULL)
    lsResults.seek(0)
    
    if ret != 0 and not useNetScratch:
        print 'Fail! Requested directory does not exist.'
        sys.exit(1)
    else:
        print 'Success!'

    cmsswRunSources = open('cmsswSourceFiles','w+')

    XROOTPREFIX = 'root://xrootd.unl.edu/'
    if(useNetScratch):
		XROOTPREFIX = ''
    for line in lsResults:
    	print line
        lineStr = str(line)
        if lineStr.count('.root'):
            fileName = lineStr.split(' ')[-1].rstrip('\n')
            fileName = 'file://' + fileName
            if useDesy or useRwth:
            	fileName = fileName[fileName.index('/store'):]
            cmsswRunSources.write(XROOTPREFIX + fileName + '\n')
    return

def copyDoNotUseDesy():
    print "Copy, from RWTH T2"
    #define the username on the T2 Storage element
    USERNAME="akunsken"
    
    # Create output directory variable
    
    RWTHSERVER="srm://grid-srm.physik.rwth-aachen.de:8443"
    OUTPUT_DIR=RWTHT2PREFIX + "/store/user/" + USERNAME + "/" + sampleName + "/" + STORAGE_DIR
    print OUTPUT_DIR
    
    #Build command to check for dir on T2
    print 'Testing whether sample name directory exists on dcache...' 
    cmd = "srmls " + OUTPUT_DIR
    
    #Get the list of files in the source directory
    lsResults = open('dcacheFiles','w+')
    ret = call(cmd, shell=True, stdout=lsResults,stderr=DEVNULL)
    lsResults.seek(0)
    
    if ret != 0 :
        print 'Fail! Are you sure to be inside a sample name directory (e.g. DeltaPhiGunPt100dPhi0_3)?'
        sys.exit(1)
    else:
        print 'Success!'
    
    sourceFiles = []
    
    #create an array with just the paths to the sources
    for line in lsResults:
        lineStr = str(line)
        if lineStr.count('.root'):
            fileName = lineStr.split(' ')[-1].rstrip('\n')
            sourceFiles.append(fileName)
    
    print 'Creating local directory for root files'
    if not os.path.exists('rootfiles'):
        os.mkdir('rootfiles')
    else:
        print "Already exists!"
    
    nFiles = len(sourceFiles)
    iterCounter = 1    
    for sourceFile in sourceFiles:
        
        if os.path.exists('rootfiles/' + sourceFile.split('/')[-1]):
            print 'File ' + sourceFile.split('/')[-1] + ' exists. Skipping!'
            continue
        print 'Copying file ' + sourceFile.split('/')[-1] + '\t[' + str(iterCounter) + '/' + str(nFiles) + ']'
        iterCounter += 1 
        copyCmd = 'srmcp ' + RWTHSERVER + sourceFile + ' file://./rootfiles'
        ret = call(copyCmd, shell=True, stdout=DEVNULL,stderr=DEVNULL)
        if ret != 0:
             print 'Something went wrong on copying. Abort!'
             sys.exit(7)
def copyUseDesy():
	print "Copy, from DESY T2"
	if dCacheDir == None:
		print "The --desy option requires a manually given path to the data!"
		sys.exit(1)
	sourceDir = DESYT2PREFIX + dCacheDir
	#Build command to check for dir on T2
	print 'Testing whether sample name directory exists on dcache...' 
	cmd = "srmls " + sourceDir
	
	localTargetDir = None
	if(targetDir != None):
	   	localTargetDir = targetDir
	else:
		localTargetDir = './lcg-copied-files'
		if not os.path.exists(localTargetDir):
			os.mkdir(localTargetDir)
    
	#Get the list of files in the source directory
	lsResults = open('dcacheFiles','w+')
	ret = call(cmd, shell=True, stdout=lsResults,stderr=DEVNULL)
	lsResults.seek(0)
	
	if ret != 0 :
		print 'Fail! Check directory!'
		sys.exit(1)
	else:
		print 'Success!'
    
	sourceFiles = []
    
    #create an array with just the paths to the sources
	for line in lsResults:
		lineStr = str(line)
		if lineStr.count('.root'):
			fileName = lineStr.split(' ')[-1].rstrip('\n')
			sourceFiles.append(fileName)			
	nFiles = 0
	if nFilesToCopy != None:
		nFiles = nFilesToCopy
	else:
		nFiles = len(sourceFiles)
	iterCounter = 1    
	for sourceFile in sourceFiles:
		if iterCounter > nFiles:
			break
		iterCounter += 1 
		if os.path.exists(localTargetDir + '/' + sourceFile.split('/')[-1]):
			print 'File ' + sourceFile.split('/')[-1] + ' exists. Skipping!'
			continue
		print 'Copying file ' + sourceFile.split('/')[-1] + '\t[' + str(iterCounter) + '/' + str(nFiles) + ']'
		
		copyCmd = 'lcg-cp ' + DESYSERVER + sourceFile + ' ' + localTargetDir + '/' + sourceFile.split('/')[-1]
		print copyCmd
		ret = call(copyCmd, shell=True, stdout=DEVNULL,stderr=DEVNULL)
		if ret != 0:
			print 'Something went wrong on copying. Abort!'
			sys.exit(7)

#If the merge option is required, the root input files are merged to one large root file
mergedFileName = ''
def merge():
    #Look for a list of the files to merge
    if mergeList != None:
        if not os.path.exists(mergeList):
            print 'Cannot merge the files. The given file with the copied files doesn\'t exist!'
            sys.exit(8)
    else:
        #Create a file that contains the adapted result from an ls
        filesInDir = open('copiedRootFiles','w')
        for fileIt in os.listdir('rootfiles'):
            filesInDir.write('file:rootfiles/' + fileIt + '\n')
        filesInDir.flush()
        filesInDir.close()
        if not os.path.exists('copiedRootFiles'):
            print 'Cannot merge the files. The file with the list of copied files is missing!'
            sys.exit(4)
    singleFileName = os.listdir('rootfiles')[0]
    singleFileNameParts = singleFileName.split('_')
    mergedFileName = singleFileNameParts[0] + '.root'
    mergeCmd = 'edmCopyPickMerge inputFiles_load='
    #Check for an optional file list
    if mergeList != None:
        mergeCmd += mergeList
    else:
        mergeCmd +=  'copiedRootFiles'
    mergeCmd += ' outputFile=' + mergedFileName
    
    if os.path.exists(mergedFileName):
        print 'File ' + mergedFileName + ' already exists. Abort Merging!'
        sys.exit(9)
    
    print 'Merging root files...'
    ret= -1
    if(mergeRootFiles):
        mergeCmd = 'hadd ' + mergedFileName
        for fileIt in os.listdir('rootfiles'):
            mergeCmd += ' rootfiles/' + fileIt
        ret = call(mergeCmd, shell=True,stderr=DEVNULL)
    else:
        ret = call(mergeCmd, shell=True,stderr=DEVNULL)
    if ret != 0: 
        print 'Something went wrong on merging. Abort!'
        print 'Are you trying to merge root histogram files? Add --merge-root-files option!'
        sys.exit(6)
    #if this option is given, the smaller source files are being removed
    if removeOriginals:
        print 'Removing source files for merging...'
        mergedFiles = None
        if mergeList != None:
            mergedFiles = open(mergeList,'r')
        else:
            mergedFiles = open('copiedRootFiles','r')
        for line in mergedFiles:
            print 'Removing ' + line.split(':')[-1].replace('\n',"")
            os.remove(line.split(':')[-1].replace('\n',""))

#If the move option is selected, moce the merged root file to a directory on net_scratch
def move():
    netScratchPath = '/net/scratch_cms/institut_3b/kuensken/' + sampleName
    #Find, whether the target directory exists
    if not os.path.exists(netScratchPath):
        print 'Target directory ' + netScratchPath + ' does not exist. Creating... '
        os.mkdir(netScratchPath)
    else:
        print 'Target directory ' + netScratchPath + ' exists.'
    #Abort, in case there is already a root file
    if os.path.exists(netScratchPath + '/' + mergedFileName):
        print 'Target file ' + netScratchPath + '/' + mergedFileName + ' exists. Exiting. '
        sys.exit(5)
    moveCmd = 'mv ' + mergedFileName + ' ' + netScratchPath
    print 'Moving ' + mergedFileName + ' to ' + netScratchPath
    ret = call(moveCmd, shell=True, stdout=DEVNULL,stderr=DEVNULL)
    if ret != 0:
        print 'Something went wrong on moving file to net_scratch. Abort!'
        sys.exit(8)
	return

def main():
	print 'Main'
	if createFileList:
		createFileList()
	if copy:
		if useDesy:
			copyUseDesy()
		else:
			copyDoNotUseDesy()
	if merge:
		merge()
	if move:
		move()
	print 'All done.'
	
if __name__ == '__main__':
	main()
    
