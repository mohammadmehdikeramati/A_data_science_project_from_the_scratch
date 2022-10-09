# -*- coding: utf-8 -*-
"""
Created on Mon Sep 19 09:26:51 2022

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



Data = pd.read_excel('C:/Users/Mehdi Keramati/Desktop/Medical data project- finalization/Data.xlsx')


le = LabelEncoder()

############################### Best two ####################

Data["Best two"] = (Data.City_code.astype(
    str) + "_" + Data.Village_StateCode.astype(str))
Data["Best two"] = le.fit_transform(
    Data["Best two"])

############################### Best three ####################

Data["Best_three"] = (Data.City_code.astype(
    str) + "_" + Data.Village_StateCode.astype(str) + "_" + Data.Interviewer_Education.astype(str))
Data["Best_three"] = le.fit_transform(
    Data["Best_three"])

############################### Best four #####################

Data["Best_four"] = (Data.City_code.astype(
    str) + "_" + Data.Interviewer_Education.astype(str) + "_" + Data.Participant_ethnicity.astype(str)
    + "_" + Data.Village_StateCode.astype(str))
Data["Best_four"] = le.fit_transform(
    Data["Best_four"])

############################### Best five #####################

Data["Best_five"] = (Data.City_code.astype(
    str) + "_" + Data.Interviewer_Education.astype(str) + "_" + Data.Participant_ethnicity.astype(str)
    + "_" + Data.Village_StateCode.astype(str) + "_" + Data.Participant_gender.astype(str))
Data["Best_five"] = le.fit_transform(
    Data["Best_five"])

############################### Best six #######################

Data["Best_six"] = (Data.City_code.astype(
    str) + "_" + Data.Interviewer_Education.astype(str) + "_" + Data.Participant_ethnicity.astype(str)
    + "_" + Data.Village_StateCode.astype(str) + "_" + Data.Participant_gender.astype(str)+ "_" + Data.Intervention_group.astype(str))
Data["Best_six"] = le.fit_transform(
    Data["Best_six"])

############################# Four participant (without eligible and intervention group considration) #######################

Data["Four_participant"] = (Data.City_code.astype(
    str) + "_" + Data.Participant_gender.astype(str)
    + "_" + Data.Participant_ethnicity.astype(str)+ "_" + Data.Village_StateCode.astype(str))
Data["Four_participant"] = le.fit_transform(
    Data["Four_participant"])


############################### Five participant (without eligible considration) #######################

Data["Five_participant"] = (Data.City_code.astype(
    str) + "_" + Data.Intervention_group.astype(str) + "_" + Data.Participant_gender.astype(str)
    + "_" + Data.Participant_ethnicity.astype(str)+ "_" + Data.Village_StateCode.astype(str))
Data["Five_participant"] = le.fit_transform(
    Data["Five_participant"])


############################### Six participant #######################

Data["Six_participant"] = (Data.City_code.astype(
    str) + "_" + Data.Intervention_group.astype(str) + "_" + Data.Participant_gender.astype(str)
    + "_" + Data.Participant_ethnicity.astype(str)+ "_" + Data.Village_StateCode.astype(str)+ "_" + Data.Interviewer_Education.astype(str))
Data["Six_participant"] = le.fit_transform(
    Data["Six_participant"])


############################### Three interviewer #######################

Data["Three_interviewer"] = (Data.Interviewer_Gender.astype(str)
    + "_" + Data.Interviewer_Ethnicity.astype(str)+ "_" + Data.Interviewer_Education.astype(str))
Data["Three_interviewer"] = le.fit_transform(
    Data["Three_interviewer"])


# Export
Data.to_excel('Data_combined_features_wisely_Final.xlsx')


# Feature visualization
plt.figure(figsize=(8,6),dpi = 100)
sb.boxplot(x="Best two", y="Quality score", data=Data, showmeans=True)


plt.show()
