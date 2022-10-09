# -*- coding: utf-8 -*-
"""
Created on Tue Jun 28 11:14:31 2022

@author: Mohammad Mehdi Keramati
"""
# Libraries
import pandas as pd
import numpy as np
from numpy import cov
from scipy.stats import pearsonr
from scipy.stats import spearmanr
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import MinMaxScaler
import seaborn as sb
import matplotlib.pyplot as plt


# Import
Data = pd.read_excel('C:/Users/Mehdi Keramati/Desktop/Medical data project- finalization/Data.xlsx')

le = LabelEncoder()

# Combining two featurs
Data['Eligible_Part/gender'] = (Data.Eligible.astype(str) +
                                "_" + Data.Participant_gender.astype(str))
Data['Eligible_Part/gender'] = le.fit_transform(Data['Eligible_Part/gender'])
Data["Eligible_Part/ethnicity"] = (Data.Eligible.astype(str) +
                                   "_" + Data.Participant_ethnicity.astype(str))
Data['Eligible_Part/ethnicity'] = le.fit_transform(
    Data['Eligible_Part/ethnicity'])
Data["Eligible_Inter/group"] = (Data.Eligible.astype(str) +
                                "_" + Data.Intervention_group.astype(str))
Data['Eligible_Inter/group'] = le.fit_transform(Data['Eligible_Inter/group'])
Data["Eligible_City/code"] = (Data.Eligible.astype(str) +
                              "_" + Data.City_code.astype(str))
Data['Eligible_City/code'] = le.fit_transform(Data['Eligible_City/code'])
Data["Eligible_Village/code"] = (Data.Eligible.astype(str) +
                                 "_" + Data.Village_StateCode.astype(str))
Data['Eligible_Village/code'] = le.fit_transform(Data['Eligible_Village/code'])
Data["Eligible_Inter/gender"] = (Data.Eligible.astype(str) +
                                 "_" + Data.Interviewer_Gender.astype(str))
Data['Eligible_Inter/gender'] = le.fit_transform(Data['Eligible_Inter/gender'])
Data["Eligible_Inter/education"] = (Data.Eligible.astype(
    str) + "_" + Data.Interviewer_Education.astype(str))
Data['Eligible_Inter/education'] = le.fit_transform(
    Data['Eligible_Inter/education'])
Data["Eligible_Inter/ethnicity"] = (Data.Eligible.astype(
    str) + "_" + Data.Interviewer_Ethnicity.astype(str))
Data['Eligible_Inter/ethnicity'] = le.fit_transform(
    Data['Eligible_Inter/ethnicity'])
Data["Part/gender_Part/ethnicity"] = (Data.Participant_gender.astype(
    str) + "_" + Data.Participant_ethnicity.astype(str))
Data['Part/gender_Part/ethnicity'] = le.fit_transform(
    Data['Part/gender_Part/ethnicity'])
Data["Part/gender_Inter/group"] = (Data.Participant_gender.astype(
    str) + "_" + Data.Intervention_group.astype(str))
Data['Part/gender_Inter/group'] = le.fit_transform(
    Data['Part/gender_Inter/group'])
Data["Part/gender_City/code"] = (Data.Participant_gender.astype(str) +
                                 "_" + Data.City_code.astype(str))
Data['Part/gender_City/code'] = le.fit_transform(Data['Part/gender_City/code'])
Data["Part/gender_Village/code"] = (Data.Participant_gender.astype(
    str) + "_" + Data.Village_StateCode.astype(str))
Data['Part/gender_Village/code'] = le.fit_transform(
    Data['Part/gender_Village/code'])
Data["Part/gender_Inter/gender"] = (Data.Participant_gender.astype(
    str) + "_" + Data.Interviewer_Gender.astype(str))
Data['Part/gender_Inter/gender'] = le.fit_transform(
    Data['Part/gender_Inter/gender'])
Data["Part/gender_Inter/education"] = (Data.Participant_gender.astype(
    str) + "_" + Data.Interviewer_Education.astype(str))
Data['Part/gender_Inter/education'] = le.fit_transform(
    Data['Part/gender_Inter/education'])
Data["Part/gender_Inter/ethnicity"] = (Data.Participant_gender.astype(
    str) + "_" + Data.Interviewer_Ethnicity.astype(str))
Data['Part/gender_Inter/ethnicity'] = le.fit_transform(
    Data['Part/gender_Inter/ethnicity'])
Data["Part/ethnicity_Inter/group"] = (Data.Participant_ethnicity.astype(
    str) + "_" + Data.Intervention_group.astype(str))
Data['Part/ethnicity_Inter/group'] = le.fit_transform(
    Data['Part/ethnicity_Inter/group'])
Data["Part/ethnicity_City/code"] = (
    Data.Participant_ethnicity.astype(str) + "_" + Data.City_code.astype(str))
Data['Part/ethnicity_City/code'] = le.fit_transform(
    Data['Part/ethnicity_City/code'])
Data["Part/ethnicity_Village/code"] = (Data.Participant_ethnicity.astype(
    str) + "_" + Data.Village_StateCode.astype(str))
Data['Part/ethnicity_Village/code'] = le.fit_transform(
    Data['Part/ethnicity_Village/code'])
Data["Part/ethnicity_Inter/gender"] = (Data.Participant_ethnicity.astype(
    str) + "_" + Data.Interviewer_Gender.astype(str))
Data['Part/ethnicity_Inter/gender'] = le.fit_transform(
    Data['Part/ethnicity_Inter/gender'])
Data["Part/ethnicity_Inter/education"] = (Data.Participant_ethnicity.astype(
    str) + "_" + Data.Interviewer_Education.astype(str))
Data['Part/ethnicity_Inter/education'] = le.fit_transform(
    Data['Part/ethnicity_Inter/education'])
Data["Part/ethnicity_Inter/ethnicity"] = (Data.Participant_ethnicity.astype(
    str) + "_" + Data.Interviewer_Ethnicity.astype(str))
Data['Part/ethnicity_Inter/ethnicity'] = le.fit_transform(
    Data['Part/ethnicity_Inter/ethnicity'])
Data["group_City/code"] = (Data.Intervention_group.astype(str) +
                           "_" + Data.City_code.astype(str))
Data['group_City/code'] = le.fit_transform(Data['group_City/code'])
Data["group_Village/code"] = (Data.Intervention_group.astype(str) +
                              "_" + Data.Village_StateCode.astype(str))
Data['group_Village/code'] = le.fit_transform(Data['group_Village/code'])
Data["group_Inter/gender"] = (Data.Intervention_group.astype(str) +
                              "_" + Data.Interviewer_Gender.astype(str))
Data['group_Inter/gender'] = le.fit_transform(Data['group_Inter/gender'])
Data["group_Inter/education"] = (Data.Intervention_group.astype(
    str) + "_" + Data.Interviewer_Education.astype(str))
Data['group_Inter/education'] = le.fit_transform(Data['group_Inter/education'])
Data["group_Inter/ethnicity"] = (Data.Intervention_group.astype(
    str) + "_" + Data.Interviewer_Ethnicity.astype(str))
Data['group_Inter/ethnicity'] = le.fit_transform(Data['group_Inter/ethnicity'])
Data["City/code_Village/Code"] = (Data.City_code.astype(str) +
                                  "_" + Data.Village_StateCode.astype(str))
Data['City/code_Village/Code'] = le.fit_transform(
    Data['City/code_Village/Code'])
Data["City/code_Inter/gender"] = (Data.City_code.astype(str) +
                                  "_" + Data.Interviewer_Gender.astype(str))
Data['City/code_Inter/gender'] = le.fit_transform(
    Data['City/code_Inter/gender'])
Data["City/code_Inter/education"] = (Data.City_code.astype(
    str) + "_" + Data.Interviewer_Education.astype(str))
Data['City/code_Inter/education'] = le.fit_transform(
    Data['City/code_Inter/education'])
Data["City/code_Inter/ethnicity"] = (Data.City_code.astype(
    str) + "_" + Data.Interviewer_Ethnicity.astype(str))
Data['City/code_Inter/ethnicity'] = le.fit_transform(
    Data['City/code_Inter/ethnicity'])
Data["Village/code_Inter/gender"] = (Data.Village_StateCode.astype(
    str) + "_" + Data.Interviewer_Gender.astype(str))
Data['Village/code_Inter/gender'] = le.fit_transform(
    Data['Village/code_Inter/gender'])
Data["Village/code_Inter/education"] = (Data.Village_StateCode.astype(
    str) + "_" + Data.Interviewer_Education.astype(str))
Data['Village/code_Inter/education'] = le.fit_transform(
    Data['Village/code_Inter/education'])
Data["Village/code_Inter/ethnicity"] = (Data.Village_StateCode.astype(
    str) + "_" + Data.Interviewer_Ethnicity.astype(str))
Data['Village/code_Inter/ethnicity'] = le.fit_transform(
    Data['Village/code_Inter/ethnicity'])
Data["Inter/gender_Inter/education"] = (Data.Interviewer_Gender.astype(
    str) + "_" + Data.Interviewer_Education.astype(str))
Data['Inter/gender_Inter/education'] = le.fit_transform(
    Data['Inter/gender_Inter/education'])
Data["Inter/gender_Inter/ethnicity"] = (Data.Interviewer_Gender.astype(
    str) + "_" + Data.Interviewer_Ethnicity.astype(str))
Data['Inter/gender_Inter/ethnicity'] = le.fit_transform(
    Data['Inter/gender_Inter/ethnicity'])
Data["Inter/education_Inter/ethnicity"] = (Data.Interviewer_Education.astype(
    str) + "_" + Data.Interviewer_Ethnicity.astype(str))
Data['Inter/education_Inter/ethnicity'] = le.fit_transform(
    Data['Inter/education_Inter/ethnicity'])

# Combining three featurs 
Data["Eligible_Part/gender_Part/ethnicity"] = (Data.Eligible.astype(
    str) + "_" + Data.Participant_gender.astype(str) + "_" + Data.Participant_ethnicity.astype(str))
Data['Eligible_Part/gender_Part/ethnicity'] = le.fit_transform(
    Data['Eligible_Part/gender_Part/ethnicity'])
Data["Eligible_Part/ethnicity_group"] = (Data.Eligible.astype(
    str) + "_" + Data.Participant_ethnicity.astype(str) + "_" + Data.Intervention_group.astype(str))
Data['Eligible_Part/ethnicity_group'] = le.fit_transform(
    Data['Eligible_Part/ethnicity_group'])
Data["Eligible_group_City/code"] = (Data.Eligible.astype(
    str) + "_" + Data.Intervention_group.astype(str) + "_" + Data.City_code.astype(str))
Data['Eligible_group_City/code'] = le.fit_transform(
    Data['Eligible_group_City/code'])
Data["Eligible_City/code_Village/code"] = (Data.Eligible.astype(
    str) + "_" + Data.City_code.astype(str) + "_" + Data.Village_StateCode.astype(str))
Data['Eligible_City/code_Village/code'] = le.fit_transform(
    Data['Eligible_City/code_Village/code'])
Data["Eligible_Village/code_Inter/gender"] = (Data.Eligible.astype(
    str) + "_" + Data.Village_StateCode.astype(str) + "_" + Data.Interviewer_Gender.astype(str))
Data['Eligible_Village/code_Inter/gender'] = le.fit_transform(
    Data['Eligible_Village/code_Inter/gender'])
Data["Eligible_Inter/gender_Inter/education"] = (Data.Eligible.astype(
    str) + "_" + Data.Interviewer_Gender.astype(str) + "_" + Data.Interviewer_Education.astype(str))
Data['Eligible_Inter/gender_Inter/education'] = le.fit_transform(
    Data['Eligible_Inter/gender_Inter/education'])
Data["Eligible_Inter/education_Inter/ethnicity"] = (Data.Eligible.astype(
    str) + "_" + Data.Interviewer_Education.astype(str) + "_" + Data.Interviewer_Ethnicity.astype(str))
Data['Eligible_Inter/education_Inter/ethnicity'] = le.fit_transform(
    Data['Eligible_Inter/education_Inter/ethnicity'])
Data["Part/gender_Part/ethnicity_group"] = (Data.Participant_gender.astype(
    str) + "_" + Data.Participant_ethnicity.astype(str) + "_" + Data.Intervention_group.astype(str))
Data['Part/gender_Part/ethnicity_group'] = le.fit_transform(
    Data['Part/gender_Part/ethnicity_group'])
Data["Part/gender_group_City/code"] = (Data.Participant_gender.astype(
    str) + "_" + Data.Intervention_group.astype(str) + "_" + Data.City_code.astype(str))
Data['Part/gender_group_City/code'] = le.fit_transform(
    Data['Part/gender_group_City/code'])
Data["Part/gender_City/code_Village/code"] = (Data.Participant_gender.astype(
    str) + "_" + Data.City_code.astype(str) + "_" + Data.Village_StateCode.astype(str))
Data['Part/gender_City/code_Village/code'] = le.fit_transform(
    Data['Part/gender_City/code_Village/code'])
Data["Part/gender_Village/code_Inter/gender"] = (Data.Participant_gender.astype(
    str) + "_" + Data.Village_StateCode.astype(str) + "_" + Data.Interviewer_Gender.astype(str))
Data['Part/gender_Village/code_Inter/gender'] = le.fit_transform(
    Data['Part/gender_Village/code_Inter/gender'])
Data["Part/gender_Inter/gender_Inter/education"] = (Data.Participant_gender.astype(
    str) + "_" + Data.Interviewer_Gender.astype(str) + "_" + Data.Interviewer_Education.astype(str))
Data['Part/gender_Inter/gender_Inter/education'] = le.fit_transform(
    Data['Part/gender_Inter/gender_Inter/education'])
Data["Part/gender_Inter/education_Inter/ethnicity"] = (Data.Participant_gender.astype(
    str) + "_" + Data.Interviewer_Education.astype(str) + "_" + Data.Interviewer_Ethnicity.astype(str))
Data['Part/gender_Inter/education_Inter/ethnicity'] = le.fit_transform(
    Data['Part/gender_Inter/education_Inter/ethnicity'])
Data["Part/ethnicity_group_City/code"] = (Data.Participant_ethnicity.astype(
    str) + "_" + Data.Intervention_group.astype(str) + "_" + Data.City_code.astype(str))
Data['Part/ethnicity_group_City/code'] = le.fit_transform(
    Data['Part/ethnicity_group_City/code'])
Data["Part/ethnicity_City/code_Village/code"] = (Data.Participant_ethnicity.astype(
    str) + "_" + Data.City_code.astype(str) + "_" + Data.Village_StateCode.astype(str))
Data['Part/ethnicity_City/code_Village/code'] = le.fit_transform(
    Data['Part/ethnicity_City/code_Village/code'])
Data["Part/ethnicity_Village/code_Inter/gender"] = (Data.Participant_ethnicity.astype(
    str) + "_" + Data.Village_StateCode.astype(str) + "_" + Data.Interviewer_Gender.astype(str))
Data['Part/ethnicity_Village/code_Inter/gender'] = le.fit_transform(
    Data['Part/ethnicity_Village/code_Inter/gender'])
Data["Part/ethnicity_Inter/gender_Inter/education"] = (Data.Participant_ethnicity.astype(
    str) + "_" + Data.Interviewer_Gender.astype(str) + "_" + Data.Interviewer_Education.astype(str))
Data['Part/ethnicity_Inter/gender_Inter/education'] = le.fit_transform(
    Data['Part/ethnicity_Inter/gender_Inter/education'])
Data["Part/ethnicity_Inter/education_Inter/ethnicity"] = (Data.Participant_ethnicity.astype(
    str) + "_" + Data.Interviewer_Education.astype(str) + "_" + Data.Interviewer_Ethnicity.astype(str))
Data['Part/ethnicity_Inter/education_Inter/ethnicity'] = le.fit_transform(
    Data['Part/ethnicity_Inter/education_Inter/ethnicity'])
Data["group_City/code_Village/code"] = (Data.Intervention_group.astype(
    str) + "_" + Data.City_code.astype(str) + "_" + Data.Village_StateCode.astype(str))
Data['group_City/code_Village/code'] = le.fit_transform(
    Data['group_City/code_Village/code'])
Data["group_Village/code_Inter/gender"] = (Data.Intervention_group.astype(
    str) + "_" + Data.Village_StateCode.astype(str) + "_" + Data.Interviewer_Gender.astype(str))
Data['group_Village/code_Inter/gender'] = le.fit_transform(
    Data['group_Village/code_Inter/gender'])
Data["group_Inter/gender_Inter/education"] = (Data.Intervention_group.astype(
    str) + "_" + Data.Interviewer_Gender.astype(str) + "_" + Data.Interviewer_Education.astype(str))
Data['group_Inter/gender_Inter/education'] = le.fit_transform(
    Data['group_Inter/gender_Inter/education'])
Data["group_Inter/education_Inter/ethnicity"] = (Data.Intervention_group.astype(
    str) + "_" + Data.Interviewer_Education.astype(str) + "_" + Data.Interviewer_Ethnicity.astype(str))
Data['group_Inter/education_Inter/ethnicity'] = le.fit_transform(
    Data['group_Inter/education_Inter/ethnicity'])
Data["City/code_Village/code_Inter/gender"] = (Data.City_code.astype(
    str) + "_" + Data.Village_StateCode.astype(str) + "_" + Data.Interviewer_Gender.astype(str))
Data['City/code_Village/code_Inter/gender'] = le.fit_transform(
    Data['City/code_Village/code_Inter/gender'])
Data["City/code_Inter/gender_Inter/education"] = (Data.City_code.astype(
    str) + "_" + Data.Interviewer_Gender.astype(str) + "_" + Data.Interviewer_Education.astype(str))
Data['City/code_Inter/gender_Inter/education'] = le.fit_transform(
    Data['City/code_Inter/gender_Inter/education'])
Data["City/code_Inter/education_Inter/ethnicity"] = (Data.City_code.astype(
    str) + "_" + Data.Interviewer_Education.astype(str) + "_" + Data.Interviewer_Ethnicity.astype(str))
Data['City/code_Inter/education_Inter/ethnicity'] = le.fit_transform(
    Data['City/code_Inter/education_Inter/ethnicity'])
Data["Village/code_Inter/gender_Inter/education"] = (Data.Village_StateCode.astype(
    str) + "_" + Data.Interviewer_Gender.astype(str) + "_" + Data.Interviewer_Education.astype(str))
Data['Village/code_Inter/gender_Inter/education'] = le.fit_transform(
    Data['Village/code_Inter/gender_Inter/education'])
Data["Village/code_Inter/education_Inter/ethnicity"] = (Data.Village_StateCode.astype(
    str) + "_" + Data.Interviewer_Education.astype(str) + "_" + Data.Interviewer_Ethnicity.astype(str))
Data['Village/code_Inter/education_Inter/ethnicity'] = le.fit_transform(
    Data['Village/code_Inter/education_Inter/ethnicity'])
Data["Inter/gender_Inter/education_Inter/ethnicity"] = (Data.Interviewer_Gender.astype(
    str) + "_" + Data.Interviewer_Education.astype(str) + "_" + Data.Interviewer_Ethnicity.astype(str))
Data['Inter/gender_Inter/education_Inter/ethnicity'] = le.fit_transform(
    Data['Inter/gender_Inter/education_Inter/ethnicity'])

#Combining four featurs 
Data["Eligible_Part/gender_Part/ethnicity_group"] = (Data.Eligible.astype(
    str) + "_" + Data.Participant_gender.astype(str) + "_" + Data.Participant_ethnicity.astype(str) + "_" + Data.Intervention_group.astype(str))
Data['Eligible_Part/gender_Part/ethnicity_group'] = le.fit_transform(
    Data['Eligible_Part/gender_Part/ethnicity_group'])
Data["Eligible_Part/gender_Part/ethnicity_City/code"] = (Data.Eligible.astype(
    str) + "_" + Data.Participant_gender.astype(str) + "_" + Data.Participant_ethnicity.astype(str) + "_" + Data.City_code.astype(str))
Data['Eligible_Part/gender_Part/ethnicity_City/code'] = le.fit_transform(
    Data['Eligible_Part/gender_Part/ethnicity_City/code'])
Data["Eligible_Part/gender_Part/ethnicity_Village/code"] = (Data.Eligible.astype(
    str) + "_" + Data.Participant_gender.astype(str) + "_" + Data.Participant_ethnicity.astype(str) + "_" + Data.Village_StateCode.astype(str))
Data['Eligible_Part/gender_Part/ethnicity_Village/code'] = le.fit_transform(
    Data['Eligible_Part/gender_Part/ethnicity_Village/code'])
Data["Eligible_Part/gender_Part/ethnicity_Inter/gender"] = (Data.Eligible.astype(
    str) + "_" + Data.Participant_gender.astype(str) + "_" + Data.Participant_ethnicity.astype(str) + "_" + Data.Interviewer_Gender.astype(str))
Data['Eligible_Part/gender_Part/ethnicity_Inter/gender'] = le.fit_transform(
    Data['Eligible_Part/gender_Part/ethnicity_Inter/gender'])
Data["Eligible_Part/gender_Part/ethnicity_Inter/education"] = (Data.Eligible.astype(
    str) + "_" + Data.Participant_gender.astype(str) + "_" + Data.Participant_ethnicity.astype(str) + "_" + Data.Interviewer_Education.astype(str))
Data['Eligible_Part/gender_Part/ethnicity_Inter/education'] = le.fit_transform(
    Data['Eligible_Part/gender_Part/ethnicity_Inter/education'])
Data["Eligible_Part/gender_Part/ethnicity_Inter/ethnicity"] = (Data.Eligible.astype(
    str) + "_" + Data.Participant_gender.astype(str) + "_" + Data.Participant_ethnicity.astype(str) + "_" + Data.Interviewer_Ethnicity.astype(str))
Data['Eligible_Part/gender_Part/ethnicity_Inter/ethnicity'] = le.fit_transform(
    Data['Eligible_Part/gender_Part/ethnicity_Inter/ethnicity'])
Data["Part/gender_Part/ethnicity_group_City/code"] = (Data.Participant_gender.astype(
    str) + "_" + Data.Participant_ethnicity.astype(str) + "_" + Data.Intervention_group.astype(str) + "_" + Data.City_code.astype(str))
Data['Part/gender_Part/ethnicity_group_City/code'] = le.fit_transform(
    Data['Part/gender_Part/ethnicity_group_City/code'])
Data["Part/gender_Part/ethnicity_group_Village/code"] = (Data.Participant_gender.astype(
    str) + "_" + Data.Participant_ethnicity.astype(str) + "_" + Data.Intervention_group.astype(str) + "_" + Data.Village_StateCode.astype(str))
Data['Part/gender_Part/ethnicity_group_Village/code'] = le.fit_transform(
    Data['Part/gender_Part/ethnicity_group_Village/code'])
Data["Part/gender_Part/ethnicity_group_Inter/gender"] = (Data.Participant_gender.astype(
    str) + "_" + Data.Participant_ethnicity.astype(str) + "_" + Data.Intervention_group.astype(str) + "_" + Data.Interviewer_Gender.astype(str))
Data['Part/gender_Part/ethnicity_group_Inter/gender'] = le.fit_transform(
    Data['Part/gender_Part/ethnicity_group_Inter/gender'])
Data["Part/gender_Part/ethnicity_group_Inter/education"] = (Data.Participant_gender.astype(
    str) + "_" + Data.Participant_ethnicity.astype(str) + "_" + Data.Intervention_group.astype(str) + "_" + Data.Interviewer_Education.astype(str))
Data['Part/gender_Part/ethnicity_group_Inter/education'] = le.fit_transform(
    Data['Part/gender_Part/ethnicity_group_Inter/education'])
Data["Part/gender_Part/ethnicity_group_Inter/ethnicity"] = (Data.Participant_gender.astype(
    str) + "_" + Data.Participant_ethnicity.astype(str) + "_" + Data.Intervention_group.astype(str) + "_" + Data.Interviewer_Ethnicity.astype(str))
Data['Part/gender_Part/ethnicity_group_Inter/ethnicity'] = le.fit_transform(
    Data['Part/gender_Part/ethnicity_group_Inter/ethnicity'])
Data["Part/ethnicity_group_City/code_Village/code"] = (Data.Participant_ethnicity.astype(
    str) + "_" + Data.Intervention_group.astype(str) + "_" + Data.City_code.astype(str) + "_" + Data.Village_StateCode.astype(str))
Data['Part/ethnicity_group_City/code_Village/code'] = le.fit_transform(
    Data['Part/ethnicity_group_City/code_Village/code'])
Data["Part/ethnicity_group_City/code_Inter/gender"] = (Data.Participant_ethnicity.astype(
    str) + "_" + Data.Intervention_group.astype(str) + "_" + Data.City_code.astype(str) + "_" + Data.Interviewer_Gender.astype(str))
Data['Part/ethnicity_group_City/code_Inter/gender'] = le.fit_transform(
    Data['Part/ethnicity_group_City/code_Inter/gender'])
Data["Part/ethnicity_group_City/code_Inter/education"] = (Data.Participant_ethnicity.astype(
    str) + "_" + Data.Intervention_group.astype(str) + "_" + Data.City_code.astype(str) + "_" + Data.Interviewer_Education.astype(str))
Data['Part/ethnicity_group_City/code_Inter/education'] = le.fit_transform(
    Data['Part/ethnicity_group_City/code_Inter/education'])
Data["Part/ethnicity_group_City/code_Inter/ethnicity"] = (Data.Participant_ethnicity.astype(
    str) + "_" + Data.Intervention_group.astype(str) + "_" + Data.City_code.astype(str) + "_" + Data.Interviewer_Ethnicity.astype(str))
Data['Part/ethnicity_group_City/code_Inter/ethnicity'] = le.fit_transform(
    Data['Part/ethnicity_group_City/code_Inter/ethnicity'])
Data["group_City/code_Village/code_Inter/gender"] = (Data.Intervention_group.astype(
    str) + "_" + Data.City_code.astype(str) + "_" + Data.Village_StateCode.astype(str) + "_" + Data.Interviewer_Gender.astype(str))
Data['group_City/code_Village/code_Inter/gender'] = le.fit_transform(
    Data['group_City/code_Village/code_Inter/gender'])
Data["group_City/code_Village/code_Inter/education"] = (Data.Intervention_group.astype(
    str) + "_" + Data.City_code.astype(str) + "_" + Data.Village_StateCode.astype(str) + "_" + Data.Interviewer_Education.astype(str))
Data['group_City/code_Village/code_Inter/education'] = le.fit_transform(
    Data['group_City/code_Village/code_Inter/education'])
Data["group_City/code_Village/code_Inter/ethnicity"] = (Data.Intervention_group.astype(
    str) + "_" + Data.City_code.astype(str) + "_" + Data.Village_StateCode.astype(str) + "_" + Data.Interviewer_Ethnicity.astype(str))
Data['group_City/code_Village/code_Inter/ethnicity'] = le.fit_transform(
    Data['group_City/code_Village/code_Inter/ethnicity'])
Data["City/code_Village/code_Inter/gender_Inter/education"] = (Data.City_code.astype(
    str) + "_" + Data.Village_StateCode.astype(str) + "_" + Data.Interviewer_Gender.astype(str) + "_" + Data.Interviewer_Education.astype(str))
Data['City/code_Village/code_Inter/gender_Inter/education'] = le.fit_transform(
    Data['City/code_Village/code_Inter/gender_Inter/education'])
Data["City/code_Village/code_Inter/gender_Inter/ethnicity"] = (Data.City_code.astype(
    str) + "_" + Data.Village_StateCode.astype(str) + "_" + Data.Interviewer_Gender.astype(str) + "_" + Data.Interviewer_Ethnicity.astype(str))
Data['City/code_Village/code_Inter/gender_Inter/ethnicity'] = le.fit_transform(
    Data['City/code_Village/code_Inter/gender_Inter/ethnicity'])
Data["Village/code_Inter/gender_Inter/education_Inter/ethnicity"] = (Data.Village_StateCode.astype(
    str) + "_" + Data.Interviewer_Gender.astype(str) + "_" + Data.Interviewer_Education.astype(str) + "_" + Data.Interviewer_Ethnicity.astype(str))
Data['Village/code_Inter/gender_Inter/education_Inter/ethnicity'] = le.fit_transform(
    Data['Village/code_Inter/gender_Inter/education_Inter/ethnicity'])

# Test four
Data["Test_three_best_plus_Interviewer/ethnicity"] = (Data.City_code.astype(
    str) + "_" + Data.Eligible.astype(str) + "_" + Data.Intervention_group.astype(str) + "_" + Data.Interviewer_Ethnicity.astype(str))
Data["Test_three_best_plus_Interviewer/ethnicity"] = le.fit_transform(
    Data["Test_three_best_plus_Interviewer/ethnicity"])

Data["Test_three_best_plus_Interviewer/education"] = (Data.City_code.astype(
    str) + "_" + Data.Eligible.astype(str) + "_" + Data.Intervention_group.astype(str) + "_" + Data.Interviewer_Education.astype(str))
Data["Test_three_best_plus_Interviewer/education"] = le.fit_transform(
    Data["Test_three_best_plus_Interviewer/education"])

Data["Test_three_best_plus_Village/StateCode"] = (Data.City_code.astype(
    str) + "_" + Data.Eligible.astype(str) + "_" + Data.Intervention_group.astype(str) + "_" + Data.Village_StateCode.astype(str))
Data["Test_three_best_plus_Village/StateCode"] = le.fit_transform(
    Data["Test_three_best_plus_Village/StateCode"])

#Combining five featurs 
Data["Eligible_Part/gender_Part/ethnicity_group_City/code"] = (Data.Eligible.astype(
    str) + "_" + Data.Participant_gender.astype(str) + "_" + Data.Participant_ethnicity.astype(str) + "_" + Data.Intervention_group.astype(str) + "_" + Data.City_code.astype(str))
Data['Eligible_Part/gender_Part/ethnicity_group_City/code'] = le.fit_transform(
    Data['Eligible_Part/gender_Part/ethnicity_group_City/code'])
Data["Eligible_Part/gender_Part/ethnicity_group_Village/code"] = (Data.Eligible.astype(
    str) + "_" + Data.Participant_gender.astype(str) + "_" + Data.Participant_ethnicity.astype(str) + "_" + Data.Intervention_group.astype(str) + "_" + Data.Village_StateCode.astype(str))
Data['Eligible_Part/gender_Part/ethnicity_group_Village/code'] = le.fit_transform(
    Data['Eligible_Part/gender_Part/ethnicity_group_Village/code'])
Data["Eligible_Part/gender_Part/ethnicity_group_Inter/gender"] = (Data.Eligible.astype(
    str) + "_" + Data.Participant_gender.astype(str) + "_" + Data.Participant_ethnicity.astype(str) + "_" + Data.Intervention_group.astype(str) + "_" + Data.Interviewer_Gender.astype(str))
Data['Eligible_Part/gender_Part/ethnicity_group_Inter/gender'] = le.fit_transform(
    Data['Eligible_Part/gender_Part/ethnicity_group_Inter/gender'])
Data["Eligible_Part/gender_Part/ethnicity_group_Inter/education"] = (Data.Eligible.astype(
    str) + "_" + Data.Participant_gender.astype(str) + "_" + Data.Participant_ethnicity.astype(str) + "_" + Data.Intervention_group.astype(str) + "_" + Data.Interviewer_Education.astype(str))
Data['Eligible_Part/gender_Part/ethnicity_group_Inter/education'] = le.fit_transform(
    Data['Eligible_Part/gender_Part/ethnicity_group_Inter/education'])
Data["Eligible_Part/gender_Part/ethnicity_group_Inter/ethnicity"] = (Data.Eligible.astype(
    str) + "_" + Data.Participant_gender.astype(str) + "_" + Data.Participant_ethnicity.astype(str) + "_" + Data.Intervention_group.astype(str) + "_" + Data.Interviewer_Ethnicity.astype(str))
Data['Eligible_Part/gender_Part/ethnicity_group_Inter/ethnicity'] = le.fit_transform(
    Data['Eligible_Part/gender_Part/ethnicity_group_Inter/ethnicity'])
Data["Part/gender_Part/ethnicity_group_City/code_Village/code"] = (Data.Participant_gender.astype(
    str) + "_" + Data.Participant_ethnicity.astype(str) + "_" + Data.Intervention_group.astype(str) + "_" + Data.City_code.astype(str) + "_" + Data.Village_StateCode.astype(str))
Data['Part/gender_Part/ethnicity_group_City/code_Village/code'] = le.fit_transform(
    Data['Part/gender_Part/ethnicity_group_City/code_Village/code'])
Data["Part/gender_Part/ethnicity_group_City/code_Inter/gender"] = (Data.Participant_gender.astype(
    str) + "_" + Data.Participant_ethnicity.astype(str) + "_" + Data.Intervention_group.astype(str) + "_" + Data.City_code.astype(str) + "_" + Data.Interviewer_Gender.astype(str))
Data['Part/gender_Part/ethnicity_group_City/code_Inter/gender'] = le.fit_transform(
    Data['Part/gender_Part/ethnicity_group_City/code_Inter/gender'])
Data["Part/gender_Part/ethnicity_group_City/code_Inter/education"] = (Data.Participant_gender.astype(
    str) + "_" + Data.Participant_ethnicity.astype(str) + "_" + Data.Intervention_group.astype(str) + "_" + Data.City_code.astype(str) + "_" + Data.Interviewer_Education.astype(str))
Data['Part/gender_Part/ethnicity_group_City/code_Inter/education'] = le.fit_transform(
    Data['Part/gender_Part/ethnicity_group_City/code_Inter/education'])
Data["Part/gender_Part/ethnicity_group_City/code_Inter/ethnicity"] = (Data.Participant_gender.astype(
    str) + "_" + Data.Participant_ethnicity.astype(str) + "_" + Data.Intervention_group.astype(str) + "_" + Data.City_code.astype(str) + "_" + Data.Interviewer_Ethnicity.astype(str))
Data['Part/gender_Part/ethnicity_group_City/code_Inter/ethnicity'] = le.fit_transform(
    Data['Part/gender_Part/ethnicity_group_City/code_Inter/ethnicity'])
Data["Part/ethnicity_group_City/code_Village/code_Inter/gender"] = (Data.Participant_ethnicity.astype(
    str) + "_" + Data.Intervention_group.astype(str) + "_" + Data.City_code.astype(str) + "_" + Data.Village_StateCode.astype(str) + "_" + Data.Interviewer_Gender.astype(str))
Data['Part/ethnicity_group_City/code_Village/code_Inter/gender'] = le.fit_transform(
    Data['Part/ethnicity_group_City/code_Village/code_Inter/gender'])
Data["Part/ethnicity_group_City/code_Village/code_Inter/education"] = (Data.Participant_ethnicity.astype(
    str) + "_" + Data.Intervention_group.astype(str) + "_" + Data.City_code.astype(str) + "_" + Data.Village_StateCode.astype(str) + "_" + Data.Interviewer_Education.astype(str))
Data['Part/ethnicity_group_City/code_Village/code_Inter/education'] = le.fit_transform(
    Data['Part/ethnicity_group_City/code_Village/code_Inter/education'])
Data["Part/ethnicity_group_City/code_Village/code_Inter/ethnicity"] = (Data.Participant_ethnicity.astype(
    str) + "_" + Data.Intervention_group.astype(str) + "_" + Data.City_code.astype(str) + "_" + Data.Village_StateCode.astype(str) + "_" + Data.Interviewer_Ethnicity.astype(str))
Data['Part/ethnicity_group_City/code_Village/code_Inter/ethnicity'] = le.fit_transform(
    Data['Part/ethnicity_group_City/code_Village/code_Inter/ethnicity'])
Data["group_City/code_Village/code_Inter/gender_Inter/education"] = (Data.Intervention_group.astype(
    str) + "_" + Data.City_code.astype(str) + "_" + Data.Village_StateCode.astype(str) + "_" + Data.Interviewer_Gender.astype(str) + "_" + Data.Interviewer_Education.astype(str))
Data['group_City/code_Village/code_Inter/gender_Inter/education'] = le.fit_transform(
    Data['group_City/code_Village/code_Inter/gender_Inter/education'])
Data["group_City/code_Village/code_Inter/gender_Inter/ethnicity"] = (Data.Intervention_group.astype(
    str) + "_" + Data.City_code.astype(str) + "_" + Data.Village_StateCode.astype(str) + "_" + Data.Interviewer_Gender.astype(str) + "_" + Data.Interviewer_Ethnicity.astype(str))
Data['group_City/code_Village/code_Inter/gender_Inter/ethnicity'] = le.fit_transform(
    Data['group_City/code_Village/code_Inter/gender_Inter/ethnicity'])
Data["City/code_Village/code_Inter/gender_Inter/education_Inter/ethnicity"] = (Data.City_code.astype(
    str) + "_" + Data.Village_StateCode.astype(str) + "_" + Data.Interviewer_Gender.astype(str) + "_" + Data.Interviewer_Education.astype(str) + "_" + Data.Interviewer_Ethnicity.astype(str))
Data['City/code_Village/code_Inter/gender_Inter/education_Inter/ethnicity'] = le.fit_transform(
    Data['City/code_Village/code_Inter/gender_Inter/education_Inter/ethnicity'])


# Test five 
Data["Best four/ethnicity"] = (Data.City_code.astype(
    str) + "_" + Data.Eligible.astype(str) + "_" + Data.Intervention_group.astype(str) + "_" + Data.Interviewer_Education.astype(str)
    + "_" + Data.Interviewer_Ethnicity.astype(str))
Data["Best four/ethnicity"] = le.fit_transform(
    Data["Best four/ethnicity"])

# Best six 
Data["Best six"] = (Data.City_code.astype(
    str) + "_" + Data.Eligible.astype(str) + "_" + Data.Intervention_group.astype(str) + "_" + Data.Interviewer_Education.astype(str)
    + "_" + Data.Interviewer_Ethnicity.astype(str)+ "_" + Data.Village_StateCode.astype(str))
Data["Best six"] = le.fit_transform(
    Data["Best six"])

#Test six participant 
Data["Six participant"] = (Data.City_code.astype(
    str) + "_" + Data.Eligible.astype(str) + "_" + Data.Intervention_group.astype(str) + "_" + Data.Participant_gender.astype(str)
    + "_" + Data.Participant_ethnicity.astype(str)+ "_" + Data.Village_StateCode.astype(str))
Data["Six participant"] = le.fit_transform(
    Data["Six participant"])

#Test three interviewer 
Data["Three interviewer"] = (Data.Interviewer_Gender.astype(str)
    + "_" + Data.Interviewer_Ethnicity.astype(str)+ "_" + Data.Interviewer_Education.astype(str))
Data["Three interviewer"] = le.fit_transform(
    Data["Three interviewer"])


# Feature visualization (F)
sb.boxplot(x="Three interviewer", y="Quality score", data=Data, showmeans=True)

plt.show()

# Export
Data.to_excel('Data_combined_features.xlsx')

