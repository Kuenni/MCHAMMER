from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()

config.General.requestName = 'noBMuPlus'
config.General.workArea = 'crab_projects'
config.General.transferOutputs = True
config.General.transferLogs = False

config.User.voGroup = 'dcms'

config.JobType.pluginName = 'PrivateMC'
config.JobType.psetName = 'SingleMuPt5to200_cfi_GEN_SIM_DIGI_DIGI2RAW_RAW2DIGI_L1_L1Reco_Reco.py'
config.JobType.maxMemoryMB = 2500

config.Data.splitting = 'EventBased'
config.Data.unitsPerJob = 1000
NJOBS = 100  # This is not a configuration parameter, but an auxiliary variable that we use in the next line.
config.Data.totalUnits = config.Data.unitsPerJob * NJOBS
config.Data.outLFNDirBase = '/store/user/%s/SingleMuPlus' % (getUsernameFromSiteDB())
config.Data.publication = False
config.Site.storageSite = 'T2_DE_RWTH'
