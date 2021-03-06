from WMCore.Configuration import Configuration
config = Configuration()
config.section_('General')
config.General.transferOutputs = True
config.General.requestName = 'zee_digiraw_v2'
config.section_('JobType')
config.JobType.psetName = 'step2_DIGI_L1_DIGI2RAW_HLT_RAW2DIGI_L1Reco_PU.py'
config.JobType.maxMemoryMB = 3500 #default 2000
config.JobType.pluginName = 'Analysis'
config.JobType.outputFiles = ['step2.root']
config.section_('Data')
config.Data.inputDataset = '/Pythia8_Z30eeJet_pthat30Norm_TuneCUETP8M1_5020GeV_Hydjet_MinBias_5020GeV_PrivMC/dgulhan-Pythia8_Z30eeJet_pthat30Norm_TuneCUETP8M1_5020GeV_cff_GEN_SIM-5874998287b4d3e6316523a609a4b2e6/USER'
config.Data.inputDBS = 'phys03'
config.Data.splitting = "FileBased"
config.Data.unitsPerJob = 1
config.Data.totalUnits = -1
config.Data.publication = True
config.Data.publishDataName = 'Pythia8_Z30eeJet_pthat30Norm_TuneCUETP8M1_5020GeV_cff_GEN_SIM_DIGIRAW_PrivMC_v1'
config.section_('User')
config.section_('Site')
config.Site.whitelist = ['T2_US_MIT']
config.Site.storageSite = 'T2_US_MIT'
