# -*- coding: utf-8 -*-
"""
Created on Mon Mar 21 08:58:41 2022

@author: Mohammad Mehdi Keramati
"""
import pandas as pd
Data=pd.read_excel('C:/Users/Mehdi Keramati/Desktop/Medical data project- finalization/Data.xlsx')

import numpy as np
import seaborn as sb
import matplotlib.pyplot as plt

plt.figure(figsize=(8,6),dpi = 100)
sb.boxplot(x="Interviewer_age", y="Quality score", data=Data, showmeans=True)



plt.show()




