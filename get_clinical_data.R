
#' Load functions
source("Module_A.R")
source("Module_B.R")

#' set data saving path
sPath1 <- "E:/Academic SoIC/SCJ/Dr. Ashish Lal/question 1/clinical_data_coad"

#' choose a cancer type
sCancer <- "COAD"

#' choose some patients
vPatientID <- c("TCGA-A7-A13F", "TCGA-AO-A12B", "TCGA-AR-A1AP", "TCGA-AR-A1AQ",
								"TCGA-AR-A1AS", "TCGA-AR-A1AV", "TCGA-AR-A1AW", "TCGA-BH-A0BZ",
								"TCGA-BH-A0DD", "TCGA-BH-A0DG")


#' =============================================================================
#' Part 1: Downloading Data of 7 different platforms using Module A functions
#' =============================================================================

#' Download somatic mutation data

DownloadBiospecimenClinicalData(cancerType = sCancer, saveFolderName = sPath1, outputFileName = "clinical_file")