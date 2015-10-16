# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: reco -s RAW2DIGI,RECO --fileout anOutputFileName.root --conditions auto:run2_data --data
import FWCore.ParameterSet.Config as cms

process = cms.Process('HoMuonAnalyzer')


# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.MagneticField_AutoFromDBCurrent_cff')
process.load('Configuration.StandardSequences.RawToDigi_Data_cff')
process.load('Configuration.StandardSequences.Reconstruction_Data_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_condDBv2_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(-1)
)


# This might prove useful when running over lots of data

# import FWCore.Utilities.FileUtils as FileUtils
# mylist = FileUtils.loadListFromFile('cmsswSourceFiles')
# 
# process.source = cms.Source("PoolSource",
#     fileNames = cms.untracked.vstring(*mylist)
# )

# # Input source
process.source = cms.Source("PoolSource",
     secondaryFileNames = cms.untracked.vstring(),
     fileNames = cms.untracked.vstring(
				#	'root://xrootd.unl.edu//store/data/Run2015A/SingleMu/RAW/v1/000/246/865/00000/F22171EA-B309-E511-9863-02163E014695.root'
			#		'root://xrootd.unl.edu//store/data/Run2015A/SingleMu/RAW/v1/000/246/936/00000/5E4D1876-110A-E511-A195-02163E01180A.root'
		'root://xrootd.unl.edu//store/data/Run2015A/SingleMu/RECO/PromptReco-v1/000/246/865/00000/2631D17B-140B-E511-AB09-02163E014641.root',
       	'root://xrootd.unl.edu//store/data/Run2015A/SingleMu/RECO/PromptReco-v1/000/246/908/00000/005954A7-220B-E511-83C0-02163E0133E6.root',
        'root://xrootd.unl.edu//store/data/Run2015A/SingleMu/RECO/PromptReco-v1/000/246/908/00000/00B486B6-260B-E511-9B45-02163E01379B.root',
        'root://xrootd.unl.edu//store/data/Run2015A/SingleMu/RECO/PromptReco-v1/000/246/908/00000/02323810-230B-E511-B710-02163E01184E.root',
        'root://xrootd.unl.edu//store/data/Run2015A/SingleMu/RECO/PromptReco-v1/000/246/908/00000/02BF2448-260B-E511-8570-02163E011A9B.root',
        'root://xrootd.unl.edu//store/data/Run2015A/SingleMu/RECO/PromptReco-v1/000/246/908/00000/04325715-4D0B-E511-A89E-02163E01396D.root',
        'root://xrootd.unl.edu//store/data/Run2015A/SingleMu/RECO/PromptReco-v1/000/246/908/00000/049A79B1-210B-E511-A78B-02163E01383E.root',
        'root://xrootd.unl.edu//store/data/Run2015A/SingleMu/RECO/PromptReco-v1/000/246/908/00000/08E63C0B-640B-E511-9B32-02163E01446B.root',
        'root://xrootd.unl.edu//store/data/Run2015A/SingleMu/RECO/PromptReco-v1/000/246/908/00000/0AC78A35-220B-E511-ABFF-02163E014409.root',
        'root://xrootd.unl.edu//store/data/Run2015A/SingleMu/RECO/PromptReco-v1/000/246/908/00000/0E3AB48E-230B-E511-823C-02163E013826.root',
        'root://xrootd.unl.edu//store/data/Run2015A/SingleMu/RECO/PromptReco-v1/000/246/908/00000/16BDCD78-3F0B-E511-8138-02163E014565.root',
        'root://xrootd.unl.edu//store/data/Run2015A/SingleMu/RECO/PromptReco-v1/000/246/908/00000/2EF9C840-230B-E511-B60F-02163E013942.root',
        'root://xrootd.unl.edu//store/data/Run2015A/SingleMu/RECO/PromptReco-v1/000/246/908/00000/382A8716-1D0B-E511-8915-02163E0142DC.root',
        'root://xrootd.unl.edu//store/data/Run2015A/SingleMu/RECO/PromptReco-v1/000/246/908/00000/3A0A4158-260B-E511-B2BE-02163E0145BA.root',
        'root://xrootd.unl.edu//store/data/Run2015A/SingleMu/RECO/PromptReco-v1/000/246/908/00000/3CF0D485-220B-E511-8776-02163E014686.root',
        'root://xrootd.unl.edu//store/data/Run2015A/SingleMu/RECO/PromptReco-v1/000/246/908/00000/3E3C1E40-2B0B-E511-828F-02163E01450B.root',
        'root://xrootd.unl.edu//store/data/Run2015A/SingleMu/RECO/PromptReco-v1/000/246/908/00000/3E476249-230B-E511-87D5-02163E014142.root')
 )

#import PhysicsTools.PythonAnalysis.LumiList as LumiList
#process.source.lumisToProcess = LumiList.LumiList(filename = 'Cert_246908-247381_13TeV_PromptReco_Collisions15_ZeroTesla_JSON.txt').getVLuminosityBlockRange()

process.options = cms.untracked.PSet(

)

process.load("FWCore.MessageService.MessageLogger_cfi")
#May need this in future processings
#process.MessageLogger.cerr.FwkReport.reportEvery = 1000

process.TFileService = cms.Service("TFileService",
                                   	fileName=cms.string('collisionData.root'),
                                   )

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    version = cms.untracked.string('$Revision: 1.19 $'),
    annotation = cms.untracked.string('reco nevts:1'),
    name = cms.untracked.string('Applications')
)

# Output definition

process.RECOSIMoutput = cms.OutputModule("PoolOutputModule",
    splitLevel = cms.untracked.int32(0),
    eventAutoFlushCompressedSize = cms.untracked.int32(5242880),
    outputCommands = process.RECOSIMEventContent.outputCommands,
    fileName = cms.untracked.string('anOutputFileName.root'),
    dataset = cms.untracked.PSet(
        filterName = cms.untracked.string(''),
        dataTier = cms.untracked.string('')
    )
)

# Additional output definition

# Other statements
from Configuration.AlCa.GlobalTag_condDBv2 import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:run2_data', '')

################################
#	HO Muon analyzer module for studies on rec hits
################################
process.hoMuonAnalyzer = cms.EDAnalyzer(
    'hoMuonAnalyzer',
    isData = cms.bool(True),
    l1MuonSrc=cms.InputTag("l1extraParticles"),
    horecoSrc = cms.InputTag("horeco"),
    hltSumAODSrc = cms.InputTag("hltTriggerSummaryAOD"),
    hoEnergyThreshold = cms.double(0.2),
	maxDeltaR = cms.double(0.3),
	debug = cms.bool(True),
	maxDeltaRL1MuonMatching = cms.double(1.),
	hoDigiSrc = cms.InputTag('simHcalDigis'),
	hoAdcThreshold = cms.int32(60)
    )

# Path and EndPath definitions
process.hoMuonAnalyzer_step = cms.Path(process.hoMuonAnalyzer)
process.raw2digi_step = cms.Path(process.RawToDigi)
process.reconstruction_step = cms.Path(process.reconstruction)
process.endjob_step = cms.EndPath(process.endOfProcess)
process.RECOSIMoutput_step = cms.EndPath(process.RECOSIMoutput)

# Schedule definition
process.schedule = cms.Schedule(
						#	process.raw2digi_step
						#	,process.reconstruction_step
							process.hoMuonAnalyzer_step
							,process.endjob_step
						#	,process.RECOSIMoutput_step
							)


