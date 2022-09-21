##Packages to import
from dataclasses import dataclass
import pandas as pd
import numpy as np
import math
import statistics
import scipy.stats
import os
import seaborn
from tableone import TableOne, load_dataset

##Importing csv file from API csv file provided from ny.gov
sparcs = pd.read_csv('https://health.data.ny.gov/resource/gnzp-ekau.csv')
sparcs

# get a count of the number of rows and columns
sparcs.shape
sparcs.columns
sparcs.dtypes

## clean the data
# list columns
list(sparcs)
############## COLUMN NAMES ##############
# remove all special characters and whitespace ' ' from column names
sparcs.columns = sparcs.columns.str.replace('[^A-Za-z0-9]+', '_') ## regex 
list(sparcs)

# change all column names to upper case
sparcs.columns = sparcs.columns.str.upper()
# replace all whitespace in column names with an underscore
sparcs.columns = sparcs.columns.str.replace(' ', '_')


##### DATASET #####
sparcs_new = sparcs.copy()
sparcs_new.dtypes
list(sparcs_new)
sparcs_new.head(5)
sparcs_new['LENGTH_OF_STAY']
sparcs_new_columns = ['RACE', 'ETHNICITY','AGE_GROUP', 'LENGTH_OF_STAY']
sparcs_new_categories = ['ETHNICITY', 'LENGTH_OF_STAY']
sparcs_new_groupby = ['ETHNICITY']
# sparcs_new['Vocation'].value_counts()
sparcs_new_table1 = TableOne(sparcs_new, columns=sparcs_new_columns, 
    categorical=sparcs_new_categories, groupby=sparcs_new_groupby, pval=False)
print(sparcs_new_table1.tabulate(tablefmt = "fancy_grid"))
sparcs_new_table1.to_csv('descriptives-nydischarges/data/sparcs_new.csv')




#Data indexes: atlas:(['UNNAMED_0', 'X', 'TYPE', 'ZIPID', 'FIPS_X', 'GISJOIN', 'FIPS_Y', 'ADI_NATRANK', 'ADI_STATERNK'], dtype='object')
###Data indexes: sparcs: (['HEALTH_SERVICE_AREA', 'HOSPITAL_COUNTY','OPERATING_CERTIFICATE_NUMBER', 'FACILITY_ID', 'FACILITY_NAME','AGE_GROUP', 'ZIP_CODE_3_DIGITS', 'GENDER', 
#'RACE', 'ETHNICITY','LENGTH_OF_STAY', 'TYPE_OF_ADMISSION', 'PATIENT_DISPOSITION','DISCHARGE_YEAR', 'CCS_DIAGNOSIS_CODE', 'CCS_DIAGNOSIS_DESCRIPTION',
#'CCS_PROCEDURE_CODE', 'CCS_PROCEDURE_DESCRIPTION', 'APR_DRG_CODE', 'APR_DRG_DESCRIPTION', 'APR_MDC_CODE', 'APR_MDC_DESCRIPTION',
#'APR_SEVERITY_OF_ILLNESS_CODE', 'APR_SEVERITY_OF_ILLNESS_DESCRIPTION', 'APR_RISK_OF_MORTALITY', 'APR_MEDICAL_SURGICAL_DESCRIPTION',
#'PAYMENT_TYPOLOGY_1', 'PAYMENT_TYPOLOGY_2', 'PAYMENT_TYPOLOGY_3', 'BIRTH_WEIGHT', 'ABORTION_EDIT_INDICATOR', 'EMERGENCY_DEPARTMENT_INDICATOR', 'TOTAL_CHARGES', 'TOTAL_COSTS'], dtype='object')

