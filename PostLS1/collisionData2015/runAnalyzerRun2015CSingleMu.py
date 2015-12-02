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

import FWCore.Utilities.FileUtils as FileUtils
mylist = FileUtils.loadListFromFile('files_SingleMuon_Run2015C-PromptReco-v1_RECO')
 
process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(*mylist)
)

import PhysicsTools.PythonAnalysis.LumiList as LumiList
process.source.lumisToProcess = LumiList.LumiList(filename = 'Cert_246908-260627_13TeV_PromptReco_Collisions15_25ns_JSON.txt').getVLuminosityBlockRange()

process.options = cms.untracked.PSet(

)

process.load("FWCore.MessageService.MessageLogger_cfi")
#May need this in future processings
process.MessageLogger.cerr.FwkReport.reportEvery = 1000

process.TFileService = cms.Service("TFileService",
                                   	fileName=cms.string('collisionDataRun2015CSingleMu.root'),
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


process.load('PhysicsTools/PatAlgos/producersLayer1/muonProducer_cfi')
process.load('PhysicsTools/PatAlgos/selectionLayer1/muonSelector_cfi')
process.patMuons.addGenMatch = cms.bool(False)

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

process.patMuonProducer_step = cms.Path(process.patMuons)
process.patMuonSelector_step = cms.Path(process.selectedPatMuons)
process.hoMuonAnalyzer_step = cms.Path(process.hoMuonAnalyzer)
#process.raw2digi_step = cms.Path(process.RawToDigi)
#process.reconstruction_step = cms.Path(process.reconstruction)
process.endjob_step = cms.EndPath(process.endOfProcess)
process.RECOSIMoutput_step = cms.EndPath(process.RECOSIMoutput)

# Schedule definition
process.schedule = cms.Schedule(
							process.patMuonProducer_step
							,process.patMuonSelector_step
							,process.hoMuonAnalyzer_step
							,process.endjob_step
							)


