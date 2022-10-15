# -*- coding: utf-8 -*-
"""
Created on Mon Jul 18 19:04:06 2022

@author: Mohammad Mehdi Keramati
"""

import math
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt


from keras.utils import np_utils
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error

from imblearn.over_sampling import RandomOverSampler
ros = RandomOverSampler(random_state=0)

Data=pd.read_excel('C:/Users/Mehdi Keramati/Desktop/Medical data project- finalization/4- Feature selection based on N.N- effect of each combined feature/Data_combined_features_wisely_Final.xlsx', index_col=0)

scaler = MinMaxScaler(feature_range=(0, 1))
encoder = LabelEncoder()

# Drop
Data=Data.drop(columns=['ID'])
Data=Data.drop(columns=['GCSID'])
Data=Data.drop(columns=['Village_Cluster'])
Data=Data.drop(columns=['Interviewer_WorkExperience'])
Data=Data.drop(columns=['Participant_age'])
Data=Data.drop(columns=['Interviewer_age'])
Data=Data.drop(columns=['FU_Month'])

# Encoding
def encoding(data_e):

     
     encoder.fit(data_e)
     data_e = encoder.transform(data_e)
     data_e = np_utils.to_categorical(data_e)

     return data_e


def scaling(data_s):
    
    mean = data_s.mean(axis=0)
    data_s -= mean
    std = data_s.std(axis=0)
    data_s /= std
    
    #data_s = data_s.reshape(-1,1)
    #data_s = scaler.fit_transform(data_s)
  
    return data_s


#Balancing
def balancing(x,y):
    
    X=pd.DataFrame(x, columns=['resampled'])
    y=pd.DataFrame(y, columns=['Quality score resampled'])
    y_resampled, X_resampled = ros.fit_resample(y, X) 
    Data_resampled= pd.concat([X_resampled,y_resampled], axis=1)
    return Data_resampled, X_resampled, y_resampled


def split(X,y):
    
    Data_resampled, X_resampled, y_resampled= balancing(X,y)
    X_resampled= encoding(X_resampled)

    # split into train and test sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=1,shuffle=True)

    #y_train= scaling(y_train)
    X_train=X_train.reshape(-1,1)
    y_train=y_train.reshape(-1,1)
    X_test=X_test.reshape(-1,1)
    y_test=y_test.reshape(-1,1)
    
    return X_train,y_train, X_test, y_test 



X= np.array(Data.loc[:,'Three_interviewer'])
y= np.array(Data.loc[:,'Quality score'])

X_1= np.array(Data.loc[:,'Four_participant'])
y_1= np.array(Data.loc[:,'Quality score'])

X_train,y_train, X_test, y_test= split(X,y)
X_train_1,y_train_1, X_test_1, y_test_1= split(X_1,y_1)



# Linear regression
from sklearn.datasets import make_regression
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error


model = LinearRegression()
model.fit(X_train, y_train)
yhat = model.predict(X_test)
mae = mean_absolute_error(y_test, yhat)
print('mae: %.3f' % mae)

model.fit(X_train_1, y_train_1)
yhat_1 = model.predict(X_test_1)
mae_1 = mean_absolute_error(y_test_1, yhat_1)
print('mae_1: %.3f' % mae_1)

# comparison
time= np.arange(0, len(y_test), 1)
time = time.reshape(-1,1)

plt.figure()
plt.plot(time[0:100],y_test[0:100])
plt.plot(time[0:100],yhat[0:100])
#plt.plot(time[0:100],yhat_1[0:100])
plt.title('linear regression prediction')
plt.ylabel('Quality Score')
plt.xlabel('Sample number')
plt.legend(['Ground Truth', 'Three_interviewer'], loc='lower right')
plt.show()

