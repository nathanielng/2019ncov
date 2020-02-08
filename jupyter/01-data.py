#!/usr/bin/env python
# coding: utf-8

# # 2019 nCov Tracking
# 
# ## 1. Data Sources
# 
# ### 1.1 Singapore
# 
# - **Ministry of Health**: https://www.moh.gov.sg/2019-ncov-wuhan
# 
# ### 1.2 Worldwide
# 
# - **John Hopkins**: https://gisanddata.maps.arcgis.com/apps/opsdashboard/index.html#/bda7594740fd40299423467b48e9ecf6
# 
# ### 1.3 Libraries & Dependencies

# In[1]:


import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import requests


# ## 2. Data
# 
# ### 2.1 Singapore Data

# In[2]:


get_ipython().run_cell_magic('writefile', 'data/singapore.csv', 'Date,Cases,URL\n23 Jan 2020,  1, https://www.moh.gov.sg/news-highlights/details/confirmed-imported-case-of-novel-coronavirus-infection-in-singapore-multi-ministry-taskforce-ramps-up-precautionary-measures\n24 Jan 2020,  3, https://www.moh.gov.sg/news-highlights/details/two-more-cases-of-confirmed-imported-case-of-novel-coronavirus-infection-in-singapore\n26 Jan 2020,  4, https://www.moh.gov.sg/news-highlights/details/fourth-confirmed-imported-case-of-wuhan-coronavirus-infection-in-singapore\n27 Jan 2020,  5, https://www.moh.gov.sg/news-highlights/details/fifth-confirmed-imported-case-of-wuhan-coronavirus-infection-in-singapore-27Jan\n28 Jan 2020,  7, https://www.channelnewsasia.com/news/singapore/wuhan-virus-singapore-latest-confirmed-cases-coronavirus-12360924\n29 Jan 2020, 10, https://www.moh.gov.sg/news-highlights/details/three-more-confirmed-imported-cases-of-wuhan-coronavirus-infection-in-singapore\n30 Jan 2020, 13, https://www.moh.gov.sg/news-highlights/details/three-more-confirmed-imported-cases-of-wuhan-coronavirus-infection-in-singapore-30Jan\n31 Jan 2020, 16, https://www.moh.gov.sg/news-highlights/details/three-more-confirmed-imported-cases-of-wuhan-coronavirus-infection-in-singapore-31-jan\n 1 Feb 2020, 18, https://www.moh.gov.sg/news-highlights/details/two-more-confirmed-imported-cases-of-novel-coronavirus-infection-in-singapore\n 2 Feb 2020, 18, https://www.moh.gov.sg/news-highlights/details/no-new-confirmed-cases-of-novel-coronavirus-infection-in-singapore\n 3 Feb 2020, 18, https://www.moh.gov.sg/news-highlights/details/no-new-confirmed-cases-of-novel-coronavirus-infection-in-singapore-3-Feb\n 4 Feb 2020, 24, https://www.moh.gov.sg/news-highlights/details/confirmed-cases-of-local-transmission-of-novel-coronavirus-infection-in-singapore\n 5 Feb 2020, 28, https://www.moh.gov.sg/news-highlights/details/four-more-confirmed-cases-of-novel-coronavirus-infection-in-singapore\n 6 Feb 2020, 30, https://www.moh.gov.sg/news-highlights/details/two-more-confirmed-cases-of-novel-coronavirus-infection-in-singapore\n 7 Feb 2020, 33, https://www.moh.gov.sg/news-highlights/details/three-more-confirmed-cases-of-novel-coronavirus-infection-in-singapore')


# In[3]:


url = 'https://www.moh.gov.sg/2019-ncov-wuhan'
dfs = pd.read_html(url)


# ### 2.2 Worldwide Data

# In[4]:


get_ipython().run_cell_magic('writefile', 'data/worldwide.csv', 'Date,Mainland China,Other Locations\n20 Jan 2020,   278,   4\n21 Jan 2020,   326,   6\n22 Jan 2020,   547,   8\n23 Jan 2020,   639,  14\n24 Jan 2020,   916,  25\n25 Jan 2020,  2000,  40\n26 Jan 2020,  2700,  57\n27 Jan 2020,  4400,  64\n28 Jan 2020,  6000,  87\n29 Jan 2020,  7700, 105\n30 Jan 2020,  9700, 118\n31 Jan 2020, 11200, 153\n 1 Feb 2020, 14300, 173\n 2 Feb 2020, 17200, 183\n 3 Feb 2020, 19700, 188')


# ## 3. Data Preprocessing

# In[5]:


dfsg = pd.read_csv('data/singapore.csv')
dfsg['Date'] = pd.to_datetime(dfsg['Date'], dayfirst=True)
dfsg.head()


# In[6]:


dfw = pd.read_csv('data/worldwide.csv')
dfw['Date'] = pd.to_datetime(dfw['Date'], dayfirst=True)
dfw['Total'] = dfw['Mainland China'] + dfw['Other Locations']


# In[7]:


dfw


# ## 4. Plots

# In[8]:


fig, ax = plt.subplots(3, 1, sharex=True, figsize=(7,12))
dfw.plot(x='Date', y='Mainland China', marker='o', ax=ax[0]);
dfw.plot(x='Date', y='Other Locations', marker='o', ax=ax[1]);
dfsg.plot(x='Date', y='Cases', marker='o', ax=ax[2], label='Singapore');

