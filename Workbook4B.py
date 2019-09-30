
# coding: utf-8

# In[10]:


#import packages
import pandas as pd
import numpy as np

#Create dataframe
Location = "datasets/gradedata.csv"
df = pd.read_csv(Location)
df.head()

#Create timemgmt column
df['timemgmt'] = np.where((df['exercise'] > 3)
                               & (df['hours'] > 17),'Busy', 'Not Busy')
df.tail(50)

