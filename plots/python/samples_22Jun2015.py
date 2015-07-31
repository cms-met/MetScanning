#22Jun2015

localDir = "~/eos/cms/store/group/phys_jetmet/schoef/private0TSkim_22Jun2015"
EGamma    =   {'name':'EGamma', 'directories': [localDir+'/EGamma/crab_EGamma_Run2015A-PromptReco-v1_RECO/150622_154147/0000']}
Jet            = {'name':'Jet', 'directories': [localDir+'/Jet/crab_Jet_Run2015A-PromptReco-v1_RECO/150622_154018/0000']}
SingleMu  = {'name':'SingleMu', 'directories': [localDir+'/SingleMu/crab_SingleMu_Run2015A-PromptReco-v1_RECO/150622_154416/0000']}
ZeroBias1 = {'name':'ZeroBias1', 'directories':[localDir+'/ZeroBias1/crab_ZeroBias1_Run2015A-PromptReco-v1_RECO/150622_154201/0000']}
ZeroBias2 = {'name':'ZeroBias2', 'directories':[localDir+'/ZeroBias2/crab_ZeroBias2_Run2015A-PromptReco-v1_RECO/150622_154224/0000']}
ZeroBias3 = {'name':'ZeroBias3', 'directories':[localDir+'/ZeroBias3/crab_ZeroBias3_Run2015A-PromptReco-v1_RECO/150622_154248/0000']}
ZeroBias4 = {'name':'ZeroBias4', 'directories':[localDir+'/ZeroBias4/crab_ZeroBias4_Run2015A-PromptReco-v1_RECO/150622_154303/0000']}
ZeroBias5 = {'name':'ZeroBias5', 'directories':[localDir+'/ZeroBias5/crab_ZeroBias5_Run2015A-PromptReco-v1_RECO/150622_154317/0000']}
ZeroBias6 = {'name':'ZeroBias6', 'directories':[localDir+'/ZeroBias6/crab_ZeroBias6_Run2015A-PromptReco-v1_RECO/150622_154331/0000']}
ZeroBias7 = {'name':'ZeroBias7', 'directories':[localDir+'/ZeroBias7/crab_ZeroBias7_Run2015A-PromptReco-v1_RECO/150622_154346/0000']}
ZeroBias8 = {'name':'ZeroBias8', 'directories':[localDir+'/ZeroBias8/crab_ZeroBias8_Run2015A-PromptReco-v1_RECO/150622_154400/0000']}
zbd = []
for s in [ZeroBias1, ZeroBias2, ZeroBias3, ZeroBias4, ZeroBias5, ZeroBias6, ZeroBias7, ZeroBias8]:
  zbd.extend(s['directories'])
ZeroBias = {'name':'ZeroBias', 'directories':zbd}

#MC 0T
localDirMC = "~/eos/cms/store/relval"
minBias = {'name':'minBias', 'directories':[localDirMC+"/CMSSW_7_4_4/RelValMinBias_13/GEN-SIM-RECO/MCRUN2_740TV1_0Tv2-v1/00000/"]}

