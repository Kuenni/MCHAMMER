# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: reco -s RAW2DIGI,RECO --conditions auto[run2_data] --customise=SLHCUpgradeSimulations/Configuration/postLS1Customs.customisePostLS1 --eventcontent FEVTDEBUG --no_exec --data
import FWCore.ParameterSet.Config as cms

process = cms.Process('RECO')

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.MagneticField_AutoFromDBCurrent_cff')
process.load('Configuration.StandardSequences.RawToDigi_Data_cff')
process.load('Configuration.StandardSequences.Reconstruction_Data_cff')
process.load('Configuration.StandardSequences.L1Reco_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_condDBv2_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(10000)
)

import FWCore.Utilities.FileUtils as FileUtils
mylist = FileUtils.loadListFromFile('files_SingleMuon_Run2015D-v1_RAW')
 
process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(*mylist)
#	fileNames = cms.untracked.vstring([''])
)

process.options = cms.untracked.PSet(

)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    annotation = cms.untracked.string('reco nevts:1'),
    name = cms.untracked.string('Applications'),
    version = cms.untracked.string('$Revision: 1.19 $')
)

# Output definition

process.FEVTDEBUGoutput = cms.OutputModule("PoolOutputModule",
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string(''),
        filterName = cms.untracked.string('')
    ),
    eventAutoFlushCompressedSize = cms.untracked.int32(5242880),
    fileName = cms.untracked.string('reco_RAW2DIGI_RECO.root'),
    outputCommands = process.FEVTDEBUGEventContent.outputCommands,
    splitLevel = cms.untracked.int32(0)
)

process.load('PhysicsTools/PatAlgos/producersLayer1/muonProducer_cfi')
process.load('PhysicsTools/PatAlgos/selectionLayer1/muonSelector_cfi')
process.patMuons.addGenMatch = cms.bool(False)

# Additional output definition
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

process.patMuonProducer_step = cms.Path(process.patMuons)
process.patMuonSelector_step = cms.Path(process.selectedPatMuons)
process.hoMuonAnalyzer_step = cms.Path(process.hoMuonAnalyzer)

process.TFileService = cms.Service("TFileService",
                                   	fileName=cms.string('jobOutputFromRaw.root'),
                                   )

# Other statements
from Configuration.AlCa.GlobalTag_condDBv2 import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:run2_data', '')

# Path and EndPath definitions
process.raw2digi_step = cms.Path(process.RawToDigi)
process.reconstruction_step = cms.Path(process.reconstruction)
process.L1Reco_step = cms.Path(process.L1Reco)

process.endjob_step = cms.EndPath(process.endOfProcess)
process.FEVTDEBUGoutput_step = cms.EndPath(process.FEVTDEBUGoutput)

# Schedule definition
process.schedule = cms.Schedule(process.raw2digi_step,
							process.reconstruction_step,
							process.L1Reco_step,
							process.patMuonProducer_step,
							process.patMuonSelector_step,
							process.hoMuonAnalyzer_step,
							process.endjob_step,
							process.FEVTDEBUGoutput_step)

# customisation of the process.

# Automatic addition of the customisation function from SLHCUpgradeSimulations.Configuration.postLS1Customs
from SLHCUpgradeSimulations.Configuration.postLS1Customs import customisePostLS1 

#call to customisation function customisePostLS1 imported from SLHCUpgradeSimulations.Configuration.postLS1Customs
process = customisePostLS1(process)

# End of customisation functions

