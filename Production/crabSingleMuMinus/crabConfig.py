from WMCore.Configuration import Configuration
config = Configuration()
config.section_('General')
config.General.transferOutputs = True
config.section_('JobType')
config.JobType.psetName = 'SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_L1Reco_RECO.py'
config.JobType.pluginName = 'privateMC'
config.JobType.outputFiles = ['SingleMuPt100_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_L1Reco_RECO.root']
config.section_('Data')
config.Data.outputDatasetTag = 'SingleMuonGunPostLS1_VtxZero'
config.Data.totalUnits = 2000000
config.Data.unitsPerJob = 10000
config.Data.splitting = 'EventBased'
config.Data.publication = False
config.section_('User')
config.section_('Site')
config.Site.storageSite = 'T2_DE_RWTH'
