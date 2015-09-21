# MetScanning



for RunD analysis you need to install the CMSSW_7_4_12 while for the runA/B/C the CMSSW_7_4_7
for the CMSSW_7_4_12 need to use the branch cms-met:HaloBranch7412
```
scramv1 project -n CMSSW_7_4_7_scanningHalo CMSSW CMSSW_7_4_7
cd CMSSW_7_4_7_scanningHalo/src
cmsenv
alias git 'git --exec-path=/cvmfs/cms.cern.ch/slc6_amd64_gcc491/external/git/1.8.3.1-odfocd/libexec/git-core/'
git cms-init
echo  DataFormats/METReco > .git/info/sparse-checkout
echo  PhysicsTools/PatAlgos/ >> .git/info/sparse-checkout
echo  RecoMET/METAlgorithms/ >> .git/info/sparse-checkout
echo  RecoMET/METFilters/ >> .git/info/sparse-checkout
echo  RecoMET/METProducers >> .git/info/sparse-checkout
git cms-merge-topic -u cms-met:HaloBranch747
git clone git@github.com:cms-met/MetScanning
scramv1 b -j 20

```


There are three new filters to be added to skim_4T.py:
```                                                                                  
process.load('RecoMET.METFilters.CSCTightHalo2015Filter_cfi')
process.CSCTightHalo2015Filter.taggingMode = cms.bool(True)
process.load('RecoMET.METFilters.CSCTightHaloTrkMuUnvetoFilter_cfi')
process.CSCTightHaloTrkMuUnvetoFilter.taggingMode = cms.bool(True)
process.load('RecoMET.METFilters.HcalStripHaloFilter_cfi')
process.HcalStripHaloFilter.taggingMode = cms.bool(True)
```

Since these filters are not present in the releases used for the data RECO, it is needed to rerun the BeamHaloId. 
Do not forget to rerun the BeamHaloId by uncommenting the first line (process.BeamHaloId) in the process path !  
This will lead to some warnings in the CSCHaloFilter case, but they have no impact on the current filter. 

## Run on local file (4T)
```
  cmsRun MetScanning/skim/python/skim_4T.py
```
## Run with crab
In ``MetScanning/skim/crab/`` edit crab_4T.py and adjust samples, JSON, and the EOS directory. 
Then do
```
  cd MetScanning/skim/crab/
  python crab_4T.py
```



# BELOW standAlone installation

## Install default
```
  cmsrel CMSSW_7_4_7
  cd CMSSW_7_4_7/src
  cmsenv
  git clone git@github.com:cms-met/MetScanning
  scram b -j9
  ```

## Customized beam halo filters (HCAL strips and updated CSC halo filters)
Below are some instructions to run the HCAL strip filter and the updated CSC halo filters. Since these filters are not present in the releases used for the data RECO, it is needed to rerun the BeamHaloId. 
Do not forget to rerun the BeamHaloId by uncommenting the first line (process.BeamHaloId) in the process path !  
This will lead to some warnings in the CSCHaloFilter case, but they have no impact on the current filter. 

## Add the dedicated filters for HALO to the scanning skim (no need to redo the first part if you have set up the release already)
```
scramv1 project -n CMSSW_7_4_7_scanningNick CMSSW CMSSW_7_4_7
cd CMSSW_7_4_7_scanningNick/src
cmsenv
alias git 'git --exec-path=/cvmfs/cms.cern.ch/slc6_amd64_gcc491/external/git/1.8.3.1-odfocd/libexec/git-core/'
git cms-init
git remote add cmssw-nick git@github.com:aminnj/cmssw
git fetch cmssw-nick
echo  DataFormats/METReco > .git/info/sparse-checkout
echo  RecoMET/METAlgorithms/ >> .git/info/sparse-checkout
echo  RecoMET/METFilters/ >> .git/info/sparse-checkout
echo  RecoMET/METProducers >> .git/info/sparse-checkout
git checkout -b NickHcalFilter cmssw-nick/hcal-cell-filter-74X
git clone git@github.com:cms-met/MetScanning
scramv1 b -j 20
```

then add the filter in skim_4T.py
  ```                                                                                  
process.load('RecoMET.METFilters.HcalStripHaloFilter_cfi')
process.HcalStripHaloFilter.taggingMode = cms.bool(True)
```


## Similarly, for the updated version of the CSC Halo Filter: 
```
scramv1 project -n CMSSW_7_4_7_scanningLaurent CMSSW CMSSW_7_4_7
cd CMSSW_7_4_7_scanningLaurent/src
cmsenv
alias git 'git --exec-path=/cvmfs/cms.cern.ch/slc6_amd64_gcc491/external/git/1.8.3.1-odfocd/libexec/git-core/'
git cms-init
git remote add cmssw-Laurent git@github.com:lathomas/cmssw
git fetch cmssw-Laurent
echo  DataFormats/METReco > .git/info/sparse-checkout
echo  PhysicsTools/PatAlgos/ >> .git/info/sparse-checkout
echo  RecoMET/METAlgorithms/ >> .git/info/sparse-checkout
echo  RecoMET/METFilters/ >> .git/info/sparse-checkout
echo  RecoMET/METProducers >> .git/info/sparse-checkout
git checkout -b LaurentCSCHaloFilter cmssw-Laurent/cschalofilter_formetscanners
git clone git@github.com:cms-met/MetScanning
scramv1 b -j 20
```
There are two new filters to be added to skim_4T.py:
process.CSCTightHalo2015Filter and process.CSCTightHaloTrkMuUnvetoFilter 
The following python files should therefore be loaded:
process.load('RecoMET.METFilters.CSCTightHalo2015Filter_cfi')
process.load('RecoMET.METFilters.CSCTightHaloTrkMuUnvetoFilter_cfi')

Note: One of these two filters will hopefully replace the current one. Applying them both together will probably lead to a rate of fakes quite large. The aim ultimately is to replace the current filter by CSCTightHalo2015

