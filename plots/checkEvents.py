from math import pi

import ROOT
ROOT.gStyle.SetOptStat(0)
from DataFormats.FWLite import Events, Handle
from PhysicsTools.PythonAnalysis import *

small = False
prefix='22Jun2015'
plotDirectory = "/afs/hephy.at/user/r/rschoefbeck/www/png0T/"

#ROOT.gStyle.SetOptStat(0)
#if not hasattr(ROOT, "tdrStyle"):
#  ROOT.gROOT.ProcessLine(".L $CMSSW_BASE/src/MetScanning/plots/scripts/tdrstyle.C")
#  ROOT.setTDRStyle()
#  ROOT.tdrStyle.SetPadRightMargin(0.18)
#  ROOT.gROOT.ProcessLine(".L $CMSSW_BASE/src/MetScanning/plots/scripts/useNiceColorPalette.C")
#  ROOT.useNiceColorPalette(255)

edmCollections = { \
#  'pfMet':("vector<reco::PFMET>", "pfMet", ""), #, "RECO")
#  'pfCaloMet':("vector<reco::PFMET>", "pfCaloMet", ""), 
#  'caloMet':("vector<reco::CaloMET>", "caloMet",""),
#  'pfClusterMet':("vector<reco::PFClusterMET>", "pfClusterMet",""),
#  'pfCandidates':("vector<reco::PFCandidate>", "particleFlow", "")
   'CSCTightHaloFilter':            ("bool",  "CSCTightHaloFilter",              "",                "SKIM"),
   'EcalDeadCellBoundaryEnergyFilter':            ("bool",  "EcalDeadCellBoundaryEnergyFilter",              "",                "SKIM"),
   'HBHEIsoNoiseFilterResult':         ("bool",  "HBHENoiseFilterResultProducer",   "HBHEIsoNoiseFilterResult",   "SKIM"),
   'HBHENoiseFilterResult':         ("bool",  "HBHENoiseFilterResultProducer",   "HBHENoiseFilterResult",   "SKIM"),
   'HBHENoiseFilterResultRun1':     ("bool",  "HBHENoiseFilterResultProducer",   "HBHENoiseFilterResultRun1",   "SKIM"),
   'HBHENoiseFilterResultRun2Loose':("bool",  "HBHENoiseFilterResultProducer",   "HBHENoiseFilterResultRun2Loose",   "SKIM"),
   'HBHENoiseFilterResultRun2Tight':("bool",  "HBHENoiseFilterResultProducer",   "HBHENoiseFilterResultRun2Tight",   "SKIM"),
}

applied_filters = ["CSCTightHaloFilter","HBHEIsoNoiseFilterResult","HBHENoiseFilterResult","HBHENoiseFilterResultRun1","HBHENoiseFilterResultRun2Loose","HBHENoiseFilterResultRun2Tight", "EcalDeadCellBoundaryEnergyFilter"]

handles={k:Handle(edmCollections[k][0]) for k in edmCollections.keys()}

#files = ["file:/data/rschoefbeck/pickEvents/nick/skim_1.root", "file:/data/rschoefbeck/pickEvents/nick/skim_2.root", "file:/data/rschoefbeck/pickEvents/nick/skim_3.root", "file:/data/rschoefbeck/pickEvents/nick/skim_4.root", "file:/data/rschoefbeck/pickEvents/nick/skim_5.root", "file:/data/rschoefbeck/pickEvents/nick/skim_6.root" ]
files = ["file:/afs/hephy.at/user/r/rschoefbeck/CMS/CMSSW_7_4_7/src/MetScanning/skim/python/skim.root" ]

events = Events(files)
events.toBegin()
products={}
missingCollections=[]

print "number of events",events.size()
for nev in range(events.size()):
  if nev%100==0:print nev,'/',events.size()
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

  for f in applied_filters:
#    if not products[f][0]: 
      print "%i:%i:%i filter %s: result: %i"%(run,lumi,event,f,products[f][0])
  print
