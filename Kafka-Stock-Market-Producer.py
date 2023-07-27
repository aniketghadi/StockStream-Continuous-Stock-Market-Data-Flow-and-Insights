#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install kafka-python


# In[ ]:


import pandas as pd
from kafka import KafkaConsumer, KafkaProducer
from time import sleep
from json import dumps
import json


# In[ ]:


producer = KafkaProducer(bootstrap_servers=['54.91.134.37:9092'],
                         value_serializer=lambda x:
                         dumps(x).encode('utf-8'))


# In[ ]:


df = pd.read_csv("indexProcessed.csv")


# In[ ]:


df.head()


# In[ ]:


while True:
    dictionary_stock = df.sample(1).to_dict(orient="records") [0]
    producer.send('kafka_test', value=dictionary_stock)
    sleep(1)


# In[ ]:




