from MetScanning.plots.helpers import getFileList
from MetScanning.plots.samples import *

import ROOT
from DataFormats.FWLite import Events, Handle
from PhysicsTools.PythonAnalysis import *

small = False
prefix='v1'
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
  'caloMet':("vector<reco::CaloMET>", "caloMet",""),
  'pfClusterMet':("vector<reco::PFClusterMET>", "pfClusterMet",""),
#  'pfCandidates':("vector<reco::PFCandidate>", "particleFlow", "")
}
handles={k:Handle(edmCollections[k][0]) for k in edmCollections.keys()}

samples = [ZeroBias]
#samples = [EGamma, SingleMu]
#samples = [SingleMu]

h_caloMet = ROOT.TH1F('caloMet', 'caloMet', 100,0,200)
h_pfClusterMet = ROOT.TH1F('pfClusterMet', 'pfClusterMet', 100,0,200)
h_caloMet_vs_pfClusterMet = ROOT.TH2F('caloVSpfCluster', 'caloVSpfCluster', 100,0,200,100,0,200)
h_caloSumET = ROOT.TH1F('caloSumET', 'caloSumET', 100,0,2000)
h_pfClusterSumET = ROOT.TH1F('pfClusterSumET', 'pfClusterSumET', 100,0,2000)
h_caloSumET_vs_pfClusterSumET = ROOT.TH2F('caloVSpfCluster', 'caloVSpfCluster', 100,0,2000,100,0,2000)

for s in samples:
  h_caloMet.Reset()
  h_pfClusterMet.Reset()
  h_caloMet_vs_pfClusterMet.Reset()

  files=[]
  for d in s['directories']:
    files.extend(getFileList(d))

  events = Events(files) if not small else Events(files[:10])
  size=events.size() if not small else 10
  events.toBegin()
  products={}
  missingCollections=[]

  for nev in range(size):
    if nev%10==0:print nev,'/',size
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
    caloMet = products['caloMet'][0].pt()
    pfClusterMet = products['pfClusterMet'][0].pt()
    caloSumET = products['caloMet'][0].sumEt()
    pfClusterSumET = products['pfClusterMet'][0].sumEt()

    h_caloMet.Fill(caloMet)
    h_pfClusterMet.Fill(pfClusterMet)
    h_caloMet_vs_pfClusterMet.Fill(caloMet, pfClusterMet)

    h_caloSumET.Fill(caloSumET)
    h_pfClusterSumET.Fill(pfClusterSumET)
    h_caloSumET_vs_pfClusterSumET.Fill(caloSumET, pfClusterSumET)

  c1 = ROOT.TCanvas()
  l = ROOT.TLegend(0.7,0.7,1,1)
  l.SetFillColor(0)
  l.SetShadowColor(ROOT.kWhite)
  l.SetBorderSize(1)
  l.AddEntry(h_caloMet, "calo MET")
  l.AddEntry(h_pfClusterMet, "pfCluster MET")
  h_caloMet.GetXaxis().SetTitle("Met (GeV)")
  h_caloMet.GetYaxis().SetTitle("Events")
  h_caloMet.Draw()
  h_pfClusterMet.SetLineColor(ROOT.kRed)
  h_pfClusterMet.Draw("same")
  l.Draw()
  c1.Print(plotDirectory+'/'+prefix+'_'+s['name']+'_1D_caloMet_vs_pfClusterMet.png')
  c1.Print(plotDirectory+'/'+prefix+'_'+s['name']+'_1D_caloMet_vs_pfClusterMet.pdf')
  c1.Print(plotDirectory+'/'+prefix+'_'+s['name']+'_1D_caloMet_vs_pfClusterMet.root')

  l = ROOT.TLegend(0.7,0.7,1,1)
  l.SetFillColor(0)
  l.SetShadowColor(ROOT.kWhite)
  l.SetBorderSize(1)
  l.AddEntry(h_caloSumET, "calo MET")
  l.AddEntry(h_pfClusterSumET, "pfCluster MET")
  h_caloSumET.GetXaxis().SetTitle("SumET (GeV)")
  h_caloSumET.GetYaxis().SetTitle("Events")
  h_caloSumET.Draw()
  h_pfClusterSumET.SetLineColor(ROOT.kRed)
  h_pfClusterSumET.Draw("same")
  l.Draw()
  c1.Print(plotDirectory+'/'+prefix+'_'+s['name']+'_1D_caloSumET_vs_pfClusterSumET.png')
  c1.Print(plotDirectory+'/'+prefix+'_'+s['name']+'_1D_caloSumET_vs_pfClusterSumET.pdf')
  c1.Print(plotDirectory+'/'+prefix+'_'+s['name']+'_1D_caloSumET_vs_pfClusterSumET.root')

  h_caloMet_vs_pfClusterMet.GetXaxis().SetTitle('caloMet')
  h_caloMet_vs_pfClusterMet.GetYaxis().SetTitle('pfClusterMet')
  h_caloMet_vs_pfClusterMet.Draw('colz')
  c1.Print(plotDirectory+'/'+prefix+'_'+s['name']+'_2D_caloMet_vs_pfClusterMet.png')
  c1.Print(plotDirectory+'/'+prefix+'_'+s['name']+'_2D_caloMet_vs_pfClusterMet.pdf')
  c1.Print(plotDirectory+'/'+prefix+'_'+s['name']+'_2D_caloMet_vs_pfClusterMet.root')

  h_caloSumET_vs_pfClusterSumET.GetXaxis().SetTitle('caloSumET')
  h_caloSumET_vs_pfClusterSumET.GetYaxis().SetTitle('pfClusterSumET')
  h_caloSumET_vs_pfClusterSumET.Draw('colz')
  c1.Print(plotDirectory+'/'+prefix+'_'+s['name']+'_2D_caloSumET_vs_pfClusterSumET.png')
  c1.Print(plotDirectory+'/'+prefix+'_'+s['name']+'_2D_caloSumET_vs_pfClusterSumET.pdf')
  c1.Print(plotDirectory+'/'+prefix+'_'+s['name']+'_2D_caloSumET_vs_pfClusterSumET.root')
