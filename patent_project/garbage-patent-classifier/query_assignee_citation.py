
# coding: utf-8

# In[1]:


import pymysql
import pandas as pd
import numpy as np
from sshtunnel import SSHTunnelForwarder


# In[2]:


df = pd.read_csv('../data/pivot.csv')
df


# ### assignee query

# In[3]:


grant_id = [i for i in df['grant_id'] if i != 0 ]


# In[10]:


# server = SSHTunnelForwarder(
#     ('ortega.gachon.ac.kr', 22), 
#     ssh_password = 'teamlab2016@ortega', 
#     ssh_username = 'teamlab', 
#     remote_bind_address = ('127.0.0.1', 3306))
# server.start()

conn = pymysql.connect(host = '127.0.0.1', 
                       port = server.local_bind_port, 
                       user = 'root', 
                       password = 'teamlab2016@ortega', 
                       db = 'uspto')
curs = conn.cursor()


# In[ ]:


assignee_list = []
for i in grant_id:
    sql = "select * from uspto.patent_assignee where patent_id={}".format(i)
    curs.execute(sql)
    rows = curs.fetchall()
    assignee_list.append(rows)


# In[6]:


# print(len(assignee_list))
# assignee_list[:20]


# ### citation query

# In[4]:


# application_id = [i[2:] for i in df['application_id']]
# print(len(application_id))
# application_id[:10]


# In[5]:


# citation_list = []

