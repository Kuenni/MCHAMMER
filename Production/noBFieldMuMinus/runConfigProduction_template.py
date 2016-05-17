# Auto generated configuration file
# using: 
# Revision: 1.381.2.7 
# Source: /local/reps/CMSSW/CMSSW/Configuration/PyReleaseValidation/python/ConfigBuilder.py,v 
# with command line options: 
#cmsDriver.py SingleMuFlatLogPt_100MeVto2TeV_cfi.py --step=GEN,SIM,DIGI,L1,DIGI2RAW,RAW2DIGI,L1Reco,RECO --conditions MCRUN2_72_V1::All --customise=SLHCUpgradeSimulations/Configuration/postLS1Customs.customisePostLS1 --eventcontent FEVTDEBUG --no_exec

import FWCore.ParameterSet.Config as cms
process = cms.Process('L1')

## Configuration parameters

# The eta range for GEN muon production
# the present DTTF goes up to |eta|<1.04, the BarrelTF will go roughly up to
# |eta|<0.9, here putting 1.05 as limit to include scattering of muons 
# before reaching the muon chambers
minEta = -0.80
maxEta =  0.80

# The phi range for GEN muon production
# presently set to study the performance of one single sector plus neighbours
minPhi = - 3.14159265359
maxPhi =   3.14159265359

# The pT range for GEN muon production
# presently set using limits of pt for muons to reach the barrel spectrometer
# and the present DTTF pT scale overflow
minPt = 1.0
maxPt = 200

# The sign of the muon
# -1 for mu- and +1 for mu+
muonCharge = -1

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')

# new_geometry added on  Nov 28, 2014
process.load('Configuration.Geometry.GeometryExtended2015Reco_cff')
process.load('Configuration.Geometry.GeometryExtended2015_cff')
process.load('Configuration.StandardSequences.MagneticField_0T_cff')
process.load('Configuration.StandardSequences.Generator_cff')
process.load('IOMC.EventVertexGenerators.VtxSmearedRealistic8TeVCollision_cfi')
process.load('GeneratorInterface.Core.genFilterSummary_cff')
process.load('Configuration.StandardSequences.SimIdeal_cff')
process.load('Configuration.StandardSequences.L1Reco_cff')
process.load('Configuration.StandardSequences.Digi_cff')
process.load('Configuration.StandardSequences.SimL1Emulator_cff')
process.load('Configuration.StandardSequences.DigiToRaw_cff')
process.load('Configuration.StandardSequences.RawToDigi_cff')
process.load('Configuration.StandardSequences.L1Extra_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
process.load('Configuration.StandardSequences.Reconstruction_cff')

## Set Vertex to 0,0,0
process.load("IOMC.EventVertexGenerators.VtxSmearedGauss_cfi")
process.VtxSmeared.SigmaX = 0.00001
process.VtxSmeared.SigmaY = 0.00001
process.VtxSmeared.SigmaZ = 0.00001

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(100)
)

# Input source
process.source = cms.Source("EmptySource")
process.source.firstLuminosityBlock = cms.untracked.uint32(%INSTANCE%)

process.options = cms.untracked.PSet(
)



if muonCharge > 0 :
	chargeTag='Plus'
else :
        chargeTag='Minus'

configTag = 'SingleMu' + chargeTag + '_Winter15_FlatPt-0' + 'to' + str(maxPt) \
       + '_MCRUN2_72_V1'

# Production Info
process.configurationMetadata = cms.untracked.PSet(
	version = cms.untracked.string('$Revision: 1.4 $'),
	annotation = cms.untracked.string(configTag),
	name = cms.untracked.string('PyReleaseValidation')
	)


# Output definition
process.FEVTDEBUGoutput = cms.OutputModule("PoolOutputModule",
  splitLevel = cms.untracked.int32(0),
  eventAutoFlushCompressedSize = cms.untracked.int32(5242880),
  outputCommands = process.FEVTDEBUGEventContent.outputCommands,
  fileName = cms.untracked.string('SingleMuPt1to200_noBField_%INSTANCE%.root'),
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
process.mix.digitizers =  cms.PSet(process.theDigitizersValid)
#Prepare for no BField
process.g4SimHits.UseMagneticField = cms.bool(False)
from Configuration.AlCa.GlobalTag import GlobalTag
#process.GlobalTag = GlobalTag(process.GlobalTag, globalTag+'::All', '')

# http://cmslxr.fnal.gov/lxr/source/Configuration/AlCa/python/autoCond.py?view=markup
from Configuration.AlCa.autoCond import autoCond
process.GlobalTag.globaltag = autoCond['run2_mc'] 

process.generator = cms.EDProducer("FlatRandomPtGunProducer",
  PGunParameters = cms.PSet(
        MinPt  = cms.double(minPt),
	MaxPt  = cms.double(maxPt),
        PartID = cms.vint32(13 * muonCharge),        
        MaxPhi = cms.double(maxPhi),
	MinPhi = cms.double(minPhi),
	MaxEta = cms.double(maxEta),
        MinEta = cms.double(minEta)        
	),
       Verbosity = cms.untracked.int32(0),
       psethack = cms.string('single mu pt ' + str(minPt) + 'to' + str(maxPt)),
       AddAntiParticle = cms.bool(False), 
       firstRun = cms.untracked.uint32(1)
)


# Path and EndPath definitions
process.generation_step   = cms.Path(process.pgen)
process.simulation_step   = cms.Path(process.psim)
process.digitisation_step = cms.Path(process.pdigi)
process.L1simulation_step = cms.Path(process.SimL1Emulator)
process.digi2raw_step     = cms.Path(process.DigiToRaw)
process.raw2digi_step     = cms.Path(process.RawToDigi)
process.reconstruction_step    = cms.Path(process.reconstruction)
process.L1extra_step           = cms.Path(process.L1Extra)
process.L1Reco_step = cms.Path(process.L1Reco)
process.genfiltersummary_step  = cms.EndPath(process.genFilterSummary)
process.endjob_step            = cms.EndPath(process.endOfProcess)
process.FEVTDEBUGoutput_step   = cms.EndPath(process.FEVTDEBUGoutput)
process.horeco_step = cms.Path(process.horeco)
# Schedule definition
process.schedule = cms.Schedule(process.generation_step,
				process.genfiltersummary_step,
				process.simulation_step,
				process.digitisation_step,
				process.L1simulation_step,
				process.digi2raw_step,
				process.raw2digi_step,
				process.horeco_step,
				process.L1Reco_step,
				process.L1extra_step,
				process.endjob_step,
				process.FEVTDEBUGoutput_step
				)

# filter all path with the production filter sequence
for path in process.paths:
	getattr(process,path)._seq = process.generator * getattr(process,path)._seq 

# customisation of the process.                                                                                                                                                                             

# Automatic addition of the customisation function from SLHCUpgradeSimulations.Configuration.postLS1Customs                                                                                                 
from SLHCUpgradeSimulations.Configuration.postLS1Customs import customisePostLS1

#call to customisation function customisePostLS1 imported from SLHCUpgradeSimulations.Configuration.postLS1Customs                                                                                           
process = customisePostLS1(process)
