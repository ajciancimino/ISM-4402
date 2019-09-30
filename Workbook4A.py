
# coding: utf-8

# In[9]:


#Import Pandas
import pandas as pd

#Create Data Frame
Location = "datasets/gradedata.csv"
df = pd.read_csv(Location)
df.head()

# Create the bin dividers
bins = [0,80,100]
# Create names for the four groups
group_names = ['Fail','Pass']

#Assigning bins
df['lettergrade'] = pd.cut(df['grade'], bins, labels=group_names)
df

