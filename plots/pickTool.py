from MetScanning.plots.helpers import getFileList
from MetScanning.plots.samples import *
from math import pi
import os
import ROOT
ROOT.gStyle.SetOptStat(0)
from DataFormats.FWLite import Events, Handle
from PhysicsTools.PythonAnalysis import *

small = False
outputDir = "~/eos/cms/store/group/phys_jetmet/schoef/private0TSkim_v3/outliers/"

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

#sample = SingleMu
#prefix = sample['name']+"_pfCaloMetBelow10_pfClusterMetAbove80"
#def pfCaloMetBelow10_pfClusterMetAbove80(products):
#  caloMet = products['caloMet'][0].pt()
#  pfCaloMet = products['pfCaloMet'][0].pt()
#  pfClusterMet = products['pfClusterMet'][0].pt()
#  if pfCaloMet<10 and pfClusterMet>80: return True
#  return False
#skimCondition = highCaloMet

sample = Jet
prefix = sample['name']+"_caloMetAbove250"
def caloMetAbove250(products):
  if products['caloMet'][0].pt()>250: return True
  return False
skimCondition = caloMetAbove250

#samples = [Jet, EGamma]
#samples = [ZeroBias]


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
  files.extend(getFileList(d))
print "Running %s in %i directory(ies) and a total of %i files."%(sample['name'], len(sample['directories']), len(files))

events = Events(files) if not small else Events(files[:10])
size=events.size() if not small else 10
events.toBegin()
products={}
missingCollections=[]
selected=[]
for nev in range(size):
  if nev%100==0:print nev,'/',size
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

  if not filterCondition(products):continue
  if not skimCondition(products):continue
  selected.append({'run':run,"lumi":lumi,"event":event,'file':os.path.expanduser(files[events.fileIndex()])})

print "Now picking %i events", len(selected)
os.system('mkdir -p %s/%s'%(outputDir,prefix))
for e in selected:
  os.system("edmCopyPickMerge eventsToProcess=%i:%i inputFiles=file:%s outputFile=%s/%s/%i_%i.root"%(e['run'],e['event'],e['file'],outputDir,prefix,e['run'],e['event'])) 

