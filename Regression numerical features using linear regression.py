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

from tensorflow import keras
from keras.models import Model
from keras.layers import Dense, Conv1D,Conv2D, Flatten, Dropout
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

Data=Data.drop(columns=['Eligible'])
Data=Data.drop(columns=['Participant_gender'])
Data=Data.drop(columns=['Participant_ethnicity'])
Data=Data.drop(columns=['Intervention_group'])
Data=Data.drop(columns=['City_code'])
Data=Data.drop(columns=['Village_StateCode'])
Data=Data.drop(columns=['Village_Participant_Nubmer'])
Data=Data.drop(columns=['Interviewer_Gender'])
Data=Data.drop(columns=['Interviewer_Education'])
Data=Data.drop(columns=['Interviewer_Ethnicity'])
Data=Data.drop(columns=['Best_three'])
Data=Data.drop(columns=['Best_four'])
Data=Data.drop(columns=['Best_five'])
Data=Data.drop(columns=['Best_six'])
Data=Data.drop(columns=['Four_participant'])
Data=Data.drop(columns=['Five_participant'])
Data=Data.drop(columns=['Six_participant'])
Data=Data.drop(columns=['Three_interviewer'])

Data = Data.dropna()
Data= Data.reset_index(drop=True)

def scaling(data_s):
    
    data_s = data_s.reshape(-1,1)
    data_s = scaler.fit_transform(data_s)
  
    return data_s


#Balancing
def balancing(x,y):
    
    X=pd.DataFrame(x, columns=['resampled'])
    y=pd.DataFrame(y, columns=['Quality score resampled'])


    y_resampled, X_resampled = ros.fit_resample(y, X) 

    Data_resampled= pd.concat([X_resampled,y_resampled], axis=1)
    
    return Data_resampled, X_resampled, y_resampled


X= np.array(Data.loc[:,'Participant_age'])
y= np.array(Data.loc[:,'Quality score'])

Data_resampled, X_resampled, y_resampled= balancing(X,y)

# split into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=1,shuffle=True)



X_train=X_train.reshape(-1,1)
y_train=y_train.reshape(-1,1)
X_test=X_test.reshape(-1,1)
y_test=y_test.reshape(-1,1)



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

# comparison
time= np.arange(0, len(y_test), 1)
time = time.reshape(-1,1)


plt.figure()
plt.plot(time[0:100],y_test[0:100])
plt.plot(time[0:100],yhat[0:100])
plt.title('linear regression prediction')
plt.ylabel('Quality Score')
plt.xlabel('Participant_age')
plt.legend(['Ground Truth', 'Prediction'], loc='lower right')
plt.show()

