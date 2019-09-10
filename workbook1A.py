
# coding: utf-8

# In[5]:


import pandas as pd

#the dataset path
Location = "jupyter/wyoming.csv"

# To add headers as we load the data...
df = pd.read_csv(Location)
df.head

