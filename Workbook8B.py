
# coding: utf-8

# In[9]:


#import packages
import pandas as pd
import matplotlib.pyplot as plt

#Setup dataframe
get_ipython().run_line_magic('matplotlib', 'inline')
names = ['Bob','Jessica','Mary','John','Mel']
absences = [3,0,1,0,8]
detentions = [2,1,0,0,1]
warnings = [2,1,5,1,2]
GradeList = list(zip(names,absences,detentions,warnings))
columns=['Names', 'Absences', 'Detentions','Warnings']
df = pd.DataFrame(data = GradeList, columns=columns)
df['TotalDemerits'] = df['Absences'] +df['Detentions'] + df['Warnings']
df

#Setup Pie chart
plt.pie(df['TotalDemerits'],
        labels=df['Names'],
        explode=(0,0,0,0.30,0),  #<<< Explode out pie for 4th student, A.K.A John
        startangle=90,
        autopct='%1.1f%%',)
plt.axis('equal')
plt.show()

