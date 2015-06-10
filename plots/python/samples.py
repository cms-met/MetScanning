#mountPoint = "~/eos/cms/store/group/phys_jetmet/schoef/private0TSkim_v0/"

#EGamma    = {'name':'EGamma', 'directories':[mountPoint+'EGamma/crab_EGamma_Run2015A-PromptReco-v1_RECO/150608_144853/0000/']} 
#SingleMu  = {'name':'SingleMu', 'directories':[mountPoint+'/SingleMu/crab_SingleMu_Run2015A-PromptReco-v1_RECO/150608_145211/0000/']} #v0

#ZeroBias1 = {'name':'ZeroBias1', 'directories':[mountPoint+'/ZeroBias1/crab_ZeroBias1_Run2015A-PromptReco-v1_RECO/150608_144900/0000/']}
#ZeroBias2 = {'name':'ZeroBias2', 'directories':[mountPoint+'/ZeroBias2/crab_ZeroBias2_Run2015A-PromptReco-v1_RECO/150608_144908/0000/']}
#ZeroBias3 = {'name':'ZeroBias3', 'directories':[mountPoint+'/ZeroBias3/crab_ZeroBias3_Run2015A-PromptReco-v1_RECO/150608_145006/0000/']}
#ZeroBias4 = {'name':'ZeroBias4', 'directories':[mountPoint+'/ZeroBias4/crab_ZeroBias4_Run2015A-PromptReco-v1_RECO/150608_145013/0000/']}
#ZeroBias5 = {'name':'ZeroBias5', 'directories':[mountPoint+'/ZeroBias5/crab_ZeroBias5_Run2015A-PromptReco-v1_RECO/150608_145021/0000/']}
#ZeroBias6 = {'name':'ZeroBias6', 'directories':[mountPoint+'/ZeroBias6/crab_ZeroBias6_Run2015A-PromptReco-v1_RECO/150608_145028/0000/']}
#ZeroBias7 = {'name':'ZeroBias7', 'directories':[mountPoint+'/ZeroBias7/crab_ZeroBias7_Run2015A-PromptReco-v1_RECO/150608_145036/0000/']}
#ZeroBias8 = {'name':'ZeroBias8', 'directories':[mountPoint+'/ZeroBias8/crab_ZeroBias8_Run2015A-PromptReco-v1_RECO/150608_145043/0000/']}
#
#zbd = []
#for s in [ZeroBias1, ZeroBias2, ZeroBias3, ZeroBias4, ZeroBias5, ZeroBias6, ZeroBias7, ZeroBias8]:
#  zbd.extend(s['directories'])
#ZeroBias = {'name':'ZeroBias', 'directories':zbd}

mountPoint = "~/eos/cms/store/group/phys_jetmet/schoef/private0TSkim_v1/"
#EGamma    = {'name':'EGamma', 'directories':[mountPoint+'/EGamma/crab_EGamma_Run2015A-PromptReco-v1_RECO/150609_151643/0000/']} 
#SingleMu  = {'name':'SingleMu', 'directories':[mountPoint+'/SingleMu/crab_SingleMu_Run2015A-PromptReco-v1_RECO/150609_151929/0000/']}

#ZeroBias1 = {'name':'ZeroBias1', 'directories':[mountPoint+'/ZeroBias1/crab_ZeroBias1_Run2015A-PromptReco-v1_RECO/150609_151800/0000/']}
#ZeroBias2 = {'name':'ZeroBias2', 'directories':[mountPoint+'/ZeroBias2/crab_ZeroBias2_Run2015A-PromptReco-v1_RECO/150609_151834/0000/']}
ZeroBias3 = {'name':'ZeroBias3', 'directories':[mountPoint+'/ZeroBias3/crab_ZeroBias3_Run2015A-PromptReco-v1_RECO/150609_151841/0000/']}
#ZeroBias4 = {'name':'ZeroBias4', 'directories':[mountPoint+'/ZeroBias4/crab_ZeroBias4_Run2015A-PromptReco-v1_RECO/150609_151849/0000/']}
ZeroBias5 = {'name':'ZeroBias5', 'directories':[mountPoint+'/ZeroBias5/crab_ZeroBias5_Run2015A-PromptReco-v1_RECO/150609_151856/0000/']}
ZeroBias6 = {'name':'ZeroBias6', 'directories':[mountPoint+'/ZeroBias6/crab_ZeroBias6_Run2015A-PromptReco-v1_RECO/150609_151903/0000/']}
ZeroBias7 = {'name':'ZeroBias7', 'directories':[mountPoint+'/ZeroBias7/crab_ZeroBias7_Run2015A-PromptReco-v1_RECO/150609_151910/0000/']}
ZeroBias8 = {'name':'ZeroBias8', 'directories':[mountPoint+'/ZeroBias8/crab_ZeroBias8_Run2015A-PromptReco-v1_RECO/150609_151920/0000/']}

zbd = []
#for s in [ZeroBias1, ZeroBias2, ZeroBias3, ZeroBias4, ZeroBias5, ZeroBias6, ZeroBias7, ZeroBias8]:
for s in [ZeroBias3, ZeroBias5, ZeroBias6, ZeroBias7, ZeroBias8]:
  zbd.extend(s['directories'])
ZeroBias = {'name':'ZeroBias', 'directories':zbd}
