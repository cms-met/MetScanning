# MetScanning
For recent instruction please visit: https://twiki.cern.ch/twiki/bin/view/CMS/MissingETScanners
## Install
```
  cmsrel CMSSW_10_1_2_patch2
  cd CMSSW_10_1_2_patch2/src
  cmsenv
  git cms-init
  git cms-addpkg RecoMET/METFilters 
  
  git clone https://github.com/didukhle/MetScanning.git
  scram b -j9
  ```
  You might need to run the following command if you want to access files via XROOT:
```
  voms-proxy-init --voms cms
```
## Run on local file:
```
  cmsRun MetScanning/skim/python/skim.py
```
## Run on AOD files:
```
  cmsRun MetScanning/skim/python/skimAOD.py
```
## Run with crab
In ``MetScanning/skim/crab/`` edit crab.py and adjust samples, JSON, and the EOS directory. 
Then do:
```
  cd MetScanning/skim/crab/
  python crab.py
```
In order to submit job with large input data:
```
  voms-proxy-init --voms cms
  source /cvmfs/cms.cern.ch/crab3/crab.sh
  
  Before submitting the jobs do a dryrun:

  crab --debug submit --config=crab.py --dryrun   

  In everything works fine you can then fully submit the jobs by:

  crab proceed
  
## Bug list!!!:
>> Compiling edm plugin /afs/cern.ch/user/l/ldidukh/CMSSW_10_1_2_patch2/src/MetScanning/tuple/test/METScanningNtupleMaker.cc 
>> Building edm plugin tmp/slc6_amd64_gcc630/src/MetScanning/tuple/test/METScanningNutpleMaker/libMETScanningNutpleMaker.so
Leaving library rule at src/MetScanning/tuple/test
@@@@ Running edmWriteConfigs for METScanningNutpleMaker
--- Registered EDM Plugin: METScanningNutpleMaker
>> Leaving Package MetScanning/tuple
>> Package MetScanning/tuple built
>> Subsystem MetScanning built
gmake[1]: Entering directory '/afs/cern.ch/user/l/ldidukh/CMSSW_10_1_2_patch2'
>> Local Products Rules ..... started
>> Local Products Rules ..... done
@@@@ Refreshing Plugins:edmPluginRefresh
>> Done generating edm plugin poisoned information
>> Creating project symlinks
>> Done python_symlink
>> Compiling python modules cfipython/slc6_amd64_gcc630
>> Compiling python modules python
>> Compiling python modules src/MetScanning/skim/python
>> Plugins of all types refreshed.
Compiling src/MetScanning/skim/python/._skimAOD.py ...
Sorry: TypeError: compile() expected string without null bytes
config/SCRAM/GMake/Makefile.rules:2168: recipe for target 'CompilePython' failed
gmake[1]: *** [CompilePython] Error 1
gmake[1]: Leaving directory '/afs/cern.ch/user/l/ldidukh/CMSSW_10_1_2_patch2'
config/SCRAM/GMake/Makefile.rules:2035: recipe for target 'src' failed
gmake: *** [src] Error 2
gmake: *** [There are compilation/build errors. Please see the detail log above.] Error 2
```
