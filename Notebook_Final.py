
# coding: utf-8

# In[4]:


import pandas as pd
location = "datasets/axisdata.csv"
df = pd.read_csv(location)
df.head()


# In[6]:


df['Cars Sold'].mean()


# In[7]:


df['Cars Sold'].max()


# In[8]:


df['Cars Sold'].min()


# In[9]:


pd.pivot_table(df, values=["Cars Sold"], index=["Gender"])


# In[10]:


df[df["Cars Sold"]>3]["Hours Worked"].mean()


# In[11]:


df["Years Experience"].mean()


# In[12]:


df[df["Cars Sold"]>3]["Years Experience"].mean()


# In[14]:


pd.pivot_table(df, values=["Cars Sold"], index=["SalesTraining"])


# In[24]:


df.plot.scatter(x='Cars Sold', y='Hours Worked')


# In[21]:


axis1 = df.boxplot(by='SalesTraining', column='Cars Sold')
axis1.set_ylim(0,10)

