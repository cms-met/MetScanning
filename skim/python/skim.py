import FWCore.ParameterSet.Config as cms

##____________________________________________________________________________||
process = cms.Process("SKIM")

##____________________________________________________________________________||
process.load("FWCore.MessageLogger.MessageLogger_cfi")

process.load("Configuration.StandardSequences.GeometryRecoDB_cff")
#process.load("Configuration.StandardSequences.MagneticField_cff")
process.load('Configuration.StandardSequences.MagneticField_AutoFromDBCurrent_cff')

process.load("SimGeneral.HepPDTESSource.pythiapdt_cfi")


##___________________________Global_Tag_______________________________________||
#process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
#from Configuration.AlCa.GlobalTag import GlobalTag
#process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:run2_mc', '')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
process.GlobalTag.globaltag = 'GR_P_V56::All'


##___________________________Input_Files______________________________________||
process.source = cms.Source(
    "PoolSource",
    #fileNames = cms.untracked.vstring("root://eoscms.cern.ch//store/data/Run2015A/SingleMu/RECO/PromptReco-v1/000/247/070/00000/A2AFED85-AB0C-E511-ACA9-02163E0142B7.root")
    fileNames = cms.untracked.vstring("root://eoscms.cern.ch//store/data/Run2015A/Jet/RECO/PromptReco-v1/000/246/960/00000/4CED9FE9-DB0B-E511-A069-02163E012432.root")
    )


##___________________________EDM_Output_File__________________________________||
process.out = cms.OutputModule(
    "PoolOutputModule",
    fileName = cms.untracked.string('skim.root'),
    SelectEvents   = cms.untracked.PSet( SelectEvents = cms.vstring('p') ),
    outputCommands = cms.untracked.vstring(
        'keep *'
#        'keep *_pfClusterMet_*_*', 'keep *_CSCTightHaloFilter_*_*', 'keep *_HBHENoiseFilterResultProducer_*_*'
        )
    )


##____________________________________________________________________________||
process.options   = cms.untracked.PSet(wantSummary = cms.untracked.bool(True))
process.MessageLogger.cerr.FwkReport.reportEvery = 50
process.maxEvents = cms.untracked.PSet(input = cms.untracked.int32(10))


##___________________________CSC_Halo_Filter__________________________________||
process.load('RecoMET.METFilters.CSCTightHaloFilter_cfi')
process.CSCTightHaloFilter.taggingMode = cms.bool(True)


##___________________________HCAL_Noise_Filter________________________________||
process.load('CommonTools.RecoAlgos.HBHENoiseFilterResultProducer_cfi')
#process.ApplyBaselineHBHENoiseFilter = cms.EDFilter('BooleanFlagFilter',
#    inputLabel = cms.InputTag('HBHENoiseFilterResultProducer','HBHENoiseFilterResult'),
#    reverseDecision = cms.bool(False)
#)
process.load('Configuration.StandardSequences.Reconstruction_Data_cff')


##___________________________PFClusterMet_____________________________________||
process.load('RecoMET.METProducers.PFClusterMET_cfi')
process.pfClusterRefsForJetsHCAL = cms.EDProducer("PFClusterRefCandidateProducer",
  src          = cms.InputTag('particleFlowClusterHCAL'),
  particleType = cms.string('pi+')
)
process.pfClusterRefsForJetsECAL = cms.EDProducer("PFClusterRefCandidateProducer",
  src          = cms.InputTag('particleFlowClusterECAL'),
  particleType = cms.string('pi+')
)
process.pfClusterRefsForJetsHF = cms.EDProducer("PFClusterRefCandidateProducer",
  src          = cms.InputTag('particleFlowClusterHF'),
  particleType = cms.string('pi+')
)
process.pfClusterRefsForJetsHO = cms.EDProducer("PFClusterRefCandidateProducer",
  src          = cms.InputTag('particleFlowClusterHO'),
  particleType = cms.string('pi+')
)
process.pfClusterRefsForJets = cms.EDProducer("PFClusterRefCandidateMerger",
  src = cms.VInputTag("pfClusterRefsForJetsHCAL", "pfClusterRefsForJetsECAL", "pfClusterRefsForJetsHF", "pfClusterRefsForJetsHO")
)
process.pfClusterMetSequence = cms.Sequence(
 process.particleFlowRecHitECAL*
 process.particleFlowRecHitHBHE*
 process.particleFlowRecHitHF*
 process.particleFlowRecHitHO*
 process.particleFlowClusterECALUncorrected*
 process.particleFlowClusterECAL*
 process.particleFlowClusterHBHE*
 process.particleFlowClusterHCAL*
 process.particleFlowClusterHF*
 process.particleFlowClusterHO*
 process.pfClusterRefsForJetsHCAL*
 process.pfClusterRefsForJetsECAL*
 process.pfClusterRefsForJetsHF*
 process.pfClusterRefsForJetsHO*
 process.pfClusterRefsForJets*
#   process.ak4PFClusterJets
 process.pfClusterMet
)


##___________________________PFCaloMet_____________________________________||
process.hltParticleFlowBlock = cms.EDProducer("PFBlockProducer",
  debug = cms.untracked.bool(False),
  verbose = cms.untracked.bool(False),
  elementImporters = cms.VPSet(
      cms.PSet(
          source = cms.InputTag("particleFlowClusterECAL"),
          #source = cms.InputTag("particleFlowClusterECALUncorrected"), #we use uncorrected
          importerName = cms.string('GenericClusterImporter')
      ),
      cms.PSet(
          source = cms.InputTag("particleFlowClusterHCAL"),
          importerName = cms.string('GenericClusterImporter')
      ),
      cms.PSet(
          source = cms.InputTag("particleFlowClusterHO"),
          importerName = cms.string('GenericClusterImporter')
      ),
      cms.PSet(
          source = cms.InputTag("particleFlowClusterHF"),
          importerName = cms.string('GenericClusterImporter')
      )
  ),
  linkDefinitions = cms.VPSet(
      cms.PSet(
          linkType = cms.string('ECAL:HCAL'),
          useKDTree = cms.bool(False),
          #linkerName = cms.string('ECALAndHCALLinker')
          linkerName = cms.string('ECALAndHCALCaloJetLinker') #new ECal and HCal Linker for PFCaloJets
      ),
      cms.PSet(
          linkType = cms.string('HCAL:HO'),
          useKDTree = cms.bool(False),
          linkerName = cms.string('HCALAndHOLinker')
      ),
      cms.PSet(
          linkType = cms.string('HFEM:HFHAD'),
          useKDTree = cms.bool(False),
          linkerName = cms.string('HFEMAndHFHADLinker')
      ),
      cms.PSet(
          linkType = cms.string('ECAL:ECAL'),
          useKDTree = cms.bool(False),
          linkerName = cms.string('ECALAndECALLinker')
      )
   )
)
from RecoParticleFlow.PFProducer.particleFlow_cfi import particleFlowTmp
process.hltParticleFlow = particleFlowTmp.clone(
    GedPhotonValueMap = cms.InputTag(""),
    useEGammaFilters = cms.bool(False),
    useEGammaElectrons = cms.bool(False), 
    useEGammaSupercluster = cms.bool(False),
    rejectTracks_Step45 = cms.bool(False),
    usePFNuclearInteractions = cms.bool(False),  
    blocks = cms.InputTag("hltParticleFlowBlock"), 
    egammaElectrons = cms.InputTag(""),
    useVerticesForNeutral = cms.bool(False),
    PFEGammaCandidates = cms.InputTag(""),
    useProtectionsForJetMET = cms.bool(False),
    usePFConversions = cms.bool(False),
    rejectTracks_Bad = cms.bool(False),
    muons = cms.InputTag(""),
    postMuonCleaning = cms.bool(False),
    usePFSCEleCalib = cms.bool(False)
    )
process.load("RecoMET.METProducers.PFMET_cfi")
process.pfCaloMet = process.pfMet.clone(
  src = cms.InputTag("hltParticleFlow"),
  alias = cms.string('pfCaloMet')
)

process.pfCaloMetSequence = cms.Sequence(
   process.hltParticleFlowBlock *
   process.hltParticleFlow *
   process.pfCaloMet
)



##___________________________High_Met_Skim____________________________________||
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
   decay = cms.string("caloMet pfClusterMet pfCaloMet"),
#   cut = cms.string("(daughter(0).pt > 80) || (daughter(0).pt/daughter(1).pt > 2 && daughter(1).pt > 40 ) || (daughter(1).pt/daughter(0).pt > 2 && daughter(0).pt > 40 )" ) #Skim v0
#   cut = cms.string("(daughter(0).pt > 60) || (daughter(1).pt > 60)" ) #Skim v1
   cut = cms.string("(daughter(0).pt > 60) || (daughter(1).pt > 60) ||  (daughter(2).pt > 60)" ) #Skim v3
#   cut = cms.string("(daughter(0).pt > 90) || (daughter(1).pt > 90) ||  (daughter(2).pt > 90)" ) #Skim v5
   )

process.metCounter = cms.EDFilter(
    "CandViewCountFilter",
    src = cms.InputTag("condMETSelector"),
    minNumber = cms.uint32(1),
    )


##___________________________Flat_Tuple________________________________________||
process.metScanNtupleMaker = cms.EDAnalyzer("METScanningNtupleMaker",
   rootOutputFile=cms.string("tuple.root"),
   caloMET=cms.InputTag("caloMet"),
   pfCaloMET=cms.InputTag("pfCaloMet"),
   pfClusterMET=cms.InputTag("pfClusterMet"),
   EcalPFClusterCollection=cms.InputTag("particleFlowClusterECAL"),
   HcalPFClusterCollection=cms.InputTag("particleFlowClusterHCAL"),
   HBHEPFClusterCollection=cms.InputTag("particleFlowClusterHBHE"),
   HOPFClusterCollection=cms.InputTag("particleFlowClusterHO"),
   HFPFClusterCollection=cms.InputTag("particleFlowClusterHF"),
   tracksCollection=cms.InputTag("generalTracks"),
   CSCfilter=cms.InputTag("CSCTightHaloFilter"),
   HBHEfilterR1=cms.InputTag("HBHENoiseFilterResultProducer","HBHENoiseFilterResultRun1"),
   HBHEfilterR2L=cms.InputTag("HBHENoiseFilterResultProducer","HBHENoiseFilterResultRun2Loose"),
   HBHEfilterR2T=cms.InputTag("HBHENoiseFilterResultProducer","HBHENoiseFilterResultRun2Tight"),
   EBRecHits=cms.InputTag("reducedEcalRecHitsEB"),
   EERecHits=cms.InputTag("reducedEcalRecHitsEE"),
   ESRecHits=cms.InputTag("reducedEcalRecHitsES")
)


##___________________________PATH______________________________________________||
process.p = cms.Path(
    process.CSCTightHaloFilter*
    process.HBHENoiseFilterResultProducer* #produces bools
#    process.ApplyBaselineHBHENoiseFilter* 
#    process.pfClusterRefsForJets*
#    process.pfClusterRefsForJets_step*
    process.pfClusterMetSequence*
    process.pfCaloMetSequence*
#    process.caloMETSelector* ##CH: caloMET skim
    process.condMETSelector* ##CH: conditial MET skim
    process.metCounter*      ##CH: needed for any of the aforementioned skims
    process.metScanNtupleMaker ##CH: writes a flat tree
    )

process.e1 = cms.EndPath(
    #process.out ##CH: write the skimmed edm file 
    )

##____________________________________________________________________________||

