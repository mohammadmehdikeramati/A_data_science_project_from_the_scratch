# -*- coding: utf-8 -*-
"""
Created on Wed Oct  5 15:58:45 2022

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
from keras.utils import np_utils

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
Data=Data.drop(columns=['FU_Month'])

X= np.array(Data.loc[:,'Best_two'])
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

Out= X_resampled.value_counts()


#Encoding
encoder = LabelEncoder()
encoder.fit(X_resampled)
X_resampled = encoder.transform(X_resampled)
X_resampled = np_utils.to_categorical(X_resampled)


X_train, X_test, y_train, y_test = train_test_split(X_resampled, y_resampled, test_size=0.33,stratify=X_resampled, random_state=1,shuffle=True)


# Network (reversed)
model = keras.Sequential() 
model.add(keras.layers.Dense(units=500,input_shape=(y_train.shape[1],), kernel_initializer='random_uniform')) 
#model.add(Dropout(0.1))
#model.add(keras.layers.Dense(units=100,input_shape=(500,1),activation='relu'))  
#model.add(Dropout(0.1))
model.add(keras.layers.Dense(units=len(Out),input_shape=(500,1),activation='softmax')) 


model.compile(loss=['categorical_crossentropy'],optimizer="adam",metrics=['accuracy'])
history = model.fit( y_train, X_train, epochs=100,batch_size=100, validation_split=0.2,verbose=1,shuffle=False)

model.summary()


# Prediction
predictions = model.predict(y_test)

test_1=predictions
test_2=predictions.argmax(1)
test_3=np.round(predictions)

X_test_test=X_test
X_test=X_test.argmax(1)

from sklearn.metrics import confusion_matrix,classification_report
print(classification_report(X_test,test_2))


# Visualization
X_test=pd.DataFrame(X_test, columns=['resampled'])
test_2=pd.DataFrame(test_2, columns=['Predict'])


print(X_test.value_counts())
print(test_2.value_counts())

Class_counter= test_2.value_counts()


X_test_test=X_test
y_test_test=y_test


X_test=X_test.reset_index(drop=True)
y_test=y_test.reset_index(drop=True)

Data_test= pd.concat([X_test,y_test], axis=1)


sb.boxplot(x="resampled", y="Quality score resampled", showmeans=True, data=Data_test)

plt.show()

plt.figure()


test_2=test_2.reset_index(drop=True)

Data_predict= pd.concat([test_2,y_test], axis=1)

plt.title('ANN prediction')

sb.boxplot(x="Predict", y="Quality score resampled", showmeans=True, data=Data_predict)

plt.show()


