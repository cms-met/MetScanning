from CRABClient.UserUtilities import config
#submit with 'python crab.py'
#Don't write to my directory (schoef), though

config = config()
config.General.requestName = 'ZeroBias1_Run2015A-PromptReco-v1_RECO'
config.General.workArea = '/afs/cern.ch/work/c/cheidegg/crab3/2015-07-03_filters_runa_flat'

config.JobType.outputFiles = ['tuple.root']
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = '../python/skim.py'

config.Data.inputDataset = '/ZeroBias1/Run2015A-PromptReco-v1/RECO'
config.Data.inputDBS = 'global'
#config.Data.lumiMask = 'json/json_DCSONLY_150710_skim_v3.txt' 
#config.Data.lumiMask = 'json/Cert_246908-247381_13TeV_PromptReco_Collisions15_ZeroTesla_JSON_CaloOnly.txt' 
#config.Data.lumiMask = 'json/Cert_246908-247381_13TeV_PromptReco_Collisions15_ZeroTesla_JSON.txt' ## released 12th June
#config.Data.lumiMask = 'json/Cert_246908-248005_13TeV_PromptReco_Collisions15_ZeroTesla_JSON_CaloOnly.txt' ## released 22th June
#config.Data.lumiMask = 'json/Cert_246908-248005_13TeV_PromptReco_Collisions15_ZeroTesla_JSON.txt' ## certified, released 23th June
#config.Data.lumiMask = 'json/Cert_246908-248038_13TeV_PromptReco_Collisions15_ZeroTesla_JSON_CaloOnly.txt' ## certified, released 29th June 
config.Data.lumiMask = 'json/Cert_246908-248038_13TeV_PromptReco_Collisions15_ZeroTesla_JSON.txt' ## certified, released 29th June
config.Data.splitting = 'LumiBased'
config.Data.unitsPerJob = 10

config.Data.publication = False
#config.Data.outLFNDirBase = '' 
#config.Data.publishDataName = ''

config.Data.outLFNDirBase = '/store/user/cheidegg/crab3/2015-07-03_filters_runa_flat'
config.Site.storageSite = 'T3_CH_PSI'

datasets=[
#'/BTagCSV/Run2015A-PromptReco-v1/RECO',
#'/BTagMu/Run2015A-PromptReco-v1/RECO',
#'/Charmonium/Run2015A-PromptReco-v1/RECO',
#'/Commissioning/Run2015A-PromptReco-v1/RECO',
#'/DisplacedJet/Run2015A-PromptReco-v1/RECO',
#'/DoubleEG/Run2015A-PromptReco-v1/RECO',
#'/DoubleMuon/Run2015A-PromptReco-v1/RECO',
#'/DoubleMuonLowMass/Run2015A-PromptReco-v1/RECO',
#'/HLTPhysics/Run2015A-PromptReco-v1/RECO',
#'/HTMHT/Run2015A-PromptReco-v1/RECO',
#'/HcalHPDNoise/Run2015A-PromptReco-v1/RECO',
#'/HcalNZS/Run2015A-PromptReco-v1/RECO',
#'/JetHT/Run2015A-PromptReco-v1/RECO',
#'/MET/Run2015A-PromptReco-v1/RECO',
#'/MuOnia/Run2015A-PromptReco-v1/RECO',
#'/MuonEG/Run2015A-PromptReco-v1/RECO',
#'/NoBPTX/Run2015A-PromptReco-v1/RECO',
#'/SingleElectron/Run2015A-PromptReco-v1/RECO',
#'/SingleMuon/Run2015A-PromptReco-v1/RECO',
#'/SinglePhoton/Run2015A-PromptReco-v1/RECO',
#'/Tau/Run2015A-PromptReco-v1/RECO',
#'/ZeroBias/Run2015A-PromptReco-v1/RECO',

#'/EGamma/Run2015A-PromptReco-v1/RECO',
#'/HighMultiplicity/Run2015A-PromptReco-v1/RECO',
#'/Jet/Run2015A-PromptReco-v1/RECO',
'/SingleMu/Run2015A-PromptReco-v1/RECO',
'/ZeroBias1/Run2015A-PromptReco-v1/RECO',
'/ZeroBias2/Run2015A-PromptReco-v1/RECO',
'/ZeroBias3/Run2015A-PromptReco-v1/RECO',
'/ZeroBias4/Run2015A-PromptReco-v1/RECO',
'/ZeroBias5/Run2015A-PromptReco-v1/RECO',
'/ZeroBias6/Run2015A-PromptReco-v1/RECO',
'/ZeroBias7/Run2015A-PromptReco-v1/RECO',
'/ZeroBias8/Run2015A-PromptReco-v1/RECO',
]

if __name__ == '__main__':
    from CRABAPI.RawCommand import crabCommand
    for dataset in datasets:
        config.Data.inputDataset = dataset
        config.General.requestName = dataset.rstrip('/').lstrip('/').replace('/','_')
#        print config.General.requestName
        crabCommand('submit', config = config)
