from MetScanning.plots.helpers import getFileList
from MetScanning.plots.samples import *
from math import pi
import ROOT
ROOT.gStyle.SetOptStat(0)
from DataFormats.FWLite import Events, Handle
from PhysicsTools.PythonAnalysis import *

small = False
prefix='v3'
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
'pfClusterECAL':("vector<reco::PFCluster>", "particleFlowClusterECAL",   ""), 
'pfClusterHCAL':("vector<reco::PFCluster>", "particleFlowClusterHBHE",   "")  
}
handles={k:Handle(edmCollections[k][0]) for k in edmCollections.keys()}

applied_filters = ["CSCTightHaloFilter", "HBHENoiseFilterResultRun2Loose"]

samples = [minBias]

h_pfClusterECAL = ROOT.TH2F('pfClusterECAL', 'pfClusterECAL', 100, -5, 5, 100, -pi, pi)
h_pfClusterHCAL = ROOT.TH2F('pfClusterHCAL', 'pfClusterHCAL', 100, -5, 5, 100, -pi, pi)

for s in samples:
  h_pfClusterECAL.Reset()
  h_pfClusterHCAL.Reset()

  files=[]
  for d in s['directories']:
    files.extend(getFileList(d))
  print "Running %s in %i directory(ies) and a total of %i files."%(s['name'], len(s['directories']), len(files))
  assert len(files)>0, "No files found for sample %s"%repr(s)
  events = Events(files) if not small else Events(files[:10])
  size=events.size() if not small else 10
  events.toBegin()
  products={}
  missingCollections=[]

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

    filter=False
    for f in applied_filters:
      if not products[f][0]: 
        print "Filtering because of %s"%f
        filter=True
        break
    if filter:continue

    pfClustersECAL = products['pfClusterECAL'] 
    for i_c, c in enumerate(pfClustersHCAL):
#      hitsAndFractions = c.hitsAndFractions()
#      recHitMultiplicity = len(hitsAndFractions)
      print "\nCluster",i_c,"energy",c.energy()
      h_pfClusterECAL.Fill(c.eta(),c.phi())
    pfClustersHCAL = products['pfClusterHCAL'] 
#    for i_c, c in enumerate(pfClustersHCAL):
##      hitsAndFractions = c.hitsAndFractions()
##      recHitMultiplicity = len(hitsAndFractions)
#      print "\nCluster",i_c,"energy",c.energy()
#      h_pfClusterHCAL.Fill(c.eta(),c.phi())

  c1 = ROOT.TCanvas()
  h_pfClustersHCAL.SetTitle("")
  h_pfClustersHCAL.GetXaxis().SetTitle('#eta')
  h_pfClustersHCAL.GetYaxis().SetTitle('#phi')
  c1.SetLogz()
  h_pfClustersHCAL.Draw('colz')
  c1.Print(plotDirectory+'/'+prefix+'_'+s['name']+'_2D_pfClustersHCAL.png')
  c1.Print(plotDirectory+'/'+prefix+'_'+s['name']+'_2D_pfClustersHCAL.pdf')
  c1.Print(plotDirectory+'/'+prefix+'_'+s['name']+'_2D_pfClustersHCAL.root')
  del c1

