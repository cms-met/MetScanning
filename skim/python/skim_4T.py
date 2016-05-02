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
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_condDBv2_cff')
#process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
#process.GlobalTag.globaltag = 'GR_P_V56::All'
from RecoLuminosity.LumiProducer.bunchSpacingProducer_cfi import *
process.GlobalTag.globaltag = '80X_dataRun2_Prompt_v8'
#80X_dataRun2_Express_v5'


##___________________________Input_Files______________________________________||
process.source = cms.Source(
    "PoolSource",
    fileNames = cms.untracked.vstring(
#'/store/data/Run2016B/HLTPhysics/RECO/PromptReco-v1/000/272/007/00000/4CD1BB37-160F-E611-A1FC-02163E0137AC.root',
#'/store/data/Run2016B/HLTPhysics/RECO/PromptReco-v1/000/272/008/00000/B67DEFBD-3B0F-E611-ADE1-02163E014771.root',
#'/store/data/Run2016B/HLTPhysics/RECO/PromptReco-v1/000/272/010/00000/608A7811-350F-E611-8DB3-02163E014678.root',
#'/store/data/Run2016B/HLTPhysics/RECO/PromptReco-v1/000/272/011/00000/1472B1C0-2310-E611-96D8-02163E0119DA.root',
#'/store/data/Run2016B/HLTPhysics/RECO/PromptReco-v1/000/272/011/00000/14F0D632-3110-E611-933D-02163E01181D.root',
#'/store/data/Run2016B/HLTPhysics/RECO/PromptReco-v1/000/272/011/00000/1EA0366E-3110-E611-80D8-02163E01249A.root',
#'/store/data/Run2016B/HLTPhysics/RECO/PromptReco-v1/000/272/011/00000/44C1F798-2B10-E611-BF46-02163E01451F.root',
#'/store/data/Run2016B/HLTPhysics/RECO/PromptReco-v1/000/272/011/00000/4A3B752F-1F10-E611-A035-02163E011CDA.root',
#'/store/data/Run2016B/HLTPhysics/RECO/PromptReco-v1/000/272/011/00000/C47D98AD-2A10-E611-B6EB-02163E014469.root',
'/store/data/Run2016B/HLTPhysics/RECO/PromptReco-v1/000/272/012/00000/6A4AFDBA-6E0F-E611-B2C5-02163E0118E4.root',
'/store/data/Run2016B/HLTPhysics/RECO/PromptReco-v1/000/272/012/00000/6E789AB1-760F-E611-A25D-02163E0143CD.root',
'/store/data/Run2016B/HLTPhysics/RECO/PromptReco-v1/000/272/012/00000/9A2FA24F-750F-E611-B070-02163E013771.root',
'/store/data/Run2016B/HLTPhysics/RECO/PromptReco-v1/000/272/012/00000/9C1C71C4-740F-E611-AECE-02163E01359B.root',
'/store/data/Run2016B/HLTPhysics/RECO/PromptReco-v1/000/272/012/00000/BCBD6558-800F-E611-A943-02163E01345F.root',
'/store/data/Run2016B/HLTPhysics/RECO/PromptReco-v1/000/272/012/00000/C62D5E92-7E0F-E611-8A53-02163E0141D0.root',
#'/store/data/Run2016B/HLTPhysics/RECO/PromptReco-v1/000/272/014/00000/18C7BC2F-970F-E611-81E0-02163E0118A8.root',
#'/store/data/Run2016B/HLTPhysics/RECO/PromptReco-v1/000/272/014/00000/2AD65F62-9B0F-E611-BB79-02163E0142BE.root',
#'/store/data/Run2016B/HLTPhysics/RECO/PromptReco-v1/000/272/014/00000/F4C31765-E70F-E611-A4CD-02163E011B93.root',
#'/store/data/Run2016B/HLTPhysics/RECO/PromptReco-v1/000/272/016/00000/E80C2BE4-C70F-E611-8B2E-02163E01443E.root',
#'/store/data/Run2016B/HLTPhysics/RECO/PromptReco-v1/000/272/017/00000/B87B5C29-9A0F-E611-9D52-02163E0129FC.root',
#'/store/data/Run2016B/HLTPhysics/RECO/PromptReco-v1/000/272/018/00000/7E0C893D-A30F-E611-8F96-02163E0119EA.root',
#'/store/data/Run2016B/HLTPhysics/RECO/PromptReco-v1/000/272/019/00000/8620D70B-980F-E611-BA11-02163E013494.root',
#'/store/data/Run2016B/HLTPhysics/RECO/PromptReco-v1/000/272/021/00000/0C72517D-B60F-E611-BE19-02163E012B89.root',
#'/store/data/Run2016B/HLTPhysics/RECO/PromptReco-v1/000/272/021/00000/14F40ABE-B40F-E611-8505-02163E0121B1.root',
#'/store/data/Run2016B/HLTPhysics/RECO/PromptReco-v1/000/272/021/00000/284A38A4-BE0F-E611-90B7-02163E01464C.root',
#'/store/data/Run2016B/HLTPhysics/RECO/PromptReco-v1/000/272/021/00000/4E056A46-AF0F-E611-86B7-02163E0135A9.root',
#'/store/data/Run2016B/HLTPhysics/RECO/PromptReco-v1/000/272/021/00000/6279125D-B30F-E611-B35E-02163E01199C.root',
#'/store/data/Run2016B/HLTPhysics/RECO/PromptReco-v1/000/272/021/00000/8CD6C812-B10F-E611-AE2D-02163E012941.root',
#'/store/data/Run2016B/HLTPhysics/RECO/PromptReco-v1/000/272/021/00000/A27F93CA-B00F-E611-B906-02163E01364F.root',
#'/store/data/Run2016B/HLTPhysics/RECO/PromptReco-v1/000/272/021/00000/CCF3F67F-B80F-E611-B19C-02163E0140DF.root',
#'/store/data/Run2016B/HLTPhysics/RECO/PromptReco-v1/000/272/022/00000/9861F5D8-E00F-E611-99B0-02163E014413.root',
#'/store/data/Run2016B/HLTPhysics/RECO/PromptReco-v1/000/272/022/00000/BEF59AD9-DF0F-E611-9B8B-02163E011C79.root',
#'/store/data/Run2016B/HLTPhysics/RECO/PromptReco-v1/000/272/022/00000/C84194BB-CC0F-E611-95EA-02163E011848.root',
#'/store/data/Run2016B/HLTPhysics/RECO/PromptReco-v1/000/272/022/00000/DCDC9F37-E10F-E611-9EED-02163E0123E8.root',
#'/store/data/Run2016B/HLTPhysics/RECO/PromptReco-v1/000/272/023/00000/062E181F-D90F-E611-BDAE-02163E01416D.root',

#'/store/express/Run2016B/ExpressPhysics/FEVT/Express-v1/000/272/012/00000/FEB65CA6-980D-E611-B0FA-02163E0135A3.root'


#'/store/express/Run2016A/ExpressPhysics/FEVT/Express-v2/000/271/170/00000/00D3C1BC-9409-E611-A2C6-02163E014408.root'
#"/store/data/Run2015B/MET/RECO/PromptReco-v1/000/251/252/00000/8CA59489-8D27-E511-A859-02163E014629.root"
)
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
process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )


##___________________________CSC_Halo_Filter__________________________________||
process.load('RecoMET.METFilters.CSCTightHaloFilter_cfi')
process.CSCTightHaloFilter.taggingMode = cms.bool(True)

process.load('RecoMET.METFilters.CSCTightHalo2015Filter_cfi')
process.CSCTightHalo2015Filter.taggingMode = cms.bool(True)
process.load('RecoMET.METFilters.CSCTightHaloTrkMuUnvetoFilter_cfi')
process.CSCTightHaloTrkMuUnvetoFilter.taggingMode = cms.bool(True)

##___________________________Global_Halo_Filter__________________________________||
process.load('RecoMET.METFilters.globalTightHalo2016Filter_cfi')
process.globalTightHalo2016Filter.taggingMode = cms.bool(True)

process.load('RecoMET.METFilters.globalSuperTightHalo2016Filter_cfi')
process.globalSuperTightHalo2016Filter.taggingMode = cms.bool(True)

##___________________________HCAL_Noise_Filter________________________________||
process.load('CommonTools.RecoAlgos.HBHENoiseFilterResultProducer_cfi')
process.HBHENoiseFilterResultProducer.minZeros = cms.int32(99999)
process.HBHENoiseFilterResultProducer.IgnoreTS4TS5ifJetInLowBVRegion=cms.bool(False)


#process.ApplyBaselineHBHENoiseFilter = cms.EDFilter('BooleanFlagFilter',
#    inputLabel = cms.InputTag('HBHENoiseFilterResultProducer','HBHENoiseFilterResult'),
#    reverseDecision = cms.bool(False)
#)
process.load('Configuration.StandardSequences.Reconstruction_Data_cff')

process.load('RecoMET.METFilters.HcalStripHaloFilter_cfi')
process.HcalStripHaloFilter.taggingMode = cms.bool(True)


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

process.goodVertices = cms.EDFilter(
  "VertexSelector",
  filter = cms.bool(False),
  src = cms.InputTag("offlinePrimaryVertices"),
  cut = cms.string("!isFake && ndof > 4 && abs(z) <= 24 && position.rho < 2")
)
process.load('RecoMET.METFilters.trackingFailureFilter_cfi')
process.trackingFailureFilter.taggingMode = cms.bool(True)

process.load('RecoMET.METFilters.EcalDeadCellTriggerPrimitiveFilter_cfi')
process.EcalDeadCellTriggerPrimitiveFilter.taggingMode = cms.bool(True)

process.load('RecoMET.METFilters.eeBadScFilter_cfi')
process.eeBadScFilter.taggingMode = cms.bool(True)

process.primaryVertexFilter = cms.EDFilter("GoodVertexFilter",
                                           vertexCollection = cms.InputTag('offlinePrimaryVertices'),
                                           minimumNDOF = cms.uint32(4) ,
                                           maxAbsZ = cms.double(24),
                                           maxd0 = cms.double(2)
                                           )

process.load('RecoMET.METFilters.EcalDeadCellBoundaryEnergyFilter_cfi')
process.EcalDeadCellBoundaryEnergyFilter.taggingMode = cms.bool(True)
process.EcalDeadCellBoundaryEnergyFilter.limitDeadCellToChannelStatusEB=cms.vint32(12, 13, 14)
process.EcalDeadCellBoundaryEnergyFilter.limitDeadCellToChannelStatusEE=cms.vint32(12, 13, 14)

process.condMETSelector = cms.EDProducer(
   "CandViewShallowCloneCombiner",
   decay = cms.string("caloMet pfMet"),
   cut = cms.string("(daughter(0).pt > 100) || (daughter(1).pt > 100)" ) 
   )

process.metCounter = cms.EDFilter(
    "CandViewCountFilter",
    src = cms.InputTag("condMETSelector"),
    minNumber = cms.uint32(1),
    )


##___________________________Flat_Tuple________________________________________||
process.metScanNtupleMaker = cms.EDAnalyzer("METScanningNtupleMaker",
                                            rootOutputFile=cms.string("tuple.root"),
                                            pfCandidates=cms.InputTag("particleFlow"),
                                            pfJets=cms.InputTag("ak4PFJets"),
                                            caloMET=cms.InputTag("caloMet"),
                                            pfCaloMET=cms.InputTag("pfCaloMet"),
                                            pfClusterMET=cms.InputTag("pfClusterMet"),
                                            pfMET=cms.InputTag("pfMet"),
                                            EcalPFClusterCollection=cms.InputTag("particleFlowClusterECAL"),
                                            HcalPFClusterCollection=cms.InputTag("particleFlowClusterHCAL"),
                                            HBHEPFClusterCollection=cms.InputTag("particleFlowClusterHBHE"),
                                            HOPFClusterCollection=cms.InputTag("particleFlowClusterHO"),
                                            HFPFClusterCollection=cms.InputTag("particleFlowClusterHF"),
                                            tracksCollection=cms.InputTag("generalTracks"),
                                            TRKfilterLETMC=cms.InputTag("logErrorTooManyClusters"),
                                            TRKfilterLETMS=cms.InputTag("logErrorTooManySeeds"),
                                            TRKfilterMSC=cms.InputTag("manystripclus53X"),
                                            TRKfilterTMSC=cms.InputTag("toomanystripclus53X"),
                                            CSC2015filter=cms.InputTag("CSCTightHalo2015Filter"),
                                            GlobalHalofilterTight=cms.InputTag("globalTightHalo2016Filter"),
                                            GlobalHalofilterSuperTight=cms.InputTag("globalSuperTightHalo2016Filter"),
                                            HcalStripHaloFilter=cms.InputTag("HcalStripHaloFilter"),
                                            HBHEfilterR1=cms.InputTag("HBHENoiseFilterResultProducer","HBHENoiseFilterResultRun1"),
                                            HBHEfilterR2L=cms.InputTag("HBHENoiseFilterResultProducer","HBHENoiseFilterResultRun2Loose"),
                                            HBHEfilterR2T=cms.InputTag("HBHENoiseFilterResultProducer","HBHENoiseFilterResultRun2Tight"),
                                            HBHEfilterISO=cms.InputTag("HBHENoiseFilterResultProducer","HBHENoiseFilterResultRun1"),
                                            ECALTPfilter=cms.InputTag("EcalDeadCellTriggerPrimitiveFilter"),
                                            ECALSCfilter=cms.InputTag("eeBadScFilter"),
                                            EBRecHits=cms.InputTag("reducedEcalRecHitsEB"),
                                            EERecHits=cms.InputTag("reducedEcalRecHitsEE"),
                                            ESRecHits=cms.InputTag("reducedEcalRecHitsES"),
                                            HcalNoise=cms.InputTag("hcalnoise")
)

# This part is needed if you want to update the BeamHaloSummary information
from RecoMET.METProducers.CSCHaloData_cfi import *
from RecoMET.METProducers.EcalHaloData_cfi import *
from RecoMET.METProducers.HcalHaloData_cfi import *
from RecoMET.METProducers.GlobalHaloData_cfi import *
from RecoMET.METProducers.BeamHaloSummary_cfi import *

process.BeamHaloId = cms.Sequence(CSCHaloData*EcalHaloData*HcalHaloData*GlobalHaloData*BeamHaloSummary)




##___________________________PATH______________________________________________||
process.p = cms.Path(
#    process.BeamHaloId* #Uncomment this if you want to rerun the BeamHaloSummary. By default this line should remain commented
    process.primaryVertexFilter*
    process.bunchSpacingProducer *
    process.CSCTightHaloFilter*
    process.HBHENoiseFilterResultProducer* #produces bools    
#    process.ApplyBaselineHBHENoiseFilter* 
    process.EcalDeadCellTriggerPrimitiveFilter*
    process.pfClusterMetSequence*
    process.pfCaloMetSequence*
    process.condMETSelector *
    process.eeBadScFilter*
    process.goodVertices*
    process.trackingFailureFilter*
    process.EcalDeadCellBoundaryEnergyFilter*
    process.CSCTightHalo2015Filter*
    process.CSCTightHaloTrkMuUnvetoFilter*
    process.globalTightHalo2016Filter * 
    process.globalSuperTightHalo2016Filter * 
    process.HcalStripHaloFilter*
#    process.metCounter*
    process.metScanNtupleMaker ##CH: writes a flat tree
    )

process.e1 = cms.EndPath(
    process.out ##CH: write the skimmed edm file 
    )

##____________________________________________________________________________||





