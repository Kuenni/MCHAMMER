# Auto generated configuration file
# using: 
# Revision: 1.20 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: SingleMuPt100_cfi -s GEN,SIM,DIGI:pdigi_valid,L1,DIGI2RAW,RAW2DIGI --conditions auto:upgradePLS3 --customise SLHCUpgradeSimulations/Configuration/combinedCustoms.cust_2023Muon --magField 38T_PostLS1 --geometry Extended2023Muon --eventcontent FEVTDEBUGHLT -n 10 --no_exec
import FWCore.ParameterSet.Config as cms

process = cms.Process('RAW2DIGI')

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load('Configuration.Geometry.GeometryExtended2023MuonReco_cff')
process.load('Configuration.Geometry.GeometryExtended2023Muon_cff')
process.load('Configuration.StandardSequences.MagneticField_38T_PostLS1_cff')
process.load('Configuration.StandardSequences.Generator_cff')
process.load('IOMC.EventVertexGenerators.VtxSmearedRealistic8TeVCollision_cfi')
process.load('GeneratorInterface.Core.genFilterSummary_cff')
process.load('Configuration.StandardSequences.SimIdeal_cff')
process.load('Configuration.StandardSequences.Digi_cff')
process.load('Configuration.StandardSequences.SimL1Emulator_cff')
process.load('Configuration.StandardSequences.DigiToRaw_cff')
process.load('Configuration.StandardSequences.RawToDigi_cff')
process.load('Configuration.StandardSequences.L1Extra_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(1000)
)

# Input source
process.source = cms.Source("EmptySource")

process.options = cms.untracked.PSet(

)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    version = cms.untracked.string('$Revision: 1.20 $'),
    annotation = cms.untracked.string('SingleMuPt100_cfi nevts:10'),
    name = cms.untracked.string('Applications')
)

# Output definition

process.FEVTDEBUGHLToutput = cms.OutputModule("PoolOutputModule",
    splitLevel = cms.untracked.int32(0),
    eventAutoFlushCompressedSize = cms.untracked.int32(5242880),
    outputCommands = process.FEVTDEBUGHLTEventContent.outputCommands,
    fileName = cms.untracked.string('SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI.root'),
    dataset = cms.untracked.PSet(
        filterName = cms.untracked.string(''),
        dataTier = cms.untracked.string('')
    ),
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('generation_step')
    )
)

# Additional output definition

# Other statements
process.genstepfilter.triggerConditions=cms.vstring("generation_step")
process.mix.digitizers = cms.PSet(process.theDigitizersValid)
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:upgradePLS3', '')

process.generator = cms.EDProducer("FlatRandomPtGunProducer",
    PGunParameters = cms.PSet(
        MaxPt = cms.double(100.01),
        MinPt = cms.double(99.99),
        PartID = cms.vint32(-13),
        MaxEta = cms.double(0.8),
        MaxPhi = cms.double(3.14159265359),
        MinEta = cms.double(-0.8),
        MinPhi = cms.double(-3.14159265359)
    ),
    Verbosity = cms.untracked.int32(0),
    psethack = cms.string('single mu pt 100'),
    AddAntiParticle = cms.bool(True),
    firstRun = cms.untracked.uint32(1)
)


# add SiPMs to HO
process.mix.digitizers.hcal.ho.pixels = cms.int32(2500)
process.mix.digitizers.hcal.ho.siPMCode = 1
process.mix.digitizers.hcal.ho.photoelectronsToAnalog = cms.vdouble([4.0]*16)


#ascii file conditions
process.hcales_ascii = hcales_ascii = cms.ESSource(
            "HcalTextCalibrations",
            input = cms.VPSet(
                cms.PSet(
                        object = cms.string('ChannelQuality'),
                        file = cms.FileInPath('HoMuonTrigger/HOSiPMCalibration/data/700_chan_qual.txt')
                        ),
                cms.PSet(
                        object = cms.string('Pedestals'),
                        file = cms.FileInPath('HoMuonTrigger/HOSiPMCalibration/data/700_pedestals.txt')
                        ),
                cms.PSet(
                        object = cms.string('PedestalWidths'),
                        file = cms.FileInPath('HoMuonTrigger/HOSiPMCalibration/data/700_pedestalWidths.txt')
                        ),
                cms.PSet(
                        object = cms.string('Gains'),
                        file = cms.FileInPath('HoMuonTrigger/HOSiPMCalibration/data/700_gains.txt')
                        ),
                )
        )

process.es_hardcode = cms.ESPrefer("HcalTextCalibrations", "hcales_ascii")




#####
# Path and EndPath definitions
process.generation_step = cms.Path(process.pgen)
process.simulation_step = cms.Path(process.psim)
process.digitisation_step = cms.Path(process.pdigi_valid)
process.L1simulation_step = cms.Path(process.SimL1Emulator)
process.digi2raw_step = cms.Path(process.DigiToRaw)
process.raw2digi_step = cms.Path(process.RawToDigi)
process.l1extra_step = cms.Path(process.L1Extra)
process.genfiltersummary_step = cms.EndPath(process.genFilterSummary)
process.endjob_step = cms.EndPath(process.endOfProcess)
process.FEVTDEBUGHLToutput_step = cms.EndPath(process.FEVTDEBUGHLToutput)
###################
from SLHCUpgradeSimulations.Configuration.combinedCustoms import cust_2023Muon
#call to customisation function cust_2023Muon imported from SLHCUpgradeSimulations.Configuration.combinedCustoms
process = cust_2023Muon(process)
#### fix
process.digitisation_step.replace(process.simHcalDigis,process.simHcalTriggerPrimitiveDigis+process.simHcalDigis+process.simHcalTTPDigis)
process.raw2digi_step.replace(process.muonDTDigis,process.hcalDigis*process.muonCSCDigis*process.muonDTDigis) 
process.digi2raw_step.replace(process.esDigiToRaw,process.esDigiToRaw+process.hcalRawData)


####
##################
# Schedule definition
process.schedule = cms.Schedule(
	process.generation_step,
	process.genfiltersummary_step,
	process.simulation_step,
	process.digitisation_step,
	process.L1simulation_step,
	process.digi2raw_step,
	process.raw2digi_step,
	process.l1extra_step,
	process.endjob_step,
	process.FEVTDEBUGHLToutput_step
	)
# filter all path with the production filter sequence
for path in process.paths:
	getattr(process,path)._seq = process.generator * getattr(process,path)._seq 

# customisation of the process.

## Automatic addition of the customisation function from SLHCUpgradeSimulations.Configuration.combinedCustoms
#from SLHCUpgradeSimulations.Configuration.combinedCustoms import cust_2023Muon 
#
##call to customisation function cust_2023Muon imported from SLHCUpgradeSimulations.Configuration.combinedCustoms
#process = cust_2023Muon(process)

# End of customisation functions
process.FEVTDEBUGHLToutput.outputCommands.append('keep *_*digi*_*_*')
process.FEVTDEBUGHLToutput.outputCommands.append('keep *_*Digi*_*_*')
