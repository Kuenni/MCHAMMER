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

## --
## Switch on PAT trigger
## --
from PhysicsTools.PatAlgos.tools.trigTools import *
from PhysicsTools.PatAlgos.triggerLayer1.triggerMatcherExamples_cfi import somePatMuonTriggerMatchTriggerMuon
process.myMatcher = somePatMuonTriggerMatchTriggerMuon.clone()
switchOnTrigger( process ) # This is optional and can be omitted.
switchOnTriggerMatchEmbedding( process, [ 'myMatcher' ])

process.patTriggerAnalyzer = cms.EDAnalyzer('HoPatTriggerAnalyzer',
	trigger      = cms.InputTag( "patTrigger" ),
    triggerEvent = cms.InputTag( "patTriggerEvent" ),
    muons        = cms.InputTag( "selectedPatMuons" ),
    muonMatch    = cms.string( 'myMatcher' ),
    minID = cms.uint32( 81 ),
    maxID = cms.uint32( 96 ))

process.patTriggerAnalyzerSequence = cms.Sequence(process.patTriggerAnalyzer)
process.p = cms.Path(process.patTriggerAnalyzer)

process.out.fileName = 'patTuple_onlyMuons.root'

process.options.wantSummary = False   ##  (to suppress the long output at the end of the job)

from PhysicsTools.PatAlgos.tools.coreTools import *
runOnData(process)#,['Muons'])