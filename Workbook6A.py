
# coding: utf-8

# In[3]:


import pandas as pd
Location = "datasets/gradedata.csv"
df = pd.read_csv(Location)
df.head()

df = df.sort_values(by=['lname','age', 'grade'],
                    ascending=[True, True, True])
df.head()

