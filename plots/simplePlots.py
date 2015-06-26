from MetScanning.plots.helpers import getFileList
from MetScanning.plots.samples_v5 import *
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

applied_filters = ["CSCTightHaloFilter", "HBHENoiseFilterResultRun1"]

#samples = [Jet]
#samples = [ZeroBias]
samples = [EGamma, Jet, ZeroBias, SingleMu]
maxMet = 350
maxSumET = 2500

caloMetThr = 90
pfCaloMetThr = 90
pfClusterMetThr = 90

h_caloMet = ROOT.TH1F('caloMet', 'caloMet', 100,0,maxMet)
h_pfCaloMet = ROOT.TH1F('pfCaloMet', 'pfCaloMet', 100,0,maxMet)
h_pfClusterMet = ROOT.TH1F('pfClusterMet', 'pfClusterMet', 100,0,maxMet)

h_caloMex = ROOT.TH1F('caloMex', 'caloMex', 100,-maxMet/2,maxMet/2)
h_pfCaloMex = ROOT.TH1F('pfCaloMex', 'pfCaloMex', 100,-maxMet/2,maxMet/2)
h_pfClusterMex = ROOT.TH1F('pfClusterMex', 'pfClusterMex', 100,-maxMet/2,maxMet/2)

h_caloMey = ROOT.TH1F('caloMey', 'caloMey', 100,-maxMet/2,maxMet/2)
h_pfCaloMey = ROOT.TH1F('pfCaloMey', 'pfCaloMey', 100,-maxMet/2,maxMet/2)
h_pfClusterMey = ROOT.TH1F('pfClusterMey', 'pfClusterMey', 100,-maxMet/2,maxMet/2)

h_caloMetPhi = ROOT.TH1F('caloMetPhi', 'caloMetPhi', 100,-pi,pi)
h_pfCaloMetPhi = ROOT.TH1F('pfCaloMetPhi', 'pfCaloMetPhi', 100,-pi,pi)
h_pfClusterMetPhi = ROOT.TH1F('pfClusterMetPhi', 'pfClusterMetPhi', 100,-pi,pi)

h_caloSumET = ROOT.TH1F('caloSumET', 'caloSumET', 100,0,maxSumET)
h_pfCaloSumET = ROOT.TH1F('pfCaloSumET', 'pfCaloSumET', 100,0,maxSumET)
h_pfClusterSumET = ROOT.TH1F('pfClusterSumET', 'pfClusterSumET', 100,0,maxSumET)

h_caloMet_vs_pfClusterMet = ROOT.TH2F('caloVSpfCluster_Met', 'caloVSpfCluster_Met', 100,0,maxMet,100,0,maxMet)
h_pfCaloMet_vs_pfClusterMet = ROOT.TH2F('pfCaloVSpfCluster_Met', 'pfCaloVSpfCluster_Met', 100,0,maxMet,100,0,maxMet)
h_caloMet_vs_pfCaloMet = ROOT.TH2F('caloVSpfCalo_Met', 'caloVSpfCalo_Met', 100,0,maxMet,100,0,maxMet)
h_caloSumET_vs_pfClusterSumET = ROOT.TH2F('caloVSpfCluster_sumET', 'caloVSpfCluster_sumET', 100,0,maxSumET,100,0,maxSumET)
h_pfCaloSumET_vs_pfClusterSumET = ROOT.TH2F('pfCaloVSpfCluster_sumET', 'pfCaloVSpfCluster_sumET', 100,0,maxSumET,100,0,maxSumET)
h_caloSumET_vs_pfCaloSumET = ROOT.TH2F('caloVSpfCalo_sumET', 'caloVSpfCalo_sumET', 100,0,maxSumET,100,0,maxSumET)

for s in samples:
  h_caloMet.Reset()
  h_pfCaloMet.Reset()
  h_pfClusterMet.Reset()

  h_caloMex.Reset()
  h_pfCaloMex.Reset()
  h_pfClusterMex.Reset()

  h_caloMey.Reset()
  h_pfCaloMey.Reset()
  h_pfClusterMey.Reset()

  h_caloMetPhi.Reset()
  h_pfCaloMetPhi.Reset()
  h_pfClusterMetPhi.Reset()

  h_caloSumET.Reset()
  h_pfCaloSumET.Reset()
  h_pfClusterSumET.Reset()

  h_caloMet_vs_pfClusterMet.Reset()
  h_pfCaloMet_vs_pfClusterMet.Reset()
  h_caloMet_vs_pfCaloMet.Reset()
  h_caloSumET_vs_pfClusterSumET.Reset()
  h_pfCaloSumET_vs_pfClusterSumET.Reset()
  h_caloSumET_vs_pfCaloSumET.Reset()

  outliers_caloMet=[]
  outliers_pfCaloMet=[]
  outliers_pfClusterMet=[]
  outliers_caloSumET=[]
  outliers_pfCaloSumET=[]
  outliers_pfClusterSumET=[]

  files=[]
  for d in s['directories']:
    files.extend(getFileList(d))
  print "Running %s in %i directory(ies) and a total of %i files."%(s['name'], len(s['directories']), len(files))

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

    caloMet = products['caloMet'][0].pt()
    pfCaloMet = products['pfCaloMet'][0].pt()
    pfClusterMet = products['pfClusterMet'][0].pt()
    caloMex = products['caloMet'][0].px()
    pfCaloMex = products['pfCaloMet'][0].px()
    pfClusterMex = products['pfClusterMet'][0].px()
    caloMey = products['caloMet'][0].py()
    pfCaloMey = products['pfCaloMet'][0].py()
    pfClusterMey = products['pfClusterMet'][0].py()
    caloMetPhi = products['caloMet'][0].phi()
    pfCaloMetPhi = products['pfCaloMet'][0].phi()
    pfClusterMetPhi = products['pfClusterMet'][0].phi()
    caloSumET = products['caloMet'][0].sumEt()
    pfClusterSumET = products['pfClusterMet'][0].sumEt()
    pfCaloSumET = products['pfCaloMet'][0].sumEt()

    if caloMet>caloMetThr: 
      h_caloMet.Fill(caloMet)
      h_caloMex     .Fill(caloMex     )
      h_caloMey     .Fill(caloMey     )
      h_caloMetPhi     .Fill(caloMetPhi     )
    if pfCaloMet>pfCaloMetThr: 
      h_pfCaloMet.Fill(pfCaloMet)
      h_pfCaloMex     .Fill(pfCaloMex     )
      h_pfCaloMey     .Fill(pfCaloMey     )
      h_pfCaloMetPhi     .Fill(pfCaloMetPhi     )
    if pfClusterMet>pfClusterMetThr: 
      h_pfClusterMet.Fill(pfClusterMet)
      h_pfClusterMex     .Fill(pfClusterMex     )
      h_pfClusterMey     .Fill(pfClusterMey     )
      h_pfClusterMetPhi     .Fill(pfClusterMetPhi     )
    if caloMet>caloMetThr or pfClusterMet>pfClusterMetThr: h_caloMet_vs_pfClusterMet.Fill(caloMet, pfClusterMet)
    if pfCaloMet>pfCaloMetThr or pfClusterMet>pfClusterMetThr: h_pfCaloMet_vs_pfClusterMet.Fill(pfCaloMet, pfClusterMet)
    if caloMet>caloMetThr or pfCaloMet>pfCaloMetThr: h_caloMet_vs_pfCaloMet.Fill(caloMet, pfCaloMet)

    if caloMet>maxMet:
      print "outlier caloMet %5.3f "%caloMet
      outliers_caloMet.append([run, lumi, event])
    if pfCaloMet>maxMet:
      print "outlier pfCaloMet %5.3f "%pfCaloMet
      outliers_pfCaloMet.append([run, lumi, event])
    if pfClusterMet>maxMet:
      print "outlier pfClusterMet %5.3f "%pfClusterMet
      outliers_pfClusterMet.append([run, lumi, event])

    h_caloSumET.Fill(caloSumET)
    h_pfCaloSumET.Fill(pfCaloSumET)
    h_pfClusterSumET.Fill(pfClusterSumET)
    h_caloSumET_vs_pfClusterSumET.Fill(caloSumET, pfClusterSumET)
    h_pfCaloSumET_vs_pfClusterSumET.Fill(pfCaloSumET, pfClusterSumET)
    h_caloSumET_vs_pfCaloSumET.Fill(caloSumET, pfCaloSumET)

    if caloSumET>maxSumET:
      print "outlier caloSumET %5.3f "%caloSumET
      outliers_caloSumET.append([run, lumi, event])
    if pfCaloSumET>maxSumET:
      print "outlier pfCaloSumET %5.3f "%pfCaloSumET
      outliers_pfCaloSumET.append([run, lumi, event])
    if pfClusterSumET>maxSumET:
      print "outlier pfClusterSumET %5.3f "%pfClusterSumET
      outliers_pfClusterSumET.append([run, lumi, event])


  print "Outliers caloMet", outliers_caloMet
  print "Outliers pfCaloMet", outliers_pfCaloMet
  print "Outliers pfClusterMet", outliers_pfClusterMet
  print "Outliers caloSumET", outliers_caloSumET
  print "Outliers pfCaloSumET", outliers_pfCaloSumET
  print "Outliers pfClusterSumET", outliers_pfClusterSumET

  c1 = ROOT.TCanvas()
  l = ROOT.TLegend(0.5,0.7,1,1)
  l.SetFillColor(0)
  l.SetShadowColor(ROOT.kWhite)
  l.SetBorderSize(1)
  l.AddEntry(h_pfCaloMet, "pfCalo Met ("+str(len(outliers_pfCaloMet))+" outliers)")
  l.AddEntry(h_caloMet, "calo Met ("+str(len(outliers_caloMet))+" outliers)")
  l.AddEntry(h_pfClusterMet, "pfCluster Met ("+str(len(outliers_pfClusterMet))+" outliers)")
  h_pfCaloMet.GetXaxis().SetTitle("Met (GeV)")
  h_pfCaloMet.GetYaxis().SetTitle("Events")
  h_pfCaloMet.SetTitle("")
  c1.SetLogy()
  h_pfCaloMet.Draw()
  h_caloMet.SetLineColor(ROOT.kGreen)
  h_caloMet.Draw("same")
  h_pfClusterMet.SetLineColor(ROOT.kRed)
  h_pfClusterMet.Draw("same")
  l.Draw()
  c1.Print(plotDirectory+'/'+prefix+'_'+s['name']+'_1D_Met.png')
  c1.Print(plotDirectory+'/'+prefix+'_'+s['name']+'_1D_Met.pdf')
  c1.Print(plotDirectory+'/'+prefix+'_'+s['name']+'_1D_Met.root')
  del c1

  c1 = ROOT.TCanvas()
  l = ROOT.TLegend(0.6,0.8,1,1)
  l.SetFillColor(0)
  l.SetShadowColor(ROOT.kWhite)
  l.SetBorderSize(1)
  l.AddEntry(h_pfCaloMex, "pfCalo Mex")
  l.AddEntry(h_caloMex, "calo Mex")
  l.AddEntry(h_pfClusterMex, "pfCluster Mex")
  h_pfCaloMex.GetXaxis().SetTitle("Mex (GeV)")
  h_pfCaloMex.GetYaxis().SetTitle("Events")
  h_pfCaloMex.SetTitle("")
  c1.SetLogy()
  h_pfCaloMex.GetYaxis().SetRangeUser(0.1, 100*h_pfCaloMex.GetMaximum())
  h_pfCaloMex.Draw()
  h_caloMex.SetLineColor(ROOT.kGreen)
  h_caloMex.Draw("same")
  h_pfClusterMex.SetLineColor(ROOT.kRed)
  h_pfClusterMex.Draw("same")
  l.Draw()
  c1.Print(plotDirectory+'/'+prefix+'_'+s['name']+'_1D_Mex.png')
  c1.Print(plotDirectory+'/'+prefix+'_'+s['name']+'_1D_Mex.pdf')
  c1.Print(plotDirectory+'/'+prefix+'_'+s['name']+'_1D_Mex.root')
  del c1

  c1 = ROOT.TCanvas()
  l = ROOT.TLegend(0.6,0.8,1,1)
  l.SetFillColor(0)
  l.SetShadowColor(ROOT.kWhite)
  l.SetBorderSize(1)
  l.AddEntry(h_pfCaloMey, "pfCalo Mey")
  l.AddEntry(h_caloMey, "calo Mey")
  l.AddEntry(h_pfClusterMey, "pfCluster Mey")
  h_pfCaloMey.GetXaxis().SetTitle("Mey (GeV)")
  h_pfCaloMey.GetYaxis().SetTitle("Events")
  h_pfCaloMey.SetTitle("")
  c1.SetLogy()
  h_pfCaloMey.GetYaxis().SetRangeUser(0.1, 100*h_pfCaloMey.GetMaximum())
  h_pfCaloMey.Draw()
  h_caloMey.SetLineColor(ROOT.kGreen)
  h_caloMey.Draw("same")
  h_pfClusterMey.SetLineColor(ROOT.kRed)
  h_pfClusterMey.Draw("same")
  l.Draw()
  c1.Print(plotDirectory+'/'+prefix+'_'+s['name']+'_1D_Mey.png')
  c1.Print(plotDirectory+'/'+prefix+'_'+s['name']+'_1D_Mey.pdf')
  c1.Print(plotDirectory+'/'+prefix+'_'+s['name']+'_1D_Mey.root')

  c1 = ROOT.TCanvas()
  l = ROOT.TLegend(0.5,0.7,1,1)
  l.SetFillColor(0)
  l.SetShadowColor(ROOT.kWhite)
  l.SetBorderSize(1)
  l.AddEntry(h_pfCaloMetPhi, "pfCalo MetPhi")
  l.AddEntry(h_caloMetPhi, "calo MetPhi")
  l.AddEntry(h_pfClusterMetPhi, "pfCluster MetPhi")
  h_pfCaloMetPhi.GetXaxis().SetTitle("MetPhi (GeV)")
  h_pfCaloMetPhi.GetYaxis().SetTitle("Events")
  h_pfCaloMetPhi.SetTitle("")
  c1.SetLogy(0)
  h_pfCaloMetPhi.GetYaxis().SetRangeUser(0.1, 1.5*h_pfCaloMetPhi.GetMaximum())
  h_pfCaloMetPhi.Draw()
  h_caloMetPhi.SetLineColor(ROOT.kGreen)
  h_caloMetPhi.Draw("same")
  h_pfClusterMetPhi.SetLineColor(ROOT.kRed)
  h_pfClusterMetPhi.Draw("same")
  l.Draw()
  c1.Print(plotDirectory+'/'+prefix+'_'+s['name']+'_1D_MetPhi.png')
  c1.Print(plotDirectory+'/'+prefix+'_'+s['name']+'_1D_MetPhi.pdf')
  c1.Print(plotDirectory+'/'+prefix+'_'+s['name']+'_1D_MetPhi.root')

  c1 = ROOT.TCanvas()
  l = ROOT.TLegend(0.5,0.7,1,1)
  l.SetFillColor(0)
  l.SetShadowColor(ROOT.kWhite)
  l.SetBorderSize(1)
  l.AddEntry(h_pfCaloSumET, "pfCalo SumET ("+str(len(outliers_pfCaloSumET))+" outliers)")
  l.AddEntry(h_caloSumET, "calo SumET ("+str(len(outliers_caloSumET))+" outliers)")
  l.AddEntry(h_pfClusterSumET, "pfCluster SumET ("+str(len(outliers_pfClusterSumET))+" outliers)")
  h_pfCaloSumET.GetXaxis().SetTitle("SumET (GeV)")
  h_pfCaloSumET.GetYaxis().SetTitle("Events")
  h_pfCaloSumET.SetTitle("")
  c1.SetLogy()
  h_pfCaloSumET.Draw()
  h_caloSumET.SetLineColor(ROOT.kGreen)
  h_caloSumET.Draw("same")
  h_pfClusterSumET.SetLineColor(ROOT.kRed)
  h_pfClusterSumET.Draw("same")
  l.Draw()
  c1.Print(plotDirectory+'/'+prefix+'_'+s['name']+'_1D_SumET.png')
  c1.Print(plotDirectory+'/'+prefix+'_'+s['name']+'_1D_SumET.pdf')
  c1.Print(plotDirectory+'/'+prefix+'_'+s['name']+'_1D_SumET.root')
  del c1

  c1 = ROOT.TCanvas()
  h_caloMet_vs_pfClusterMet.SetTitle("")
  h_caloMet_vs_pfClusterMet.GetXaxis().SetTitle('caloMet')
  h_caloMet_vs_pfClusterMet.GetYaxis().SetTitle('pfClusterMet')
  c1.SetLogz()
  h_caloMet.SetTitle("")
  h_caloMet_vs_pfClusterMet.Draw('colz')
  line=ROOT.TLine(0,0,h_caloMet_vs_pfClusterMet.GetXaxis().GetXmax(),h_caloMet_vs_pfClusterMet.GetXaxis().GetXmax())
  line.Draw()
  c1.Print(plotDirectory+'/'+prefix+'_'+s['name']+'_2D_caloMet_vs_pfClusterMet.png')
  c1.Print(plotDirectory+'/'+prefix+'_'+s['name']+'_2D_caloMet_vs_pfClusterMet.pdf')
  c1.Print(plotDirectory+'/'+prefix+'_'+s['name']+'_2D_caloMet_vs_pfClusterMet.root')
  del c1

  c1 = ROOT.TCanvas()
  h_caloSumET_vs_pfClusterSumET.SetTitle("")
  h_caloSumET_vs_pfClusterSumET.GetXaxis().SetTitle('caloSumET')
  h_caloSumET_vs_pfClusterSumET.GetYaxis().SetTitle('pfClusterSumET')
  c1.SetLogz()
  h_caloSumET_vs_pfClusterSumET.Draw('colz')
  line=ROOT.TLine(0,0,h_caloSumET_vs_pfClusterSumET.GetXaxis().GetXmax(),h_caloSumET_vs_pfClusterSumET.GetXaxis().GetXmax())
  line.Draw()
  c1.Print(plotDirectory+'/'+prefix+'_'+s['name']+'_2D_caloSumET_vs_pfClusterSumET.png')
  c1.Print(plotDirectory+'/'+prefix+'_'+s['name']+'_2D_caloSumET_vs_pfClusterSumET.pdf')
  c1.Print(plotDirectory+'/'+prefix+'_'+s['name']+'_2D_caloSumET_vs_pfClusterSumET.root')
  del c1

  c1 = ROOT.TCanvas()
  h_caloMet_vs_pfCaloMet.SetTitle("")
  h_caloMet_vs_pfCaloMet.GetXaxis().SetTitle('caloMet')
  h_caloMet_vs_pfCaloMet.GetYaxis().SetTitle('pfCaloMet')
  c1.SetLogz()
  h_caloMet.SetTitle("")
  h_caloMet_vs_pfCaloMet.Draw('colz')
  line=ROOT.TLine(0,0,h_caloMet_vs_pfCaloMet.GetXaxis().GetXmax(),h_caloMet_vs_pfCaloMet.GetXaxis().GetXmax())
  line.Draw()
  c1.Print(plotDirectory+'/'+prefix+'_'+s['name']+'_2D_caloMet_vs_pfCaloMet.png')
  c1.Print(plotDirectory+'/'+prefix+'_'+s['name']+'_2D_caloMet_vs_pfCaloMet.pdf')
  c1.Print(plotDirectory+'/'+prefix+'_'+s['name']+'_2D_caloMet_vs_pfCaloMet.root')
  del c1

  c1 = ROOT.TCanvas()
  h_caloSumET_vs_pfCaloSumET.SetTitle("")
  h_caloSumET_vs_pfCaloSumET.GetXaxis().SetTitle('caloSumET')
  h_caloSumET_vs_pfCaloSumET.GetYaxis().SetTitle('pfCaloSumET')
  c1.SetLogz()
  h_caloSumET_vs_pfCaloSumET.Draw('colz')
  line=ROOT.TLine(0,0,h_caloSumET_vs_pfCaloSumET.GetXaxis().GetXmax(),h_caloSumET_vs_pfCaloSumET.GetXaxis().GetXmax())
  line.Draw()
  c1.Print(plotDirectory+'/'+prefix+'_'+s['name']+'_2D_caloSumET_vs_pfCaloSumET.png')
  c1.Print(plotDirectory+'/'+prefix+'_'+s['name']+'_2D_caloSumET_vs_pfCaloSumET.pdf')
  c1.Print(plotDirectory+'/'+prefix+'_'+s['name']+'_2D_caloSumET_vs_pfCaloSumET.root')
  del c1

  c1 = ROOT.TCanvas()
  h_pfCaloMet_vs_pfClusterMet.SetTitle("")
  h_pfCaloMet_vs_pfClusterMet.GetXaxis().SetTitle('pfCaloMet')
  h_pfCaloMet_vs_pfClusterMet.GetYaxis().SetTitle('pfClusterMet')
  c1.SetLogz()
  h_caloMet.SetTitle("")
  h_pfCaloMet_vs_pfClusterMet.Draw('colz')
  line=ROOT.TLine(0,0,h_pfCaloMet_vs_pfClusterMet.GetXaxis().GetXmax(),h_pfCaloMet_vs_pfClusterMet.GetXaxis().GetXmax())
  line.Draw()
  c1.Print(plotDirectory+'/'+prefix+'_'+s['name']+'_2D_pfCaloMet_vs_pfClusterMet.png')
  c1.Print(plotDirectory+'/'+prefix+'_'+s['name']+'_2D_pfCaloMet_vs_pfClusterMet.pdf')
  c1.Print(plotDirectory+'/'+prefix+'_'+s['name']+'_2D_pfCaloMet_vs_pfClusterMet.root')
  del c1

  c1 = ROOT.TCanvas()
  h_pfCaloSumET_vs_pfClusterSumET.SetTitle("")
  h_pfCaloSumET_vs_pfClusterSumET.GetXaxis().SetTitle('pfCaloSumET')
  h_pfCaloSumET_vs_pfClusterSumET.GetYaxis().SetTitle('pfClusterSumET')
  c1.SetLogz()
  h_pfCaloSumET_vs_pfClusterSumET.Draw('colz')
  line=ROOT.TLine(0,0,h_pfCaloSumET_vs_pfClusterSumET.GetXaxis().GetXmax(),h_pfCaloSumET_vs_pfClusterSumET.GetXaxis().GetXmax())
  line.Draw()
  c1.Print(plotDirectory+'/'+prefix+'_'+s['name']+'_2D_pfCaloSumET_vs_pfClusterSumET.png')
  c1.Print(plotDirectory+'/'+prefix+'_'+s['name']+'_2D_pfCaloSumET_vs_pfClusterSumET.pdf')
  c1.Print(plotDirectory+'/'+prefix+'_'+s['name']+'_2D_pfCaloSumET_vs_pfClusterSumET.root')
  del c1
