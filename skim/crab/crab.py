from CRABClient.UserUtilities import config
#submit with 'python crab.py'
#Don't write to my directory (schoef), though

config = config()
config.General.requestName = 'ZeroBias1_Run2015A-PromptReco-v1_RECO'
config.General.workArea = '2015-06-12_runa_flat2'

config.JobType.outputFiles = ['tuple.root']
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = '../python/skim.py'

config.Data.inputDataset = '/ZeroBias1/Run2015A-PromptReco-v1/RECO'
config.Data.inputDBS = 'global'
config.Data.lumiMask = 'json_DCSONLY_150709_skim_v1.txt' 
config.Data.splitting = 'LumiBased'
config.Data.unitsPerJob = 15

config.Data.publication = False
#config.Data.outLFNDirBase = '' 
#config.Data.publishDataName = ''

config.Data.outLFNDirBase = '/store/user/cheidegg/METskims/2015-06-12_runa_flat'
config.Site.storageSite = 'T3_CH_PSI'

datasets=[
'/EGamma/Run2015A-PromptReco-v1/RECO',
'/Jet/Run2015A-PromptReco-v1/RECO',
'/ZeroBias1/Run2015A-PromptReco-v1/RECO',
'/ZeroBias2/Run2015A-PromptReco-v1/RECO',
'/ZeroBias3/Run2015A-PromptReco-v1/RECO',
'/ZeroBias4/Run2015A-PromptReco-v1/RECO',
'/ZeroBias5/Run2015A-PromptReco-v1/RECO',
'/ZeroBias6/Run2015A-PromptReco-v1/RECO',
'/ZeroBias7/Run2015A-PromptReco-v1/RECO',
'/ZeroBias8/Run2015A-PromptReco-v1/RECO',
'/SingleMu/Run2015A-PromptReco-v1/RECO'
]

if __name__ == '__main__':
    from CRABAPI.RawCommand import crabCommand
    for dataset in datasets:
        config.Data.inputDataset = dataset
        config.General.requestName = dataset.rstrip('/').lstrip('/').replace('/','_')
#        print config.General.requestName
        crabCommand('submit', config = config)
