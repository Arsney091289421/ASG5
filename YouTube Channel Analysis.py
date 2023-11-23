#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Install necessary package
get_ipython().system('pip install pymysql')
get_ipython().system('pip install pandas sqlalchemy')


# In[2]:


# Import Python Libraries
import pandas as pd
from sqlalchemy import create_engine


# In[3]:


# Load the dataset 
df = pd.read_csv('youtube_dataset.csv') 


# In[4]:


# Define a function to calculate the distribution of channel types
def calculate_channeltype_distribution(dataset):
    channeltype_distribution = dataset['channeltype'].value_counts()
    return channeltype_distribution


# In[5]:


# Select the top 1000 records
top_1000_records = df.head(1000)


# In[6]:


# Calculate channel type distribution
channeltype_distribution = calculate_channeltype_distribution(top_1000_records)


# In[7]:


print("ChannelType Distribution:")
print(channeltype_distribution)


# In[8]:


# Save the top 1000 records to a CSV file
top_1000_records.to_csv('top_1000_channels.csv', index=False)


# In[9]:


# Create a database engine
engine = create_engine('mysql+pymysql://<username>:<password>@<host>:<port>/<database>')

# Write the DataFrame to the 'Top1000Channels' table in the database
top_1000_records.to_sql('Top1000Channels', con=engine, index=False, if_exists='replace')


# In[ ]:





# In[ ]:




