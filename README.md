# MetScanning
## Install (4T)
```
  cmsrel CMSSW_7_4_7
  cd CMSSW_7_4_7/src
  cmsenv
  git clone git@github.com:cms-met/MetScanning
  scram b -j9
  ```
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

## Add the dedicated filters for HALO to the scanning skim (no need to redo the first part if you have set up the release already)

scramv1 project -n CMSSW_7_4_7_scanningNick CMSSW CMSSW_7_4_7
cd CMSSW_7_4_7_scanningNick/src
cmsenv
alias git 'git --exec-path=/cvmfs/cms.cern.ch/slc6_amd64_gcc491/external/git/1.8.3.1-odfocd/libexec/git-core/'
git cms-init
git remote add cmssw-nick git@github.com:aminnj/cmssw
git fetch cmssw-nick
echo  DataFormats/METReco > .git/info/sparse-checkout
echo  PhysicsTools/PatAlgos/ >> .git/info/sparse-checkout
echo  RecoMET/METAlgorithms/ >> .git/info/sparse-checkout
echo  RecoMET/METFilters/ >> .git/info/sparse-checkout
echo  RecoMET/METProducers >> .git/info/sparse-checkout
git checkout -b NickHcalFilter cmssw-nick/hcal-cell-filter-74X
git clone git@github.com:cms-met/MetScanning
scramv1 b -j 20
