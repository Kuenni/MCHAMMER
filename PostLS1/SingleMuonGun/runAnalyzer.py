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
	'/store/user/akunsken/SingleMuonGunPostLS1/SingleMuPt100_cfi_GEN_SIM_DIGI_DIGI2RAW_RAW2DIGI_L1_L1Reco_3_2_Lcw.root',
	'/store/user/akunsken/SingleMuonGunPostLS1/SingleMuPt100_cfi_GEN_SIM_DIGI_DIGI2RAW_RAW2DIGI_L1_L1Reco_61_1_axK.root',
	'/store/user/akunsken/SingleMuonGunPostLS1/SingleMuPt100_cfi_GEN_SIM_DIGI_DIGI2RAW_RAW2DIGI_L1_L1Reco_44_2_MLj.root',
	'/store/user/akunsken/SingleMuonGunPostLS1/SingleMuPt100_cfi_GEN_SIM_DIGI_DIGI2RAW_RAW2DIGI_L1_L1Reco_50_2_0UU.root',
	'/store/user/akunsken/SingleMuonGunPostLS1/SingleMuPt100_cfi_GEN_SIM_DIGI_DIGI2RAW_RAW2DIGI_L1_L1Reco_58_2_Lwl.root',
	'/store/user/akunsken/SingleMuonGunPostLS1/SingleMuPt100_cfi_GEN_SIM_DIGI_DIGI2RAW_RAW2DIGI_L1_L1Reco_67_2_W56.root',
	'/store/user/akunsken/SingleMuonGunPostLS1/SingleMuPt100_cfi_GEN_SIM_DIGI_DIGI2RAW_RAW2DIGI_L1_L1Reco_16_2_TUH.root',
	'/store/user/akunsken/SingleMuonGunPostLS1/SingleMuPt100_cfi_GEN_SIM_DIGI_DIGI2RAW_RAW2DIGI_L1_L1Reco_6_2_KSq.root',
	'/store/user/akunsken/SingleMuonGunPostLS1/SingleMuPt100_cfi_GEN_SIM_DIGI_DIGI2RAW_RAW2DIGI_L1_L1Reco_80_1_ocb.root',
	'/store/user/akunsken/SingleMuonGunPostLS1/SingleMuPt100_cfi_GEN_SIM_DIGI_DIGI2RAW_RAW2DIGI_L1_L1Reco_73_1_jBc.root',
	'/store/user/akunsken/SingleMuonGunPostLS1/SingleMuPt100_cfi_GEN_SIM_DIGI_DIGI2RAW_RAW2DIGI_L1_L1Reco_40_1_XBr.root',
	'/store/user/akunsken/SingleMuonGunPostLS1/SingleMuPt100_cfi_GEN_SIM_DIGI_DIGI2RAW_RAW2DIGI_L1_L1Reco_99_1_jzd.root',
	'/store/user/akunsken/SingleMuonGunPostLS1/SingleMuPt100_cfi_GEN_SIM_DIGI_DIGI2RAW_RAW2DIGI_L1_L1Reco_2_1_pxH.root',
	'/store/user/akunsken/SingleMuonGunPostLS1/SingleMuPt100_cfi_GEN_SIM_DIGI_DIGI2RAW_RAW2DIGI_L1_L1Reco_31_1_KPz.root',
	'/store/user/akunsken/SingleMuonGunPostLS1/SingleMuPt100_cfi_GEN_SIM_DIGI_DIGI2RAW_RAW2DIGI_L1_L1Reco_1_1_IO4.root',
	'/store/user/akunsken/SingleMuonGunPostLS1/SingleMuPt100_cfi_GEN_SIM_DIGI_DIGI2RAW_RAW2DIGI_L1_L1Reco_66_1_gMl.root',
	'/store/user/akunsken/SingleMuonGunPostLS1/SingleMuPt100_cfi_GEN_SIM_DIGI_DIGI2RAW_RAW2DIGI_L1_L1Reco_62_1_oLN.root',
	'/store/user/akunsken/SingleMuonGunPostLS1/SingleMuPt100_cfi_GEN_SIM_DIGI_DIGI2RAW_RAW2DIGI_L1_L1Reco_47_1_6eZ.root',
	'/store/user/akunsken/SingleMuonGunPostLS1/SingleMuPt100_cfi_GEN_SIM_DIGI_DIGI2RAW_RAW2DIGI_L1_L1Reco_12_1_iJo.root',
	'/store/user/akunsken/SingleMuonGunPostLS1/SingleMuPt100_cfi_GEN_SIM_DIGI_DIGI2RAW_RAW2DIGI_L1_L1Reco_64_1_K2Q.root',
	'/store/user/akunsken/SingleMuonGunPostLS1/SingleMuPt100_cfi_GEN_SIM_DIGI_DIGI2RAW_RAW2DIGI_L1_L1Reco_70_1_4UJ.root',
	'/store/user/akunsken/SingleMuonGunPostLS1/SingleMuPt100_cfi_GEN_SIM_DIGI_DIGI2RAW_RAW2DIGI_L1_L1Reco_14_1_p98.root',
	'/store/user/akunsken/SingleMuonGunPostLS1/SingleMuPt100_cfi_GEN_SIM_DIGI_DIGI2RAW_RAW2DIGI_L1_L1Reco_63_1_hkG.root',
	'/store/user/akunsken/SingleMuonGunPostLS1/SingleMuPt100_cfi_GEN_SIM_DIGI_DIGI2RAW_RAW2DIGI_L1_L1Reco_57_1_Q0r.root',
	'/store/user/akunsken/SingleMuonGunPostLS1/SingleMuPt100_cfi_GEN_SIM_DIGI_DIGI2RAW_RAW2DIGI_L1_L1Reco_65_1_AMu.root',
	'/store/user/akunsken/SingleMuonGunPostLS1/SingleMuPt100_cfi_GEN_SIM_DIGI_DIGI2RAW_RAW2DIGI_L1_L1Reco_92_1_BTH.root',
	'/store/user/akunsken/SingleMuonGunPostLS1/SingleMuPt100_cfi_GEN_SIM_DIGI_DIGI2RAW_RAW2DIGI_L1_L1Reco_15_1_xYD.root',
	'/store/user/akunsken/SingleMuonGunPostLS1/SingleMuPt100_cfi_GEN_SIM_DIGI_DIGI2RAW_RAW2DIGI_L1_L1Reco_43_1_ugT.root',
	'/store/user/akunsken/SingleMuonGunPostLS1/SingleMuPt100_cfi_GEN_SIM_DIGI_DIGI2RAW_RAW2DIGI_L1_L1Reco_49_1_6BW.root',
	'/store/user/akunsken/SingleMuonGunPostLS1/SingleMuPt100_cfi_GEN_SIM_DIGI_DIGI2RAW_RAW2DIGI_L1_L1Reco_82_1_6IX.root',
	'/store/user/akunsken/SingleMuonGunPostLS1/SingleMuPt100_cfi_GEN_SIM_DIGI_DIGI2RAW_RAW2DIGI_L1_L1Reco_88_1_L2n.root',
	'/store/user/akunsken/SingleMuonGunPostLS1/SingleMuPt100_cfi_GEN_SIM_DIGI_DIGI2RAW_RAW2DIGI_L1_L1Reco_45_1_Mjh.root',
	'/store/user/akunsken/SingleMuonGunPostLS1/SingleMuPt100_cfi_GEN_SIM_DIGI_DIGI2RAW_RAW2DIGI_L1_L1Reco_98_1_tYH.root',
	'/store/user/akunsken/SingleMuonGunPostLS1/SingleMuPt100_cfi_GEN_SIM_DIGI_DIGI2RAW_RAW2DIGI_L1_L1Reco_83_1_X8h.root',
	'/store/user/akunsken/SingleMuonGunPostLS1/SingleMuPt100_cfi_GEN_SIM_DIGI_DIGI2RAW_RAW2DIGI_L1_L1Reco_17_1_KyN.root',
	'/store/user/akunsken/SingleMuonGunPostLS1/SingleMuPt100_cfi_GEN_SIM_DIGI_DIGI2RAW_RAW2DIGI_L1_L1Reco_87_1_ZDx.root',
	'/store/user/akunsken/SingleMuonGunPostLS1/SingleMuPt100_cfi_GEN_SIM_DIGI_DIGI2RAW_RAW2DIGI_L1_L1Reco_42_1_hgC.root',
	'/store/user/akunsken/SingleMuonGunPostLS1/SingleMuPt100_cfi_GEN_SIM_DIGI_DIGI2RAW_RAW2DIGI_L1_L1Reco_86_1_iJe.root',
	'/store/user/akunsken/SingleMuonGunPostLS1/SingleMuPt100_cfi_GEN_SIM_DIGI_DIGI2RAW_RAW2DIGI_L1_L1Reco_89_1_dUO.root',
	'/store/user/akunsken/SingleMuonGunPostLS1/SingleMuPt100_cfi_GEN_SIM_DIGI_DIGI2RAW_RAW2DIGI_L1_L1Reco_13_1_g51.root',
	'/store/user/akunsken/SingleMuonGunPostLS1/SingleMuPt100_cfi_GEN_SIM_DIGI_DIGI2RAW_RAW2DIGI_L1_L1Reco_84_1_5Nd.root',
	'/store/user/akunsken/SingleMuonGunPostLS1/SingleMuPt100_cfi_GEN_SIM_DIGI_DIGI2RAW_RAW2DIGI_L1_L1Reco_5_1_jED.root',
	'/store/user/akunsken/SingleMuonGunPostLS1/SingleMuPt100_cfi_GEN_SIM_DIGI_DIGI2RAW_RAW2DIGI_L1_L1Reco_77_1_pIu.root',
	'/store/user/akunsken/SingleMuonGunPostLS1/SingleMuPt100_cfi_GEN_SIM_DIGI_DIGI2RAW_RAW2DIGI_L1_L1Reco_20_1_aSt.root',
	'/store/user/akunsken/SingleMuonGunPostLS1/SingleMuPt100_cfi_GEN_SIM_DIGI_DIGI2RAW_RAW2DIGI_L1_L1Reco_75_1_RFD.root',
	'/store/user/akunsken/SingleMuonGunPostLS1/SingleMuPt100_cfi_GEN_SIM_DIGI_DIGI2RAW_RAW2DIGI_L1_L1Reco_94_1_7c2.root',
	'/store/user/akunsken/SingleMuonGunPostLS1/SingleMuPt100_cfi_GEN_SIM_DIGI_DIGI2RAW_RAW2DIGI_L1_L1Reco_95_1_AbJ.root',
	'/store/user/akunsken/SingleMuonGunPostLS1/SingleMuPt100_cfi_GEN_SIM_DIGI_DIGI2RAW_RAW2DIGI_L1_L1Reco_76_1_syG.root',
	'/store/user/akunsken/SingleMuonGunPostLS1/SingleMuPt100_cfi_GEN_SIM_DIGI_DIGI2RAW_RAW2DIGI_L1_L1Reco_26_1_u7z.root',
	'/store/user/akunsken/SingleMuonGunPostLS1/SingleMuPt100_cfi_GEN_SIM_DIGI_DIGI2RAW_RAW2DIGI_L1_L1Reco_23_1_byo.root',
	'/store/user/akunsken/SingleMuonGunPostLS1/SingleMuPt100_cfi_GEN_SIM_DIGI_DIGI2RAW_RAW2DIGI_L1_L1Reco_24_1_o6j.root',
	'/store/user/akunsken/SingleMuonGunPostLS1/SingleMuPt100_cfi_GEN_SIM_DIGI_DIGI2RAW_RAW2DIGI_L1_L1Reco_21_1_jFK.root',
	'/store/user/akunsken/SingleMuonGunPostLS1/SingleMuPt100_cfi_GEN_SIM_DIGI_DIGI2RAW_RAW2DIGI_L1_L1Reco_38_1_ZJd.root',
	'/store/user/akunsken/SingleMuonGunPostLS1/SingleMuPt100_cfi_GEN_SIM_DIGI_DIGI2RAW_RAW2DIGI_L1_L1Reco_55_1_7wg.root',
	'/store/user/akunsken/SingleMuonGunPostLS1/SingleMuPt100_cfi_GEN_SIM_DIGI_DIGI2RAW_RAW2DIGI_L1_L1Reco_74_1_0HS.root',
	'/store/user/akunsken/SingleMuonGunPostLS1/SingleMuPt100_cfi_GEN_SIM_DIGI_DIGI2RAW_RAW2DIGI_L1_L1Reco_29_1_II8.root',
	'/store/user/akunsken/SingleMuonGunPostLS1/SingleMuPt100_cfi_GEN_SIM_DIGI_DIGI2RAW_RAW2DIGI_L1_L1Reco_18_1_BcT.root',
	'/store/user/akunsken/SingleMuonGunPostLS1/SingleMuPt100_cfi_GEN_SIM_DIGI_DIGI2RAW_RAW2DIGI_L1_L1Reco_39_1_wzS.root',
	'/store/user/akunsken/SingleMuonGunPostLS1/SingleMuPt100_cfi_GEN_SIM_DIGI_DIGI2RAW_RAW2DIGI_L1_L1Reco_59_1_fGn.root',
	'/store/user/akunsken/SingleMuonGunPostLS1/SingleMuPt100_cfi_GEN_SIM_DIGI_DIGI2RAW_RAW2DIGI_L1_L1Reco_60_1_dG6.root',
	'/store/user/akunsken/SingleMuonGunPostLS1/SingleMuPt100_cfi_GEN_SIM_DIGI_DIGI2RAW_RAW2DIGI_L1_L1Reco_36_1_57J.root',
	'/store/user/akunsken/SingleMuonGunPostLS1/SingleMuPt100_cfi_GEN_SIM_DIGI_DIGI2RAW_RAW2DIGI_L1_L1Reco_91_1_3FL.root',
	'/store/user/akunsken/SingleMuonGunPostLS1/SingleMuPt100_cfi_GEN_SIM_DIGI_DIGI2RAW_RAW2DIGI_L1_L1Reco_19_1_9Yr.root',
	'/store/user/akunsken/SingleMuonGunPostLS1/SingleMuPt100_cfi_GEN_SIM_DIGI_DIGI2RAW_RAW2DIGI_L1_L1Reco_85_1_A5c.root',
	'/store/user/akunsken/SingleMuonGunPostLS1/SingleMuPt100_cfi_GEN_SIM_DIGI_DIGI2RAW_RAW2DIGI_L1_L1Reco_90_1_xeC.root',
	'/store/user/akunsken/SingleMuonGunPostLS1/SingleMuPt100_cfi_GEN_SIM_DIGI_DIGI2RAW_RAW2DIGI_L1_L1Reco_69_1_tJg.root',
	'/store/user/akunsken/SingleMuonGunPostLS1/SingleMuPt100_cfi_GEN_SIM_DIGI_DIGI2RAW_RAW2DIGI_L1_L1Reco_7_1_XJZ.root',
	'/store/user/akunsken/SingleMuonGunPostLS1/SingleMuPt100_cfi_GEN_SIM_DIGI_DIGI2RAW_RAW2DIGI_L1_L1Reco_51_1_Hc0.root',
	'/store/user/akunsken/SingleMuonGunPostLS1/SingleMuPt100_cfi_GEN_SIM_DIGI_DIGI2RAW_RAW2DIGI_L1_L1Reco_93_1_6IP.root',
	'/store/user/akunsken/SingleMuonGunPostLS1/SingleMuPt100_cfi_GEN_SIM_DIGI_DIGI2RAW_RAW2DIGI_L1_L1Reco_81_1_7J8.root',
	'/store/user/akunsken/SingleMuonGunPostLS1/SingleMuPt100_cfi_GEN_SIM_DIGI_DIGI2RAW_RAW2DIGI_L1_L1Reco_54_1_z0i.root',
	'/store/user/akunsken/SingleMuonGunPostLS1/SingleMuPt100_cfi_GEN_SIM_DIGI_DIGI2RAW_RAW2DIGI_L1_L1Reco_53_1_YhG.root',
	'/store/user/akunsken/SingleMuonGunPostLS1/SingleMuPt100_cfi_GEN_SIM_DIGI_DIGI2RAW_RAW2DIGI_L1_L1Reco_56_1_zMi.root',
	'/store/user/akunsken/SingleMuonGunPostLS1/SingleMuPt100_cfi_GEN_SIM_DIGI_DIGI2RAW_RAW2DIGI_L1_L1Reco_9_1_Qf3.root',
	'/store/user/akunsken/SingleMuonGunPostLS1/SingleMuPt100_cfi_GEN_SIM_DIGI_DIGI2RAW_RAW2DIGI_L1_L1Reco_48_1_LKR.root',
	'/store/user/akunsken/SingleMuonGunPostLS1/SingleMuPt100_cfi_GEN_SIM_DIGI_DIGI2RAW_RAW2DIGI_L1_L1Reco_4_1_Gtc.root',
	'/store/user/akunsken/SingleMuonGunPostLS1/SingleMuPt100_cfi_GEN_SIM_DIGI_DIGI2RAW_RAW2DIGI_L1_L1Reco_96_1_H2c.root',
	'/store/user/akunsken/SingleMuonGunPostLS1/SingleMuPt100_cfi_GEN_SIM_DIGI_DIGI2RAW_RAW2DIGI_L1_L1Reco_97_1_hB7.root',
	'/store/user/akunsken/SingleMuonGunPostLS1/SingleMuPt100_cfi_GEN_SIM_DIGI_DIGI2RAW_RAW2DIGI_L1_L1Reco_41_1_Jea.root',
	'/store/user/akunsken/SingleMuonGunPostLS1/SingleMuPt100_cfi_GEN_SIM_DIGI_DIGI2RAW_RAW2DIGI_L1_L1Reco_8_1_q6e.root',
	'/store/user/akunsken/SingleMuonGunPostLS1/SingleMuPt100_cfi_GEN_SIM_DIGI_DIGI2RAW_RAW2DIGI_L1_L1Reco_79_1_OT7.root',
	'/store/user/akunsken/SingleMuonGunPostLS1/SingleMuPt100_cfi_GEN_SIM_DIGI_DIGI2RAW_RAW2DIGI_L1_L1Reco_68_1_tzp.root',
	'/store/user/akunsken/SingleMuonGunPostLS1/SingleMuPt100_cfi_GEN_SIM_DIGI_DIGI2RAW_RAW2DIGI_L1_L1Reco_78_1_2Hz.root',
	'/store/user/akunsken/SingleMuonGunPostLS1/SingleMuPt100_cfi_GEN_SIM_DIGI_DIGI2RAW_RAW2DIGI_L1_L1Reco_27_1_juc.root',
	'/store/user/akunsken/SingleMuonGunPostLS1/SingleMuPt100_cfi_GEN_SIM_DIGI_DIGI2RAW_RAW2DIGI_L1_L1Reco_52_1_5IP.root',
	'/store/user/akunsken/SingleMuonGunPostLS1/SingleMuPt100_cfi_GEN_SIM_DIGI_DIGI2RAW_RAW2DIGI_L1_L1Reco_25_1_36f.root',
	'/store/user/akunsken/SingleMuonGunPostLS1/SingleMuPt100_cfi_GEN_SIM_DIGI_DIGI2RAW_RAW2DIGI_L1_L1Reco_11_1_3h1.root',
	'/store/user/akunsken/SingleMuonGunPostLS1/SingleMuPt100_cfi_GEN_SIM_DIGI_DIGI2RAW_RAW2DIGI_L1_L1Reco_10_1_sBm.root',
	'/store/user/akunsken/SingleMuonGunPostLS1/SingleMuPt100_cfi_GEN_SIM_DIGI_DIGI2RAW_RAW2DIGI_L1_L1Reco_46_1_xkl.root',
	'/store/user/akunsken/SingleMuonGunPostLS1/SingleMuPt100_cfi_GEN_SIM_DIGI_DIGI2RAW_RAW2DIGI_L1_L1Reco_22_1_mBV.root',
	'/store/user/akunsken/SingleMuonGunPostLS1/SingleMuPt100_cfi_GEN_SIM_DIGI_DIGI2RAW_RAW2DIGI_L1_L1Reco_72_1_1Fg.root'
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
process.load('Configuration.StandardSequences.L1Extra_cff')




process.FEVTDEBUGHLToutput = cms.OutputModule("PoolOutputModule",
    splitLevel = cms.untracked.int32(0),
    eventAutoFlushCompressedSize = cms.untracked.int32(1048576),
    outputCommands = process.FEVTDEBUGHLTEventContent.outputCommands,
    fileName = cms.untracked.string('SingleMuPt100_WithL1Extra.root'),
    dataset = cms.untracked.PSet(
        filterName = cms.untracked.string(''),
        dataTier = cms.untracked.string('')
    ),
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('l1extra_step')
    )
)


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
process.L1simulation_step = cms.Path(process.SimL1Emulator)
process.l1extra_step = cms.Path(process.L1Extra)
process.horeco_step = cms.Path(process.horeco)
process.l1MuonGenMatch_step = cms.Path(process.l1MuonGenMatch)
process.demo_step = cms.Path(process.hoMuonAnalyzer)
process.FEVTDEBUGHLToutput_step = cms.EndPath(process.FEVTDEBUGHLToutput)


#Schedule Definition
process.schedule = cms.Schedule(
#	process.L1simulation_step,
#	process.l1extra_step,
	process.horeco_step,
	process.l1MuonGenMatch_step,
	process.demo_step,
#	process.FEVTDEBUGHLToutput_step
	)


# Automatic addition of the customisation function from SLHCUpgradeSimulations.Configuration.postLS1Customs
from SLHCUpgradeSimulations.Configuration.postLS1Customs import customisePostLS1 

#call to customisation function customisePostLS1 imported from SLHCUpgradeSimulations.Configuration.postLS1Customs
process = customisePostLS1(process)

# End of customisation functions
