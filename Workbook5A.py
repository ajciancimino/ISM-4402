
# coding: utf-8

# In[4]:


#Import packages
import pandas as pd
import numpy as np

#Set dataframe
Location = "datasets/gradedata.csv"
df = pd.read_csv(Location)
df.tail()

#Randomly select 500 rows from dataset
df.take(np.random.permutation(len(df))[:500])

