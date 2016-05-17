import FWCore.ParameterSet.Config as cms

process = cms.Process('HoPatTriggerAnalyzer')
## switch to uncheduled modeprocess.load('Configuration.StandardSequences.Services_cff')
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
from Configuration.AlCa.GlobalTag_condDBv2 import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:run2_data')

process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring('file://./patTuple_onlyMuons.root')
)
process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(100)
)
process.TFileService = cms.Service("TFileService",
	fileName=cms.string('patTriggerAnalyzerOutput.root'),
	)

## Define the analyzer
process.patTriggerAnalyzer = cms.EDAnalyzer('HoPatTriggerAnalyzer',
	trigger      = cms.InputTag( "patTrigger" ),
    triggerEvent = cms.InputTag( "patTriggerEvent" ),
    muons        = cms.InputTag( "selectedPatMuons" ),
    muonMatch    = cms.string( 'myMatcher' ),

#   minID = cms.uint32( 81 ), 	//Those to are from the original PAT Trigger Analyzer
#   maxID = cms.uint32( 96 )	//The IDs are the TriggerObjectTypes

	#I have to add these parameters again for the HOMatcher class
	#Maybe there is a better way to do this
	horecoSrc = cms.InputTag("horeco"),
	hoEnergyThreshold = cms.double(0.2),	#0.2 GeV
	maxDeltaR = cms.double(0.3),
	hoDigiSrc = cms.InputTag('simHcalDigis')
    )

process.p = cms.Path(process.patTriggerAnalyzer)
