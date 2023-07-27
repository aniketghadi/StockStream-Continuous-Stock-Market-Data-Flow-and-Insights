#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install s3fs


# In[2]:


from kafka import KafkaConsumer
from time import sleep
from json import dumps,loads
import json
from s3fs import S3FileSystem


# In[3]:


consumer = KafkaConsumer('kafka_test',
                        bootstrap_servers=['54.91.134.37:9092'],
                        value_deserializer=lambda x:loads(x.decode('utf-8')))


# In[4]:


s3= S3FileSystem()


# In[ ]:


for count, i in enumerate(consumer):
     with s3.open("s3://kafka-stock-market-data-analysis/stock_market_{}.json".format(count), 'w') as file:
        json.dump(i.value, file)  


# In[ ]:




