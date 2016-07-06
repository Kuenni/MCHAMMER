import FWCore.ParameterSet.Config as cms

from TrackingTools.TrackAssociator.default_cfi import TrackAssociatorParameterBlock
parameters = TrackAssociatorParameterBlock.TrackAssociatorParameters

parameters.useEcal = False
parameters.useHcal = False
parameters.useMuon = False

hoTriggerAnalyzer = cms.EDAnalyzer('hoTriggerAnalyzer',
	genSrc = cms.InputTag("genParticles"),
    l1MuonSrc=cms.InputTag("l1extraParticles"),
    horecoSrc = cms.InputTag("horeco"),
    hltSumAODSrc = cms.InputTag("hltTriggerSummaryAOD"),
    l1MuonGenMatchSrc = cms.InputTag("l1MuonGenMatch"),
    hoEnergyThreshold = cms.double(0.2),
	maxDeltaR = cms.double(0.3),
	debug = cms.bool(True),
	isData = cms.bool(False),
	maxDeltaRL1MuonMatching = cms.double(1.),
	TrackAssociatorParameters=parameters,
	hoDigiSrc = cms.InputTag('simHcalDigis'),
	hoAdcThreshold = cms.int32(60)		
)
