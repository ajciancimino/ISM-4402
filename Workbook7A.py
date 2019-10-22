
# coding: utf-8

# In[55]:


import pandas as pd
names = ['Bob','Jessica','Mary','John','Mel']
grades = [76,83,77,78,95]
GradeList = list(zip(names,grades))
df = pd.DataFrame(data = GradeList,
                  columns=['Names', 'Grades'])
get_ipython().run_line_magic('matplotlib', 'inline')
# df.plot()

import matplotlib.pyplot as plt
df.plot()
displayText = "WOW"
xloc = 0
yloc = 76
xtext = 160
ytext = 20

plt.annotate(displayText,
             xy=(xloc, yloc),
#              arrowprops=dict(facecolor='black',
#                              shrink=0.05),
                             xytext=(xtext,ytext),
                             xycoords=('axes fraction', 'data'),
                             textcoords='offset points')

