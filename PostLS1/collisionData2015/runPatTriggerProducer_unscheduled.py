import FWCore.ParameterSet.Config as cms

process = cms.Process('HoPatTriggerProducer')

process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.MagneticField_AutoFromDBCurrent_cff')
process.load( 'TrackingTools.TrackAssociator.DetIdAssociatorESProducer_cff' )
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load("PhysicsTools.PatAlgos.patSequences_cff")
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_condDBv2_cff')

# Set the global Tag
from Configuration.AlCa.GlobalTag_condDBv2 import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:run2_data')

## Options and Output Report
process.options = cms.untracked.PSet(
  wantSummary = cms.untracked.bool( False ),
  allowUnscheduled = cms.untracked.bool(True)
)
#process.Tracer = cms.Service("Tracer")

## Output Module Configuration (expects a path 'p')
from PhysicsTools.PatAlgos.patEventContent_cff import patEventContentNoCleaning
process.out = cms.OutputModule("PoolOutputModule",
                               fileName = cms.untracked.string('patTuple.root'),
                               ## save only events passing the full path
                               #SelectEvents = cms.untracked.PSet( SelectEvents = cms.vstring('p') ),
                               ## save PAT output; you need a '*' to unpack the list of commands
                               ## 'patEventContent'
                               outputCommands = cms.untracked.vstring('drop *', *patEventContentNoCleaning )
                               )

process.outpath = cms.EndPath(process.out)

## make sure to keep the created objects
process.out.outputCommands = ['keep *_selectedPat*_*_*'
							,'keep *_*horeco*_*_*'
							,'keep *_*myMatcher*_*_*'
							,'keep *_*_*myMatcher*_*'
							,'keep *_*muon*_*_RECO'
							,'keep *_patTrigger*_*_*'
							]
process.out.fileName = 'patTuple_onlyMuons.root'

## Source of data
import FWCore.Utilities.FileUtils as FileUtils
mylist = FileUtils.loadListFromFile('files_SingleMuon_Run2015D-PromptReco-v4_RECO')
 
process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(*mylist)
)

####
# Limit Event number
####
process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(100)
)

## --
## Switch on PAT trigger
## --
from PhysicsTools.PatAlgos.tools.trigTools import *
process.myMatcher = cms.EDProducer(
   "PATTriggerMatcherDRLessByR"           # match by DeltaR and DeltaPt, best match by DeltaR
 , src     = cms.InputTag( 'selectedPatMuons' )
 , matched = cms.InputTag( 'patTrigger' )    # default producer label as defined in PhysicsTools/PatAlgos/python/triggerLayer1/triggerProducer_cfi.py
 , matchedCuts = cms.string( 'type( "TriggerL1Mu" )' )
 , maxDeltaR = cms.double( 1 )
 , resolveAmbiguities    = cms.bool( True )  # only one match per trigger object
 , resolveByMatchQuality = cms.bool( True ) # take best match found per reco object
 )
switchOnTrigger( process )
switchOnTriggerMatching(process,['myMatcher'])
switchOnTriggerMatchEmbedding( process, [ 'myMatcher' ])
process.patTrigger.addL1Algos = cms.bool(True)
process.patTrigger.saveL1Refs = cms.bool(True)
process.patTrigger.l1ExtraMu = cms.InputTag('l1extraParticles','')
switchOnTrigger(process)
#switchOnTriggerMatching(process,['myMatcher'])
switchOnTriggerMatchEmbedding( process, [ 'myMatcher' ])

##
# Tell PAT to run on data
##
from PhysicsTools.PatAlgos.tools.coreTools import *
runOnData(process)

##
# Get the file service 
##
process.TFileService = cms.Service("TFileService",
	fileName=cms.string('patTriggerAnalyzerOutput.root'),
	)
##
# Instanciate the analyzer
##
process.analyzer = cms.EDAnalyzer('HoPatTriggerAnalyzer',
	trigger      = cms.InputTag( "patTrigger" ),
    triggerEvent = cms.InputTag( "patTriggerEvent" ),
    muons        = cms.InputTag( "selectedPatMuons" ),
    muonMatch    = cms.string( 'myMatcher' ),

	#I have to add these parameters again for the HOMatcher class
	#Maybe there is a better way to do this
	horecoSrc = cms.InputTag("horeco"),
	hoEnergyThreshold = cms.double(0.2),	#0.2 GeV
	maxDeltaR = cms.double(0.3),
	hoDigiSrc = cms.InputTag('simHcalDigis')
    )

## ---
## Define the path
## ---
process.p = cms.Path(
	process.analyzer
)
