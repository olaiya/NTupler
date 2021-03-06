from CRABClient.UserUtilities import config
config = config()

config.General.requestName = 'ww_nTuple_production'
config.General.workArea = 'crab_projects'

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'nTupleProduction.py'

config.Data.inputDataset = '/WW_TuneCUETP8M1_13TeV-pythia8/RunIISpring15DR74-Asympt50ns_MCRUN2_74_V9A-v1/MINIAODSIM'
config.Data.inputDBS = 'global'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 10
config.Data.outLFNDirBase = '/store/user/olaiya/NTuples/WW' #Wherever you want the ntuples to go on the RAL T2
config.Data.publication = False
config.Data.publishDataName = 'RAL_nTuple_PROD'

config.Site.storageSite = 'T2_UK_SGrid_RALPP'
