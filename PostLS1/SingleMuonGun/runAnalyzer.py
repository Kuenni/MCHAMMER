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
	'/store/user/akunsken/SingleMuonGunPostLS1/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_15_1_a97.root',
	'/store/user/akunsken/SingleMuonGunPostLS1/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_21_1_Orm.root',
	'/store/user/akunsken/SingleMuonGunPostLS1/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_17_1_w2T.root',
	'/store/user/akunsken/SingleMuonGunPostLS1/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_16_1_RxV.root',
	'/store/user/akunsken/SingleMuonGunPostLS1/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_11_1_xXm.root',
	'/store/user/akunsken/SingleMuonGunPostLS1/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_64_1_aZM.root',
	'/store/user/akunsken/SingleMuonGunPostLS1/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_22_1_nNF.root',
	'/store/user/akunsken/SingleMuonGunPostLS1/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_10_1_O7j.root',
	'/store/user/akunsken/SingleMuonGunPostLS1/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_1_1_HqA.root',
	'/store/user/akunsken/SingleMuonGunPostLS1/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_12_1_5Rf.root',
	'/store/user/akunsken/SingleMuonGunPostLS1/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_7_1_ePK.root',
	'/store/user/akunsken/SingleMuonGunPostLS1/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_9_1_Ig1.root',
	'/store/user/akunsken/SingleMuonGunPostLS1/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_39_1_w5j.root',
	'/store/user/akunsken/SingleMuonGunPostLS1/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_18_1_mYF.root',
	'/store/user/akunsken/SingleMuonGunPostLS1/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_33_1_Ttf.root',
	'/store/user/akunsken/SingleMuonGunPostLS1/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_19_1_XRt.root',
	'/store/user/akunsken/SingleMuonGunPostLS1/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_20_1_tTo.root',
	'/store/user/akunsken/SingleMuonGunPostLS1/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_8_1_oPc.root',
	'/store/user/akunsken/SingleMuonGunPostLS1/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_58_1_cZo.root',
	'/store/user/akunsken/SingleMuonGunPostLS1/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_99_1_sdQ.root',
	'/store/user/akunsken/SingleMuonGunPostLS1/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_97_1_TqL.root',
	'/store/user/akunsken/SingleMuonGunPostLS1/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_2_1_5jE.root',
	'/store/user/akunsken/SingleMuonGunPostLS1/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_4_1_hnC.root',
	'/store/user/akunsken/SingleMuonGunPostLS1/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_95_1_8jr.root',
	'/store/user/akunsken/SingleMuonGunPostLS1/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_94_1_cMy.root',
	'/store/user/akunsken/SingleMuonGunPostLS1/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_3_1_gR7.root',
	'/store/user/akunsken/SingleMuonGunPostLS1/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_14_1_Xrn.root',
	'/store/user/akunsken/SingleMuonGunPostLS1/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_13_1_WKp.root',
	'/store/user/akunsken/SingleMuonGunPostLS1/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_81_1_oTH.root',
	'/store/user/akunsken/SingleMuonGunPostLS1/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_6_1_DCJ.root',
	'/store/user/akunsken/SingleMuonGunPostLS1/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_93_1_qpj.root',
	'/store/user/akunsken/SingleMuonGunPostLS1/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_5_1_ost.root',
	'/store/user/akunsken/SingleMuonGunPostLS1/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_32_1_Avn.root',
	'/store/user/akunsken/SingleMuonGunPostLS1/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_92_1_1sD.root',
	'/store/user/akunsken/SingleMuonGunPostLS1/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_63_1_zJm.root',
	'/store/user/akunsken/SingleMuonGunPostLS1/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_50_1_8Mi.root',
	'/store/user/akunsken/SingleMuonGunPostLS1/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_100_1_kjI.root',
	'/store/user/akunsken/SingleMuonGunPostLS1/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_74_1_Zw9.root',
	'/store/user/akunsken/SingleMuonGunPostLS1/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_57_1_NrJ.root',
	'/store/user/akunsken/SingleMuonGunPostLS1/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_55_1_LSA.root',
	'/store/user/akunsken/SingleMuonGunPostLS1/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_78_1_xvV.root',
	'/store/user/akunsken/SingleMuonGunPostLS1/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_98_1_anz.root',
	'/store/user/akunsken/SingleMuonGunPostLS1/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_61_1_Uq5.root',
	'/store/user/akunsken/SingleMuonGunPostLS1/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_79_1_DU3.root',
	'/store/user/akunsken/SingleMuonGunPostLS1/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_24_1_T2o.root',
	'/store/user/akunsken/SingleMuonGunPostLS1/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_75_1_7Dp.root',
	'/store/user/akunsken/SingleMuonGunPostLS1/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_69_1_Eeb.root',
	'/store/user/akunsken/SingleMuonGunPostLS1/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_60_1_IT9.root',
	'/store/user/akunsken/SingleMuonGunPostLS1/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_77_1_u5E.root',
	'/store/user/akunsken/SingleMuonGunPostLS1/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_83_1_9vD.root',
	'/store/user/akunsken/SingleMuonGunPostLS1/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_44_1_kz3.root',
	'/store/user/akunsken/SingleMuonGunPostLS1/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_62_1_NIW.root',
	'/store/user/akunsken/SingleMuonGunPostLS1/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_76_1_jwE.root',
	'/store/user/akunsken/SingleMuonGunPostLS1/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_51_1_Nns.root',
	'/store/user/akunsken/SingleMuonGunPostLS1/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_96_1_Vxv.root',
	'/store/user/akunsken/SingleMuonGunPostLS1/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_67_1_aTJ.root',
	'/store/user/akunsken/SingleMuonGunPostLS1/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_88_1_3Kv.root',
	'/store/user/akunsken/SingleMuonGunPostLS1/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_91_1_mPe.root',
	'/store/user/akunsken/SingleMuonGunPostLS1/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_90_1_TnD.root',
	'/store/user/akunsken/SingleMuonGunPostLS1/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_70_1_uFD.root',
	'/store/user/akunsken/SingleMuonGunPostLS1/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_56_1_TEF.root',
	'/store/user/akunsken/SingleMuonGunPostLS1/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_41_1_Trh.root',
	'/store/user/akunsken/SingleMuonGunPostLS1/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_26_1_y9L.root',
	'/store/user/akunsken/SingleMuonGunPostLS1/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_87_1_BNF.root',
	'/store/user/akunsken/SingleMuonGunPostLS1/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_30_1_WKQ.root',
	'/store/user/akunsken/SingleMuonGunPostLS1/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_82_1_jmN.root',
	'/store/user/akunsken/SingleMuonGunPostLS1/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_38_1_nw5.root',
	'/store/user/akunsken/SingleMuonGunPostLS1/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_35_1_hUr.root',
	'/store/user/akunsken/SingleMuonGunPostLS1/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_89_1_fT8.root',
	'/store/user/akunsken/SingleMuonGunPostLS1/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_73_1_7bo.root',
	'/store/user/akunsken/SingleMuonGunPostLS1/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_84_1_lAZ.root',
	'/store/user/akunsken/SingleMuonGunPostLS1/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_23_1_ErO.root',
	'/store/user/akunsken/SingleMuonGunPostLS1/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_42_1_DTs.root',
	'/store/user/akunsken/SingleMuonGunPostLS1/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_25_1_eHb.root',
	'/store/user/akunsken/SingleMuonGunPostLS1/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_40_1_mE4.root',
	'/store/user/akunsken/SingleMuonGunPostLS1/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_80_1_SoL.root',
	'/store/user/akunsken/SingleMuonGunPostLS1/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_59_1_kj1.root',
	'/store/user/akunsken/SingleMuonGunPostLS1/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_28_1_rJ2.root',
	'/store/user/akunsken/SingleMuonGunPostLS1/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_66_1_hvJ.root',
	'/store/user/akunsken/SingleMuonGunPostLS1/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_27_1_dOz.root',
	'/store/user/akunsken/SingleMuonGunPostLS1/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_31_1_W4u.root',
	'/store/user/akunsken/SingleMuonGunPostLS1/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_68_1_09h.root',
	'/store/user/akunsken/SingleMuonGunPostLS1/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_53_1_Ke7.root',
	'/store/user/akunsken/SingleMuonGunPostLS1/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_45_1_ykg.root',
	'/store/user/akunsken/SingleMuonGunPostLS1/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_71_1_vGO.root',
	'/store/user/akunsken/SingleMuonGunPostLS1/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_52_1_rDb.root',
	'/store/user/akunsken/SingleMuonGunPostLS1/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_47_1_oqv.root',
	'/store/user/akunsken/SingleMuonGunPostLS1/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_72_1_u9I.root',
	'/store/user/akunsken/SingleMuonGunPostLS1/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_86_1_gCQ.root',
	'/store/user/akunsken/SingleMuonGunPostLS1/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_43_1_USN.root',
	'/store/user/akunsken/SingleMuonGunPostLS1/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_54_1_UUn.root',
	'/store/user/akunsken/SingleMuonGunPostLS1/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_36_1_jAE.root',
	'/store/user/akunsken/SingleMuonGunPostLS1/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_46_1_nlz.root',
	'/store/user/akunsken/SingleMuonGunPostLS1/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_49_1_q87.root',
	'/store/user/akunsken/SingleMuonGunPostLS1/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_37_1_RZU.root',
	'/store/user/akunsken/SingleMuonGunPostLS1/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_48_1_e1G.root',
	'/store/user/akunsken/SingleMuonGunPostLS1/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_29_1_Osc.root',
	'/store/user/akunsken/SingleMuonGunPostLS1/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_65_1_QeZ.root',
	'/store/user/akunsken/SingleMuonGunPostLS1/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_85_1_g4u.root',
	'/store/user/akunsken/SingleMuonGunPostLS1/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_34_2_nKt.root'
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
process.load('L1Trigger.Configuration.L1Extra_cff')

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
process.l1extra_step = cms.Path(process.L1Extra)
process.horeco_step = cms.Path(process.horeco)
process.l1MuonGenMatch_step = cms.Path(process.l1MuonGenMatch)
process.demo_step = cms.Path(process.hoMuonAnalyzer)


#Schedule Definition
process.schedule = cms.Schedule(
#	process.L1simulation_step,
	process.l1extra_step,
	process.horeco_step,
	process.l1MuonGenMatch_step,
	process.demo_step
	)


# Automatic addition of the customisation function from SLHCUpgradeSimulations.Configuration.postLS1Customs
from SLHCUpgradeSimulations.Configuration.postLS1Customs import customisePostLS1 

#call to customisation function customisePostLS1 imported from SLHCUpgradeSimulations.Configuration.postLS1Customs
process = customisePostLS1(process)

# End of customisation functions
