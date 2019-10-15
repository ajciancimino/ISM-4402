
# coding: utf-8

# In[8]:


import pandas as pd
import numpy as np
import statsmodels.formula.api as sm

Location = "datasets/gradedata.csv"
df = pd.read_csv(Location)


df['genderBool'] = np.where((df['gender'] == "female"),'1', '0')
df.head()

result = sm.ols(
    formula='grade ~ gender + exercise + hours'
    ,data=df).fit()
result.summary()

