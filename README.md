# MetScanning
## Install
```
  cmsrel CMSSW_7_4_4_patch2
  cd CMSSW_7_4_4_patch2/src
  cmsenv
  git cms-addpkg RecoParticleFlow/PFProducer
  git cherry-pick af5c1ba33e88b3be627c262eb93d678f9f70e729
  git clone https://github.com/cms-met/MetScanning
  scram b -j9
  ```
## Run on local file
```
  cmsRun MetScanning/skim/python/skim.py
```
## Run with crab
In ``MetScanning/skim/crab/`` edit crab.py and adjust samples, JSON, and the EOS directory. 
Then do
```
  cd MetScanning/skim/crab/
  python crab.py
```
