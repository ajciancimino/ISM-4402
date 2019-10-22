
# coding: utf-8

# In[3]:


#Add imports
import matplotlib.pyplot as plt
import pandas as pd

#Define Data
names = ['Bob','Jessica','Mary','John','Mel']
status = ['Senior','Freshman','Sophomore','Senior','Junior']
grades = [76,95,77,78,99]
GradeList = list(zip(names, status, grades))
df = pd.DataFrame(data = GradeList, columns=['Names', 'Status','Grades'])

get_ipython().magic(u'matplotlib inline')
df.plot(kind='bar')





df2 = df.set_index(df['Status'])
df2.plot(kind="bar")

