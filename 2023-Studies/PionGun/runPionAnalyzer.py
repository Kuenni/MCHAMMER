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
        '/store/user/akunsken/PionGun2023NoExtraCalib/PionGun2023NoExtraCalib/a351453415fe506672b2e12372b31e05/SinglePiPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_100_1_LOh.root',
       '/store/user/akunsken/PionGun2023NoExtraCalib/PionGun2023NoExtraCalib/a351453415fe506672b2e12372b31e05/SinglePiPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_101_1_PFQ.root',
       '/store/user/akunsken/PionGun2023NoExtraCalib/PionGun2023NoExtraCalib/a351453415fe506672b2e12372b31e05/SinglePiPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_102_1_rDP.root',
       '/store/user/akunsken/PionGun2023NoExtraCalib/PionGun2023NoExtraCalib/a351453415fe506672b2e12372b31e05/SinglePiPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_103_1_RHD.root',
       '/store/user/akunsken/PionGun2023NoExtraCalib/PionGun2023NoExtraCalib/a351453415fe506672b2e12372b31e05/SinglePiPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_104_1_Wxf.root',
       '/store/user/akunsken/PionGun2023NoExtraCalib/PionGun2023NoExtraCalib/a351453415fe506672b2e12372b31e05/SinglePiPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_105_1_HFs.root',
       '/store/user/akunsken/PionGun2023NoExtraCalib/PionGun2023NoExtraCalib/a351453415fe506672b2e12372b31e05/SinglePiPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_106_1_2YE.root',
       '/store/user/akunsken/PionGun2023NoExtraCalib/PionGun2023NoExtraCalib/a351453415fe506672b2e12372b31e05/SinglePiPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_107_2_zLe.root',
       '/store/user/akunsken/PionGun2023NoExtraCalib/PionGun2023NoExtraCalib/a351453415fe506672b2e12372b31e05/SinglePiPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_108_1_9Pj.root',
       '/store/user/akunsken/PionGun2023NoExtraCalib/PionGun2023NoExtraCalib/a351453415fe506672b2e12372b31e05/SinglePiPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_109_1_RKC.root',
       '/store/user/akunsken/PionGun2023NoExtraCalib/PionGun2023NoExtraCalib/a351453415fe506672b2e12372b31e05/SinglePiPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_10_1_qrz.root',
       '/store/user/akunsken/PionGun2023NoExtraCalib/PionGun2023NoExtraCalib/a351453415fe506672b2e12372b31e05/SinglePiPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_110_1_N4o.root',
       '/store/user/akunsken/PionGun2023NoExtraCalib/PionGun2023NoExtraCalib/a351453415fe506672b2e12372b31e05/SinglePiPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_111_1_YJ8.root',
       '/store/user/akunsken/PionGun2023NoExtraCalib/PionGun2023NoExtraCalib/a351453415fe506672b2e12372b31e05/SinglePiPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_112_1_Gzt.root',
       '/store/user/akunsken/PionGun2023NoExtraCalib/PionGun2023NoExtraCalib/a351453415fe506672b2e12372b31e05/SinglePiPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_113_1_Oew.root',
       '/store/user/akunsken/PionGun2023NoExtraCalib/PionGun2023NoExtraCalib/a351453415fe506672b2e12372b31e05/SinglePiPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_114_1_Qda.root',
       '/store/user/akunsken/PionGun2023NoExtraCalib/PionGun2023NoExtraCalib/a351453415fe506672b2e12372b31e05/SinglePiPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_115_1_Qus.root',
       '/store/user/akunsken/PionGun2023NoExtraCalib/PionGun2023NoExtraCalib/a351453415fe506672b2e12372b31e05/SinglePiPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_116_1_FD1.root',
       '/store/user/akunsken/PionGun2023NoExtraCalib/PionGun2023NoExtraCalib/a351453415fe506672b2e12372b31e05/SinglePiPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_117_2_k19.root',
       '/store/user/akunsken/PionGun2023NoExtraCalib/PionGun2023NoExtraCalib/a351453415fe506672b2e12372b31e05/SinglePiPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_118_1_JFn.root',
       '/store/user/akunsken/PionGun2023NoExtraCalib/PionGun2023NoExtraCalib/a351453415fe506672b2e12372b31e05/SinglePiPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_119_2_dtJ.root',
       '/store/user/akunsken/PionGun2023NoExtraCalib/PionGun2023NoExtraCalib/a351453415fe506672b2e12372b31e05/SinglePiPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_11_1_QrR.root',
       '/store/user/akunsken/PionGun2023NoExtraCalib/PionGun2023NoExtraCalib/a351453415fe506672b2e12372b31e05/SinglePiPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_120_2_Qdx.root',
       '/store/user/akunsken/PionGun2023NoExtraCalib/PionGun2023NoExtraCalib/a351453415fe506672b2e12372b31e05/SinglePiPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_121_2_gSL.root',
       '/store/user/akunsken/PionGun2023NoExtraCalib/PionGun2023NoExtraCalib/a351453415fe506672b2e12372b31e05/SinglePiPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_122_1_aKM.root',
       '/store/user/akunsken/PionGun2023NoExtraCalib/PionGun2023NoExtraCalib/a351453415fe506672b2e12372b31e05/SinglePiPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_123_1_PPq.root',
       '/store/user/akunsken/PionGun2023NoExtraCalib/PionGun2023NoExtraCalib/a351453415fe506672b2e12372b31e05/SinglePiPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_124_1_mNM.root',
       '/store/user/akunsken/PionGun2023NoExtraCalib/PionGun2023NoExtraCalib/a351453415fe506672b2e12372b31e05/SinglePiPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_125_1_E8B.root',
       '/store/user/akunsken/PionGun2023NoExtraCalib/PionGun2023NoExtraCalib/a351453415fe506672b2e12372b31e05/SinglePiPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_126_1_8zx.root',
       '/store/user/akunsken/PionGun2023NoExtraCalib/PionGun2023NoExtraCalib/a351453415fe506672b2e12372b31e05/SinglePiPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_127_2_BKK.root',
       '/store/user/akunsken/PionGun2023NoExtraCalib/PionGun2023NoExtraCalib/a351453415fe506672b2e12372b31e05/SinglePiPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_128_2_3R1.root',
       '/store/user/akunsken/PionGun2023NoExtraCalib/PionGun2023NoExtraCalib/a351453415fe506672b2e12372b31e05/SinglePiPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_129_1_OVP.root',
       '/store/user/akunsken/PionGun2023NoExtraCalib/PionGun2023NoExtraCalib/a351453415fe506672b2e12372b31e05/SinglePiPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_12_1_gd8.root',
       '/store/user/akunsken/PionGun2023NoExtraCalib/PionGun2023NoExtraCalib/a351453415fe506672b2e12372b31e05/SinglePiPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_130_2_3s4.root',
       '/store/user/akunsken/PionGun2023NoExtraCalib/PionGun2023NoExtraCalib/a351453415fe506672b2e12372b31e05/SinglePiPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_131_1_wWa.root',
       '/store/user/akunsken/PionGun2023NoExtraCalib/PionGun2023NoExtraCalib/a351453415fe506672b2e12372b31e05/SinglePiPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_132_2_M5y.root',
       '/store/user/akunsken/PionGun2023NoExtraCalib/PionGun2023NoExtraCalib/a351453415fe506672b2e12372b31e05/SinglePiPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_133_1_xBu.root',
       '/store/user/akunsken/PionGun2023NoExtraCalib/PionGun2023NoExtraCalib/a351453415fe506672b2e12372b31e05/SinglePiPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_134_1_cjU.root',
       '/store/user/akunsken/PionGun2023NoExtraCalib/PionGun2023NoExtraCalib/a351453415fe506672b2e12372b31e05/SinglePiPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_135_1_bq9.root',
       '/store/user/akunsken/PionGun2023NoExtraCalib/PionGun2023NoExtraCalib/a351453415fe506672b2e12372b31e05/SinglePiPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_136_1_RcG.root',
       '/store/user/akunsken/PionGun2023NoExtraCalib/PionGun2023NoExtraCalib/a351453415fe506672b2e12372b31e05/SinglePiPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_137_2_7uA.root',
       '/store/user/akunsken/PionGun2023NoExtraCalib/PionGun2023NoExtraCalib/a351453415fe506672b2e12372b31e05/SinglePiPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_138_2_8Kw.root',
       '/store/user/akunsken/PionGun2023NoExtraCalib/PionGun2023NoExtraCalib/a351453415fe506672b2e12372b31e05/SinglePiPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_139_3_P33.root',
       '/store/user/akunsken/PionGun2023NoExtraCalib/PionGun2023NoExtraCalib/a351453415fe506672b2e12372b31e05/SinglePiPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_13_1_P0i.root',
       '/store/user/akunsken/PionGun2023NoExtraCalib/PionGun2023NoExtraCalib/a351453415fe506672b2e12372b31e05/SinglePiPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_140_1_Fl1.root',
       '/store/user/akunsken/PionGun2023NoExtraCalib/PionGun2023NoExtraCalib/a351453415fe506672b2e12372b31e05/SinglePiPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_141_1_kNi.root',
       '/store/user/akunsken/PionGun2023NoExtraCalib/PionGun2023NoExtraCalib/a351453415fe506672b2e12372b31e05/SinglePiPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_142_1_NqN.root',
       '/store/user/akunsken/PionGun2023NoExtraCalib/PionGun2023NoExtraCalib/a351453415fe506672b2e12372b31e05/SinglePiPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_143_1_pg2.root',
       '/store/user/akunsken/PionGun2023NoExtraCalib/PionGun2023NoExtraCalib/a351453415fe506672b2e12372b31e05/SinglePiPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_144_1_P3r.root',
       '/store/user/akunsken/PionGun2023NoExtraCalib/PionGun2023NoExtraCalib/a351453415fe506672b2e12372b31e05/SinglePiPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_145_1_Vjz.root',
       '/store/user/akunsken/PionGun2023NoExtraCalib/PionGun2023NoExtraCalib/a351453415fe506672b2e12372b31e05/SinglePiPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_146_1_qA1.root',
       '/store/user/akunsken/PionGun2023NoExtraCalib/PionGun2023NoExtraCalib/a351453415fe506672b2e12372b31e05/SinglePiPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_147_1_sLr.root',
       '/store/user/akunsken/PionGun2023NoExtraCalib/PionGun2023NoExtraCalib/a351453415fe506672b2e12372b31e05/SinglePiPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_148_1_nBh.root',
       '/store/user/akunsken/PionGun2023NoExtraCalib/PionGun2023NoExtraCalib/a351453415fe506672b2e12372b31e05/SinglePiPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_149_1_yFF.root',
       '/store/user/akunsken/PionGun2023NoExtraCalib/PionGun2023NoExtraCalib/a351453415fe506672b2e12372b31e05/SinglePiPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_14_1_tdp.root',
       '/store/user/akunsken/PionGun2023NoExtraCalib/PionGun2023NoExtraCalib/a351453415fe506672b2e12372b31e05/SinglePiPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_150_1_QYP.root',
       '/store/user/akunsken/PionGun2023NoExtraCalib/PionGun2023NoExtraCalib/a351453415fe506672b2e12372b31e05/SinglePiPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_151_1_VII.root',
       '/store/user/akunsken/PionGun2023NoExtraCalib/PionGun2023NoExtraCalib/a351453415fe506672b2e12372b31e05/SinglePiPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_152_1_seE.root',
       '/store/user/akunsken/PionGun2023NoExtraCalib/PionGun2023NoExtraCalib/a351453415fe506672b2e12372b31e05/SinglePiPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_153_1_Y3a.root',
       '/store/user/akunsken/PionGun2023NoExtraCalib/PionGun2023NoExtraCalib/a351453415fe506672b2e12372b31e05/SinglePiPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_154_1_U3L.root',
       '/store/user/akunsken/PionGun2023NoExtraCalib/PionGun2023NoExtraCalib/a351453415fe506672b2e12372b31e05/SinglePiPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_155_1_scz.root',
       '/store/user/akunsken/PionGun2023NoExtraCalib/PionGun2023NoExtraCalib/a351453415fe506672b2e12372b31e05/SinglePiPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_156_1_gD7.root',
       '/store/user/akunsken/PionGun2023NoExtraCalib/PionGun2023NoExtraCalib/a351453415fe506672b2e12372b31e05/SinglePiPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_157_3_4Ig.root',
       '/store/user/akunsken/PionGun2023NoExtraCalib/PionGun2023NoExtraCalib/a351453415fe506672b2e12372b31e05/SinglePiPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_158_1_upV.root',
       '/store/user/akunsken/PionGun2023NoExtraCalib/PionGun2023NoExtraCalib/a351453415fe506672b2e12372b31e05/SinglePiPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_159_1_naT.root',
       '/store/user/akunsken/PionGun2023NoExtraCalib/PionGun2023NoExtraCalib/a351453415fe506672b2e12372b31e05/SinglePiPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_15_1_Out.root',
       '/store/user/akunsken/PionGun2023NoExtraCalib/PionGun2023NoExtraCalib/a351453415fe506672b2e12372b31e05/SinglePiPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_160_1_se9.root',
       '/store/user/akunsken/PionGun2023NoExtraCalib/PionGun2023NoExtraCalib/a351453415fe506672b2e12372b31e05/SinglePiPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_161_1_47q.root',
       '/store/user/akunsken/PionGun2023NoExtraCalib/PionGun2023NoExtraCalib/a351453415fe506672b2e12372b31e05/SinglePiPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_162_1_GvK.root',
       '/store/user/akunsken/PionGun2023NoExtraCalib/PionGun2023NoExtraCalib/a351453415fe506672b2e12372b31e05/SinglePiPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_163_1_Mt4.root',
       '/store/user/akunsken/PionGun2023NoExtraCalib/PionGun2023NoExtraCalib/a351453415fe506672b2e12372b31e05/SinglePiPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_164_1_sch.root',
       '/store/user/akunsken/PionGun2023NoExtraCalib/PionGun2023NoExtraCalib/a351453415fe506672b2e12372b31e05/SinglePiPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_165_1_iFy.root',
       '/store/user/akunsken/PionGun2023NoExtraCalib/PionGun2023NoExtraCalib/a351453415fe506672b2e12372b31e05/SinglePiPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_166_2_ZQD.root',
       '/store/user/akunsken/PionGun2023NoExtraCalib/PionGun2023NoExtraCalib/a351453415fe506672b2e12372b31e05/SinglePiPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_167_1_h8L.root',
       '/store/user/akunsken/PionGun2023NoExtraCalib/PionGun2023NoExtraCalib/a351453415fe506672b2e12372b31e05/SinglePiPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_168_1_5Np.root',
       '/store/user/akunsken/PionGun2023NoExtraCalib/PionGun2023NoExtraCalib/a351453415fe506672b2e12372b31e05/SinglePiPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_169_1_8Kf.root',
       '/store/user/akunsken/PionGun2023NoExtraCalib/PionGun2023NoExtraCalib/a351453415fe506672b2e12372b31e05/SinglePiPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_16_1_Qf5.root',
       '/store/user/akunsken/PionGun2023NoExtraCalib/PionGun2023NoExtraCalib/a351453415fe506672b2e12372b31e05/SinglePiPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_170_1_L0J.root',
       '/store/user/akunsken/PionGun2023NoExtraCalib/PionGun2023NoExtraCalib/a351453415fe506672b2e12372b31e05/SinglePiPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_171_2_lvg.root',
       '/store/user/akunsken/PionGun2023NoExtraCalib/PionGun2023NoExtraCalib/a351453415fe506672b2e12372b31e05/SinglePiPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_172_2_nHb.root',
       '/store/user/akunsken/PionGun2023NoExtraCalib/PionGun2023NoExtraCalib/a351453415fe506672b2e12372b31e05/SinglePiPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_173_1_gGT.root',
       '/store/user/akunsken/PionGun2023NoExtraCalib/PionGun2023NoExtraCalib/a351453415fe506672b2e12372b31e05/SinglePiPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_174_2_sJy.root',
       '/store/user/akunsken/PionGun2023NoExtraCalib/PionGun2023NoExtraCalib/a351453415fe506672b2e12372b31e05/SinglePiPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_175_1_oi5.root',
       '/store/user/akunsken/PionGun2023NoExtraCalib/PionGun2023NoExtraCalib/a351453415fe506672b2e12372b31e05/SinglePiPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_176_1_XYS.root',
       '/store/user/akunsken/PionGun2023NoExtraCalib/PionGun2023NoExtraCalib/a351453415fe506672b2e12372b31e05/SinglePiPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_177_1_JEu.root',
       '/store/user/akunsken/PionGun2023NoExtraCalib/PionGun2023NoExtraCalib/a351453415fe506672b2e12372b31e05/SinglePiPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_178_1_oP2.root',
       '/store/user/akunsken/PionGun2023NoExtraCalib/PionGun2023NoExtraCalib/a351453415fe506672b2e12372b31e05/SinglePiPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_179_1_k9y.root',
       '/store/user/akunsken/PionGun2023NoExtraCalib/PionGun2023NoExtraCalib/a351453415fe506672b2e12372b31e05/SinglePiPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_17_1_AA4.root',
       '/store/user/akunsken/PionGun2023NoExtraCalib/PionGun2023NoExtraCalib/a351453415fe506672b2e12372b31e05/SinglePiPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_180_1_Mvn.root',
       '/store/user/akunsken/PionGun2023NoExtraCalib/PionGun2023NoExtraCalib/a351453415fe506672b2e12372b31e05/SinglePiPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_181_1_0IT.root',
       '/store/user/akunsken/PionGun2023NoExtraCalib/PionGun2023NoExtraCalib/a351453415fe506672b2e12372b31e05/SinglePiPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_182_1_b2b.root',
       '/store/user/akunsken/PionGun2023NoExtraCalib/PionGun2023NoExtraCalib/a351453415fe506672b2e12372b31e05/SinglePiPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_183_1_OQI.root',
       '/store/user/akunsken/PionGun2023NoExtraCalib/PionGun2023NoExtraCalib/a351453415fe506672b2e12372b31e05/SinglePiPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_184_1_c6W.root',
       '/store/user/akunsken/PionGun2023NoExtraCalib/PionGun2023NoExtraCalib/a351453415fe506672b2e12372b31e05/SinglePiPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_185_1_tUB.root',
       '/store/user/akunsken/PionGun2023NoExtraCalib/PionGun2023NoExtraCalib/a351453415fe506672b2e12372b31e05/SinglePiPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_186_2_AGP.root',
       '/store/user/akunsken/PionGun2023NoExtraCalib/PionGun2023NoExtraCalib/a351453415fe506672b2e12372b31e05/SinglePiPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_187_2_KeW.root',
       '/store/user/akunsken/PionGun2023NoExtraCalib/PionGun2023NoExtraCalib/a351453415fe506672b2e12372b31e05/SinglePiPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_188_1_T3l.root',
       '/store/user/akunsken/PionGun2023NoExtraCalib/PionGun2023NoExtraCalib/a351453415fe506672b2e12372b31e05/SinglePiPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_189_1_rrJ.root',
       '/store/user/akunsken/PionGun2023NoExtraCalib/PionGun2023NoExtraCalib/a351453415fe506672b2e12372b31e05/SinglePiPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_18_1_B35.root',
       '/store/user/akunsken/PionGun2023NoExtraCalib/PionGun2023NoExtraCalib/a351453415fe506672b2e12372b31e05/SinglePiPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_190_1_q8o.root',
       '/store/user/akunsken/PionGun2023NoExtraCalib/PionGun2023NoExtraCalib/a351453415fe506672b2e12372b31e05/SinglePiPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_191_1_XGW.root',
       '/store/user/akunsken/PionGun2023NoExtraCalib/PionGun2023NoExtraCalib/a351453415fe506672b2e12372b31e05/SinglePiPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_192_1_Jvr.root',
       '/store/user/akunsken/PionGun2023NoExtraCalib/PionGun2023NoExtraCalib/a351453415fe506672b2e12372b31e05/SinglePiPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_193_1_srg.root',
       '/store/user/akunsken/PionGun2023NoExtraCalib/PionGun2023NoExtraCalib/a351453415fe506672b2e12372b31e05/SinglePiPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_194_1_Fpb.root',
       '/store/user/akunsken/PionGun2023NoExtraCalib/PionGun2023NoExtraCalib/a351453415fe506672b2e12372b31e05/SinglePiPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_195_1_4Cz.root',
       '/store/user/akunsken/PionGun2023NoExtraCalib/PionGun2023NoExtraCalib/a351453415fe506672b2e12372b31e05/SinglePiPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_196_1_hYf.root',
       '/store/user/akunsken/PionGun2023NoExtraCalib/PionGun2023NoExtraCalib/a351453415fe506672b2e12372b31e05/SinglePiPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_197_1_yaj.root',
       '/store/user/akunsken/PionGun2023NoExtraCalib/PionGun2023NoExtraCalib/a351453415fe506672b2e12372b31e05/SinglePiPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_198_1_UAq.root',
       '/store/user/akunsken/PionGun2023NoExtraCalib/PionGun2023NoExtraCalib/a351453415fe506672b2e12372b31e05/SinglePiPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_199_1_Lsf.root',
       '/store/user/akunsken/PionGun2023NoExtraCalib/PionGun2023NoExtraCalib/a351453415fe506672b2e12372b31e05/SinglePiPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_19_2_tZX.root',
       '/store/user/akunsken/PionGun2023NoExtraCalib/PionGun2023NoExtraCalib/a351453415fe506672b2e12372b31e05/SinglePiPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_1_1_RTm.root',
       '/store/user/akunsken/PionGun2023NoExtraCalib/PionGun2023NoExtraCalib/a351453415fe506672b2e12372b31e05/SinglePiPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_200_1_0Im.root',
       '/store/user/akunsken/PionGun2023NoExtraCalib/PionGun2023NoExtraCalib/a351453415fe506672b2e12372b31e05/SinglePiPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_20_1_eDH.root',
       '/store/user/akunsken/PionGun2023NoExtraCalib/PionGun2023NoExtraCalib/a351453415fe506672b2e12372b31e05/SinglePiPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_21_1_75M.root',
       '/store/user/akunsken/PionGun2023NoExtraCalib/PionGun2023NoExtraCalib/a351453415fe506672b2e12372b31e05/SinglePiPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_22_1_6m7.root',
       '/store/user/akunsken/PionGun2023NoExtraCalib/PionGun2023NoExtraCalib/a351453415fe506672b2e12372b31e05/SinglePiPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_23_1_Tbx.root',
       '/store/user/akunsken/PionGun2023NoExtraCalib/PionGun2023NoExtraCalib/a351453415fe506672b2e12372b31e05/SinglePiPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_24_1_dtg.root',
       '/store/user/akunsken/PionGun2023NoExtraCalib/PionGun2023NoExtraCalib/a351453415fe506672b2e12372b31e05/SinglePiPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_25_1_C0D.root',
       '/store/user/akunsken/PionGun2023NoExtraCalib/PionGun2023NoExtraCalib/a351453415fe506672b2e12372b31e05/SinglePiPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_26_1_79N.root',
       '/store/user/akunsken/PionGun2023NoExtraCalib/PionGun2023NoExtraCalib/a351453415fe506672b2e12372b31e05/SinglePiPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_27_1_bEa.root',
       '/store/user/akunsken/PionGun2023NoExtraCalib/PionGun2023NoExtraCalib/a351453415fe506672b2e12372b31e05/SinglePiPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_28_1_Nvs.root',
       '/store/user/akunsken/PionGun2023NoExtraCalib/PionGun2023NoExtraCalib/a351453415fe506672b2e12372b31e05/SinglePiPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_29_1_IUI.root',
       '/store/user/akunsken/PionGun2023NoExtraCalib/PionGun2023NoExtraCalib/a351453415fe506672b2e12372b31e05/SinglePiPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_2_1_1af.root',
       '/store/user/akunsken/PionGun2023NoExtraCalib/PionGun2023NoExtraCalib/a351453415fe506672b2e12372b31e05/SinglePiPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_30_1_56Q.root',
       '/store/user/akunsken/PionGun2023NoExtraCalib/PionGun2023NoExtraCalib/a351453415fe506672b2e12372b31e05/SinglePiPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_31_1_gph.root',
       '/store/user/akunsken/PionGun2023NoExtraCalib/PionGun2023NoExtraCalib/a351453415fe506672b2e12372b31e05/SinglePiPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_32_1_RMW.root',
       '/store/user/akunsken/PionGun2023NoExtraCalib/PionGun2023NoExtraCalib/a351453415fe506672b2e12372b31e05/SinglePiPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_33_2_mG7.root',
       '/store/user/akunsken/PionGun2023NoExtraCalib/PionGun2023NoExtraCalib/a351453415fe506672b2e12372b31e05/SinglePiPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_34_1_oeq.root',
       '/store/user/akunsken/PionGun2023NoExtraCalib/PionGun2023NoExtraCalib/a351453415fe506672b2e12372b31e05/SinglePiPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_35_1_tXj.root',
       '/store/user/akunsken/PionGun2023NoExtraCalib/PionGun2023NoExtraCalib/a351453415fe506672b2e12372b31e05/SinglePiPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_36_1_ooE.root',
       '/store/user/akunsken/PionGun2023NoExtraCalib/PionGun2023NoExtraCalib/a351453415fe506672b2e12372b31e05/SinglePiPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_37_1_2GT.root',
       '/store/user/akunsken/PionGun2023NoExtraCalib/PionGun2023NoExtraCalib/a351453415fe506672b2e12372b31e05/SinglePiPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_38_1_9YJ.root',
       '/store/user/akunsken/PionGun2023NoExtraCalib/PionGun2023NoExtraCalib/a351453415fe506672b2e12372b31e05/SinglePiPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_39_1_9yP.root',
       '/store/user/akunsken/PionGun2023NoExtraCalib/PionGun2023NoExtraCalib/a351453415fe506672b2e12372b31e05/SinglePiPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_3_1_ZPM.root',
       '/store/user/akunsken/PionGun2023NoExtraCalib/PionGun2023NoExtraCalib/a351453415fe506672b2e12372b31e05/SinglePiPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_40_1_YjH.root',
       '/store/user/akunsken/PionGun2023NoExtraCalib/PionGun2023NoExtraCalib/a351453415fe506672b2e12372b31e05/SinglePiPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_41_1_GoY.root',
       '/store/user/akunsken/PionGun2023NoExtraCalib/PionGun2023NoExtraCalib/a351453415fe506672b2e12372b31e05/SinglePiPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_42_1_EmA.root',
       '/store/user/akunsken/PionGun2023NoExtraCalib/PionGun2023NoExtraCalib/a351453415fe506672b2e12372b31e05/SinglePiPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_43_1_IpH.root',
       '/store/user/akunsken/PionGun2023NoExtraCalib/PionGun2023NoExtraCalib/a351453415fe506672b2e12372b31e05/SinglePiPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_44_1_h9S.root',
       '/store/user/akunsken/PionGun2023NoExtraCalib/PionGun2023NoExtraCalib/a351453415fe506672b2e12372b31e05/SinglePiPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_45_1_5o5.root',
       '/store/user/akunsken/PionGun2023NoExtraCalib/PionGun2023NoExtraCalib/a351453415fe506672b2e12372b31e05/SinglePiPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_46_1_k3q.root',
       '/store/user/akunsken/PionGun2023NoExtraCalib/PionGun2023NoExtraCalib/a351453415fe506672b2e12372b31e05/SinglePiPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_47_1_xRD.root',
       '/store/user/akunsken/PionGun2023NoExtraCalib/PionGun2023NoExtraCalib/a351453415fe506672b2e12372b31e05/SinglePiPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_48_1_HxZ.root',
       '/store/user/akunsken/PionGun2023NoExtraCalib/PionGun2023NoExtraCalib/a351453415fe506672b2e12372b31e05/SinglePiPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_49_1_Mo5.root',
       '/store/user/akunsken/PionGun2023NoExtraCalib/PionGun2023NoExtraCalib/a351453415fe506672b2e12372b31e05/SinglePiPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_4_1_lds.root',
       '/store/user/akunsken/PionGun2023NoExtraCalib/PionGun2023NoExtraCalib/a351453415fe506672b2e12372b31e05/SinglePiPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_50_1_DB8.root',
       '/store/user/akunsken/PionGun2023NoExtraCalib/PionGun2023NoExtraCalib/a351453415fe506672b2e12372b31e05/SinglePiPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_51_1_5pm.root',
       '/store/user/akunsken/PionGun2023NoExtraCalib/PionGun2023NoExtraCalib/a351453415fe506672b2e12372b31e05/SinglePiPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_52_1_7Dn.root',
       '/store/user/akunsken/PionGun2023NoExtraCalib/PionGun2023NoExtraCalib/a351453415fe506672b2e12372b31e05/SinglePiPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_53_2_WEW.root',
       '/store/user/akunsken/PionGun2023NoExtraCalib/PionGun2023NoExtraCalib/a351453415fe506672b2e12372b31e05/SinglePiPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_54_1_6Cq.root',
       '/store/user/akunsken/PionGun2023NoExtraCalib/PionGun2023NoExtraCalib/a351453415fe506672b2e12372b31e05/SinglePiPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_55_1_BbZ.root',
       '/store/user/akunsken/PionGun2023NoExtraCalib/PionGun2023NoExtraCalib/a351453415fe506672b2e12372b31e05/SinglePiPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_56_1_pUA.root',
       '/store/user/akunsken/PionGun2023NoExtraCalib/PionGun2023NoExtraCalib/a351453415fe506672b2e12372b31e05/SinglePiPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_57_1_Te2.root',
       '/store/user/akunsken/PionGun2023NoExtraCalib/PionGun2023NoExtraCalib/a351453415fe506672b2e12372b31e05/SinglePiPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_58_1_zkP.root',
       '/store/user/akunsken/PionGun2023NoExtraCalib/PionGun2023NoExtraCalib/a351453415fe506672b2e12372b31e05/SinglePiPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_59_1_ALn.root',
       '/store/user/akunsken/PionGun2023NoExtraCalib/PionGun2023NoExtraCalib/a351453415fe506672b2e12372b31e05/SinglePiPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_5_1_2nb.root',
       '/store/user/akunsken/PionGun2023NoExtraCalib/PionGun2023NoExtraCalib/a351453415fe506672b2e12372b31e05/SinglePiPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_60_1_3sx.root',
       '/store/user/akunsken/PionGun2023NoExtraCalib/PionGun2023NoExtraCalib/a351453415fe506672b2e12372b31e05/SinglePiPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_61_1_oeY.root',
       '/store/user/akunsken/PionGun2023NoExtraCalib/PionGun2023NoExtraCalib/a351453415fe506672b2e12372b31e05/SinglePiPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_62_1_rkd.root',
       '/store/user/akunsken/PionGun2023NoExtraCalib/PionGun2023NoExtraCalib/a351453415fe506672b2e12372b31e05/SinglePiPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_63_1_ddx.root',
       '/store/user/akunsken/PionGun2023NoExtraCalib/PionGun2023NoExtraCalib/a351453415fe506672b2e12372b31e05/SinglePiPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_64_1_OJn.root',
       '/store/user/akunsken/PionGun2023NoExtraCalib/PionGun2023NoExtraCalib/a351453415fe506672b2e12372b31e05/SinglePiPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_65_2_uDq.root',
       '/store/user/akunsken/PionGun2023NoExtraCalib/PionGun2023NoExtraCalib/a351453415fe506672b2e12372b31e05/SinglePiPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_66_2_jIE.root',
       '/store/user/akunsken/PionGun2023NoExtraCalib/PionGun2023NoExtraCalib/a351453415fe506672b2e12372b31e05/SinglePiPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_67_1_Jed.root',
       '/store/user/akunsken/PionGun2023NoExtraCalib/PionGun2023NoExtraCalib/a351453415fe506672b2e12372b31e05/SinglePiPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_68_1_B76.root',
       '/store/user/akunsken/PionGun2023NoExtraCalib/PionGun2023NoExtraCalib/a351453415fe506672b2e12372b31e05/SinglePiPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_69_1_ZRG.root',
       '/store/user/akunsken/PionGun2023NoExtraCalib/PionGun2023NoExtraCalib/a351453415fe506672b2e12372b31e05/SinglePiPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_6_1_p2S.root',
       '/store/user/akunsken/PionGun2023NoExtraCalib/PionGun2023NoExtraCalib/a351453415fe506672b2e12372b31e05/SinglePiPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_70_1_pY7.root',
       '/store/user/akunsken/PionGun2023NoExtraCalib/PionGun2023NoExtraCalib/a351453415fe506672b2e12372b31e05/SinglePiPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_71_1_W6I.root',
       '/store/user/akunsken/PionGun2023NoExtraCalib/PionGun2023NoExtraCalib/a351453415fe506672b2e12372b31e05/SinglePiPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_72_1_lRC.root',
       '/store/user/akunsken/PionGun2023NoExtraCalib/PionGun2023NoExtraCalib/a351453415fe506672b2e12372b31e05/SinglePiPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_73_1_rYH.root',
       '/store/user/akunsken/PionGun2023NoExtraCalib/PionGun2023NoExtraCalib/a351453415fe506672b2e12372b31e05/SinglePiPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_74_1_T0D.root',
       '/store/user/akunsken/PionGun2023NoExtraCalib/PionGun2023NoExtraCalib/a351453415fe506672b2e12372b31e05/SinglePiPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_75_1_Vdo.root',
       '/store/user/akunsken/PionGun2023NoExtraCalib/PionGun2023NoExtraCalib/a351453415fe506672b2e12372b31e05/SinglePiPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_76_1_3xg.root',
       '/store/user/akunsken/PionGun2023NoExtraCalib/PionGun2023NoExtraCalib/a351453415fe506672b2e12372b31e05/SinglePiPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_77_1_kvG.root',
       '/store/user/akunsken/PionGun2023NoExtraCalib/PionGun2023NoExtraCalib/a351453415fe506672b2e12372b31e05/SinglePiPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_78_1_Fw4.root',
       '/store/user/akunsken/PionGun2023NoExtraCalib/PionGun2023NoExtraCalib/a351453415fe506672b2e12372b31e05/SinglePiPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_79_1_eDH.root',
       '/store/user/akunsken/PionGun2023NoExtraCalib/PionGun2023NoExtraCalib/a351453415fe506672b2e12372b31e05/SinglePiPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_7_1_MvS.root',
       '/store/user/akunsken/PionGun2023NoExtraCalib/PionGun2023NoExtraCalib/a351453415fe506672b2e12372b31e05/SinglePiPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_80_1_kR7.root',
       '/store/user/akunsken/PionGun2023NoExtraCalib/PionGun2023NoExtraCalib/a351453415fe506672b2e12372b31e05/SinglePiPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_81_2_wQ7.root',
       '/store/user/akunsken/PionGun2023NoExtraCalib/PionGun2023NoExtraCalib/a351453415fe506672b2e12372b31e05/SinglePiPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_82_1_MNu.root',
       '/store/user/akunsken/PionGun2023NoExtraCalib/PionGun2023NoExtraCalib/a351453415fe506672b2e12372b31e05/SinglePiPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_83_1_rmc.root',
       '/store/user/akunsken/PionGun2023NoExtraCalib/PionGun2023NoExtraCalib/a351453415fe506672b2e12372b31e05/SinglePiPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_84_2_DkV.root',
       '/store/user/akunsken/PionGun2023NoExtraCalib/PionGun2023NoExtraCalib/a351453415fe506672b2e12372b31e05/SinglePiPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_85_1_loM.root',
       '/store/user/akunsken/PionGun2023NoExtraCalib/PionGun2023NoExtraCalib/a351453415fe506672b2e12372b31e05/SinglePiPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_86_1_IOB.root',
       '/store/user/akunsken/PionGun2023NoExtraCalib/PionGun2023NoExtraCalib/a351453415fe506672b2e12372b31e05/SinglePiPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_87_1_w5V.root',
       '/store/user/akunsken/PionGun2023NoExtraCalib/PionGun2023NoExtraCalib/a351453415fe506672b2e12372b31e05/SinglePiPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_88_1_WgA.root',
       '/store/user/akunsken/PionGun2023NoExtraCalib/PionGun2023NoExtraCalib/a351453415fe506672b2e12372b31e05/SinglePiPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_89_1_toH.root',
       '/store/user/akunsken/PionGun2023NoExtraCalib/PionGun2023NoExtraCalib/a351453415fe506672b2e12372b31e05/SinglePiPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_8_1_LqX.root',
       '/store/user/akunsken/PionGun2023NoExtraCalib/PionGun2023NoExtraCalib/a351453415fe506672b2e12372b31e05/SinglePiPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_90_1_KsR.root',
       '/store/user/akunsken/PionGun2023NoExtraCalib/PionGun2023NoExtraCalib/a351453415fe506672b2e12372b31e05/SinglePiPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_91_1_UEt.root',
       '/store/user/akunsken/PionGun2023NoExtraCalib/PionGun2023NoExtraCalib/a351453415fe506672b2e12372b31e05/SinglePiPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_92_1_Jnm.root',
       '/store/user/akunsken/PionGun2023NoExtraCalib/PionGun2023NoExtraCalib/a351453415fe506672b2e12372b31e05/SinglePiPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_93_1_KTt.root',
       '/store/user/akunsken/PionGun2023NoExtraCalib/PionGun2023NoExtraCalib/a351453415fe506672b2e12372b31e05/SinglePiPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_94_1_Mcr.root',
       '/store/user/akunsken/PionGun2023NoExtraCalib/PionGun2023NoExtraCalib/a351453415fe506672b2e12372b31e05/SinglePiPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_95_1_BDr.root',
       '/store/user/akunsken/PionGun2023NoExtraCalib/PionGun2023NoExtraCalib/a351453415fe506672b2e12372b31e05/SinglePiPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_96_1_PTr.root',
       '/store/user/akunsken/PionGun2023NoExtraCalib/PionGun2023NoExtraCalib/a351453415fe506672b2e12372b31e05/SinglePiPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_97_1_WzC.root',
       '/store/user/akunsken/PionGun2023NoExtraCalib/PionGun2023NoExtraCalib/a351453415fe506672b2e12372b31e05/SinglePiPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_98_1_10d.root',
       '/store/user/akunsken/PionGun2023NoExtraCalib/PionGun2023NoExtraCalib/a351453415fe506672b2e12372b31e05/SinglePiPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_99_1_TsI.root',
       '/store/user/akunsken/PionGun2023NoExtraCalib/PionGun2023NoExtraCalib/a351453415fe506672b2e12372b31e05/SinglePiPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_9_1_rSg.root'
      
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

#Global Tag
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

#turn off HO ZS
#process.hcalRawData.HO = cms.untracked.InputTag("simHcalUnsuppressedDigis", "", "")


#horeco
process.load('Configuration.StandardSequences.Reconstruction_cff')


from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'DES23_62_V1::All', '')


process.hoMuonAnalyzer = cms.EDAnalyzer(
    'PionAnalyzer',
    genSrc = cms.InputTag("genParticles"),
    l1MuonSrc=cms.InputTag("l1extraParticles"),
    #stdMuSrc = cms.InputTag("standAloneMuons"),
    horecoSrc = cms.InputTag("horeco"),
    #L1GtTmLInputTag = cms.InputTag("l1GtTriggerMenuLite")
    hltSumAODSrc = cms.InputTag("hltTriggerSummaryAOD"),
    l1MuonGenMatchSrc = cms.InputTag("l1MuonGenMatch")
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

process.horeco_step = cms.Path(process.horeco)
process.l1MuonGenMatch_step = cms.Path(process.l1MuonGenMatch)
process.demo_step = cms.Path(process.hoMuonAnalyzer)

#Schedule Definition
process.schedule = cms.Schedule(
	process.horeco_step,
	process.l1MuonGenMatch_step,
	process.demo_step
	)


# Automatic addition of the customisation function from SLHCUpgradeSimulations.Configuration.combinedCustoms
from SLHCUpgradeSimulations.Configuration.combinedCustoms import cust_2023Muon 

#call to customisation function cust_2023Muon imported from SLHCUpgradeSimulations.Configuration.combinedCustoms
process = cust_2023Muon(process)
