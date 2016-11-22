import FWCore.ParameterSet.Config as cms

##____________________________________________________________________________||
process = cms.Process("SKIM")


##____________________________________________________________________________||
process.load("FWCore.MessageLogger.MessageLogger_cfi")

process.load("Configuration.StandardSequences.GeometryRecoDB_cff")
#process.load("Configuration.StandardSequences.MagneticField_cff")
process.load('Configuration.StandardSequences.MagneticField_AutoFromDBCurrent_cff')

process.load("SimGeneral.HepPDTESSource.pythiapdt_cfi")

process.load("RecoLocalCalo.EcalRecAlgos.EcalSeverityLevelESProducer_cfi")

##___________________________Global_Tag_______________________________________||
#process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
#from Configuration.AlCa.GlobalTag import GlobalTag
#process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:run2_mc', '')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_condDBv2_cff')
#process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
#process.GlobalTag.globaltag = 'GR_P_V56::All'
process.load("RecoLuminosity.LumiProducer.bunchSpacingProducer_cfi")
process.GlobalTag.globaltag = '80X_dataRun2_Express_v6'    #'80X_dataRun2_Prompt_v8'
#80X_dataRun2_Express_v5'


##___________________________Input_Files______________________________________||

#process.source = cms.Source("PoolSource", fileNames = cms.untracked.vstring())

process.source = cms.Source(
    "PoolSource",
    fileNames = cms.untracked.vstring(
        "/store/data/Run2016B/MET/AOD/01Jul2016-v1/20000/B0368187-794F-E611-9A86-02163E01156C.root"

)
    )

##___________________________EDM_Output_File__________________________________||
process.out = cms.OutputModule(
    "PoolOutputModule",
    isReco = cms.bool(False),
    fileName = cms.untracked.string('skim.root'),
    SelectEvents   = cms.untracked.PSet( SelectEvents = cms.vstring('p') ),
    outputCommands = cms.untracked.vstring(
        'keep *'
#        'keep *_pfClusterMet_*_*', 'keep *_CSCTightHaloFilter_*_*', 'keep *_HBHENoiseFilterResultProducer_*_*'
        )
    )


##____________________________________________________________________________||
process.options   = cms.untracked.PSet(wantSummary = cms.untracked.bool(True))

#process.options = cms.untracked.PSet(SkipEvent = cms.untracked.vstring('ProductNotFound'))

process.MessageLogger.cerr.FwkReport.reportEvery = 50
process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(10) )


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

process.load('RecoMET.METFilters.HcalStripHaloFilter_cfi')
process.HcalStripHaloFilter.taggingMode = cms.bool(True)

process.goodVertices = cms.EDFilter(
  "VertexSelector",
  filter = cms.bool(False),
  isReco = cms.bool(False),
  src = cms.InputTag("offlinePrimaryVertices"),
  cut = cms.string("!isFake && ndof > 4 && abs(z) <= 24 && position.rho < 2")
)
process.load('RecoMET.METFilters.trackingFailureFilter_cfi')
process.trackingFailureFilter.taggingMode = cms.bool(True)

process.load('RecoMET.METFilters.EcalDeadCellTriggerPrimitiveFilter_cfi')
process.EcalDeadCellTriggerPrimitiveFilter.taggingMode = cms.bool(True)

process.load('RecoMET.METFilters.eeBadScFilter_cfi')
process.eeBadScFilter.taggingMode = cms.bool(True)

process.load('RecoMET.METFilters.BadChargedCandidateFilter_cfi')
process.BadChargedCandidateFilter.taggingMode = cms.bool(True)

process.load('RecoMET.METFilters.BadPFMuonFilter_cfi')
process.BadPFMuonFilter.taggingMode = cms.bool(True)
#process.BadPFMuonFilter.debug = cms.bool(True) 

process.load('RecoMET.METFilters.BadChargedCandidateSummer16Filter_cfi')
process.BadChargedCandidateSummer16Filter.taggingMode = cms.bool(True)

process.load('RecoMET.METFilters.BadPFMuonSummer16Filter_cfi')
process.BadPFMuonSummer16Filter.taggingMode = cms.bool(True)

process.primaryVertexFilter = cms.EDFilter("GoodVertexFilter",
                                           isReco = cms.bool(False),
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
   isReco = cms.bool(False),
   decay = cms.string("caloMet pfMet"),
   cut = cms.string("(daughter(0).pt > 80) || (daughter(1).pt > 80)" ) 
   )

process.metCounter = cms.EDFilter(
    "CandViewCountFilter",
    isReco = cms.bool(False),
    src = cms.InputTag("condMETSelector"),
    minNumber = cms.uint32(1),
    )


process.metScanNtupleMaker = cms.EDAnalyzer("METScanningNtupleMaker",
                                            isReco = cms.bool(False),
                                            rootOutputFile=cms.string("tuple.root"),
                                            muonCandidates=cms.InputTag("muons"),
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
                                            BadChCandFilter=cms.InputTag("BadChargedCandidateFilter"),
                                            BadPFMuon=cms.InputTag("BadPFMuonFilter"),
                                            BadChCandSummer16Filter=cms.InputTag("BadChargedCandidateSummer16Filter"),
                                            BadPFMuonOld=cms.InputTag("BadPFMuonSummer16Filter"),
                                            OfflinePrimaryVertices = cms.InputTag("offlinePrimaryVertices"),
                                            HcalNoise=cms.InputTag("hcalnoise")
                                            
)

# This part is needed if you want to update the BeamHaloSummary information
from RecoMET.METProducers.CSCHaloData_cfi import *
from RecoMET.METProducers.EcalHaloData_cfi import *
from RecoMET.METProducers.HcalHaloData_cfi import *
from RecoMET.METProducers.GlobalHaloData_cfi import *
from RecoMET.METProducers.BeamHaloSummary_cfi import *

#process.BeamHaloId = cms.Sequence(CSCHaloData*EcalHaloData*HcalHaloData*GlobalHaloData*BeamHaloSummary)


##___________________________PATH______________________________________________||
process.p = cms.Path(
#    process.BeamHaloId* #Uncomment this if you want to rerun the BeamHaloSummary. By default this line should remain commented
   
    process.primaryVertexFilter*
    process.bunchSpacingProducer *
    process.condMETSelector *
    process.metCounter* #uncomment this line to apply a met cut
    process.CSCTightHaloFilter*
    process.HBHENoiseFilterResultProducer* #produces bools    
#    process.ApplyBaselineHBHENoiseFilter* 
    process.EcalDeadCellTriggerPrimitiveFilter*
    process.eeBadScFilter*
    process.goodVertices*
    process.trackingFailureFilter*
    process.EcalDeadCellBoundaryEnergyFilter*
    process.CSCTightHalo2015Filter*
    process.CSCTightHaloTrkMuUnvetoFilter*
    process.globalTightHalo2016Filter * 
    process.globalSuperTightHalo2016Filter * 
    process.HcalStripHaloFilter*
    process.BadChargedCandidateFilter*
    process.BadPFMuonFilter*
    process.BadChargedCandidateSummer16Filter*
    process.BadPFMuonSummer16Filter*
    process.metScanNtupleMaker ##CH: writes a flat tree
    )

#process.e1 = cms.EndPath(
 #   process.out ##CH: write the skimmed edm file 
  #  )
