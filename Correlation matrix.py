# -*- coding: utf-8 -*-
"""
Created on Thu May 12 16:48:06 2022

@author: Mohammad Mehdi Keramati
"""
import pandas as pd
import numpy as np
from numpy import cov
from scipy.stats import pearsonr
from scipy.stats import spearmanr

Data=pd.read_excel('C:/Users/Mehdi Keramati/Desktop/Medical data project- finalization/Data.xlsx')

Data=Data.drop(columns='ID')
Data=Data.drop(columns='GCSID')

Pearson_folds = Data.corr()
Spearman_folds = Data.corr(method='spearman')



print('###################### Eligibe P-value #############################')
Pearsonr_cofficent, Pearsonr_P_value_Eligible = pearsonr(Data.Eligible, Data["Quality score"])
Spearman_cofficent, Spearman_P_value_Eligible = spearmanr(Data.Eligible, Data["Quality score"])
print('Eligible Pearsonr P_value:',Pearsonr_P_value_Eligible)
print('Eligible Spearman P_value:',Spearman_P_value_Eligible)

print('###################### Participant_age P-value #############################')
Pearsonr_cofficent, Pearsonr_P_value_Participant_age = pearsonr(Data.Participant_age, Data["Quality score"])
Spearman_cofficent, Spearman_P_value_Participant_age = spearmanr(Data.Participant_age, Data["Quality score"])
print('Participant_age Pearsonr P_value:',Pearsonr_P_value_Participant_age)
print('Participant_age Spearman P_value:',Spearman_P_value_Participant_age)

print('###################### Participant_gender P-value #############################')
Pearsonr_cofficent, Pearsonr_P_value_Participant_gender = pearsonr(Data.Participant_gender, Data["Quality score"])
Spearman_cofficent, Spearman_P_value_Participant_gender = spearmanr(Data.Participant_gender, Data["Quality score"])
print('Participant_gender Pearsonr P_value:',Pearsonr_P_value_Participant_gender)
print('Participant_gender Spearman P_value:',Spearman_P_value_Participant_gender)

print('###################### Participant_ethnicity P-value #############################')
Pearsonr_cofficent, Pearsonr_P_value_Participant_ethnicity = pearsonr(Data.Participant_ethnicity, Data["Quality score"])
Spearman_cofficent, Spearman_P_value_Participant_ethnicity = spearmanr(Data.Participant_ethnicity, Data["Quality score"])
print('Participant_ethnicity Pearsonr P_value:',Pearsonr_P_value_Participant_ethnicity)
print('Participant_ethnicity Spearman P_value:',Spearman_P_value_Participant_ethnicity)

print('###################### Intervention_group P-value #############################')
Pearsonr_cofficent, Pearsonr_P_value_Intervention_group = pearsonr(Data.Intervention_group, Data["Quality score"])
Spearman_cofficent, Spearman_P_value_Intervention_group = spearmanr(Data.Intervention_group, Data["Quality score"])
print('Intervention_group Pearsonr P_value:',Pearsonr_P_value_Intervention_group)
print('Intervention_group Spearman P_value:',Spearman_P_value_Intervention_group)

print('###################### City_code P-value #############################')
Pearsonr_cofficent, Pearsonr_P_value_City_code = pearsonr(Data.City_code, Data["Quality score"])
Spearman_cofficent, Spearman_P_value_City_code = spearmanr(Data.City_code, Data["Quality score"])
print('City_code Pearsonr P_value:',Pearsonr_P_value_City_code)
print('City_code Spearman P_value:',Spearman_P_value_City_code)

print('###################### Village_Cluster P-value #############################')
Pearsonr_cofficent, Pearsonr_P_value_Village_Cluster = pearsonr(Data.Village_Cluster, Data["Quality score"])
Spearman_cofficent, Spearman_P_value_Village_Cluster = spearmanr(Data.Village_Cluster, Data["Quality score"])
print('Village_Cluster Pearsonr P_value:',Pearsonr_P_value_Village_Cluster)
print('Village_Cluster Spearman P_value:',Spearman_P_value_Village_Cluster)

print('###################### Village_StateCode P-value #############################')
Pearsonr_cofficent, Pearsonr_P_value_Village_StateCode = pearsonr(Data.Village_StateCode, Data["Quality score"])
Spearman_cofficent, Spearman_P_value_Village_StateCode = spearmanr(Data.Village_StateCode, Data["Quality score"])
print('Village_StateCode Pearsonr P_value:',Pearsonr_P_value_Village_StateCode)
print('Village_StateCode Spearman P_value:',Spearman_P_value_Village_StateCode)

print('###################### Village_Participant_Nubmer P-value #############################')
Pearsonr_cofficent, Pearsonr_P_value_Village_Participant_Nubmer = pearsonr(Data.Village_Participant_Nubmer, Data["Quality score"])
Spearman_cofficent, Spearman_P_value_Village_Participant_Nubmer = spearmanr(Data.Village_Participant_Nubmer, Data["Quality score"])
print('Village_Participant_Nubmer Pearsonr P_value:',Pearsonr_P_value_Village_Participant_Nubmer)
print('Village_Participant_Nubmer Spearman P_value:',Spearman_P_value_Village_Participant_Nubmer)

print('###################### Interviewer_Gender P-value #############################')
Pearsonr_cofficent, Pearsonr_P_value_Interviewer_Gender = pearsonr(Data.Interviewer_Gender, Data["Quality score"])
Spearman_cofficent, Spearman_P_value_Interviewer_Gender = spearmanr(Data.Interviewer_Gender, Data["Quality score"])
print('Interviewer_Gender Pearsonr P_value:',Pearsonr_P_value_Interviewer_Gender)
print('Interviewer_Gender Spearman P_value:',Spearman_P_value_Interviewer_Gender)

print('###################### Interviewer_Education P-value #############################')
Pearsonr_cofficent, Pearsonr_P_value_Interviewer_Education = pearsonr(Data.Interviewer_Education, Data["Quality score"])
Spearman_cofficent, Spearman_P_value_Interviewer_Education = spearmanr(Data.Interviewer_Education, Data["Quality score"])
print('Interviewer_Education Pearsonr P_value:',Pearsonr_P_value_Interviewer_Education)
print('Interviewer_Education Spearman P_value:',Spearman_P_value_Interviewer_Education)

print('###################### Interviewer_Ethnicity P-value #############################')
Pearsonr_cofficent, Pearsonr_P_value_Interviewer_Ethnicity = pearsonr(Data.Interviewer_Ethnicity, Data["Quality score"])
Spearman_cofficent, Spearman_P_value_Interviewer_Ethnicity = spearmanr(Data.Interviewer_Ethnicity, Data["Quality score"])
print('Interviewer_Ethnicity Pearsonr P_value:',Pearsonr_P_value_Interviewer_Ethnicity)
print('Interviewer_Ethnicity Spearman P_value:',Spearman_P_value_Interviewer_Ethnicity)

print('###################### FU_Month P-value #############################')
Pearsonr_cofficent, Pearsonr_P_value_FU_Month = pearsonr(Data.FU_Month, Data["Quality score"])
Spearman_cofficent, Spearman_P_value_FU_Month = spearmanr(Data.FU_Month, Data["Quality score"])
print('FU_Month Pearsonr P_value:',Pearsonr_P_value_FU_Month)
print('FU_Month Spearman P_value:',Spearman_P_value_FU_Month)