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
				'/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_100_1_1SE.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_101_1_YFu.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_102_1_q6I.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_103_1_F88.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_104_1_OCg.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_105_1_PZR.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_106_1_Sqx.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_107_1_Ipr.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_108_1_uh9.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_109_1_LR8.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_10_2_WIN.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_110_1_Ttx.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_111_1_UqV.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_112_1_Cg9.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_113_1_G7n.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_114_1_5E9.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_115_1_bHj.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_116_1_UGs.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_117_1_heN.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_118_1_xed.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_119_1_3Zp.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_11_2_wu0.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_120_1_xNx.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_121_1_s7Z.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_122_1_HKp.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_123_1_6w0.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_124_1_CkH.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_125_1_9uz.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_126_1_rlq.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_127_1_6ic.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_128_1_hwC.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_129_1_844.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_12_2_ci5.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_130_1_rKQ.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_131_1_gY9.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_132_1_6Pg.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_133_1_HnM.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_134_1_cep.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_135_1_etF.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_136_1_ol6.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_137_1_yxc.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_138_1_66T.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_139_1_WI4.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_13_2_Wkr.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_140_1_UQr.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_141_1_Fa9.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_142_1_WC1.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_143_1_qpn.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_144_1_uF2.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_145_1_7rC.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_146_1_FVB.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_147_1_o9L.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_148_1_OFx.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_149_1_1Re.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_14_2_8RQ.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_150_1_qFm.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_151_1_zAv.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_152_1_amr.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_153_1_CBW.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_154_1_7HI.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_155_1_aoq.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_156_1_omZ.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_157_1_0BB.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_158_1_MRB.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_159_1_oAF.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_15_1_FwL.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_160_1_YDF.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_161_1_vfb.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_162_1_MAk.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_163_1_Yrl.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_164_1_CYe.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_165_2_hWG.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_166_1_QXy.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_167_1_oOY.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_168_1_myk.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_169_1_0iG.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_16_1_OwP.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_170_1_puu.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_171_1_V5l.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_172_1_zrg.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_173_1_cKZ.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_174_1_lOE.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_175_1_XiE.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_176_1_oXz.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_177_1_Xvq.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_178_1_kmC.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_179_1_7mZ.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_17_1_qpf.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_180_1_cHK.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_181_2_3aS.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_182_2_JST.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_183_1_mHS.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_184_1_Z1r.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_185_1_pmR.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_186_1_far.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_187_1_nhP.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_188_1_enu.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_189_1_rRU.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_18_1_kBm.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_190_1_ssh.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_191_1_o8C.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_192_1_A6g.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_193_1_Rqt.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_194_1_5Xx.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_195_1_zsl.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_196_1_nkl.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_197_1_iFo.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_198_1_uYC.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_199_1_4Yq.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_19_1_eAu.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_1_1_eRq.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_200_1_OLh.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_201_1_WqE.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_202_1_Ems.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_203_1_Hvn.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_204_1_dvg.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_205_1_KR8.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_206_1_WTx.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_207_1_iBx.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_208_1_0sC.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_209_1_vcS.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_20_1_CO6.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_210_1_HGz.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_211_1_3i7.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_212_1_fD7.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_213_1_qqS.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_214_1_tgX.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_215_1_lm9.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_216_1_cxR.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_217_1_FV7.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_218_1_HDI.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_219_1_bet.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_21_1_GVL.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_220_1_mvu.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_221_1_akf.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_222_1_Vcs.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_223_1_BS5.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_224_1_3nf.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_225_1_z4H.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_226_1_MOs.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_227_1_PJF.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_228_1_poJ.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_229_1_05i.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_22_1_3hC.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_230_1_EkO.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_231_1_gtq.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_232_1_awb.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_233_1_1iF.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_234_1_ubR.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_235_1_1UE.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_236_1_Orl.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_237_1_uh2.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_238_1_VWy.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_239_1_cdq.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_23_1_iQI.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_240_1_06a.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_241_1_QjS.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_242_1_lfR.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_243_1_52j.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_244_1_NdY.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_245_1_k9O.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_246_1_Sl1.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_247_1_2NW.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_248_1_pXR.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_249_1_elF.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_24_1_DB6.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_250_1_k2a.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_251_1_7Vb.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_252_1_gWx.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_253_1_XTf.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_254_1_xcr.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_255_1_odp.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_256_1_HGn.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_257_1_C5n.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_258_1_QlM.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_259_1_WlA.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_25_1_JCj.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_260_1_Pnr.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_261_1_fyj.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_262_1_z79.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_263_1_41i.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_264_1_3iR.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_265_1_rwK.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_266_1_LtT.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_267_1_qTi.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_268_1_RbH.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_269_1_4dt.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_26_1_0oa.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_270_1_jBE.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_271_1_2ud.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_272_1_kBn.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_273_1_f0L.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_274_1_dnE.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_275_1_V40.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_276_1_C37.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_277_1_mKz.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_278_1_I1A.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_279_1_AF3.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_27_1_6R9.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_280_1_pO2.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_281_1_lHq.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_282_1_PSz.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_283_1_Bnh.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_284_1_ji0.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_285_1_KGN.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_286_1_xZB.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_287_1_dwY.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_288_1_8gB.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_289_1_g7B.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_28_1_fYA.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_290_1_3KV.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_291_1_LN6.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_292_1_U3s.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_293_1_Q6U.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_294_1_ggm.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_295_1_Lsb.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_296_1_A99.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_297_1_a3x.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_298_1_Lhg.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_299_1_vaY.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_29_1_Mxy.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_2_2_NBt.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_300_1_n13.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_301_1_0EM.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_302_1_Tl0.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_303_1_LHl.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_304_1_cdR.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_305_1_Evy.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_306_1_WRA.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_307_1_5qr.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_308_1_j5w.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_309_1_HAR.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_30_1_gwY.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_310_1_LAk.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_311_1_77R.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_312_1_sx2.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_313_1_NAp.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_314_1_nGK.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_315_1_RHf.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_316_1_cBf.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_317_1_j39.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_318_1_re0.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_319_1_Mvf.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_31_1_GkF.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_320_1_0BY.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_321_1_365.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_322_1_8HQ.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_323_1_Y1V.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_324_1_boF.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_325_1_Y7a.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_326_1_qBb.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_327_1_IOi.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_328_1_VbG.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_329_1_ReL.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_32_1_rBl.root'
   ])

readFiles.extend( [

       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_330_1_sZH.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_331_1_ZIa.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_332_1_fLV.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_333_1_4fR.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_334_1_4ZD.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_335_1_AN3.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_336_1_LtY.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_337_1_PTq.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_338_1_AhZ.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_339_1_T0R.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_33_1_X60.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_340_1_5gz.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_341_1_myp.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_342_1_CFP.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_343_1_zz4.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_344_1_EEo.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_345_1_Ydz.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_346_1_uKX.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_347_1_Bva.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_348_1_5De.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_349_1_NKh.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_34_1_EwE.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_350_1_CIW.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_351_1_4xk.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_352_1_YY2.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_353_1_f69.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_354_1_SkW.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_355_1_jD4.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_356_1_Shc.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_357_1_2ir.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_358_1_LAV.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_359_1_Pbu.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_35_1_Pte.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_360_1_RVv.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_361_1_8ki.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_362_1_K0m.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_363_1_POV.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_364_1_PIL.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_365_1_Kv7.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_366_1_VK8.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_367_1_oI3.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_368_1_wgx.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_369_1_dk5.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_36_2_U4d.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_370_1_92k.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_371_1_DDa.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_372_1_dOR.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_373_1_rJY.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_374_1_0rU.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_375_1_xbT.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_376_1_ZYN.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_377_1_rSZ.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_378_1_88g.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_379_1_MhW.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_37_1_GsW.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_380_1_hlp.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_381_1_yi0.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_382_1_0XY.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_383_1_nS8.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_384_1_WTk.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_385_1_7rp.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_386_1_pH1.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_387_1_xFk.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_388_1_GIP.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_389_1_Jaz.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_38_1_IMC.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_390_1_aSq.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_391_1_wfM.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_392_1_ImG.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_393_1_w3U.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_394_1_CPQ.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_395_1_bzK.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_396_1_oza.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_397_1_JQi.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_398_1_Nvt.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_399_1_c83.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_39_1_hgI.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_3_2_upR.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_400_1_iaX.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_40_1_5Y7.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_41_1_EWA.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_42_1_pss.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_43_1_Whm.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_44_1_yCv.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_45_1_u92.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_46_1_pNL.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_47_1_roe.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_48_1_ZVC.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_49_1_XEn.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_4_2_CFz.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_50_1_cPm.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_51_1_LRv.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_52_1_MF4.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_53_1_ZsG.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_54_1_Ags.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_55_1_ZLz.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_56_1_Vsy.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_57_1_YKj.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_58_1_g97.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_59_1_iYI.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_5_2_NYi.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_60_2_TLO.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_61_2_6F7.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_62_1_eJA.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_63_1_jyJ.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_64_1_FR5.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_65_1_csA.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_66_1_Fah.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_67_1_gph.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_68_1_WjV.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_69_1_zHG.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_6_2_W1i.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_70_1_VVT.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_71_1_Hcu.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_72_1_AcO.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_73_1_iXG.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_74_1_2hL.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_75_1_gjD.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_76_1_KH0.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_77_1_Soz.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_78_1_qd2.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_79_1_N3b.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_7_2_GtL.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_80_1_ZU5.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_81_1_BCA.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_82_1_vDW.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_83_1_Vq7.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_84_1_lkV.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_85_1_ygm.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_86_1_uqa.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_87_1_J2p.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_88_1_ukU.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_89_1_74s.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_8_2_JS6.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_90_1_DrK.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_91_1_riT.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_92_1_CJ5.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_93_1_2y2.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_94_1_PUx.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_95_1_FJr.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_96_1_gZZ.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_97_1_08d.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_98_1_uTa.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_99_1_SHY.root',
       '/store/user/akunsken/MuonGun2023PtRange/MuonGun2023PtRange/a1be6704b024117db9141725b8a2f5f7/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_9_2_etK.root' 
       ] )

process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load('Configuration.Geometry.GeometryExtended2023MuonReco_cff')
process.load('Configuration.Geometry.GeometryExtended2023Muon_cff')
process.load('Configuration.StandardSequences.MagneticField_38T_PostLS1_cff')
process.load('Configuration.StandardSequences.Generator_cff')
process.load('IOMC.EventVertexGenerators.VtxSmearedHLLHC_cfi')
process.load('GeneratorInterface.Core.genFilterSummary_cff')
process.load('Configuration.StandardSequences.SimIdeal_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')


# Digi, RawToDigi and Necessary Configuartion Files
#process.load('Configuration.StandardSequences.Digi_cff')
#process.load('Configuration.StandardSequences.DigiToRaw_cff')
#process.load('Configuration.StandardSequences.SimL1Emulator_cff')


#Global Tag
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
#process.GlobalTag.globaltag='DES23_62_V1::All'
#RawToDigi
#process.load('Configuration.StandardSequences.RawToDigi_cff')

#turn off HO ZS
#process.hcalRawData.HO = cms.untracked.InputTag("simHcalUnsuppressedDigis", "", "")

#L1Extra
#process.load('L1Trigger.Configuration.L1Extra_cff')

#horeco
process.load('Configuration.StandardSequences.Reconstruction_cff')

#process.mix.digitizers = cms.PSet(process.theDigitizersValid)

from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'DES23_62_V1::All', '')


process.hoMuonAnalyzer = cms.EDAnalyzer(
    'hoMuonAnalyzer',
    genSrc = cms.InputTag("genParticles"),
    l1MuonSrc=cms.InputTag("l1extraParticles"),
    #stdMuSrc = cms.InputTag("standAloneMuons"),
    horecoSrc = cms.InputTag("horeco"),
    #L1GtTmLInputTag = cms.InputTag("l1GtTriggerMenuLite")
    hltSumAODSrc = cms.InputTag("hltTriggerSummaryAOD"),
    l1MuonGenMatchSrc = cms.InputTag("l1MuonGenMatch"),
    maxDeltaR = cms.double(0.3),
    hoEnergyThreshold = cms.double(0.2)
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


#For the HLT
# customisation of the process.
# Automatic addition of the customisation function from HLTrigger.Configuration.customizeHLTforMC
#from HLTrigger.Configuration.customizeHLTforMC import customizeHLTforMC
#call to customisation function customizeHLTforMC imported from HLTrigger.Configuration.customizeHLTforMC
#process = customizeHLTforMC(process)

#HLT Tester
#import HLTrigger.HLTcore.triggerSummaryAnalyzerAOD_cfi
#process.tsaAOD = HLTrigger.HLTcore.triggerSummaryAnalyzerAOD_cfi.triggerSummaryAnalyzerAOD.clone()
#process.tsa = cms.Path(process.tsaAOD)#+process.tsaRAW)

#Schedule Definition
process.schedule = cms.Schedule(
#	process.digitisation_step,
#	process.digi2raw_step,
#	process.raw2digi_step,
#	process.L1simulation_step,
#	process.l1extra_step,
	process.horeco_step,
	process.l1MuonGenMatch_step,
	process.demo_step
	)
                                #,process.tsa)


# Automatic addition of the customisation function from SLHCUpgradeSimulations.Configuration.combinedCustoms
from SLHCUpgradeSimulations.Configuration.combinedCustoms import cust_2023Muon 

#call to customisation function cust_2023Muon imported from SLHCUpgradeSimulations.Configuration.combinedCustoms
process = cust_2023Muon(process)
