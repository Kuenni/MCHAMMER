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
       '/store/user/akunsken/MuonGun2023NoExtraCalib/MuonGun2023NoExtraCalib/ebaee5b1cde984d67970cccabb0beb1c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_100_2_Gyg.root',
       '/store/user/akunsken/MuonGun2023NoExtraCalib/MuonGun2023NoExtraCalib/ebaee5b1cde984d67970cccabb0beb1c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_101_1_84t.root',
       '/store/user/akunsken/MuonGun2023NoExtraCalib/MuonGun2023NoExtraCalib/ebaee5b1cde984d67970cccabb0beb1c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_102_1_3wE.root',
       '/store/user/akunsken/MuonGun2023NoExtraCalib/MuonGun2023NoExtraCalib/ebaee5b1cde984d67970cccabb0beb1c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_103_1_H1F.root',
       '/store/user/akunsken/MuonGun2023NoExtraCalib/MuonGun2023NoExtraCalib/ebaee5b1cde984d67970cccabb0beb1c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_104_1_Cpr.root',
       '/store/user/akunsken/MuonGun2023NoExtraCalib/MuonGun2023NoExtraCalib/ebaee5b1cde984d67970cccabb0beb1c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_105_1_tdl.root',
       '/store/user/akunsken/MuonGun2023NoExtraCalib/MuonGun2023NoExtraCalib/ebaee5b1cde984d67970cccabb0beb1c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_106_1_nAc.root',
       '/store/user/akunsken/MuonGun2023NoExtraCalib/MuonGun2023NoExtraCalib/ebaee5b1cde984d67970cccabb0beb1c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_107_1_ghE.root',
       '/store/user/akunsken/MuonGun2023NoExtraCalib/MuonGun2023NoExtraCalib/ebaee5b1cde984d67970cccabb0beb1c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_108_1_tJZ.root',
       '/store/user/akunsken/MuonGun2023NoExtraCalib/MuonGun2023NoExtraCalib/ebaee5b1cde984d67970cccabb0beb1c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_109_1_O9S.root',
       '/store/user/akunsken/MuonGun2023NoExtraCalib/MuonGun2023NoExtraCalib/ebaee5b1cde984d67970cccabb0beb1c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_10_1_qNp.root',
       '/store/user/akunsken/MuonGun2023NoExtraCalib/MuonGun2023NoExtraCalib/ebaee5b1cde984d67970cccabb0beb1c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_110_1_HwK.root',
       '/store/user/akunsken/MuonGun2023NoExtraCalib/MuonGun2023NoExtraCalib/ebaee5b1cde984d67970cccabb0beb1c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_111_1_398.root',
       '/store/user/akunsken/MuonGun2023NoExtraCalib/MuonGun2023NoExtraCalib/ebaee5b1cde984d67970cccabb0beb1c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_112_1_7Tb.root',
       '/store/user/akunsken/MuonGun2023NoExtraCalib/MuonGun2023NoExtraCalib/ebaee5b1cde984d67970cccabb0beb1c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_113_1_O85.root',
       '/store/user/akunsken/MuonGun2023NoExtraCalib/MuonGun2023NoExtraCalib/ebaee5b1cde984d67970cccabb0beb1c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_114_1_pei.root',
       '/store/user/akunsken/MuonGun2023NoExtraCalib/MuonGun2023NoExtraCalib/ebaee5b1cde984d67970cccabb0beb1c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_115_1_5oJ.root',
       '/store/user/akunsken/MuonGun2023NoExtraCalib/MuonGun2023NoExtraCalib/ebaee5b1cde984d67970cccabb0beb1c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_116_1_fBD.root',
       '/store/user/akunsken/MuonGun2023NoExtraCalib/MuonGun2023NoExtraCalib/ebaee5b1cde984d67970cccabb0beb1c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_117_1_RNJ.root',
       '/store/user/akunsken/MuonGun2023NoExtraCalib/MuonGun2023NoExtraCalib/ebaee5b1cde984d67970cccabb0beb1c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_118_1_pJJ.root',
       '/store/user/akunsken/MuonGun2023NoExtraCalib/MuonGun2023NoExtraCalib/ebaee5b1cde984d67970cccabb0beb1c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_119_1_K13.root',
       '/store/user/akunsken/MuonGun2023NoExtraCalib/MuonGun2023NoExtraCalib/ebaee5b1cde984d67970cccabb0beb1c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_11_1_E2t.root',
       '/store/user/akunsken/MuonGun2023NoExtraCalib/MuonGun2023NoExtraCalib/ebaee5b1cde984d67970cccabb0beb1c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_120_1_eR5.root',
       '/store/user/akunsken/MuonGun2023NoExtraCalib/MuonGun2023NoExtraCalib/ebaee5b1cde984d67970cccabb0beb1c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_121_1_zHs.root',
       '/store/user/akunsken/MuonGun2023NoExtraCalib/MuonGun2023NoExtraCalib/ebaee5b1cde984d67970cccabb0beb1c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_122_1_bZ7.root',
       '/store/user/akunsken/MuonGun2023NoExtraCalib/MuonGun2023NoExtraCalib/ebaee5b1cde984d67970cccabb0beb1c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_123_1_qRh.root',
       '/store/user/akunsken/MuonGun2023NoExtraCalib/MuonGun2023NoExtraCalib/ebaee5b1cde984d67970cccabb0beb1c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_124_1_iAy.root',
       '/store/user/akunsken/MuonGun2023NoExtraCalib/MuonGun2023NoExtraCalib/ebaee5b1cde984d67970cccabb0beb1c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_125_1_Qmu.root',
       '/store/user/akunsken/MuonGun2023NoExtraCalib/MuonGun2023NoExtraCalib/ebaee5b1cde984d67970cccabb0beb1c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_126_1_K5a.root',
       '/store/user/akunsken/MuonGun2023NoExtraCalib/MuonGun2023NoExtraCalib/ebaee5b1cde984d67970cccabb0beb1c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_127_1_Qx9.root',
       '/store/user/akunsken/MuonGun2023NoExtraCalib/MuonGun2023NoExtraCalib/ebaee5b1cde984d67970cccabb0beb1c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_128_1_gJf.root',
       '/store/user/akunsken/MuonGun2023NoExtraCalib/MuonGun2023NoExtraCalib/ebaee5b1cde984d67970cccabb0beb1c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_129_1_O2s.root',
       '/store/user/akunsken/MuonGun2023NoExtraCalib/MuonGun2023NoExtraCalib/ebaee5b1cde984d67970cccabb0beb1c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_12_1_Uw7.root',
       '/store/user/akunsken/MuonGun2023NoExtraCalib/MuonGun2023NoExtraCalib/ebaee5b1cde984d67970cccabb0beb1c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_130_1_n8e.root',
       '/store/user/akunsken/MuonGun2023NoExtraCalib/MuonGun2023NoExtraCalib/ebaee5b1cde984d67970cccabb0beb1c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_131_1_osW.root',
       '/store/user/akunsken/MuonGun2023NoExtraCalib/MuonGun2023NoExtraCalib/ebaee5b1cde984d67970cccabb0beb1c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_132_1_5Qw.root',
       '/store/user/akunsken/MuonGun2023NoExtraCalib/MuonGun2023NoExtraCalib/ebaee5b1cde984d67970cccabb0beb1c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_133_1_eiv.root',
       '/store/user/akunsken/MuonGun2023NoExtraCalib/MuonGun2023NoExtraCalib/ebaee5b1cde984d67970cccabb0beb1c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_134_1_CpQ.root',
       '/store/user/akunsken/MuonGun2023NoExtraCalib/MuonGun2023NoExtraCalib/ebaee5b1cde984d67970cccabb0beb1c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_135_1_jik.root',
       '/store/user/akunsken/MuonGun2023NoExtraCalib/MuonGun2023NoExtraCalib/ebaee5b1cde984d67970cccabb0beb1c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_136_1_XHo.root',
       '/store/user/akunsken/MuonGun2023NoExtraCalib/MuonGun2023NoExtraCalib/ebaee5b1cde984d67970cccabb0beb1c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_137_1_KIh.root',
       '/store/user/akunsken/MuonGun2023NoExtraCalib/MuonGun2023NoExtraCalib/ebaee5b1cde984d67970cccabb0beb1c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_138_1_ShC.root',
       '/store/user/akunsken/MuonGun2023NoExtraCalib/MuonGun2023NoExtraCalib/ebaee5b1cde984d67970cccabb0beb1c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_139_1_Rd2.root',
       '/store/user/akunsken/MuonGun2023NoExtraCalib/MuonGun2023NoExtraCalib/ebaee5b1cde984d67970cccabb0beb1c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_13_1_aJP.root',
       '/store/user/akunsken/MuonGun2023NoExtraCalib/MuonGun2023NoExtraCalib/ebaee5b1cde984d67970cccabb0beb1c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_140_1_u9U.root',
       '/store/user/akunsken/MuonGun2023NoExtraCalib/MuonGun2023NoExtraCalib/ebaee5b1cde984d67970cccabb0beb1c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_141_1_zU1.root',
       '/store/user/akunsken/MuonGun2023NoExtraCalib/MuonGun2023NoExtraCalib/ebaee5b1cde984d67970cccabb0beb1c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_142_1_skH.root',
       '/store/user/akunsken/MuonGun2023NoExtraCalib/MuonGun2023NoExtraCalib/ebaee5b1cde984d67970cccabb0beb1c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_143_1_krC.root',
       '/store/user/akunsken/MuonGun2023NoExtraCalib/MuonGun2023NoExtraCalib/ebaee5b1cde984d67970cccabb0beb1c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_144_2_e95.root',
       '/store/user/akunsken/MuonGun2023NoExtraCalib/MuonGun2023NoExtraCalib/ebaee5b1cde984d67970cccabb0beb1c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_145_1_rm7.root',
       '/store/user/akunsken/MuonGun2023NoExtraCalib/MuonGun2023NoExtraCalib/ebaee5b1cde984d67970cccabb0beb1c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_146_1_L8D.root',
       '/store/user/akunsken/MuonGun2023NoExtraCalib/MuonGun2023NoExtraCalib/ebaee5b1cde984d67970cccabb0beb1c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_147_1_VAI.root',
       '/store/user/akunsken/MuonGun2023NoExtraCalib/MuonGun2023NoExtraCalib/ebaee5b1cde984d67970cccabb0beb1c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_148_2_YtL.root',
       '/store/user/akunsken/MuonGun2023NoExtraCalib/MuonGun2023NoExtraCalib/ebaee5b1cde984d67970cccabb0beb1c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_149_1_S0E.root',
       '/store/user/akunsken/MuonGun2023NoExtraCalib/MuonGun2023NoExtraCalib/ebaee5b1cde984d67970cccabb0beb1c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_14_1_7sf.root',
       '/store/user/akunsken/MuonGun2023NoExtraCalib/MuonGun2023NoExtraCalib/ebaee5b1cde984d67970cccabb0beb1c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_150_1_p25.root',
       '/store/user/akunsken/MuonGun2023NoExtraCalib/MuonGun2023NoExtraCalib/ebaee5b1cde984d67970cccabb0beb1c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_151_2_dkI.root',
       '/store/user/akunsken/MuonGun2023NoExtraCalib/MuonGun2023NoExtraCalib/ebaee5b1cde984d67970cccabb0beb1c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_152_1_Zmx.root',
       '/store/user/akunsken/MuonGun2023NoExtraCalib/MuonGun2023NoExtraCalib/ebaee5b1cde984d67970cccabb0beb1c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_153_1_Wpe.root',
       '/store/user/akunsken/MuonGun2023NoExtraCalib/MuonGun2023NoExtraCalib/ebaee5b1cde984d67970cccabb0beb1c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_154_2_FZL.root',
       '/store/user/akunsken/MuonGun2023NoExtraCalib/MuonGun2023NoExtraCalib/ebaee5b1cde984d67970cccabb0beb1c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_155_1_LWU.root',
       '/store/user/akunsken/MuonGun2023NoExtraCalib/MuonGun2023NoExtraCalib/ebaee5b1cde984d67970cccabb0beb1c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_156_1_HdD.root',
       '/store/user/akunsken/MuonGun2023NoExtraCalib/MuonGun2023NoExtraCalib/ebaee5b1cde984d67970cccabb0beb1c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_157_1_A2l.root',
       '/store/user/akunsken/MuonGun2023NoExtraCalib/MuonGun2023NoExtraCalib/ebaee5b1cde984d67970cccabb0beb1c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_158_1_bG7.root',
       '/store/user/akunsken/MuonGun2023NoExtraCalib/MuonGun2023NoExtraCalib/ebaee5b1cde984d67970cccabb0beb1c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_159_1_j3v.root',
       '/store/user/akunsken/MuonGun2023NoExtraCalib/MuonGun2023NoExtraCalib/ebaee5b1cde984d67970cccabb0beb1c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_15_1_5aT.root',
       '/store/user/akunsken/MuonGun2023NoExtraCalib/MuonGun2023NoExtraCalib/ebaee5b1cde984d67970cccabb0beb1c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_160_1_Opg.root',
       '/store/user/akunsken/MuonGun2023NoExtraCalib/MuonGun2023NoExtraCalib/ebaee5b1cde984d67970cccabb0beb1c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_161_1_Sbj.root',
       '/store/user/akunsken/MuonGun2023NoExtraCalib/MuonGun2023NoExtraCalib/ebaee5b1cde984d67970cccabb0beb1c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_162_1_i9i.root',
       '/store/user/akunsken/MuonGun2023NoExtraCalib/MuonGun2023NoExtraCalib/ebaee5b1cde984d67970cccabb0beb1c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_163_1_Yn8.root',
       '/store/user/akunsken/MuonGun2023NoExtraCalib/MuonGun2023NoExtraCalib/ebaee5b1cde984d67970cccabb0beb1c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_164_1_Pm1.root',
       '/store/user/akunsken/MuonGun2023NoExtraCalib/MuonGun2023NoExtraCalib/ebaee5b1cde984d67970cccabb0beb1c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_165_1_if8.root',
       '/store/user/akunsken/MuonGun2023NoExtraCalib/MuonGun2023NoExtraCalib/ebaee5b1cde984d67970cccabb0beb1c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_166_1_FjC.root',
       '/store/user/akunsken/MuonGun2023NoExtraCalib/MuonGun2023NoExtraCalib/ebaee5b1cde984d67970cccabb0beb1c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_167_1_tpF.root',
       '/store/user/akunsken/MuonGun2023NoExtraCalib/MuonGun2023NoExtraCalib/ebaee5b1cde984d67970cccabb0beb1c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_168_1_3Hm.root',
       '/store/user/akunsken/MuonGun2023NoExtraCalib/MuonGun2023NoExtraCalib/ebaee5b1cde984d67970cccabb0beb1c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_169_1_OEU.root',
       '/store/user/akunsken/MuonGun2023NoExtraCalib/MuonGun2023NoExtraCalib/ebaee5b1cde984d67970cccabb0beb1c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_16_1_keC.root',
       '/store/user/akunsken/MuonGun2023NoExtraCalib/MuonGun2023NoExtraCalib/ebaee5b1cde984d67970cccabb0beb1c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_170_2_TIy.root',
       '/store/user/akunsken/MuonGun2023NoExtraCalib/MuonGun2023NoExtraCalib/ebaee5b1cde984d67970cccabb0beb1c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_171_1_agE.root',
       '/store/user/akunsken/MuonGun2023NoExtraCalib/MuonGun2023NoExtraCalib/ebaee5b1cde984d67970cccabb0beb1c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_172_1_6mB.root',
       '/store/user/akunsken/MuonGun2023NoExtraCalib/MuonGun2023NoExtraCalib/ebaee5b1cde984d67970cccabb0beb1c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_173_1_BRz.root',
       '/store/user/akunsken/MuonGun2023NoExtraCalib/MuonGun2023NoExtraCalib/ebaee5b1cde984d67970cccabb0beb1c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_174_1_7kb.root',
       '/store/user/akunsken/MuonGun2023NoExtraCalib/MuonGun2023NoExtraCalib/ebaee5b1cde984d67970cccabb0beb1c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_175_1_YYi.root',
       '/store/user/akunsken/MuonGun2023NoExtraCalib/MuonGun2023NoExtraCalib/ebaee5b1cde984d67970cccabb0beb1c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_176_1_OWn.root',
       '/store/user/akunsken/MuonGun2023NoExtraCalib/MuonGun2023NoExtraCalib/ebaee5b1cde984d67970cccabb0beb1c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_177_1_3uW.root',
       '/store/user/akunsken/MuonGun2023NoExtraCalib/MuonGun2023NoExtraCalib/ebaee5b1cde984d67970cccabb0beb1c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_178_1_Keq.root',
       '/store/user/akunsken/MuonGun2023NoExtraCalib/MuonGun2023NoExtraCalib/ebaee5b1cde984d67970cccabb0beb1c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_179_1_cHi.root',
       '/store/user/akunsken/MuonGun2023NoExtraCalib/MuonGun2023NoExtraCalib/ebaee5b1cde984d67970cccabb0beb1c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_17_1_R56.root',
       '/store/user/akunsken/MuonGun2023NoExtraCalib/MuonGun2023NoExtraCalib/ebaee5b1cde984d67970cccabb0beb1c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_180_1_wjb.root',
       '/store/user/akunsken/MuonGun2023NoExtraCalib/MuonGun2023NoExtraCalib/ebaee5b1cde984d67970cccabb0beb1c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_181_1_q5n.root',
       '/store/user/akunsken/MuonGun2023NoExtraCalib/MuonGun2023NoExtraCalib/ebaee5b1cde984d67970cccabb0beb1c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_182_1_Yu0.root',
       '/store/user/akunsken/MuonGun2023NoExtraCalib/MuonGun2023NoExtraCalib/ebaee5b1cde984d67970cccabb0beb1c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_183_1_G6w.root',
       '/store/user/akunsken/MuonGun2023NoExtraCalib/MuonGun2023NoExtraCalib/ebaee5b1cde984d67970cccabb0beb1c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_184_1_uhL.root',
       '/store/user/akunsken/MuonGun2023NoExtraCalib/MuonGun2023NoExtraCalib/ebaee5b1cde984d67970cccabb0beb1c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_185_1_UJj.root',
       '/store/user/akunsken/MuonGun2023NoExtraCalib/MuonGun2023NoExtraCalib/ebaee5b1cde984d67970cccabb0beb1c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_186_1_Hh1.root',
       '/store/user/akunsken/MuonGun2023NoExtraCalib/MuonGun2023NoExtraCalib/ebaee5b1cde984d67970cccabb0beb1c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_187_1_ouz.root',
       '/store/user/akunsken/MuonGun2023NoExtraCalib/MuonGun2023NoExtraCalib/ebaee5b1cde984d67970cccabb0beb1c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_188_1_qcj.root',
       '/store/user/akunsken/MuonGun2023NoExtraCalib/MuonGun2023NoExtraCalib/ebaee5b1cde984d67970cccabb0beb1c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_189_1_MEK.root',
       '/store/user/akunsken/MuonGun2023NoExtraCalib/MuonGun2023NoExtraCalib/ebaee5b1cde984d67970cccabb0beb1c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_18_1_dT4.root',
       '/store/user/akunsken/MuonGun2023NoExtraCalib/MuonGun2023NoExtraCalib/ebaee5b1cde984d67970cccabb0beb1c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_190_1_9K2.root',
       '/store/user/akunsken/MuonGun2023NoExtraCalib/MuonGun2023NoExtraCalib/ebaee5b1cde984d67970cccabb0beb1c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_191_1_JFN.root',
       '/store/user/akunsken/MuonGun2023NoExtraCalib/MuonGun2023NoExtraCalib/ebaee5b1cde984d67970cccabb0beb1c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_192_1_353.root',
       '/store/user/akunsken/MuonGun2023NoExtraCalib/MuonGun2023NoExtraCalib/ebaee5b1cde984d67970cccabb0beb1c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_193_1_8lD.root',
       '/store/user/akunsken/MuonGun2023NoExtraCalib/MuonGun2023NoExtraCalib/ebaee5b1cde984d67970cccabb0beb1c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_194_1_OeD.root',
       '/store/user/akunsken/MuonGun2023NoExtraCalib/MuonGun2023NoExtraCalib/ebaee5b1cde984d67970cccabb0beb1c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_195_1_zIM.root',
       '/store/user/akunsken/MuonGun2023NoExtraCalib/MuonGun2023NoExtraCalib/ebaee5b1cde984d67970cccabb0beb1c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_196_1_nOm.root',
       '/store/user/akunsken/MuonGun2023NoExtraCalib/MuonGun2023NoExtraCalib/ebaee5b1cde984d67970cccabb0beb1c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_197_1_J0r.root',
       '/store/user/akunsken/MuonGun2023NoExtraCalib/MuonGun2023NoExtraCalib/ebaee5b1cde984d67970cccabb0beb1c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_198_1_lwx.root',
       '/store/user/akunsken/MuonGun2023NoExtraCalib/MuonGun2023NoExtraCalib/ebaee5b1cde984d67970cccabb0beb1c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_199_1_qBq.root',
       '/store/user/akunsken/MuonGun2023NoExtraCalib/MuonGun2023NoExtraCalib/ebaee5b1cde984d67970cccabb0beb1c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_19_1_xZQ.root',
       '/store/user/akunsken/MuonGun2023NoExtraCalib/MuonGun2023NoExtraCalib/ebaee5b1cde984d67970cccabb0beb1c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_1_1_hxR.root',
       '/store/user/akunsken/MuonGun2023NoExtraCalib/MuonGun2023NoExtraCalib/ebaee5b1cde984d67970cccabb0beb1c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_200_1_7Yo.root',
       '/store/user/akunsken/MuonGun2023NoExtraCalib/MuonGun2023NoExtraCalib/ebaee5b1cde984d67970cccabb0beb1c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_20_1_2i1.root',
       '/store/user/akunsken/MuonGun2023NoExtraCalib/MuonGun2023NoExtraCalib/ebaee5b1cde984d67970cccabb0beb1c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_21_1_4dv.root',
       '/store/user/akunsken/MuonGun2023NoExtraCalib/MuonGun2023NoExtraCalib/ebaee5b1cde984d67970cccabb0beb1c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_22_1_Am2.root',
       '/store/user/akunsken/MuonGun2023NoExtraCalib/MuonGun2023NoExtraCalib/ebaee5b1cde984d67970cccabb0beb1c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_23_1_mPa.root',
       '/store/user/akunsken/MuonGun2023NoExtraCalib/MuonGun2023NoExtraCalib/ebaee5b1cde984d67970cccabb0beb1c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_24_1_8Fa.root',
       '/store/user/akunsken/MuonGun2023NoExtraCalib/MuonGun2023NoExtraCalib/ebaee5b1cde984d67970cccabb0beb1c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_25_1_Fk1.root',
       '/store/user/akunsken/MuonGun2023NoExtraCalib/MuonGun2023NoExtraCalib/ebaee5b1cde984d67970cccabb0beb1c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_26_1_ppU.root',
       '/store/user/akunsken/MuonGun2023NoExtraCalib/MuonGun2023NoExtraCalib/ebaee5b1cde984d67970cccabb0beb1c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_27_1_reP.root',
       '/store/user/akunsken/MuonGun2023NoExtraCalib/MuonGun2023NoExtraCalib/ebaee5b1cde984d67970cccabb0beb1c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_28_1_DsZ.root',
       '/store/user/akunsken/MuonGun2023NoExtraCalib/MuonGun2023NoExtraCalib/ebaee5b1cde984d67970cccabb0beb1c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_29_1_pPL.root',
       '/store/user/akunsken/MuonGun2023NoExtraCalib/MuonGun2023NoExtraCalib/ebaee5b1cde984d67970cccabb0beb1c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_2_1_Ryg.root',
       '/store/user/akunsken/MuonGun2023NoExtraCalib/MuonGun2023NoExtraCalib/ebaee5b1cde984d67970cccabb0beb1c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_30_1_ecE.root',
       '/store/user/akunsken/MuonGun2023NoExtraCalib/MuonGun2023NoExtraCalib/ebaee5b1cde984d67970cccabb0beb1c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_31_1_Xro.root',
       '/store/user/akunsken/MuonGun2023NoExtraCalib/MuonGun2023NoExtraCalib/ebaee5b1cde984d67970cccabb0beb1c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_32_1_Rnz.root',
       '/store/user/akunsken/MuonGun2023NoExtraCalib/MuonGun2023NoExtraCalib/ebaee5b1cde984d67970cccabb0beb1c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_33_1_czc.root',
       '/store/user/akunsken/MuonGun2023NoExtraCalib/MuonGun2023NoExtraCalib/ebaee5b1cde984d67970cccabb0beb1c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_34_1_K0A.root',
       '/store/user/akunsken/MuonGun2023NoExtraCalib/MuonGun2023NoExtraCalib/ebaee5b1cde984d67970cccabb0beb1c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_35_1_uY0.root',
       '/store/user/akunsken/MuonGun2023NoExtraCalib/MuonGun2023NoExtraCalib/ebaee5b1cde984d67970cccabb0beb1c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_36_1_535.root',
       '/store/user/akunsken/MuonGun2023NoExtraCalib/MuonGun2023NoExtraCalib/ebaee5b1cde984d67970cccabb0beb1c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_37_1_oVr.root',
       '/store/user/akunsken/MuonGun2023NoExtraCalib/MuonGun2023NoExtraCalib/ebaee5b1cde984d67970cccabb0beb1c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_38_1_pWn.root',
       '/store/user/akunsken/MuonGun2023NoExtraCalib/MuonGun2023NoExtraCalib/ebaee5b1cde984d67970cccabb0beb1c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_39_1_U2D.root',
       '/store/user/akunsken/MuonGun2023NoExtraCalib/MuonGun2023NoExtraCalib/ebaee5b1cde984d67970cccabb0beb1c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_3_1_Ztx.root',
       '/store/user/akunsken/MuonGun2023NoExtraCalib/MuonGun2023NoExtraCalib/ebaee5b1cde984d67970cccabb0beb1c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_40_1_RZX.root',
       '/store/user/akunsken/MuonGun2023NoExtraCalib/MuonGun2023NoExtraCalib/ebaee5b1cde984d67970cccabb0beb1c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_41_1_kmC.root',
       '/store/user/akunsken/MuonGun2023NoExtraCalib/MuonGun2023NoExtraCalib/ebaee5b1cde984d67970cccabb0beb1c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_42_1_KNn.root',
       '/store/user/akunsken/MuonGun2023NoExtraCalib/MuonGun2023NoExtraCalib/ebaee5b1cde984d67970cccabb0beb1c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_43_1_THJ.root',
       '/store/user/akunsken/MuonGun2023NoExtraCalib/MuonGun2023NoExtraCalib/ebaee5b1cde984d67970cccabb0beb1c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_44_1_aTn.root',
       '/store/user/akunsken/MuonGun2023NoExtraCalib/MuonGun2023NoExtraCalib/ebaee5b1cde984d67970cccabb0beb1c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_45_1_yVl.root',
       '/store/user/akunsken/MuonGun2023NoExtraCalib/MuonGun2023NoExtraCalib/ebaee5b1cde984d67970cccabb0beb1c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_46_1_FBo.root',
       '/store/user/akunsken/MuonGun2023NoExtraCalib/MuonGun2023NoExtraCalib/ebaee5b1cde984d67970cccabb0beb1c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_47_1_lIW.root',
       '/store/user/akunsken/MuonGun2023NoExtraCalib/MuonGun2023NoExtraCalib/ebaee5b1cde984d67970cccabb0beb1c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_48_1_Xav.root',
       '/store/user/akunsken/MuonGun2023NoExtraCalib/MuonGun2023NoExtraCalib/ebaee5b1cde984d67970cccabb0beb1c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_49_1_JxR.root',
       '/store/user/akunsken/MuonGun2023NoExtraCalib/MuonGun2023NoExtraCalib/ebaee5b1cde984d67970cccabb0beb1c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_4_1_jIU.root',
       '/store/user/akunsken/MuonGun2023NoExtraCalib/MuonGun2023NoExtraCalib/ebaee5b1cde984d67970cccabb0beb1c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_50_1_y8Q.root',
       '/store/user/akunsken/MuonGun2023NoExtraCalib/MuonGun2023NoExtraCalib/ebaee5b1cde984d67970cccabb0beb1c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_51_2_1C3.root',
       '/store/user/akunsken/MuonGun2023NoExtraCalib/MuonGun2023NoExtraCalib/ebaee5b1cde984d67970cccabb0beb1c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_52_1_x8q.root',
       '/store/user/akunsken/MuonGun2023NoExtraCalib/MuonGun2023NoExtraCalib/ebaee5b1cde984d67970cccabb0beb1c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_53_1_loy.root',
       '/store/user/akunsken/MuonGun2023NoExtraCalib/MuonGun2023NoExtraCalib/ebaee5b1cde984d67970cccabb0beb1c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_54_1_NEO.root',
       '/store/user/akunsken/MuonGun2023NoExtraCalib/MuonGun2023NoExtraCalib/ebaee5b1cde984d67970cccabb0beb1c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_55_1_VM1.root',
       '/store/user/akunsken/MuonGun2023NoExtraCalib/MuonGun2023NoExtraCalib/ebaee5b1cde984d67970cccabb0beb1c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_56_1_oPr.root',
       '/store/user/akunsken/MuonGun2023NoExtraCalib/MuonGun2023NoExtraCalib/ebaee5b1cde984d67970cccabb0beb1c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_57_1_mA8.root',
       '/store/user/akunsken/MuonGun2023NoExtraCalib/MuonGun2023NoExtraCalib/ebaee5b1cde984d67970cccabb0beb1c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_58_1_hhP.root',
       '/store/user/akunsken/MuonGun2023NoExtraCalib/MuonGun2023NoExtraCalib/ebaee5b1cde984d67970cccabb0beb1c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_59_1_Ths.root',
       '/store/user/akunsken/MuonGun2023NoExtraCalib/MuonGun2023NoExtraCalib/ebaee5b1cde984d67970cccabb0beb1c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_5_1_IgI.root',
       '/store/user/akunsken/MuonGun2023NoExtraCalib/MuonGun2023NoExtraCalib/ebaee5b1cde984d67970cccabb0beb1c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_60_1_qwZ.root',
       '/store/user/akunsken/MuonGun2023NoExtraCalib/MuonGun2023NoExtraCalib/ebaee5b1cde984d67970cccabb0beb1c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_61_1_CMv.root',
       '/store/user/akunsken/MuonGun2023NoExtraCalib/MuonGun2023NoExtraCalib/ebaee5b1cde984d67970cccabb0beb1c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_62_1_GIY.root',
       '/store/user/akunsken/MuonGun2023NoExtraCalib/MuonGun2023NoExtraCalib/ebaee5b1cde984d67970cccabb0beb1c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_63_1_Ggt.root',
       '/store/user/akunsken/MuonGun2023NoExtraCalib/MuonGun2023NoExtraCalib/ebaee5b1cde984d67970cccabb0beb1c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_64_1_SH6.root',
       '/store/user/akunsken/MuonGun2023NoExtraCalib/MuonGun2023NoExtraCalib/ebaee5b1cde984d67970cccabb0beb1c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_65_1_rFj.root',
       '/store/user/akunsken/MuonGun2023NoExtraCalib/MuonGun2023NoExtraCalib/ebaee5b1cde984d67970cccabb0beb1c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_66_1_95j.root',
       '/store/user/akunsken/MuonGun2023NoExtraCalib/MuonGun2023NoExtraCalib/ebaee5b1cde984d67970cccabb0beb1c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_67_1_V9t.root',
       '/store/user/akunsken/MuonGun2023NoExtraCalib/MuonGun2023NoExtraCalib/ebaee5b1cde984d67970cccabb0beb1c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_68_1_P09.root',
       '/store/user/akunsken/MuonGun2023NoExtraCalib/MuonGun2023NoExtraCalib/ebaee5b1cde984d67970cccabb0beb1c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_69_1_D0O.root',
       '/store/user/akunsken/MuonGun2023NoExtraCalib/MuonGun2023NoExtraCalib/ebaee5b1cde984d67970cccabb0beb1c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_6_1_i5u.root',
       '/store/user/akunsken/MuonGun2023NoExtraCalib/MuonGun2023NoExtraCalib/ebaee5b1cde984d67970cccabb0beb1c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_70_1_QIM.root',
       '/store/user/akunsken/MuonGun2023NoExtraCalib/MuonGun2023NoExtraCalib/ebaee5b1cde984d67970cccabb0beb1c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_71_1_d5O.root',
       '/store/user/akunsken/MuonGun2023NoExtraCalib/MuonGun2023NoExtraCalib/ebaee5b1cde984d67970cccabb0beb1c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_72_1_Hxp.root',
       '/store/user/akunsken/MuonGun2023NoExtraCalib/MuonGun2023NoExtraCalib/ebaee5b1cde984d67970cccabb0beb1c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_73_1_Jxs.root',
       '/store/user/akunsken/MuonGun2023NoExtraCalib/MuonGun2023NoExtraCalib/ebaee5b1cde984d67970cccabb0beb1c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_74_1_XRc.root',
       '/store/user/akunsken/MuonGun2023NoExtraCalib/MuonGun2023NoExtraCalib/ebaee5b1cde984d67970cccabb0beb1c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_75_1_UOF.root',
       '/store/user/akunsken/MuonGun2023NoExtraCalib/MuonGun2023NoExtraCalib/ebaee5b1cde984d67970cccabb0beb1c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_76_1_K3Z.root',
       '/store/user/akunsken/MuonGun2023NoExtraCalib/MuonGun2023NoExtraCalib/ebaee5b1cde984d67970cccabb0beb1c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_77_1_1wT.root',
       '/store/user/akunsken/MuonGun2023NoExtraCalib/MuonGun2023NoExtraCalib/ebaee5b1cde984d67970cccabb0beb1c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_78_1_2W4.root',
       '/store/user/akunsken/MuonGun2023NoExtraCalib/MuonGun2023NoExtraCalib/ebaee5b1cde984d67970cccabb0beb1c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_79_1_CBJ.root',
       '/store/user/akunsken/MuonGun2023NoExtraCalib/MuonGun2023NoExtraCalib/ebaee5b1cde984d67970cccabb0beb1c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_7_1_d90.root',
       '/store/user/akunsken/MuonGun2023NoExtraCalib/MuonGun2023NoExtraCalib/ebaee5b1cde984d67970cccabb0beb1c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_80_1_r02.root',
       '/store/user/akunsken/MuonGun2023NoExtraCalib/MuonGun2023NoExtraCalib/ebaee5b1cde984d67970cccabb0beb1c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_81_1_YNL.root',
       '/store/user/akunsken/MuonGun2023NoExtraCalib/MuonGun2023NoExtraCalib/ebaee5b1cde984d67970cccabb0beb1c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_82_1_ww1.root',
       '/store/user/akunsken/MuonGun2023NoExtraCalib/MuonGun2023NoExtraCalib/ebaee5b1cde984d67970cccabb0beb1c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_83_1_txd.root',
       '/store/user/akunsken/MuonGun2023NoExtraCalib/MuonGun2023NoExtraCalib/ebaee5b1cde984d67970cccabb0beb1c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_84_1_TMp.root',
       '/store/user/akunsken/MuonGun2023NoExtraCalib/MuonGun2023NoExtraCalib/ebaee5b1cde984d67970cccabb0beb1c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_85_2_b0v.root',
       '/store/user/akunsken/MuonGun2023NoExtraCalib/MuonGun2023NoExtraCalib/ebaee5b1cde984d67970cccabb0beb1c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_86_1_eoY.root',
       '/store/user/akunsken/MuonGun2023NoExtraCalib/MuonGun2023NoExtraCalib/ebaee5b1cde984d67970cccabb0beb1c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_87_1_qfV.root',
       '/store/user/akunsken/MuonGun2023NoExtraCalib/MuonGun2023NoExtraCalib/ebaee5b1cde984d67970cccabb0beb1c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_88_1_TWN.root',
       '/store/user/akunsken/MuonGun2023NoExtraCalib/MuonGun2023NoExtraCalib/ebaee5b1cde984d67970cccabb0beb1c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_89_1_eSL.root',
       '/store/user/akunsken/MuonGun2023NoExtraCalib/MuonGun2023NoExtraCalib/ebaee5b1cde984d67970cccabb0beb1c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_8_1_TXD.root',
       '/store/user/akunsken/MuonGun2023NoExtraCalib/MuonGun2023NoExtraCalib/ebaee5b1cde984d67970cccabb0beb1c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_90_1_QZM.root',
       '/store/user/akunsken/MuonGun2023NoExtraCalib/MuonGun2023NoExtraCalib/ebaee5b1cde984d67970cccabb0beb1c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_91_1_gSI.root',
       '/store/user/akunsken/MuonGun2023NoExtraCalib/MuonGun2023NoExtraCalib/ebaee5b1cde984d67970cccabb0beb1c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_92_1_rHL.root',
       '/store/user/akunsken/MuonGun2023NoExtraCalib/MuonGun2023NoExtraCalib/ebaee5b1cde984d67970cccabb0beb1c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_93_1_JmS.root',
       '/store/user/akunsken/MuonGun2023NoExtraCalib/MuonGun2023NoExtraCalib/ebaee5b1cde984d67970cccabb0beb1c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_94_1_6sO.root',
       '/store/user/akunsken/MuonGun2023NoExtraCalib/MuonGun2023NoExtraCalib/ebaee5b1cde984d67970cccabb0beb1c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_95_1_TaB.root',
       '/store/user/akunsken/MuonGun2023NoExtraCalib/MuonGun2023NoExtraCalib/ebaee5b1cde984d67970cccabb0beb1c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_96_2_Yvy.root',
       '/store/user/akunsken/MuonGun2023NoExtraCalib/MuonGun2023NoExtraCalib/ebaee5b1cde984d67970cccabb0beb1c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_97_1_0AH.root',
       '/store/user/akunsken/MuonGun2023NoExtraCalib/MuonGun2023NoExtraCalib/ebaee5b1cde984d67970cccabb0beb1c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_99_1_d3L.root',
       '/store/user/akunsken/MuonGun2023NoExtraCalib/MuonGun2023NoExtraCalib/ebaee5b1cde984d67970cccabb0beb1c/SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_9_1_JQk.root' ] )


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
