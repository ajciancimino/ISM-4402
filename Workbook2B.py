
# coding: utf-8

# In[12]:


import pandas as pd
from sqlalchemy import create_engine
# Connect to sqlite db
db_file = r'datasets/salesdata.db'
engine = create_engine(r"sqlite:///{}"
    .format(db_file))

# V---This was used to find table names---V
# sql = "select name from sqlite_master"
# "where type = 'table';"
# ^---------------------------------------^

#Selecting all from the scores table
sql = 'SELECT * from scores'

sales_data_df = pd.read_sql(sql, engine)
sales_data_df

