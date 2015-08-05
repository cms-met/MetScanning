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
process.GlobalTag.globaltag = 'MCRUN2_74_V9A'


##___________________________Input_Files______________________________________||
process.source = cms.Source(
    "PoolSource",
    #fileNames = cms.untracked.vstring("root://eoscms.cern.ch//store/express/Run2015B/ExpressPhysics/FEVT/Express-v1/000/250/985/00000/04380D9C-0F24-E511-9772-02163E0127EF.root")
#    fileNames = cms.untracked.vstring("root://eoscms.cern.ch//store/express/Run2015B/ExpressPhysics/FEVT/Express-v1/000/250/985/00000/8CB978A3-1024-E511-A2E5-02163E011BC8.root")
    #fileNames = cms.untracked.vstring("root://eoscms.cern.ch//store/express/Run2015B/ExpressPhysics/FEVT/Express-v1/000/250/987/00000/D4337B5F-1224-E511-9969-02163E011BB6.root")
    fileNames = cms.untracked.vstring(
#"file:/data/rschoefbeck/pickEvents/nick/pickevents_1.root", 
#"file:/data/rschoefbeck/pickEvents/nick/pickevents_2.root", 
#"file:/data/rschoefbeck/pickEvents/nick/pickevents_3.root", 
#"file:/data/rschoefbeck/pickEvents/nick/pickevents_4.root", 
#"file:/data/rschoefbeck/pickEvents/nick/pickevents_5.root", 
"file:/afs/cern.ch/user/m/mschoene/public/pickevents_17July_RECO.root"
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


##___________________________HCAL_Noise_Filter________________________________||
process.load('CommonTools.RecoAlgos.HBHENoiseFilterResultProducer_cfi')
process.HBHENoiseFilterResultProducer.minZeros = cms.int32(99999)

#process.ApplyBaselineHBHENoiseFilter = cms.EDFilter('BooleanFlagFilter',
#    inputLabel = cms.InputTag('HBHENoiseFilterResultProducer','HBHENoiseFilterResult'),
#    reverseDecision = cms.bool(False)
#)

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

process.load('RecoMET.METFilters.EcalDeadCellBoundaryEnergyFilter_cfi')
process.EcalDeadCellBoundaryEnergyFilter.taggingMode = cms.bool(True)
process.EcalDeadCellBoundaryEnergyFilter.limitDeadCellToChannelStatusEB=cms.vint32(12, 13, 14)
process.EcalDeadCellBoundaryEnergyFilter.limitDeadCellToChannelStatusEE=cms.vint32(12, 13, 14)

process.load('RecoMET.METFilters.eeBadScFilter_cfi')
process.eeBadScFilter.taggingMode = cms.bool(True)

process.primaryVertexFilter = cms.EDFilter("GoodVertexFilter",
                                           vertexCollection = cms.InputTag('offlinePrimaryVertices'),
                                           minimumNDOF = cms.uint32(4) ,
                                           maxAbsZ = cms.double(24),
                                           maxd0 = cms.double(2)
)

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


##___________________________PATH______________________________________________||
process.p = cms.Path(
    process.primaryVertexFilter*
    process.CSCTightHaloFilter*
    process.HBHENoiseFilterResultProducer* #produces bools
#    process.ApplyBaselineHBHENoiseFilter* 
    process.EcalDeadCellTriggerPrimitiveFilter*
#    process.pfClusterMetSequence*
#    process.pfCaloMetSequence*
    process.eeBadScFilter*
    process.primaryVertexFilter*
    process.goodVertices* 
    process.trackingFailureFilter*
    process.EcalDeadCellBoundaryEnergyFilter
#    *process.condMETSelector
#    *process.metCounter
#   *process.metScanNtupleMaker ##CH: writes a flat tree
    )

process.e1 = cms.EndPath(
    process.out ##CH: write the skimmed edm file 
    )

##____________________________________________________________________________||

