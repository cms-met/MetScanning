from math import pi

import ROOT
ROOT.gStyle.SetOptStat(0)
from DataFormats.FWLite import Events, Handle
from PhysicsTools.PythonAnalysis import *


edmCollections = { \
  'offlineSlimmedPrimaryVertices':("vector<reco::Vertex>", "offlineSlimmedPrimaryVertices", "", "PAT"),
  'TriggerResults':("edm::TriggerResults", "TriggerResults", "", "PAT")
}

#flags = ["Flag_HBHENoiseFilter" , "Flag_CSCTightHaloFilter" , "Flag_hcalLaserEventFilter" , "Flag_EcalDeadCellTriggerPrimitiveFilter" , "Flag_trackingFailureFilter" , "Flag_eeBadScFilter" , "Flag_ecalLaserCorrFilter" , "Flag_trkPOGFilters" , "Flag_trkPOG_manystripclus53X" , "Flag_trkPOG_toomanystripclus53X" , "Flag_trkPOG_logErrorTooManyClusters" , "Flag_METFilters", "Flag_goodVertices"]
flags = ["Flag_trackingFailureFilter" , "Flag_goodVertices"]
handles={k:Handle(edmCollections[k][0]) for k in edmCollections.keys()}

#files = ["file:/afs/cern.ch/user/m/mschoene/public/pickevents_17July_mAOD.root" ]
files = ["file:../../../../cmssw/CMSSW_7_4_7/src/miniAOD-prod_PAT.root" ]

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

    res={}
    for f in flags:
      trigVec = ROOT.vector(ROOT.string)()
      trigVec.push_back(f) 
      trigVecBit = ROOT.vector(ROOT.string)()
      trigVecBit.push_back(f) 
      triggerBitCheckersSingleBit = ROOT.heppy.TriggerBitChecker(trigVecBit)
      res[f]=triggerBitCheckersSingleBit.check(events.object(), products['TriggerResults'])

  print "\n################## Event: %i:%i:%i ########################"% (run,lumi,event)
  print "Filter flags mAOD:"
  for f in flags:
    print "%40s"%f, res[f]

  nGood = 0
  print "Vertices: Found a total of %i"%products["offlineSlimmedPrimaryVertices"].size()
  for i, v in enumerate(products["offlineSlimmedPrimaryVertices"]):
    fake = v.isFake()
    ndof = v.ndof()
    z    = v.z()
    rho  = v.position().rho()
    good = not(fake) and (ndof>4) and abs(z)<24 and rho<2
    if good:nGood += 1
    print " Vertex %i: good %i, fake %i, ndof %f, z %f, rho %f"%(i, good, fake, ndof, z, rho)
    if i>=2: 
      print "<skip remaining>"
      break
  cons = "consistent" if (nGood>=1 and res[f]) or (nGood==0 and not res[f]) else "inconsistent"
  print "-->Found %i good vertices, flag is %i. This is\033[1m %s\033[0m."%(nGood, res["Flag_goodVertices"], cons)
      
