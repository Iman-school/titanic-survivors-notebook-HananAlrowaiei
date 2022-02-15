#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd


# In[4]:


df = pd.read_csv('titanic-passengers.csv', sep=';')
df.head(20)


# In[5]:


df.info()


# In[7]:


df.isnull()


# In[8]:


df.isnull().sum()


# In[9]:


#Number of missing values in Age 
df['Age'].isnull().sum()


# In[10]:


#Number of missing values in Cabin
df['Cabin'].isnull().sum()


# In[11]:


#Number of missing values in Emabarked
df['Embarked'].isnull().sum()


# In[ ]:




