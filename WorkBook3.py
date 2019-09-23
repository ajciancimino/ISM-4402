
# coding: utf-8

# In[8]:


import pandas as pd

#dataframe setup
names = ['Bob','Jessica','Mary','John','Mel']
grades = [76,-2,77,78,101]
GradeList = list(zip(names,grades))
df = pd.DataFrame(data = GradeList,columns=['Names', 'Grades'])

#Adjust grades above max to 100
df.loc[(df['Grades'] >= 100,'Grades')] = 100

#Adjust grades below min to 0
df.loc[(df['Grades'] <= 0,'Grades')] = 0
df

