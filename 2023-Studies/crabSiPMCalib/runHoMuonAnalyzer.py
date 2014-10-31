import FWCore.ParameterSet.Config as cms

process = cms.Process("Demo")

process.load("FWCore.MessageService.MessageLogger_cfi")
process.MessageLogger.cerr.FwkReport.reportEvery = 100

process.TFileService = cms.Service("TFileService",
                                   fileName=cms.string('L1MuonHistogram.root')
                                   )


process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )

readFiles = cms.untracked.vstring()
readFiles.extend( [
       '/store/user/akunsken/MuonGun2023SiPMCalib/MuonGun2023SiPMCalib/7f97035a1e8068bec0f6c51bfc2d367c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_100_1_YZC.root',
       '/store/user/akunsken/MuonGun2023SiPMCalib/MuonGun2023SiPMCalib/7f97035a1e8068bec0f6c51bfc2d367c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_101_1_Oxa.root',
       '/store/user/akunsken/MuonGun2023SiPMCalib/MuonGun2023SiPMCalib/7f97035a1e8068bec0f6c51bfc2d367c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_102_1_OvB.root',
       '/store/user/akunsken/MuonGun2023SiPMCalib/MuonGun2023SiPMCalib/7f97035a1e8068bec0f6c51bfc2d367c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_103_1_EzB.root',
       '/store/user/akunsken/MuonGun2023SiPMCalib/MuonGun2023SiPMCalib/7f97035a1e8068bec0f6c51bfc2d367c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_104_1_fZA.root',
       '/store/user/akunsken/MuonGun2023SiPMCalib/MuonGun2023SiPMCalib/7f97035a1e8068bec0f6c51bfc2d367c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_105_1_Cez.root',
       '/store/user/akunsken/MuonGun2023SiPMCalib/MuonGun2023SiPMCalib/7f97035a1e8068bec0f6c51bfc2d367c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_106_1_0bC.root',
       '/store/user/akunsken/MuonGun2023SiPMCalib/MuonGun2023SiPMCalib/7f97035a1e8068bec0f6c51bfc2d367c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_107_1_m4a.root',
       '/store/user/akunsken/MuonGun2023SiPMCalib/MuonGun2023SiPMCalib/7f97035a1e8068bec0f6c51bfc2d367c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_108_1_klX.root',
       '/store/user/akunsken/MuonGun2023SiPMCalib/MuonGun2023SiPMCalib/7f97035a1e8068bec0f6c51bfc2d367c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_109_1_Nsj.root',
       '/store/user/akunsken/MuonGun2023SiPMCalib/MuonGun2023SiPMCalib/7f97035a1e8068bec0f6c51bfc2d367c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_10_1_rH6.root',
       '/store/user/akunsken/MuonGun2023SiPMCalib/MuonGun2023SiPMCalib/7f97035a1e8068bec0f6c51bfc2d367c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_110_1_Efr.root',
       '/store/user/akunsken/MuonGun2023SiPMCalib/MuonGun2023SiPMCalib/7f97035a1e8068bec0f6c51bfc2d367c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_111_1_05c.root',
       '/store/user/akunsken/MuonGun2023SiPMCalib/MuonGun2023SiPMCalib/7f97035a1e8068bec0f6c51bfc2d367c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_112_1_LGe.root',
       '/store/user/akunsken/MuonGun2023SiPMCalib/MuonGun2023SiPMCalib/7f97035a1e8068bec0f6c51bfc2d367c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_113_1_C2t.root',
       '/store/user/akunsken/MuonGun2023SiPMCalib/MuonGun2023SiPMCalib/7f97035a1e8068bec0f6c51bfc2d367c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_114_1_XKJ.root',
       '/store/user/akunsken/MuonGun2023SiPMCalib/MuonGun2023SiPMCalib/7f97035a1e8068bec0f6c51bfc2d367c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_115_1_cVQ.root',
       '/store/user/akunsken/MuonGun2023SiPMCalib/MuonGun2023SiPMCalib/7f97035a1e8068bec0f6c51bfc2d367c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_116_1_4vO.root',
       '/store/user/akunsken/MuonGun2023SiPMCalib/MuonGun2023SiPMCalib/7f97035a1e8068bec0f6c51bfc2d367c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_117_1_2ol.root',
       '/store/user/akunsken/MuonGun2023SiPMCalib/MuonGun2023SiPMCalib/7f97035a1e8068bec0f6c51bfc2d367c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_118_1_nyL.root',
       '/store/user/akunsken/MuonGun2023SiPMCalib/MuonGun2023SiPMCalib/7f97035a1e8068bec0f6c51bfc2d367c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_119_1_DL1.root',
       '/store/user/akunsken/MuonGun2023SiPMCalib/MuonGun2023SiPMCalib/7f97035a1e8068bec0f6c51bfc2d367c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_11_1_wOB.root',
       '/store/user/akunsken/MuonGun2023SiPMCalib/MuonGun2023SiPMCalib/7f97035a1e8068bec0f6c51bfc2d367c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_120_1_6JI.root',
       '/store/user/akunsken/MuonGun2023SiPMCalib/MuonGun2023SiPMCalib/7f97035a1e8068bec0f6c51bfc2d367c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_121_1_pGT.root',
       '/store/user/akunsken/MuonGun2023SiPMCalib/MuonGun2023SiPMCalib/7f97035a1e8068bec0f6c51bfc2d367c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_122_1_EW4.root',
       '/store/user/akunsken/MuonGun2023SiPMCalib/MuonGun2023SiPMCalib/7f97035a1e8068bec0f6c51bfc2d367c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_123_1_crS.root',
       '/store/user/akunsken/MuonGun2023SiPMCalib/MuonGun2023SiPMCalib/7f97035a1e8068bec0f6c51bfc2d367c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_124_1_Wtd.root',
       '/store/user/akunsken/MuonGun2023SiPMCalib/MuonGun2023SiPMCalib/7f97035a1e8068bec0f6c51bfc2d367c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_125_1_RgY.root',
       '/store/user/akunsken/MuonGun2023SiPMCalib/MuonGun2023SiPMCalib/7f97035a1e8068bec0f6c51bfc2d367c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_126_1_ffp.root',
       '/store/user/akunsken/MuonGun2023SiPMCalib/MuonGun2023SiPMCalib/7f97035a1e8068bec0f6c51bfc2d367c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_127_1_R0b.root',
       '/store/user/akunsken/MuonGun2023SiPMCalib/MuonGun2023SiPMCalib/7f97035a1e8068bec0f6c51bfc2d367c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_128_1_nrw.root',
       '/store/user/akunsken/MuonGun2023SiPMCalib/MuonGun2023SiPMCalib/7f97035a1e8068bec0f6c51bfc2d367c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_129_1_DPr.root',
       '/store/user/akunsken/MuonGun2023SiPMCalib/MuonGun2023SiPMCalib/7f97035a1e8068bec0f6c51bfc2d367c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_12_1_DNk.root',
       '/store/user/akunsken/MuonGun2023SiPMCalib/MuonGun2023SiPMCalib/7f97035a1e8068bec0f6c51bfc2d367c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_130_1_1SW.root',
       '/store/user/akunsken/MuonGun2023SiPMCalib/MuonGun2023SiPMCalib/7f97035a1e8068bec0f6c51bfc2d367c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_131_1_A6z.root',
       '/store/user/akunsken/MuonGun2023SiPMCalib/MuonGun2023SiPMCalib/7f97035a1e8068bec0f6c51bfc2d367c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_132_1_PfG.root',
       '/store/user/akunsken/MuonGun2023SiPMCalib/MuonGun2023SiPMCalib/7f97035a1e8068bec0f6c51bfc2d367c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_133_1_kH1.root',
       '/store/user/akunsken/MuonGun2023SiPMCalib/MuonGun2023SiPMCalib/7f97035a1e8068bec0f6c51bfc2d367c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_134_1_PuR.root',
       '/store/user/akunsken/MuonGun2023SiPMCalib/MuonGun2023SiPMCalib/7f97035a1e8068bec0f6c51bfc2d367c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_135_1_JDc.root',
       '/store/user/akunsken/MuonGun2023SiPMCalib/MuonGun2023SiPMCalib/7f97035a1e8068bec0f6c51bfc2d367c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_136_1_dom.root',
       '/store/user/akunsken/MuonGun2023SiPMCalib/MuonGun2023SiPMCalib/7f97035a1e8068bec0f6c51bfc2d367c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_137_1_bf1.root',
       '/store/user/akunsken/MuonGun2023SiPMCalib/MuonGun2023SiPMCalib/7f97035a1e8068bec0f6c51bfc2d367c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_138_1_HLS.root',
       '/store/user/akunsken/MuonGun2023SiPMCalib/MuonGun2023SiPMCalib/7f97035a1e8068bec0f6c51bfc2d367c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_139_1_zzW.root',
       '/store/user/akunsken/MuonGun2023SiPMCalib/MuonGun2023SiPMCalib/7f97035a1e8068bec0f6c51bfc2d367c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_13_1_ARL.root',
       '/store/user/akunsken/MuonGun2023SiPMCalib/MuonGun2023SiPMCalib/7f97035a1e8068bec0f6c51bfc2d367c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_140_1_fT5.root',
       '/store/user/akunsken/MuonGun2023SiPMCalib/MuonGun2023SiPMCalib/7f97035a1e8068bec0f6c51bfc2d367c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_141_1_8Nv.root',
       '/store/user/akunsken/MuonGun2023SiPMCalib/MuonGun2023SiPMCalib/7f97035a1e8068bec0f6c51bfc2d367c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_142_1_i9u.root',
       '/store/user/akunsken/MuonGun2023SiPMCalib/MuonGun2023SiPMCalib/7f97035a1e8068bec0f6c51bfc2d367c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_143_1_rGv.root',
       '/store/user/akunsken/MuonGun2023SiPMCalib/MuonGun2023SiPMCalib/7f97035a1e8068bec0f6c51bfc2d367c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_144_1_QWK.root',
       '/store/user/akunsken/MuonGun2023SiPMCalib/MuonGun2023SiPMCalib/7f97035a1e8068bec0f6c51bfc2d367c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_145_1_9Lq.root',
       '/store/user/akunsken/MuonGun2023SiPMCalib/MuonGun2023SiPMCalib/7f97035a1e8068bec0f6c51bfc2d367c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_146_1_9ux.root',
       '/store/user/akunsken/MuonGun2023SiPMCalib/MuonGun2023SiPMCalib/7f97035a1e8068bec0f6c51bfc2d367c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_147_1_AT1.root',
       '/store/user/akunsken/MuonGun2023SiPMCalib/MuonGun2023SiPMCalib/7f97035a1e8068bec0f6c51bfc2d367c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_148_1_P87.root',
       '/store/user/akunsken/MuonGun2023SiPMCalib/MuonGun2023SiPMCalib/7f97035a1e8068bec0f6c51bfc2d367c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_149_1_fUV.root',
       '/store/user/akunsken/MuonGun2023SiPMCalib/MuonGun2023SiPMCalib/7f97035a1e8068bec0f6c51bfc2d367c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_14_1_Vqa.root',
       '/store/user/akunsken/MuonGun2023SiPMCalib/MuonGun2023SiPMCalib/7f97035a1e8068bec0f6c51bfc2d367c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_150_1_Kjr.root',
       '/store/user/akunsken/MuonGun2023SiPMCalib/MuonGun2023SiPMCalib/7f97035a1e8068bec0f6c51bfc2d367c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_151_1_G5Z.root',
       '/store/user/akunsken/MuonGun2023SiPMCalib/MuonGun2023SiPMCalib/7f97035a1e8068bec0f6c51bfc2d367c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_152_1_Nfq.root',
       '/store/user/akunsken/MuonGun2023SiPMCalib/MuonGun2023SiPMCalib/7f97035a1e8068bec0f6c51bfc2d367c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_153_1_9cC.root',
       '/store/user/akunsken/MuonGun2023SiPMCalib/MuonGun2023SiPMCalib/7f97035a1e8068bec0f6c51bfc2d367c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_154_1_Iig.root',
       '/store/user/akunsken/MuonGun2023SiPMCalib/MuonGun2023SiPMCalib/7f97035a1e8068bec0f6c51bfc2d367c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_155_1_f8G.root',
       '/store/user/akunsken/MuonGun2023SiPMCalib/MuonGun2023SiPMCalib/7f97035a1e8068bec0f6c51bfc2d367c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_156_1_SFI.root',
       '/store/user/akunsken/MuonGun2023SiPMCalib/MuonGun2023SiPMCalib/7f97035a1e8068bec0f6c51bfc2d367c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_157_1_egm.root',
       '/store/user/akunsken/MuonGun2023SiPMCalib/MuonGun2023SiPMCalib/7f97035a1e8068bec0f6c51bfc2d367c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_158_1_dHq.root',
       '/store/user/akunsken/MuonGun2023SiPMCalib/MuonGun2023SiPMCalib/7f97035a1e8068bec0f6c51bfc2d367c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_159_1_W3s.root',
       '/store/user/akunsken/MuonGun2023SiPMCalib/MuonGun2023SiPMCalib/7f97035a1e8068bec0f6c51bfc2d367c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_15_1_5zK.root',
       '/store/user/akunsken/MuonGun2023SiPMCalib/MuonGun2023SiPMCalib/7f97035a1e8068bec0f6c51bfc2d367c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_160_1_3Lm.root',
       '/store/user/akunsken/MuonGun2023SiPMCalib/MuonGun2023SiPMCalib/7f97035a1e8068bec0f6c51bfc2d367c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_161_1_wN5.root',
       '/store/user/akunsken/MuonGun2023SiPMCalib/MuonGun2023SiPMCalib/7f97035a1e8068bec0f6c51bfc2d367c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_162_1_NG8.root',
       '/store/user/akunsken/MuonGun2023SiPMCalib/MuonGun2023SiPMCalib/7f97035a1e8068bec0f6c51bfc2d367c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_163_1_Yf1.root',
       '/store/user/akunsken/MuonGun2023SiPMCalib/MuonGun2023SiPMCalib/7f97035a1e8068bec0f6c51bfc2d367c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_164_1_1JG.root',
       '/store/user/akunsken/MuonGun2023SiPMCalib/MuonGun2023SiPMCalib/7f97035a1e8068bec0f6c51bfc2d367c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_165_1_36C.root',
       '/store/user/akunsken/MuonGun2023SiPMCalib/MuonGun2023SiPMCalib/7f97035a1e8068bec0f6c51bfc2d367c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_166_1_uuP.root',
       '/store/user/akunsken/MuonGun2023SiPMCalib/MuonGun2023SiPMCalib/7f97035a1e8068bec0f6c51bfc2d367c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_167_1_u6H.root',
       '/store/user/akunsken/MuonGun2023SiPMCalib/MuonGun2023SiPMCalib/7f97035a1e8068bec0f6c51bfc2d367c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_168_1_7Pj.root',
       '/store/user/akunsken/MuonGun2023SiPMCalib/MuonGun2023SiPMCalib/7f97035a1e8068bec0f6c51bfc2d367c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_169_1_BNp.root',
       '/store/user/akunsken/MuonGun2023SiPMCalib/MuonGun2023SiPMCalib/7f97035a1e8068bec0f6c51bfc2d367c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_16_1_kqa.root',
       '/store/user/akunsken/MuonGun2023SiPMCalib/MuonGun2023SiPMCalib/7f97035a1e8068bec0f6c51bfc2d367c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_170_1_9X7.root',
       '/store/user/akunsken/MuonGun2023SiPMCalib/MuonGun2023SiPMCalib/7f97035a1e8068bec0f6c51bfc2d367c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_171_1_OgR.root',
       '/store/user/akunsken/MuonGun2023SiPMCalib/MuonGun2023SiPMCalib/7f97035a1e8068bec0f6c51bfc2d367c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_172_1_y5b.root',
       '/store/user/akunsken/MuonGun2023SiPMCalib/MuonGun2023SiPMCalib/7f97035a1e8068bec0f6c51bfc2d367c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_173_1_hVO.root',
       '/store/user/akunsken/MuonGun2023SiPMCalib/MuonGun2023SiPMCalib/7f97035a1e8068bec0f6c51bfc2d367c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_174_1_BnD.root',
       '/store/user/akunsken/MuonGun2023SiPMCalib/MuonGun2023SiPMCalib/7f97035a1e8068bec0f6c51bfc2d367c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_175_1_Wx1.root',
       '/store/user/akunsken/MuonGun2023SiPMCalib/MuonGun2023SiPMCalib/7f97035a1e8068bec0f6c51bfc2d367c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_176_1_vyu.root',
       '/store/user/akunsken/MuonGun2023SiPMCalib/MuonGun2023SiPMCalib/7f97035a1e8068bec0f6c51bfc2d367c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_177_1_Nip.root',
       '/store/user/akunsken/MuonGun2023SiPMCalib/MuonGun2023SiPMCalib/7f97035a1e8068bec0f6c51bfc2d367c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_178_1_O5O.root',
       '/store/user/akunsken/MuonGun2023SiPMCalib/MuonGun2023SiPMCalib/7f97035a1e8068bec0f6c51bfc2d367c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_179_1_ozu.root',
       '/store/user/akunsken/MuonGun2023SiPMCalib/MuonGun2023SiPMCalib/7f97035a1e8068bec0f6c51bfc2d367c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_17_1_r4o.root',
       '/store/user/akunsken/MuonGun2023SiPMCalib/MuonGun2023SiPMCalib/7f97035a1e8068bec0f6c51bfc2d367c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_180_1_L79.root',
       '/store/user/akunsken/MuonGun2023SiPMCalib/MuonGun2023SiPMCalib/7f97035a1e8068bec0f6c51bfc2d367c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_181_1_U8G.root',
       '/store/user/akunsken/MuonGun2023SiPMCalib/MuonGun2023SiPMCalib/7f97035a1e8068bec0f6c51bfc2d367c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_182_1_cNt.root',
       '/store/user/akunsken/MuonGun2023SiPMCalib/MuonGun2023SiPMCalib/7f97035a1e8068bec0f6c51bfc2d367c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_183_1_WfH.root',
       '/store/user/akunsken/MuonGun2023SiPMCalib/MuonGun2023SiPMCalib/7f97035a1e8068bec0f6c51bfc2d367c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_184_1_94e.root',
       '/store/user/akunsken/MuonGun2023SiPMCalib/MuonGun2023SiPMCalib/7f97035a1e8068bec0f6c51bfc2d367c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_185_1_mCj.root',
       '/store/user/akunsken/MuonGun2023SiPMCalib/MuonGun2023SiPMCalib/7f97035a1e8068bec0f6c51bfc2d367c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_186_1_RvX.root',
       '/store/user/akunsken/MuonGun2023SiPMCalib/MuonGun2023SiPMCalib/7f97035a1e8068bec0f6c51bfc2d367c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_187_1_UO7.root',
       '/store/user/akunsken/MuonGun2023SiPMCalib/MuonGun2023SiPMCalib/7f97035a1e8068bec0f6c51bfc2d367c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_188_1_sKI.root',
       '/store/user/akunsken/MuonGun2023SiPMCalib/MuonGun2023SiPMCalib/7f97035a1e8068bec0f6c51bfc2d367c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_189_1_Muc.root',
       '/store/user/akunsken/MuonGun2023SiPMCalib/MuonGun2023SiPMCalib/7f97035a1e8068bec0f6c51bfc2d367c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_18_1_ngQ.root',
       '/store/user/akunsken/MuonGun2023SiPMCalib/MuonGun2023SiPMCalib/7f97035a1e8068bec0f6c51bfc2d367c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_190_1_gMO.root',
       '/store/user/akunsken/MuonGun2023SiPMCalib/MuonGun2023SiPMCalib/7f97035a1e8068bec0f6c51bfc2d367c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_191_1_cXX.root',
       '/store/user/akunsken/MuonGun2023SiPMCalib/MuonGun2023SiPMCalib/7f97035a1e8068bec0f6c51bfc2d367c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_192_1_6J8.root',
       '/store/user/akunsken/MuonGun2023SiPMCalib/MuonGun2023SiPMCalib/7f97035a1e8068bec0f6c51bfc2d367c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_193_1_mys.root',
       '/store/user/akunsken/MuonGun2023SiPMCalib/MuonGun2023SiPMCalib/7f97035a1e8068bec0f6c51bfc2d367c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_194_1_pt5.root',
       '/store/user/akunsken/MuonGun2023SiPMCalib/MuonGun2023SiPMCalib/7f97035a1e8068bec0f6c51bfc2d367c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_195_1_XMy.root',
       '/store/user/akunsken/MuonGun2023SiPMCalib/MuonGun2023SiPMCalib/7f97035a1e8068bec0f6c51bfc2d367c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_196_1_83h.root',
       '/store/user/akunsken/MuonGun2023SiPMCalib/MuonGun2023SiPMCalib/7f97035a1e8068bec0f6c51bfc2d367c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_197_1_PoK.root',
       '/store/user/akunsken/MuonGun2023SiPMCalib/MuonGun2023SiPMCalib/7f97035a1e8068bec0f6c51bfc2d367c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_198_1_Cxf.root',
       '/store/user/akunsken/MuonGun2023SiPMCalib/MuonGun2023SiPMCalib/7f97035a1e8068bec0f6c51bfc2d367c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_199_1_xZ8.root',
       '/store/user/akunsken/MuonGun2023SiPMCalib/MuonGun2023SiPMCalib/7f97035a1e8068bec0f6c51bfc2d367c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_19_1_jtJ.root',
       '/store/user/akunsken/MuonGun2023SiPMCalib/MuonGun2023SiPMCalib/7f97035a1e8068bec0f6c51bfc2d367c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_1_2_IRc.root',
       '/store/user/akunsken/MuonGun2023SiPMCalib/MuonGun2023SiPMCalib/7f97035a1e8068bec0f6c51bfc2d367c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_200_1_ESW.root',
       '/store/user/akunsken/MuonGun2023SiPMCalib/MuonGun2023SiPMCalib/7f97035a1e8068bec0f6c51bfc2d367c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_20_1_Lj7.root',
       '/store/user/akunsken/MuonGun2023SiPMCalib/MuonGun2023SiPMCalib/7f97035a1e8068bec0f6c51bfc2d367c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_21_1_wp5.root',
       '/store/user/akunsken/MuonGun2023SiPMCalib/MuonGun2023SiPMCalib/7f97035a1e8068bec0f6c51bfc2d367c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_22_1_yBF.root',
       '/store/user/akunsken/MuonGun2023SiPMCalib/MuonGun2023SiPMCalib/7f97035a1e8068bec0f6c51bfc2d367c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_23_1_hnn.root',
       '/store/user/akunsken/MuonGun2023SiPMCalib/MuonGun2023SiPMCalib/7f97035a1e8068bec0f6c51bfc2d367c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_24_1_oND.root',
       '/store/user/akunsken/MuonGun2023SiPMCalib/MuonGun2023SiPMCalib/7f97035a1e8068bec0f6c51bfc2d367c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_25_1_8nF.root',
       '/store/user/akunsken/MuonGun2023SiPMCalib/MuonGun2023SiPMCalib/7f97035a1e8068bec0f6c51bfc2d367c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_26_1_WCs.root',
       '/store/user/akunsken/MuonGun2023SiPMCalib/MuonGun2023SiPMCalib/7f97035a1e8068bec0f6c51bfc2d367c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_27_1_48x.root',
       '/store/user/akunsken/MuonGun2023SiPMCalib/MuonGun2023SiPMCalib/7f97035a1e8068bec0f6c51bfc2d367c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_28_1_u7C.root',
       '/store/user/akunsken/MuonGun2023SiPMCalib/MuonGun2023SiPMCalib/7f97035a1e8068bec0f6c51bfc2d367c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_29_1_WrQ.root',
       '/store/user/akunsken/MuonGun2023SiPMCalib/MuonGun2023SiPMCalib/7f97035a1e8068bec0f6c51bfc2d367c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_2_2_Bbf.root',
       '/store/user/akunsken/MuonGun2023SiPMCalib/MuonGun2023SiPMCalib/7f97035a1e8068bec0f6c51bfc2d367c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_30_2_YIo.root',
       '/store/user/akunsken/MuonGun2023SiPMCalib/MuonGun2023SiPMCalib/7f97035a1e8068bec0f6c51bfc2d367c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_31_1_fLL.root',
       '/store/user/akunsken/MuonGun2023SiPMCalib/MuonGun2023SiPMCalib/7f97035a1e8068bec0f6c51bfc2d367c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_32_1_ZpI.root',
       '/store/user/akunsken/MuonGun2023SiPMCalib/MuonGun2023SiPMCalib/7f97035a1e8068bec0f6c51bfc2d367c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_33_1_yRR.root',
       '/store/user/akunsken/MuonGun2023SiPMCalib/MuonGun2023SiPMCalib/7f97035a1e8068bec0f6c51bfc2d367c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_34_1_w8f.root',
       '/store/user/akunsken/MuonGun2023SiPMCalib/MuonGun2023SiPMCalib/7f97035a1e8068bec0f6c51bfc2d367c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_35_1_QQf.root',
       '/store/user/akunsken/MuonGun2023SiPMCalib/MuonGun2023SiPMCalib/7f97035a1e8068bec0f6c51bfc2d367c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_36_1_jT7.root',
       '/store/user/akunsken/MuonGun2023SiPMCalib/MuonGun2023SiPMCalib/7f97035a1e8068bec0f6c51bfc2d367c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_37_1_bHd.root',
       '/store/user/akunsken/MuonGun2023SiPMCalib/MuonGun2023SiPMCalib/7f97035a1e8068bec0f6c51bfc2d367c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_38_1_04t.root',
       '/store/user/akunsken/MuonGun2023SiPMCalib/MuonGun2023SiPMCalib/7f97035a1e8068bec0f6c51bfc2d367c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_39_1_xxh.root',
       '/store/user/akunsken/MuonGun2023SiPMCalib/MuonGun2023SiPMCalib/7f97035a1e8068bec0f6c51bfc2d367c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_3_2_luP.root',
       '/store/user/akunsken/MuonGun2023SiPMCalib/MuonGun2023SiPMCalib/7f97035a1e8068bec0f6c51bfc2d367c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_40_1_q9E.root',
       '/store/user/akunsken/MuonGun2023SiPMCalib/MuonGun2023SiPMCalib/7f97035a1e8068bec0f6c51bfc2d367c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_41_1_vI9.root',
       '/store/user/akunsken/MuonGun2023SiPMCalib/MuonGun2023SiPMCalib/7f97035a1e8068bec0f6c51bfc2d367c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_42_1_2m1.root',
       '/store/user/akunsken/MuonGun2023SiPMCalib/MuonGun2023SiPMCalib/7f97035a1e8068bec0f6c51bfc2d367c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_43_1_sAo.root',
       '/store/user/akunsken/MuonGun2023SiPMCalib/MuonGun2023SiPMCalib/7f97035a1e8068bec0f6c51bfc2d367c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_44_1_PV7.root',
       '/store/user/akunsken/MuonGun2023SiPMCalib/MuonGun2023SiPMCalib/7f97035a1e8068bec0f6c51bfc2d367c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_45_1_jWr.root',
       '/store/user/akunsken/MuonGun2023SiPMCalib/MuonGun2023SiPMCalib/7f97035a1e8068bec0f6c51bfc2d367c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_46_1_NzM.root',
       '/store/user/akunsken/MuonGun2023SiPMCalib/MuonGun2023SiPMCalib/7f97035a1e8068bec0f6c51bfc2d367c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_47_1_oCi.root',
       '/store/user/akunsken/MuonGun2023SiPMCalib/MuonGun2023SiPMCalib/7f97035a1e8068bec0f6c51bfc2d367c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_48_1_sTh.root',
       '/store/user/akunsken/MuonGun2023SiPMCalib/MuonGun2023SiPMCalib/7f97035a1e8068bec0f6c51bfc2d367c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_49_1_3vr.root',
       '/store/user/akunsken/MuonGun2023SiPMCalib/MuonGun2023SiPMCalib/7f97035a1e8068bec0f6c51bfc2d367c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_4_1_TK7.root',
       '/store/user/akunsken/MuonGun2023SiPMCalib/MuonGun2023SiPMCalib/7f97035a1e8068bec0f6c51bfc2d367c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_50_1_nAq.root',
       '/store/user/akunsken/MuonGun2023SiPMCalib/MuonGun2023SiPMCalib/7f97035a1e8068bec0f6c51bfc2d367c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_51_1_za4.root',
       '/store/user/akunsken/MuonGun2023SiPMCalib/MuonGun2023SiPMCalib/7f97035a1e8068bec0f6c51bfc2d367c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_52_1_n5V.root',
       '/store/user/akunsken/MuonGun2023SiPMCalib/MuonGun2023SiPMCalib/7f97035a1e8068bec0f6c51bfc2d367c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_53_1_fk3.root',
       '/store/user/akunsken/MuonGun2023SiPMCalib/MuonGun2023SiPMCalib/7f97035a1e8068bec0f6c51bfc2d367c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_54_2_7yT.root',
       '/store/user/akunsken/MuonGun2023SiPMCalib/MuonGun2023SiPMCalib/7f97035a1e8068bec0f6c51bfc2d367c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_55_2_NmH.root',
       '/store/user/akunsken/MuonGun2023SiPMCalib/MuonGun2023SiPMCalib/7f97035a1e8068bec0f6c51bfc2d367c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_56_1_g3U.root',
       '/store/user/akunsken/MuonGun2023SiPMCalib/MuonGun2023SiPMCalib/7f97035a1e8068bec0f6c51bfc2d367c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_57_2_J3r.root',
       '/store/user/akunsken/MuonGun2023SiPMCalib/MuonGun2023SiPMCalib/7f97035a1e8068bec0f6c51bfc2d367c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_58_2_GNM.root',
       '/store/user/akunsken/MuonGun2023SiPMCalib/MuonGun2023SiPMCalib/7f97035a1e8068bec0f6c51bfc2d367c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_59_2_fhS.root',
       '/store/user/akunsken/MuonGun2023SiPMCalib/MuonGun2023SiPMCalib/7f97035a1e8068bec0f6c51bfc2d367c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_5_1_8jv.root',
       '/store/user/akunsken/MuonGun2023SiPMCalib/MuonGun2023SiPMCalib/7f97035a1e8068bec0f6c51bfc2d367c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_60_2_H2O.root',
       '/store/user/akunsken/MuonGun2023SiPMCalib/MuonGun2023SiPMCalib/7f97035a1e8068bec0f6c51bfc2d367c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_61_1_x9Q.root',
       '/store/user/akunsken/MuonGun2023SiPMCalib/MuonGun2023SiPMCalib/7f97035a1e8068bec0f6c51bfc2d367c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_62_2_cPa.root',
       '/store/user/akunsken/MuonGun2023SiPMCalib/MuonGun2023SiPMCalib/7f97035a1e8068bec0f6c51bfc2d367c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_63_2_CU1.root',
       '/store/user/akunsken/MuonGun2023SiPMCalib/MuonGun2023SiPMCalib/7f97035a1e8068bec0f6c51bfc2d367c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_64_1_jxb.root',
       '/store/user/akunsken/MuonGun2023SiPMCalib/MuonGun2023SiPMCalib/7f97035a1e8068bec0f6c51bfc2d367c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_65_1_1t2.root',
       '/store/user/akunsken/MuonGun2023SiPMCalib/MuonGun2023SiPMCalib/7f97035a1e8068bec0f6c51bfc2d367c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_66_1_JXH.root',
       '/store/user/akunsken/MuonGun2023SiPMCalib/MuonGun2023SiPMCalib/7f97035a1e8068bec0f6c51bfc2d367c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_67_1_zZf.root',
       '/store/user/akunsken/MuonGun2023SiPMCalib/MuonGun2023SiPMCalib/7f97035a1e8068bec0f6c51bfc2d367c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_68_1_sI1.root',
       '/store/user/akunsken/MuonGun2023SiPMCalib/MuonGun2023SiPMCalib/7f97035a1e8068bec0f6c51bfc2d367c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_69_1_AJF.root',
       '/store/user/akunsken/MuonGun2023SiPMCalib/MuonGun2023SiPMCalib/7f97035a1e8068bec0f6c51bfc2d367c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_6_1_l7C.root',
       '/store/user/akunsken/MuonGun2023SiPMCalib/MuonGun2023SiPMCalib/7f97035a1e8068bec0f6c51bfc2d367c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_70_1_VNB.root',
       '/store/user/akunsken/MuonGun2023SiPMCalib/MuonGun2023SiPMCalib/7f97035a1e8068bec0f6c51bfc2d367c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_71_2_wk4.root',
       '/store/user/akunsken/MuonGun2023SiPMCalib/MuonGun2023SiPMCalib/7f97035a1e8068bec0f6c51bfc2d367c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_72_2_jum.root',
       '/store/user/akunsken/MuonGun2023SiPMCalib/MuonGun2023SiPMCalib/7f97035a1e8068bec0f6c51bfc2d367c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_73_2_h65.root',
       '/store/user/akunsken/MuonGun2023SiPMCalib/MuonGun2023SiPMCalib/7f97035a1e8068bec0f6c51bfc2d367c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_74_1_gRT.root',
       '/store/user/akunsken/MuonGun2023SiPMCalib/MuonGun2023SiPMCalib/7f97035a1e8068bec0f6c51bfc2d367c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_75_2_kTY.root',
       '/store/user/akunsken/MuonGun2023SiPMCalib/MuonGun2023SiPMCalib/7f97035a1e8068bec0f6c51bfc2d367c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_76_2_Nvv.root',
       '/store/user/akunsken/MuonGun2023SiPMCalib/MuonGun2023SiPMCalib/7f97035a1e8068bec0f6c51bfc2d367c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_77_3_NAY.root',
       '/store/user/akunsken/MuonGun2023SiPMCalib/MuonGun2023SiPMCalib/7f97035a1e8068bec0f6c51bfc2d367c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_78_1_Qg9.root',
       '/store/user/akunsken/MuonGun2023SiPMCalib/MuonGun2023SiPMCalib/7f97035a1e8068bec0f6c51bfc2d367c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_79_1_nE4.root',
       '/store/user/akunsken/MuonGun2023SiPMCalib/MuonGun2023SiPMCalib/7f97035a1e8068bec0f6c51bfc2d367c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_7_1_33v.root',
       '/store/user/akunsken/MuonGun2023SiPMCalib/MuonGun2023SiPMCalib/7f97035a1e8068bec0f6c51bfc2d367c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_80_1_IZg.root',
       '/store/user/akunsken/MuonGun2023SiPMCalib/MuonGun2023SiPMCalib/7f97035a1e8068bec0f6c51bfc2d367c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_81_1_XFV.root',
       '/store/user/akunsken/MuonGun2023SiPMCalib/MuonGun2023SiPMCalib/7f97035a1e8068bec0f6c51bfc2d367c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_82_1_wUg.root',
       '/store/user/akunsken/MuonGun2023SiPMCalib/MuonGun2023SiPMCalib/7f97035a1e8068bec0f6c51bfc2d367c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_83_1_h0z.root',
       '/store/user/akunsken/MuonGun2023SiPMCalib/MuonGun2023SiPMCalib/7f97035a1e8068bec0f6c51bfc2d367c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_84_1_mgs.root',
       '/store/user/akunsken/MuonGun2023SiPMCalib/MuonGun2023SiPMCalib/7f97035a1e8068bec0f6c51bfc2d367c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_85_1_WDY.root',
       '/store/user/akunsken/MuonGun2023SiPMCalib/MuonGun2023SiPMCalib/7f97035a1e8068bec0f6c51bfc2d367c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_86_1_6Md.root',
       '/store/user/akunsken/MuonGun2023SiPMCalib/MuonGun2023SiPMCalib/7f97035a1e8068bec0f6c51bfc2d367c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_87_1_jNP.root',
       '/store/user/akunsken/MuonGun2023SiPMCalib/MuonGun2023SiPMCalib/7f97035a1e8068bec0f6c51bfc2d367c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_88_1_f89.root',
       '/store/user/akunsken/MuonGun2023SiPMCalib/MuonGun2023SiPMCalib/7f97035a1e8068bec0f6c51bfc2d367c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_89_1_V0k.root',
       '/store/user/akunsken/MuonGun2023SiPMCalib/MuonGun2023SiPMCalib/7f97035a1e8068bec0f6c51bfc2d367c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_8_1_JUA.root',
       '/store/user/akunsken/MuonGun2023SiPMCalib/MuonGun2023SiPMCalib/7f97035a1e8068bec0f6c51bfc2d367c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_90_1_4WJ.root',
       '/store/user/akunsken/MuonGun2023SiPMCalib/MuonGun2023SiPMCalib/7f97035a1e8068bec0f6c51bfc2d367c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_91_1_t4z.root',
       '/store/user/akunsken/MuonGun2023SiPMCalib/MuonGun2023SiPMCalib/7f97035a1e8068bec0f6c51bfc2d367c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_92_1_TUO.root',
       '/store/user/akunsken/MuonGun2023SiPMCalib/MuonGun2023SiPMCalib/7f97035a1e8068bec0f6c51bfc2d367c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_93_1_dss.root',
       '/store/user/akunsken/MuonGun2023SiPMCalib/MuonGun2023SiPMCalib/7f97035a1e8068bec0f6c51bfc2d367c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_94_1_CDT.root',
       '/store/user/akunsken/MuonGun2023SiPMCalib/MuonGun2023SiPMCalib/7f97035a1e8068bec0f6c51bfc2d367c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_95_1_QUZ.root',
       '/store/user/akunsken/MuonGun2023SiPMCalib/MuonGun2023SiPMCalib/7f97035a1e8068bec0f6c51bfc2d367c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_96_1_3zd.root',
       '/store/user/akunsken/MuonGun2023SiPMCalib/MuonGun2023SiPMCalib/7f97035a1e8068bec0f6c51bfc2d367c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_97_1_yqb.root',
       '/store/user/akunsken/MuonGun2023SiPMCalib/MuonGun2023SiPMCalib/7f97035a1e8068bec0f6c51bfc2d367c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_98_1_hAu.root',
       '/store/user/akunsken/MuonGun2023SiPMCalib/MuonGun2023SiPMCalib/7f97035a1e8068bec0f6c51bfc2d367c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_99_1_JIx.root',
       '/store/user/akunsken/MuonGun2023SiPMCalib/MuonGun2023SiPMCalib/7f97035a1e8068bec0f6c51bfc2d367c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_9_1_x8d.root' ] )

process.source = cms.Source("PoolSource",
    # replace 'myfile.root' with the source file you want to use
    fileNames = readFiles
)

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
    hoEnergyThreshold = cms.double(0.2),
    maxDeltaR = cms.double(0.3)
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
