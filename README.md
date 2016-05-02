# MetScanning
## Install (4T)
```
  cmsrel CMSSW_8_0_5
  cd CMSSW_8_0_5/src
  cmsenv
  git clone git@github.com:cms-met/MetScanning
  scram b -j9
  ```
## Run on local file (4T)
```
  cmsRun MetScanning/skim/python/skim_4T.py
```
You might need to run the following command if you want to access files via XROOT:
```
  voms-proxy-init --voms cms
```

## Run with crab
In ``MetScanning/skim/crab/`` edit crab_4T.py and adjust samples, JSON, and the EOS directory. 
Then do
```
  cd MetScanning/skim/crab/
  python crab_4T.py
```
