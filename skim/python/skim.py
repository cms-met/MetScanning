import FWCore.ParameterSet.Config as cms

##____________________________________________________________________________||
process = cms.Process("SKIM")

##____________________________________________________________________________||
process.load("FWCore.MessageLogger.MessageLogger_cfi")

process.load("Configuration.StandardSequences.GeometryRecoDB_cff")
process.load("Configuration.StandardSequences.MagneticField_cff")


##____________________________________________________________________________||
process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:run2_mc', '')

##____________________________________________________________________________||
process.source = cms.Source(
    "PoolSource",
    #fileNames = cms.untracked.vstring("root://eoscms.cern.ch//store/data/Run2015A/HcalHPDNoise/RAW/v1/000/246/877/00000/9A0372A1-B809-E511-ABDF-02163E01440B.root")
    #fileNames = cms.untracked.vstring("root://eoscms.cern.ch//store/data/Run2015A/SingleMu/RECO/PromptReco-v1/000/246/865/00000/2631D17B-140B-E511-AB09-02163E014641.root")
    fileNames = cms.untracked.vstring("root://eoscms.cern.ch//store/data/Run2015A/SingleMu/RECO/PromptReco-v1/000/247/070/00000/A2AFED85-AB0C-E511-ACA9-02163E0142B7.root")
    #fileNames = cms.untracked.vstring("root://eoscms.cern.ch//store/data/Run2015A/ZeroBias1/RECO/PromptReco-v1/000/246/930/00000/2E8CE084-930B-E511-88E0-02163E0145E7.root")
    )

##____________________________________________________________________________||
process.out = cms.OutputModule(
    "PoolOutputModule",
    fileName = cms.untracked.string('skim.root'),
    SelectEvents   = cms.untracked.PSet( SelectEvents = cms.vstring('p') ),
    outputCommands = cms.untracked.vstring(
        'keep *'
        )
    )

##____________________________________________________________________________||
process.options   = cms.untracked.PSet(wantSummary = cms.untracked.bool(True))
process.MessageLogger.cerr.FwkReport.reportEvery = 50
process.maxEvents = cms.untracked.PSet(input = cms.untracked.int32(-1))

##____________________________________________________________________________||
process.load('RecoMET.METFilters.CSCTightHaloFilter_cfi')

##____________________________________________________________________________||
process.load('CommonTools.RecoAlgos.HBHENoiseFilterResultProducer_cfi')
process.ApplyBaselineHBHENoiseFilter = cms.EDFilter('BooleanFlagFilter',
    inputLabel = cms.InputTag('HBHENoiseFilterResultProducer','HBHENoiseFilterResult'),
    reverseDecision = cms.bool(False)
)
##____________________________________________________________________________||
process.load('RecoMET.METProducers.PFClusterMET_cfi')
process.load('RecoJets.JetProducers.PFClustersForJets_cff')


### select events with high caloMET 
#process.caloMETSelector = cms.EDFilter(
#    "CandViewSelector",
#    src = cms.InputTag("caloMet"),
##    src = cms.InputTag("caloMetM"), #muon corrected
#    cut = cms.string( "pt()>50" )
#    )
#process.clusterMETSelector = cms.EDFilter(
#    "CandViewSelector",
#    src = cms.InputTag("pfClusterMet"),
#    cut = cms.string( "pt()>50" )
#    )


process.condMETSelector = cms.EDProducer(
   "CandViewShallowCloneCombiner",
   decay = cms.string("caloMet pfClusterMet"),
   cut = cms.string("(daughter(0).pt > 80) || (daughter(0).pt/daughter(1).pt > 2 && daughter(1).pt > 40 ) || (daughter(1).pt/daughter(0).pt > 2 && daughter(0).pt > 40 )" )
   )


process.metCounter = cms.EDFilter(
    "CandViewCountFilter",
    src = cms.InputTag("condMETSelector"),
    minNumber = cms.uint32(1),
    )

##____________________________________________________________________________||
process.p = cms.Path(
    process.CSCTightHaloFilter*
    process.HBHENoiseFilterResultProducer*
    process.ApplyBaselineHBHENoiseFilter*
    process.pfClusterRefsForJetsHCAL*
    process.pfClusterRefsForJetsECAL*
    process.pfClusterRefsForJets*
    process.pfClusterMet*
#    process.caloMETSelector*
    process.condMETSelector*
    process.metCounter
    )

process.e1 = cms.EndPath(
    process.out
    )

##____________________________________________________________________________||

