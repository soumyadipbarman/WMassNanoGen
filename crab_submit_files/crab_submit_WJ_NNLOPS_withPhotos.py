from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()

config.General.requestName = 'WplusJToMuNu_TuneCUETP8M1_13TeV-powheg-NNLOPS-pythia8-photosFix'
config.General.workArea = 'crab_projects'
config.General.transferOutputs = True
config.General.transferLogs = True

config.JobType.pluginName = 'PrivateMC'
config.JobType.psetName = '../configs/WJ_NNLOPS_withPhotos_cfg.py'

config.Data.outputPrimaryDataset = 'WplusJToMuNu_TuneCUETP8M1_13TeV-powheg-NNLOPS-pythia8-photosFix'
config.Data.splitting = 'EventBased'
config.Data.unitsPerJob = 400
NJOBS = 7000  # This is not a configuration parameter, but an auxiliary variable that we use in the next line.
config.Data.totalUnits = config.Data.unitsPerJob * NJOBS
config.Data.outLFNDirBase = '/store/user/%s/' % (getUsernameFromSiteDB())
config.Data.publication = True
config.Data.outputDatasetTag = 'RunIISummer15wmLHEGS'

config.Site.storageSite = 'T2_CH_CERN'
