from CRABClient.UserUtilities import config
#submit with 'python crab.py'
#Don't write to my directory (schoef), though

config = config()
config.General.requestName = 'ZeroBias1_Run2015A-PromptReco-v1_RECO'
config.General.workArea = 'private0TSkim_30Jun2015'

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = '../python/skim_0T.py'

config.Data.inputDataset = '/ZeroBias1/Run2015A-PromptReco-v1/RECO'
config.Data.inputDBS = 'global'
#config.Data.lumiMask = 'json/Cert_246908-247381_13TeV_PromptReco_Collisions15_ZeroTesla_JSON.txt' 
config.Data.lumiMask = 'json/Cert_246908-248038_13TeV_PromptReco_Collisions15_ZeroTesla_JSON_CaloOnly.txt' 
config.Data.splitting = 'LumiBased'
config.Data.unitsPerJob = 5

config.Data.publication = False
#config.Data.outLFNDirBase = '' 
#config.Data.publishDataName = ''

config.Data.outLFNDirBase = '/store/group/phys_jetmet/schoef/private0TSkim_30Jun2015/'
config.Site.storageSite = 'T2_CH_CERN'

datasets=[
'/MET/Run2015A-PromptReco-v1/RECO',
'/HighMultiplicity/Run2015A-PromptReco-v1/RECO',
'/Jet/Run2015A-PromptReco-v1/RECO',
'/JetHT/Run2015A-PromptReco-v1/RECO',
'/SingleElectron/Run2015A-PromptReco-v1/RECO',
'/SinglePhoton/Run2015A-PromptReco-v1/RECO',
'/BTagCSV/Run2015A-PromptReco-v1/RECO',
'/BTagMu/Run2015A-PromptReco-v1/RECO',
'/EGamma/Run2015A-PromptReco-v1/RECO',
'/ZeroBias1/Run2015A-PromptReco-v1/RECO',
'/ZeroBias2/Run2015A-PromptReco-v1/RECO',
'/ZeroBias3/Run2015A-PromptReco-v1/RECO',
#'/ZeroBias4/Run2015A-PromptReco-v1/RECO',
#'/ZeroBias5/Run2015A-PromptReco-v1/RECO',
#'/ZeroBias6/Run2015A-PromptReco-v1/RECO',
#'/ZeroBias7/Run2015A-PromptReco-v1/RECO',
#'/ZeroBias8/Run2015A-PromptReco-v1/RECO',
#'/SingleMu/Run2015A-PromptReco-v1/RECO',
]

if __name__ == '__main__':
    from CRABAPI.RawCommand import crabCommand
    for dataset in datasets:
        config.Data.inputDataset = dataset
        config.General.requestName = dataset.rstrip('/').lstrip('/').replace('/','_')
#        print config.General.requestName
        crabCommand('submit', config = config)
