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
