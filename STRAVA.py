#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#import model
from stravaio import strava_oauth2
from stravalib.client import Client
get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


# In[ ]:


#login details for API
STRAVA_CLIENT_ID = <id>
STRAVA_CLIENT_SECRET = "<secret>
client = strava_oauth2(client_id=STRAVA_CLIENT_ID, client_secret=STRAVA_CLIENT_SECRET)


# In[ ]:


#grab token by passing temp token
access_token = client.get('access_token')
client = Client(access_token=access_token)


# In[ ]:


#call all activities
activities = client.get_activities(limit=1000)


# In[ ]:


sample = list(activities)[0]
sample.to_dict()


# In[ ]:


#prepare the data columns for the df
my_cols =['average_speed',
          'elapsed_time',
          'moving_time', 
          'distance',
          'elapsed_time',
          'total_elevation_gain',
          'type', 
          'start_date_local']


# In[ ]:


#get the data appended to create a df
data = []
for activity in activities:
    my_dict = activity.to_dict()
    data.append([my_dict.get(x) for x in my_cols])


# In[ ]:


#create the df
df = pd.DataFrame(data, columns=my_cols)


# In[ ]:


df.to_csv('data.csv')


# In[ ]:





# In[ ]:




