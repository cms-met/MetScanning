from math import pi

import ROOT
ROOT.gStyle.SetOptStat(0)
from DataFormats.FWLite import Events, Handle
from PhysicsTools.PythonAnalysis import *


edmCollections = { \
  'offlinePrimaryVertices':("vector<reco::Vertex>", "offlinePrimaryVertices", "", "RECO"),
}

handles={k:Handle(edmCollections[k][0]) for k in edmCollections.keys()}

files = ["file:/afs/cern.ch/user/m/mschoene/public/pickevents_17July_RECO.root" ]
#files = ["file:../skim/python/skim.root" ]

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

  print "\nEvent: %i:%i:%i "% (run,lumi,event)

  print "Vertices: Found a total of %i"%products["offlinePrimaryVertices"].size()
  nGood = 0
  for i, v in enumerate(products["offlinePrimaryVertices"]):
    fake = v.isFake()
    ndof = v.ndof()
    z    = v.z()
    rho  = v.position().rho()
    good = not(fake) and (ndof>4) and abs(z)<24 and rho<2
    if good:nGood += 1
    print "Vertex %i: good %i, fake %i, ndof %f, z %f, rho %f"%(i, good, fake, ndof, z, rho)
    if i>=2: 
      print "<skip remaining>"
      break
  print "Found at least %i good vertices"%nGood
      
