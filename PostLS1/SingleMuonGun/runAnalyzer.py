import FWCore.ParameterSet.Config as cms

process = cms.Process("Demo")

process.load("FWCore.MessageService.MessageLogger_cfi")
process.MessageLogger.cerr.FwkReport.reportEvery = 100

process.TFileService = cms.Service("TFileService",
                                   fileName=cms.string('L1MuonHistogram.root')
                                   )


process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )

readFiles = cms.untracked.vstring()
process.source = cms.Source("PoolSource",
    # replace 'myfile.root' with the source file you want to use
    fileNames = readFiles
)

readFiles.extend( [

       ] )



# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load('Configuration.Geometry.GeometryExtended2015Reco_cff')
process.load('Configuration.Geometry.GeometryExtended2015_cff')
process.load('Configuration.StandardSequences.MagneticField_38T_PostLS1_cff')
process.load('Configuration.StandardSequences.Generator_cff')
process.load('IOMC.EventVertexGenerators.VtxSmearedRealistic8TeVCollision_cfi')
process.load('GeneratorInterface.Core.genFilterSummary_cff')
process.load('Configuration.StandardSequences.SimIdeal_cff')
process.load('Configuration.StandardSequences.Digi_cff')
process.load('Configuration.StandardSequences.SimL1Emulator_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

#turn off HO ZS
#process.hcalRawData.HO = cms.untracked.InputTag("simHcalUnsuppressedDigis", "", "")

#L1Extra
#process.load('L1Trigger.Configuration.L1Extra_cff')

#horeco
process.load('Configuration.StandardSequences.Reconstruction_cff')

from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'POSTLS171_V15::All', '')


process.hoMuonAnalyzer = cms.EDAnalyzer(
    'hoMuonAnalyzer',
    genSrc = cms.InputTag("genParticles"),
    l1MuonSrc=cms.InputTag("l1extraParticles"),
    #stdMuSrc = cms.InputTag("standAloneMuons"),
    horecoSrc = cms.InputTag("horeco"),
    #L1GtTmLInputTag = cms.InputTag("l1GtTriggerMenuLite")
    hltSumAODSrc = cms.InputTag("hltTriggerSummaryAOD"),
    l1MuonGenMatchSrc = cms.InputTag("l1MuonGenMatch"),
    hoEnergyThreshold = cms.double(0.2),
	maxDeltaR = cms.double(0.3),
	debug = cms.bool(True),
	maxDeltaRL1MuonMatching = cms.double(1.)
    )

#Alternative matcher: TrivialDeltaRMatcher
process.l1MuonGenMatch = cms.EDProducer("MCTruthDeltaRMatcherNew",
     src = cms.InputTag("l1extraParticles"),
     matched = cms.InputTag("genParticles"),
     distMin = cms.double(0.15),
#     matchPDGId = cms.vint32( 13 ) # muons
)

process.options = cms.untracked.PSet(

)

#Try using different source for hoReco
process.horeco.digiLabel = cms.InputTag('simHcalDigis')

#Path definitions
#process.digitisation_step = cms.Path(process.pdigi)
#process.digi2raw_step = cms.Path(process.DigiToRaw)
#process.raw2digi_step = cms.Path(process.RawToDigi)
#process.L1simulation_step = cms.Path(process.SimL1Emulator)
#process.l1extra_step = cms.Path(process.L1Extra)
process.horeco_step = cms.Path(process.horeco)
process.l1MuonGenMatch_step = cms.Path(process.l1MuonGenMatch)
process.demo_step = cms.Path(process.hoMuonAnalyzer)


#Schedule Definition
process.schedule = cms.Schedule(
#	process.L1simulation_step,
#	process.l1extra_step,
	process.horeco_step,
	process.l1MuonGenMatch_step,
	process.demo_step
	)


# Automatic addition of the customisation function from SLHCUpgradeSimulations.Configuration.postLS1Customs
from SLHCUpgradeSimulations.Configuration.postLS1Customs import customisePostLS1 

#call to customisation function customisePostLS1 imported from SLHCUpgradeSimulations.Configuration.postLS1Customs
process = customisePostLS1(process)

# End of customisation functions
