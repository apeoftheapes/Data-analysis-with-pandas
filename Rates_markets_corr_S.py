#!/usr/bin/env python
# coding: utf-8

# In[48]:


import numpy as np
from datetime import datetime
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('TVC_SILVER, 1M.csv')
df['time'] = df['time'].apply(lambda x: datetime.utcfromtimestamp(x).strftime('%Y-%m-%d'))
df['MoM_pct_change_close']= df['close'].pct_change(fill_method ='ffill')
df['monthly_rate_diff'] = df['USINTR, FEDERAL RESERVE: Open'].diff(periods = 1)

df.drop(columns = ['Basis' ,'Upper','Lower','EMA','USINTR, FEDERAL RESERVE: Open','USINTR, FEDERAL RESERVE: High','USINTR, FEDERAL RESERVE: Low','Smoothing Line','MA','Smoothing Line','Plot','Plot','MA','Smoothing Line','Volume','Volume MA', 'Smoothing Line.1', 'Plot.1','MA.1','Smoothing Line.2'], inplace=True)
# filter the time
filt = (df['time'] > '1975')

df[filt]


# In[53]:


# set timeframe as you whish
filt = (df['time'] > '1975')
df_tf = df[filt] 

x = df_tf['time']
y1 = df_tf['close']
y2 = df_tf['USINTR, FEDERAL RESERVE: Close']

fig, ax1 = plt.subplots()

ax2 = ax1.twinx()
ax1.plot(x, y1, 'g-')
ax2.plot(x, y2, 'b-')

# timestamps were too close, slicker solution surely exsist, probably with locator params
every_nth = 150
for n, label in enumerate(ax1.xaxis.get_ticklabels()):
    if n % every_nth != 0:
        label.set_visible(False)

ax1.set_xlabel('year')
ax1.set_ylabel('close', color='g')
ax2.set_ylabel('USINTR, FEDERAL RESERVE: Close', color='b')

plt.show()


# In[54]:


# set timeframe as you whish 
filt = (df['time'] > '1975')
df_tf = df[filt] 

x = df_tf['time']
y1 = df_tf['MoM_pct_change_close']
y2 = df_tf['monthly_rate_diff']

fig, ax1 = plt.subplots()

ax2 = ax1.twinx()
ax1.plot(x, y1, 'b-')
ax2.scatter(x, y2, marker='o', linewidths= 0.1, c= 'red')

# timestamps were too close, slicker solution surely exsist, probably with locator params
every_nth = 150
for n, label in enumerate(ax1.xaxis.get_ticklabels()):
    if n % every_nth != 0:
        label.set_visible(False)

ax1.set_xlabel('year')
ax1.set_ylabel('MoM_pct_change_close', color='b')
ax2.set_ylabel('monthly_rate_diff', color='r')

#observe % price changes plotet along monthly rate changes
plt.show()


# In[40]:


#observe correlation 
filt = (df['time'] > '1980')
df_tf = df[filt] 

df_tf['close'].corr(df['USINTR, FEDERAL RESERVE: Close'], method='pearson', min_periods=1)


# In[42]:


# we are interested in positive correlation in rising rates environments
filt = (df['time'] > '1975')
df_tf = df[filt] 

filt2 = (df['USINTR, FEDERAL RESERVE: Close'] >= 1) & (df['monthly_rate_diff'] > 0)
df_tf[filt2]


# In[51]:


filt = (df['time'] > '1975')
df_tf = df[filt]

filt2 = (df['USINTR, FEDERAL RESERVE: Close'] >= 1) & (df['monthly_rate_diff'] > 0)
df_tf[filt2]

df_tf_high_rates_with_hiking = df_tf[filt2]

#calculate correlation in risig rates environemnts
df_tf_high_rates_with_hiking['close'].corr(df['USINTR, FEDERAL RESERVE: Close'], method='pearson', min_periods=1)


# In[ ]:




