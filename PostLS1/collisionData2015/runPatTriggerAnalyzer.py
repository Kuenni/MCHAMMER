## import skeleton process
from PhysicsTools.PatAlgos.patTemplate_cfg import *
## switch to uncheduled mode
process.options.allowUnscheduled = cms.untracked.bool(True)
#process.Tracer = cms.Service("Tracer")

process.load( "PhysicsTools.PatAlgos.producersLayer1.patCandidates_cff" )
process.load( "PhysicsTools.PatAlgos.selectionLayer1.selectedPatCandidates_cff" )
## make sure to keep the created objects
process.out.outputCommands = ['keep *_selectedPat*_*_*']

process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:run2_data')
## Source

import FWCore.Utilities.FileUtils as FileUtils
mylist = FileUtils.loadListFromFile('files_SingleMuon_Run2015D-PromptReco-v4_RECO')
 
process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(*mylist)
)
process.maxEvents.input = 100

process.TFileService = cms.Service("TFileService",
	fileName=cms.string('patTriggerAnalyzerOutput.root'),
	)

## --
## Switch on PAT trigger
## --
from PhysicsTools.PatAlgos.tools.trigTools import *
from PhysicsTools.PatAlgos.triggerLayer1.triggerMatcherExamples_cfi import somePatMuonTriggerMatchTriggerMuon
process.myMatcher = somePatMuonTriggerMatchTriggerMuon.clone()
switchOnTrigger( process )
switchOnTriggerMatching(process,['myMatcher'])
switchOnTriggerMatchEmbedding( process, [ 'myMatcher' ])
process.patTrigger.addL1Algos = cms.bool(True)
process.patTrigger.saveL1Refs = cms.bool(True)
process.patTrigger.l1ExtraMu = cms.InputTag('l1extraParticles','')
switchOnTrigger(process)
#switchOnTriggerMatching(process,['myMatcher'])
switchOnTriggerMatchEmbedding( process, [ 'myMatcher' ])
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

process.patTriggerAnalyzerSequence = cms.Sequence(process.patTriggerAnalyzer)
process.p = cms.Path(process.patTriggerAnalyzer)

process.out.fileName = 'patTuple_onlyMuons.root'

process.options.wantSummary = False   ##  (to suppress the long output at the end of the job)

from PhysicsTools.PatAlgos.tools.coreTools import *
runOnData(process)#,['Muons'])