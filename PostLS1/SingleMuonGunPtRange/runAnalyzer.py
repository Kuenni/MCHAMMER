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
	'/store/user/akunsken/SingleMuonGunPtRangePostLS1/SingleMuPt1to100_cfi_GEN_SIM_DIGI_DIGI2RAW_RAW2DIGI_L1_L1Reco_8_5_U8q.root',
	'/store/user/akunsken/SingleMuonGunPtRangePostLS1/SingleMuPt1to100_cfi_GEN_SIM_DIGI_DIGI2RAW_RAW2DIGI_L1_L1Reco_9_5_Lvo.root',
	'/store/user/akunsken/SingleMuonGunPtRangePostLS1/SingleMuPt1to100_cfi_GEN_SIM_DIGI_DIGI2RAW_RAW2DIGI_L1_L1Reco_10_5_ZvP.root',
	'/store/user/akunsken/SingleMuonGunPtRangePostLS1/SingleMuPt1to100_cfi_GEN_SIM_DIGI_DIGI2RAW_RAW2DIGI_L1_L1Reco_51_2_lXN.root',
	'/store/user/akunsken/SingleMuonGunPtRangePostLS1/SingleMuPt1to100_cfi_GEN_SIM_DIGI_DIGI2RAW_RAW2DIGI_L1_L1Reco_63_2_vGy.root',
	'/store/user/akunsken/SingleMuonGunPtRangePostLS1/SingleMuPt1to100_cfi_GEN_SIM_DIGI_DIGI2RAW_RAW2DIGI_L1_L1Reco_64_5_dro.root',
	'/store/user/akunsken/SingleMuonGunPtRangePostLS1/SingleMuPt1to100_cfi_GEN_SIM_DIGI_DIGI2RAW_RAW2DIGI_L1_L1Reco_61_2_Frg.root',
	'/store/user/akunsken/SingleMuonGunPtRangePostLS1/SingleMuPt1to100_cfi_GEN_SIM_DIGI_DIGI2RAW_RAW2DIGI_L1_L1Reco_60_2_Or1.root',
	'/store/user/akunsken/SingleMuonGunPtRangePostLS1/SingleMuPt1to100_cfi_GEN_SIM_DIGI_DIGI2RAW_RAW2DIGI_L1_L1Reco_65_2_cvJ.root',
	'/store/user/akunsken/SingleMuonGunPtRangePostLS1/SingleMuPt1to100_cfi_GEN_SIM_DIGI_DIGI2RAW_RAW2DIGI_L1_L1Reco_59_2_Hl1.root',
	'/store/user/akunsken/SingleMuonGunPtRangePostLS1/SingleMuPt1to100_cfi_GEN_SIM_DIGI_DIGI2RAW_RAW2DIGI_L1_L1Reco_66_5_U6r.root',
	'/store/user/akunsken/SingleMuonGunPtRangePostLS1/SingleMuPt1to100_cfi_GEN_SIM_DIGI_DIGI2RAW_RAW2DIGI_L1_L1Reco_55_2_K1x.root',
	'/store/user/akunsken/SingleMuonGunPtRangePostLS1/SingleMuPt1to100_cfi_GEN_SIM_DIGI_DIGI2RAW_RAW2DIGI_L1_L1Reco_88_5_9KI.root',
	'/store/user/akunsken/SingleMuonGunPtRangePostLS1/SingleMuPt1to100_cfi_GEN_SIM_DIGI_DIGI2RAW_RAW2DIGI_L1_L1Reco_57_2_SG9.root',
	'/store/user/akunsken/SingleMuonGunPtRangePostLS1/SingleMuPt1to100_cfi_GEN_SIM_DIGI_DIGI2RAW_RAW2DIGI_L1_L1Reco_52_2_hLY.root',
	'/store/user/akunsken/SingleMuonGunPtRangePostLS1/SingleMuPt1to100_cfi_GEN_SIM_DIGI_DIGI2RAW_RAW2DIGI_L1_L1Reco_56_2_Nr4.root',
	'/store/user/akunsken/SingleMuonGunPtRangePostLS1/SingleMuPt1to100_cfi_GEN_SIM_DIGI_DIGI2RAW_RAW2DIGI_L1_L1Reco_6_5_M8N.root',
	'/store/user/akunsken/SingleMuonGunPtRangePostLS1/SingleMuPt1to100_cfi_GEN_SIM_DIGI_DIGI2RAW_RAW2DIGI_L1_L1Reco_5_5_uWO.root',
	'/store/user/akunsken/SingleMuonGunPtRangePostLS1/SingleMuPt1to100_cfi_GEN_SIM_DIGI_DIGI2RAW_RAW2DIGI_L1_L1Reco_4_5_nd9.root',
	'/store/user/akunsken/SingleMuonGunPtRangePostLS1/SingleMuPt1to100_cfi_GEN_SIM_DIGI_DIGI2RAW_RAW2DIGI_L1_L1Reco_3_5_zWb.root',
	'/store/user/akunsken/SingleMuonGunPtRangePostLS1/SingleMuPt1to100_cfi_GEN_SIM_DIGI_DIGI2RAW_RAW2DIGI_L1_L1Reco_2_5_jYu.root',
	'/store/user/akunsken/SingleMuonGunPtRangePostLS1/SingleMuPt1to100_cfi_GEN_SIM_DIGI_DIGI2RAW_RAW2DIGI_L1_L1Reco_7_5_PcN.root',
	'/store/user/akunsken/SingleMuonGunPtRangePostLS1/SingleMuPt1to100_cfi_GEN_SIM_DIGI_DIGI2RAW_RAW2DIGI_L1_L1Reco_13_5_jML.root',
	'/store/user/akunsken/SingleMuonGunPtRangePostLS1/SingleMuPt1to100_cfi_GEN_SIM_DIGI_DIGI2RAW_RAW2DIGI_L1_L1Reco_11_5_Wec.root',
	'/store/user/akunsken/SingleMuonGunPtRangePostLS1/SingleMuPt1to100_cfi_GEN_SIM_DIGI_DIGI2RAW_RAW2DIGI_L1_L1Reco_12_5_pxr.root',
	'/store/user/akunsken/SingleMuonGunPtRangePostLS1/SingleMuPt1to100_cfi_GEN_SIM_DIGI_DIGI2RAW_RAW2DIGI_L1_L1Reco_14_5_wzP.root',
	'/store/user/akunsken/SingleMuonGunPtRangePostLS1/SingleMuPt1to100_cfi_GEN_SIM_DIGI_DIGI2RAW_RAW2DIGI_L1_L1Reco_15_5_qfF.root',
	'/store/user/akunsken/SingleMuonGunPtRangePostLS1/SingleMuPt1to100_cfi_GEN_SIM_DIGI_DIGI2RAW_RAW2DIGI_L1_L1Reco_28_5_93a.root',
	'/store/user/akunsken/SingleMuonGunPtRangePostLS1/SingleMuPt1to100_cfi_GEN_SIM_DIGI_DIGI2RAW_RAW2DIGI_L1_L1Reco_16_5_47K.root',
	'/store/user/akunsken/SingleMuonGunPtRangePostLS1/SingleMuPt1to100_cfi_GEN_SIM_DIGI_DIGI2RAW_RAW2DIGI_L1_L1Reco_29_5_Esu.root',
	'/store/user/akunsken/SingleMuonGunPtRangePostLS1/SingleMuPt1to100_cfi_GEN_SIM_DIGI_DIGI2RAW_RAW2DIGI_L1_L1Reco_27_5_OXa.root',
	'/store/user/akunsken/SingleMuonGunPtRangePostLS1/SingleMuPt1to100_cfi_GEN_SIM_DIGI_DIGI2RAW_RAW2DIGI_L1_L1Reco_20_5_iR9.root',
	'/store/user/akunsken/SingleMuonGunPtRangePostLS1/SingleMuPt1to100_cfi_GEN_SIM_DIGI_DIGI2RAW_RAW2DIGI_L1_L1Reco_50_5_E5i.root',
	'/store/user/akunsken/SingleMuonGunPtRangePostLS1/SingleMuPt1to100_cfi_GEN_SIM_DIGI_DIGI2RAW_RAW2DIGI_L1_L1Reco_33_2_ti9.root',
	'/store/user/akunsken/SingleMuonGunPtRangePostLS1/SingleMuPt1to100_cfi_GEN_SIM_DIGI_DIGI2RAW_RAW2DIGI_L1_L1Reco_26_5_9ve.root',
	'/store/user/akunsken/SingleMuonGunPtRangePostLS1/SingleMuPt1to100_cfi_GEN_SIM_DIGI_DIGI2RAW_RAW2DIGI_L1_L1Reco_19_5_qIb.root',
	'/store/user/akunsken/SingleMuonGunPtRangePostLS1/SingleMuPt1to100_cfi_GEN_SIM_DIGI_DIGI2RAW_RAW2DIGI_L1_L1Reco_17_5_5gb.root',
	'/store/user/akunsken/SingleMuonGunPtRangePostLS1/SingleMuPt1to100_cfi_GEN_SIM_DIGI_DIGI2RAW_RAW2DIGI_L1_L1Reco_18_5_GKu.root',
	'/store/user/akunsken/SingleMuonGunPtRangePostLS1/SingleMuPt1to100_cfi_GEN_SIM_DIGI_DIGI2RAW_RAW2DIGI_L1_L1Reco_24_5_O1q.root',
	'/store/user/akunsken/SingleMuonGunPtRangePostLS1/SingleMuPt1to100_cfi_GEN_SIM_DIGI_DIGI2RAW_RAW2DIGI_L1_L1Reco_21_5_4Tj.root',
	'/store/user/akunsken/SingleMuonGunPtRangePostLS1/SingleMuPt1to100_cfi_GEN_SIM_DIGI_DIGI2RAW_RAW2DIGI_L1_L1Reco_25_5_bRZ.root',
	'/store/user/akunsken/SingleMuonGunPtRangePostLS1/SingleMuPt1to100_cfi_GEN_SIM_DIGI_DIGI2RAW_RAW2DIGI_L1_L1Reco_23_5_GEe.root',
	'/store/user/akunsken/SingleMuonGunPtRangePostLS1/SingleMuPt1to100_cfi_GEN_SIM_DIGI_DIGI2RAW_RAW2DIGI_L1_L1Reco_22_5_P1h.root',
	'/store/user/akunsken/SingleMuonGunPtRangePostLS1/SingleMuPt1to100_cfi_GEN_SIM_DIGI_DIGI2RAW_RAW2DIGI_L1_L1Reco_30_5_oSV.root',
	'/store/user/akunsken/SingleMuonGunPtRangePostLS1/SingleMuPt1to100_cfi_GEN_SIM_DIGI_DIGI2RAW_RAW2DIGI_L1_L1Reco_1_4_qkE.root',
	'/store/user/akunsken/SingleMuonGunPtRangePostLS1/SingleMuPt1to100_cfi_GEN_SIM_DIGI_DIGI2RAW_RAW2DIGI_L1_L1Reco_98_3_NE9.root',
	'/store/user/akunsken/SingleMuonGunPtRangePostLS1/SingleMuPt1to100_cfi_GEN_SIM_DIGI_DIGI2RAW_RAW2DIGI_L1_L1Reco_100_3_zqA.root',
	'/store/user/akunsken/SingleMuonGunPtRangePostLS1/SingleMuPt1to100_cfi_GEN_SIM_DIGI_DIGI2RAW_RAW2DIGI_L1_L1Reco_94_3_DEm.root',
	'/store/user/akunsken/SingleMuonGunPtRangePostLS1/SingleMuPt1to100_cfi_GEN_SIM_DIGI_DIGI2RAW_RAW2DIGI_L1_L1Reco_95_1_zRw.root',
	'/store/user/akunsken/SingleMuonGunPtRangePostLS1/SingleMuPt1to100_cfi_GEN_SIM_DIGI_DIGI2RAW_RAW2DIGI_L1_L1Reco_84_1_r6h.root',
	'/store/user/akunsken/SingleMuonGunPtRangePostLS1/SingleMuPt1to100_cfi_GEN_SIM_DIGI_DIGI2RAW_RAW2DIGI_L1_L1Reco_71_1_Mkb.root',
	'/store/user/akunsken/SingleMuonGunPtRangePostLS1/SingleMuPt1to100_cfi_GEN_SIM_DIGI_DIGI2RAW_RAW2DIGI_L1_L1Reco_53_1_e6a.root',
	'/store/user/akunsken/SingleMuonGunPtRangePostLS1/SingleMuPt1to100_cfi_GEN_SIM_DIGI_DIGI2RAW_RAW2DIGI_L1_L1Reco_35_1_Q9T.root',
	'/store/user/akunsken/SingleMuonGunPtRangePostLS1/SingleMuPt1to100_cfi_GEN_SIM_DIGI_DIGI2RAW_RAW2DIGI_L1_L1Reco_92_1_YDx.root',
	'/store/user/akunsken/SingleMuonGunPtRangePostLS1/SingleMuPt1to100_cfi_GEN_SIM_DIGI_DIGI2RAW_RAW2DIGI_L1_L1Reco_48_1_eYp.root',
	'/store/user/akunsken/SingleMuonGunPtRangePostLS1/SingleMuPt1to100_cfi_GEN_SIM_DIGI_DIGI2RAW_RAW2DIGI_L1_L1Reco_49_1_l24.root',
	'/store/user/akunsken/SingleMuonGunPtRangePostLS1/SingleMuPt1to100_cfi_GEN_SIM_DIGI_DIGI2RAW_RAW2DIGI_L1_L1Reco_47_1_iQr.root',
	'/store/user/akunsken/SingleMuonGunPtRangePostLS1/SingleMuPt1to100_cfi_GEN_SIM_DIGI_DIGI2RAW_RAW2DIGI_L1_L1Reco_38_1_M9P.root',
	'/store/user/akunsken/SingleMuonGunPtRangePostLS1/SingleMuPt1to100_cfi_GEN_SIM_DIGI_DIGI2RAW_RAW2DIGI_L1_L1Reco_41_1_t7c.root',
	'/store/user/akunsken/SingleMuonGunPtRangePostLS1/SingleMuPt1to100_cfi_GEN_SIM_DIGI_DIGI2RAW_RAW2DIGI_L1_L1Reco_45_1_ohS.root',
	'/store/user/akunsken/SingleMuonGunPtRangePostLS1/SingleMuPt1to100_cfi_GEN_SIM_DIGI_DIGI2RAW_RAW2DIGI_L1_L1Reco_40_1_CDD.root',
	'/store/user/akunsken/SingleMuonGunPtRangePostLS1/SingleMuPt1to100_cfi_GEN_SIM_DIGI_DIGI2RAW_RAW2DIGI_L1_L1Reco_37_1_tjz.root',
	'/store/user/akunsken/SingleMuonGunPtRangePostLS1/SingleMuPt1to100_cfi_GEN_SIM_DIGI_DIGI2RAW_RAW2DIGI_L1_L1Reco_39_1_NrQ.root',
	'/store/user/akunsken/SingleMuonGunPtRangePostLS1/SingleMuPt1to100_cfi_GEN_SIM_DIGI_DIGI2RAW_RAW2DIGI_L1_L1Reco_36_1_chO.root',
	'/store/user/akunsken/SingleMuonGunPtRangePostLS1/SingleMuPt1to100_cfi_GEN_SIM_DIGI_DIGI2RAW_RAW2DIGI_L1_L1Reco_42_1_5bQ.root',
	'/store/user/akunsken/SingleMuonGunPtRangePostLS1/SingleMuPt1to100_cfi_GEN_SIM_DIGI_DIGI2RAW_RAW2DIGI_L1_L1Reco_34_1_caM.root',
	'/store/user/akunsken/SingleMuonGunPtRangePostLS1/SingleMuPt1to100_cfi_GEN_SIM_DIGI_DIGI2RAW_RAW2DIGI_L1_L1Reco_90_1_oaz.root',
	'/store/user/akunsken/SingleMuonGunPtRangePostLS1/SingleMuPt1to100_cfi_GEN_SIM_DIGI_DIGI2RAW_RAW2DIGI_L1_L1Reco_72_1_UBg.root',
	'/store/user/akunsken/SingleMuonGunPtRangePostLS1/SingleMuPt1to100_cfi_GEN_SIM_DIGI_DIGI2RAW_RAW2DIGI_L1_L1Reco_97_1_NpB.root',
	'/store/user/akunsken/SingleMuonGunPtRangePostLS1/SingleMuPt1to100_cfi_GEN_SIM_DIGI_DIGI2RAW_RAW2DIGI_L1_L1Reco_73_1_Xci.root',
	'/store/user/akunsken/SingleMuonGunPtRangePostLS1/SingleMuPt1to100_cfi_GEN_SIM_DIGI_DIGI2RAW_RAW2DIGI_L1_L1Reco_62_1_T3U.root',
	'/store/user/akunsken/SingleMuonGunPtRangePostLS1/SingleMuPt1to100_cfi_GEN_SIM_DIGI_DIGI2RAW_RAW2DIGI_L1_L1Reco_46_1_59f.root',
	'/store/user/akunsken/SingleMuonGunPtRangePostLS1/SingleMuPt1to100_cfi_GEN_SIM_DIGI_DIGI2RAW_RAW2DIGI_L1_L1Reco_67_1_Rpr.root',
	'/store/user/akunsken/SingleMuonGunPtRangePostLS1/SingleMuPt1to100_cfi_GEN_SIM_DIGI_DIGI2RAW_RAW2DIGI_L1_L1Reco_91_1_DSm.root',
	'/store/user/akunsken/SingleMuonGunPtRangePostLS1/SingleMuPt1to100_cfi_GEN_SIM_DIGI_DIGI2RAW_RAW2DIGI_L1_L1Reco_58_1_dvk.root',
	'/store/user/akunsken/SingleMuonGunPtRangePostLS1/SingleMuPt1to100_cfi_GEN_SIM_DIGI_DIGI2RAW_RAW2DIGI_L1_L1Reco_85_1_3uO.root',
	'/store/user/akunsken/SingleMuonGunPtRangePostLS1/SingleMuPt1to100_cfi_GEN_SIM_DIGI_DIGI2RAW_RAW2DIGI_L1_L1Reco_93_1_zvh.root',
	'/store/user/akunsken/SingleMuonGunPtRangePostLS1/SingleMuPt1to100_cfi_GEN_SIM_DIGI_DIGI2RAW_RAW2DIGI_L1_L1Reco_89_1_W7v.root',
	'/store/user/akunsken/SingleMuonGunPtRangePostLS1/SingleMuPt1to100_cfi_GEN_SIM_DIGI_DIGI2RAW_RAW2DIGI_L1_L1Reco_99_1_5Yd.root',
	'/store/user/akunsken/SingleMuonGunPtRangePostLS1/SingleMuPt1to100_cfi_GEN_SIM_DIGI_DIGI2RAW_RAW2DIGI_L1_L1Reco_69_1_xG2.root',
	'/store/user/akunsken/SingleMuonGunPtRangePostLS1/SingleMuPt1to100_cfi_GEN_SIM_DIGI_DIGI2RAW_RAW2DIGI_L1_L1Reco_96_1_2nB.root',
	'/store/user/akunsken/SingleMuonGunPtRangePostLS1/SingleMuPt1to100_cfi_GEN_SIM_DIGI_DIGI2RAW_RAW2DIGI_L1_L1Reco_82_1_DDw.root',
	'/store/user/akunsken/SingleMuonGunPtRangePostLS1/SingleMuPt1to100_cfi_GEN_SIM_DIGI_DIGI2RAW_RAW2DIGI_L1_L1Reco_79_1_k97.root',
	'/store/user/akunsken/SingleMuonGunPtRangePostLS1/SingleMuPt1to100_cfi_GEN_SIM_DIGI_DIGI2RAW_RAW2DIGI_L1_L1Reco_70_1_TvO.root',
	'/store/user/akunsken/SingleMuonGunPtRangePostLS1/SingleMuPt1to100_cfi_GEN_SIM_DIGI_DIGI2RAW_RAW2DIGI_L1_L1Reco_77_1_rMH.root',
	'/store/user/akunsken/SingleMuonGunPtRangePostLS1/SingleMuPt1to100_cfi_GEN_SIM_DIGI_DIGI2RAW_RAW2DIGI_L1_L1Reco_76_1_FZ7.root',
	'/store/user/akunsken/SingleMuonGunPtRangePostLS1/SingleMuPt1to100_cfi_GEN_SIM_DIGI_DIGI2RAW_RAW2DIGI_L1_L1Reco_86_1_nwx.root',
	'/store/user/akunsken/SingleMuonGunPtRangePostLS1/SingleMuPt1to100_cfi_GEN_SIM_DIGI_DIGI2RAW_RAW2DIGI_L1_L1Reco_44_1_eOn.root',
	'/store/user/akunsken/SingleMuonGunPtRangePostLS1/SingleMuPt1to100_cfi_GEN_SIM_DIGI_DIGI2RAW_RAW2DIGI_L1_L1Reco_81_1_nc3.root',
	'/store/user/akunsken/SingleMuonGunPtRangePostLS1/SingleMuPt1to100_cfi_GEN_SIM_DIGI_DIGI2RAW_RAW2DIGI_L1_L1Reco_68_1_ejl.root',
	'/store/user/akunsken/SingleMuonGunPtRangePostLS1/SingleMuPt1to100_cfi_GEN_SIM_DIGI_DIGI2RAW_RAW2DIGI_L1_L1Reco_83_1_HBm.root',
	'/store/user/akunsken/SingleMuonGunPtRangePostLS1/SingleMuPt1to100_cfi_GEN_SIM_DIGI_DIGI2RAW_RAW2DIGI_L1_L1Reco_74_1_TmQ.root',
	'/store/user/akunsken/SingleMuonGunPtRangePostLS1/SingleMuPt1to100_cfi_GEN_SIM_DIGI_DIGI2RAW_RAW2DIGI_L1_L1Reco_87_1_Rnr.root',
	'/store/user/akunsken/SingleMuonGunPtRangePostLS1/SingleMuPt1to100_cfi_GEN_SIM_DIGI_DIGI2RAW_RAW2DIGI_L1_L1Reco_32_1_gSK.root',
	'/store/user/akunsken/SingleMuonGunPtRangePostLS1/SingleMuPt1to100_cfi_GEN_SIM_DIGI_DIGI2RAW_RAW2DIGI_L1_L1Reco_43_1_yjR.root',
	'/store/user/akunsken/SingleMuonGunPtRangePostLS1/SingleMuPt1to100_cfi_GEN_SIM_DIGI_DIGI2RAW_RAW2DIGI_L1_L1Reco_54_1_e3f.root',
	'/store/user/akunsken/SingleMuonGunPtRangePostLS1/SingleMuPt1to100_cfi_GEN_SIM_DIGI_DIGI2RAW_RAW2DIGI_L1_L1Reco_78_1_v9r.root',
	'/store/user/akunsken/SingleMuonGunPtRangePostLS1/SingleMuPt1to100_cfi_GEN_SIM_DIGI_DIGI2RAW_RAW2DIGI_L1_L1Reco_31_1_j6r.root',
	'/store/user/akunsken/SingleMuonGunPtRangePostLS1/SingleMuPt1to100_cfi_GEN_SIM_DIGI_DIGI2RAW_RAW2DIGI_L1_L1Reco_80_1_Abn.root',
	'/store/user/akunsken/SingleMuonGunPtRangePostLS1/SingleMuPt1to100_cfi_GEN_SIM_DIGI_DIGI2RAW_RAW2DIGI_L1_L1Reco_75_1_x2O.root'
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
