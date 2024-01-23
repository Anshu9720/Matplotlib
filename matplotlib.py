#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[2]:


df=pd.read_csv('sharma-kohli.csv')


# In[3]:


df.head()


# In[4]:


df.describe()


# In[9]:


df.mean()


# In[18]:


plt.plot(df['index'],df['RG Sharma'])
plt.plot(df['index'],df['V Kohli'])
plt.title('Virat kohli vs Rohit Sharma')
plt.xlabel('Year')
plt.ylabel('Runs')


# In[29]:


plt.plot(df['index'],df['RG Sharma'],color='yellow',)
plt.plot(df['index'],df['V Kohli'],color='red')
plt.title('Virat kohli vs Rohit Sharma')
plt.xlabel('Year')
plt.ylabel('Runs')


# In[37]:


plt.plot(df['index'],df['RG Sharma'],color='yellow',linestyle='dashdot',linewidth=4)
plt.plot(df['index'],df['V Kohli'],color='red',linestyle='dashdot',linewidth=4)
plt.title('Virat kohli vs Rohit Sharma')
plt.xlabel('Year')
plt.ylabel('Runs')


# In[45]:


plt.plot(df['index'],df['RG Sharma'],color='yellow',linestyle='dashdot',linewidth=4)
plt.plot(df['index'],df['V Kohli'],color='red',linestyle='dashdot',linewidth=4)
plt.title('Virat kohli vs Rohit Sharma')
plt.xlabel('Year')
plt.ylabel('Runs')


# In[ ]:




