from MetScanning.plots.helpers import getFileList
from MetScanning.plots.samples_v5 import *
from math import pi
import os
import ROOT
from subprocess import call
ROOT.gStyle.SetOptStat(0)
from DataFormats.FWLite import Events, Handle
from PhysicsTools.PythonAnalysis import *

small = False
outputDir = os.path.expanduser("~/eos/cms/store/group/phys_jetmet/schoef/private0TSkim_v5/outliers/")

edmCollections = { \
#  'pfMet':("vector<reco::PFMET>", "pfMet", ""), #, "RECO")
  'pfCaloMet':("vector<reco::PFMET>", "pfCaloMet", ""), 
  'caloMet':("vector<reco::CaloMET>", "caloMet",""),
  'pfClusterMet':("vector<reco::PFClusterMET>", "pfClusterMet",""),
#  'pfCandidates':("vector<reco::PFCandidate>", "particleFlow", "")
   'CSCTightHaloFilter':            ("bool",  "CSCTightHaloFilter",              "",                "SKIM"),
   'HBHENoiseFilterResult':         ("bool",  "HBHENoiseFilterResultProducer",   "HBHENoiseFilterResult",   "SKIM"),
   'HBHENoiseFilterResultRun1':     ("bool",  "HBHENoiseFilterResultProducer",   "HBHENoiseFilterResultRun1",   "SKIM"),
   'HBHENoiseFilterResultRun2Loose':("bool",  "HBHENoiseFilterResultProducer",   "HBHENoiseFilterResultRun2Loose",   "SKIM"),
   'HBHENoiseFilterResultRun2Tight':("bool",  "HBHENoiseFilterResultProducer",   "HBHENoiseFilterResultRun2Tight",   "SKIM"),
}
handles={k:Handle(edmCollections[k][0]) for k in edmCollections.keys()}

def lowerCut(products, var, thr):
  if products[var][0].pt()>=thr: return True
  return False
def upperCut(products, var, thr):
  if products[var][0].pt()<thr: return True
  return False

sample = ZeroBias
if small:
  prefix = sample['name']+"_test"
else:
  prefix = sample['name']+"_caloMetAbove80"

skimCondition = lambda products:lowerCut(products, 'caloMet', 80)

def filterCondition(products):
  passed=True
  applied_filters = ["CSCTightHaloFilter", "HBHENoiseFilterResultRun2Tight"]
  for f in applied_filters:
    if not products[f][0]: 
      print "Filtering because of %s"%f
      passed = False
      break
  return passed


files=[]
for d in sample['directories']:
  if small:
    files.extend(getFileList(d)[:1])
  else:
    files.extend(getFileList(d))
print "Running %s in %i directory(ies) and a total of %i files."%(sample['name'], len(sample['directories']), len(files))

#files = ["/afs/cern.ch/user/s/schoef/eos/cms/store/group/phys_jetmet/schoef/private0TSkim_v3/Jet/crab_Jet_Run2015A-PromptReco-v1_RECO/150610_094813/0000/skim_20.root"]

selected=[]
for i_f, f in enumerate(files):
  print "Running over file %i: %s"%(i_f, f)
  events = Events([f])
  size=events.size()
  events.toBegin()
  products={}
  missingCollections=[]
  for nev in xrange(size):
    #if nev%100==0:print nev,'/',size
    events.to(nev)
    eaux=events.eventAuxiliary()
    run=eaux.run()           
    event=eaux.event()
    lumi=eaux.luminosityBlock()
    for k in [ x for x in edmCollections.keys() if x not in missingCollections]:
      try:
        events.getByLabel(edmCollections[k][1:],handles[k])
        products[k]=handles[k].product()
      except:
        products[k]=None
        print "Not found:",k
        missingCollections.append(k)
    if not small:
      if not filterCondition(products):continue
      if not skimCondition(products):continue
    selected.append({'run':run,"lumi":lumi,"event":event,'file':os.path.expanduser(f)})
  del events

print "Now picking %i events" % len(selected)
os.system('mkdir -p %s/%s'%(outputDir,prefix))
for e in selected:
  outputFile=os.path.expanduser("%s/%s/%i_%i.root"%(outputDir,prefix,e['run'],e['event']))
#  print "Running\nedmCopyPickMerge eventsToProcess=%i:%i inputFiles=file:%s outputFile=%s\n"%(e['run'],e['event'],e['file'],outputFile) 
#  os.system("edmCopyPickMerge eventsToProcess=%i:%i inputFiles=file:%s outputFile=%s"%(e['run'],e['event'],e['file'],outputFile)) 
  call(["edmCopyPickMerge", "eventsToProcess=%i:%i"%(e['run'],e['event']), "inputFiles=file:%s"%e['file'], "outputFile=%s"%outputFile])
