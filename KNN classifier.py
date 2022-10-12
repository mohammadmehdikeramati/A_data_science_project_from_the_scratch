
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  3 10:04:30 2022

@author: Mohammad Mehdi Keramati
"""

import pandas as pd
import numpy as np

from imblearn.over_sampling import RandomOverSampler
ros = RandomOverSampler(random_state=0)

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from tensorflow import keras
from keras.models import Model
from keras.layers import Dense, Conv1D,Conv2D, Flatten, Dropout
from sklearn.preprocessing import LabelEncoder

from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix,classification_report, precision_score

import matplotlib.pyplot as plt
import seaborn as sb

Data = pd.read_excel('C:/Users/Mehdi Keramati/Desktop/Medical data project- finalization/4- Feature selection based on N.N- effect of each combined feature/Data_combined_features_wisely_Final.xlsx', index_col=0)


# Counting before balancing
print(Data['Eligible'].value_counts())
print(Data['Participant_gender'].value_counts())
print(Data['Participant_ethnicity'].value_counts())
print(Data['Intervention_group'].value_counts())
print(Data['City_code'].value_counts())
print(Data['Village_StateCode'].value_counts())
print(Data['Village_Participant_Nubmer'].value_counts())
print(Data['Interviewer_Gender'].value_counts())
print(Data['Interviewer_Education'].value_counts())
print(Data['Interviewer_Ethnicity'].value_counts())
print(Data['FU_Month'].value_counts())


print(Data['Best_three'].value_counts())
print(Data['Best_four'].value_counts())
print(Data['Best_five'].value_counts())
print(Data['Best_six'].value_counts())
print(Data['Four_participant'].value_counts())
print(Data['Five_participant'].value_counts())
print(Data['Six_participant'].value_counts())
print(Data['Three_interviewer'].value_counts())


# Drop
Data=Data.drop(columns=['ID'])
Data=Data.drop(columns=['GCSID'])
Data=Data.drop(columns=['Village_Cluster'])
Data=Data.drop(columns=['Interviewer_WorkExperience'])
Data=Data.drop(columns=['Interviewer_age'])

X= np.array(Data.loc[:,'Best_five'])
y= np.array(Data.loc[:,'Quality score'])


#Balancing
def balancing(x,y):
    
    X= np.array(x)
    y= np.array(y)

    X=pd.DataFrame(X, columns=['resampled'])
    y=pd.DataFrame(y, columns=['Quality score resampled'])

    y_resampled, X_resampled = ros.fit_resample(y, X) 

    Data_resampled= pd.concat([X_resampled,y_resampled], axis=1)
    
    return Data_resampled, X_resampled, y_resampled
 
   
Data_resampled, X_resampled, y_resampled= balancing(X,y)
print(Data_resampled['resampled'].value_counts())

X_train, X_test, y_train, y_test = train_test_split(X_resampled, y_resampled, test_size=0.33,stratify=X_resampled, random_state=1,shuffle=True)


# KNN (reversed)
knn= KNeighborsClassifier(n_neighbors=3,metric='minkowski',p=2)
knn.fit(y_train,X_train)
predict=knn.predict(y_test)
predict=pd.DataFrame(predict, columns=['Predict'])

print(classification_report(X_test,predict))

print(X_test.value_counts())
print(predict.value_counts())

Class_counter= predict.value_counts()

print(precision_score(X_test, predict,average='weighted', zero_division='warn'))
 

# Visualization
X_test=X_test.reset_index(drop=True)
y_test=y_test.reset_index(drop=True)

Data_test= pd.concat([X_test,y_test], axis=1)


sb.boxplot(x="resampled", y="Quality score resampled", showmeans=True, data=Data_test)

plt.show()

plt.figure()


predict=predict.reset_index(drop=True)

Data_predict= pd.concat([predict,y_test], axis=1)

plt.title('knn prediction')

sb.boxplot(x="Predict", y="Quality score resampled", showmeans=True, data=Data_predict)

plt.show()