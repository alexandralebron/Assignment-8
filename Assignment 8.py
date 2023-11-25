#!/usr/bin/env python
# coding: utf-8

# In[ ]:


'''
Alexandra Lebron
'''


# In[1]:


from html_table_parser.parser import HTMLTableParser
import pandas as pd
import plotly.express as px
import requests
import numpy as np

url = "https://en.wikipedia.org/wiki/Anscombe%27s_quartet"
response = requests.get(url)

p = HTMLTableParser()
p.feed(response.text)


# In[2]:


# Making our data frame and preprocessing
df = pd.DataFrame(p.tables[1])
df = df.iloc[2:,:].astype(float).reset_index(drop=True)
setI = df [[0,1]]
setII = df [[2,3]]
setIII = df [[4,5]]
setIV = df [[6,7]]

setI.columns = ["x", "y"]
# To avoid warning
setI = setI.copy()
setI["Set"] = "I"

setII.columns = ["x", "y"]
# To avoid warning
setII = setII.copy()
setII["Set"] = "II"

setIII.columns = ["x", "y"]
# To avoid warning
setIII = setIII.copy()
setIII["Set"] = "III"

setIV.columns = ["x", "y"]
# To avoid warning
setIV = setIV.copy()
setIV["Set"] = "IV"

sets_list = [setI, setII, setIII, setIV]
sets_df = pd.concat(sets_list).reset_index(drop=True)


# In[3]:


sets_df


# In[3]:


fig = px.scatter(sets_df, x="x", y="y", facet_col = "Set", trendline = "ols")
fig.show()


# Compute and print the 2x2 Covariance and Correlation matrix for each dataset.

# In[12]:


# Correlation matrix
for count, i in enumerate(sets_list):
    print("Set =", i.iloc[0][2])
    print(i.corr())
    print("\n")


# In[11]:


# Covariance matrix
for count, i in enumerate(sets_list):
    print("Set =", i.iloc[0][2])
    print(i.cov())
    print("\n")

