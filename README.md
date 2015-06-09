# MetScanning
## Install
```
  cmsrel CMSSW_7_4_4_patch2
  cd CMSSW_7_4_4_patch2/src
  git clone https://github.com/cms-met/MetScanning
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
