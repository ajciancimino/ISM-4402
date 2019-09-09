
# coding: utf-8

# In[16]:


import pandas as pd
names = ['Bob','Jessica','Mary','John','Mel']
grades = [76,95,77,78,99]
bsdegrees = [1,1,0,0,1]
msdegrees = [2,1,0,0,0]
phddegrees = [0,1,0,0,0]
Degrees = list(zip(names,grades,bsdegrees,msdegrees,phddegrees))
columns = ['Names','Grades','BS','MS','PhD']
df = pd.DataFrame(data = Degrees, columns=column)
df
df.to_csv('degrees.csv',index=False,header=False)

