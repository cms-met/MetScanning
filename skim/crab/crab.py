from CRABClient.UserUtilities import config, getUsernameFromSiteDB
#submit with 'python crab.py'
#Don't write to my directory (schoef), though

config = config()
config.General.requestName = 'ExpressPhysics_Run2016B-Express-v1_FEVT'  #'ZeroBias1_Run2015A-PromptReco-v1_RECO'
config.General.workArea =  'Run2016B_int/MET/' # 'private4TSkim_24Jul2015_update'
config.General.transferOutputs = True
config.General.transferLogs = True

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = '../python/skim.py'
config.JobType.outputFiles = ['tuple.root']
config.Data.inputDataset = '/ExpressPhysics/Run2016B-Express-v1/FEVT'  #'/ZeroBias1/Run2015A-PromptReco-v1/RECO'
config.Data.inputDBS = 'global'
config.Data.lumiMask =  'https://cms-service-dqm.web.cern.ch/cms-service-dqm/CAF/certification/Collisions16/13TeV/DCSOnly/json_DCSONLY.txt' #'json/Cert_251562-251883_13TeV_PromptReco_Collisions15_JSON_UPDATEONLY.txt'
config.Data.splitting = 'LumiBased'
config.Data.unitsPerJob = 10
config.Data.runRange = '272818'
config.Data.publication = False

#config.Data.ignoreLocality = True                                                                                                                                                                       
#config.Site.whitelist = ['T1_US_FNAL'] 

#config.Data.outLFNDirBase = '' 
#config.Data.publishDataName = ''

config.Data.outLFNDirBase = '/store/user/%s/' % (getUsernameFromSiteDB())  #'/store/group/phys_jetmet/beranek/private4TSkim_24Jul2015_update/'
config.Site.storageSite = 'T2_DE_DESY'

'''
datasets=[
'/ExpressPhysics/Run2015B-Express-v1/FEVT',
'/ZeroBias1/Run2015B-PromptReco-v1/RECO',
'/ZeroBias2/Run2015B-PromptReco-v1/RECO',
'/ZeroBias3/Run2015B-PromptReco-v1/RECO',
'/ZeroBias4/Run2015B-PromptReco-v1/RECO',
'/ZeroBias5/Run2015B-PromptReco-v1/RECO',
'/ZeroBias6/Run2015B-PromptReco-v1/RECO',
'/ZeroBias7/Run2015B-PromptReco-v1/RECO',
'/ZeroBias8/Run2015B-PromptReco-v1/RECO',
'/EGamma/Run2015B-PromptReco-v1/RECO',
'/Jet/Run2015B-PromptReco-v1/RECO',
'/JetHT/Run2015B-PromptReco-v1/RECO',
'/MinimumBias/Run2015B-PromptReco-v1/RECO',
'/HTMHT/Run2015B-PromptReco-v1/RECO',
'/SingleMu/Run2015B-PromptReco-v1/RECO',
'/SingleMuon/Run2015B-PromptReco-v1/RECO',
'/DoubleEG/Run2015B-PromptReco-v1/RECO',
'/DoubleMuon/Run2015B-PromptReco-v1/RECO',
'/HighMultiplicity/Run2015B-PromptReco-v1/RECO',
'/MET/Run2015B-PromptReco-v1/RECO',
'/SingleElectron/Run2015B-PromptReco-v1/RECO',
'/SinglePhoton/Run2015B-PromptReco-v1/RECO',
'/Tau/Run2015B-PromptReco-v1/RECO',
]

if __name__ == '__main__':
    from CRABAPI.RawCommand import crabCommand
    for dataset in datasets:
        config.Data.inputDataset = dataset
        config.General.requestName = dataset.rstrip('/').lstrip('/').replace('/','_')
#        print config.General.requestName
        crabCommand('submit', config = config)
'''
