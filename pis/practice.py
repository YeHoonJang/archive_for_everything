
# coding: utf-8

# In[2]:

import requests
from bs4 import BeautifulSoup
import urllib
from urllib import request
import zipfile
import os


# In[3]:

req = requests.get('https://www.google.com/googlebooks/uspto-patents-grants-text.html')
html = req.text
soup = BeautifulSoup(html, 'html.parser')


# <br>
# html에서 parser할 태그 확인 → copy selector<br>
# container > a:nth-child(18)

# In[4]:

my_url = soup.select('body > a')
print("Start Downloading...\n")

file_name_list = []

for url in my_url[:1]:
    file_name = url.get('href').split('/')[-1]
    file_name_list.append(file_name)
    print(file_name)
    print(file_name_list)
    
    urllib.request.urlretrieve(url.get('href'), file_name)
    print("Downloading '"+file_name+"' is done\n")


# In[5]:

import os

if not os.path.isdir("C:/workspace/code_for_study/pis/patent_file/"):
    os.mkdir("C:/workspace/code_for_study/pis/patent_file/")

unzipped_file_list = []

for i in file_name_list:
    
    file_path = "C:\workspace\code_for_study\pis" + "\\" + str(i)
    print(file_path)
    
    unzipped_name = i.split('.')[0]
    p_directory = "C:/workspace/code_for_study/pis/patent_file/" + unzipped_name[-6:]
    
    if not os.path.isdir(p_directory):
        os.mkdir(p_directory)
    
    unzipped_file_name = unzipped_name + ".xml"
    
    unzipped_file_list.append(unzipped_file_name + str(".xml"))
    print(unzipped_file_name, unzipped_file_list, unzipped_name)
    
    
    patent_text = p_directory + "/" + str(unzipped_name[-6:]+".xml")

#     unzipped_file_path = "C:/workspace/code_for_study/pis/patent_file"
    
    patent_zip = zipfile.ZipFile(file_path)
    patent_zip.extract(unzipped_file_name,p_directory)
    
    patent_zip.close()


# In[7]:

unzipped_name[-6:]


# In[ ]:

import os

p_directory = "C:/workspace/code_for_study/pis/patent_file/" + unzipped_name[-6:]
patent_text = p_directory + "/" + str(unzipped_name+".xml")

f = open(patent_text, "r")
patent = ''
while True:
    line = f.readline()
    patent += line
    if not line: break
    
f.close()


# In[ ]:

p_directory


# In[ ]:

import re


# In[ ]:

start_index = [i.start() for i in re.finditer("""\<\?xml version="1.0" encoding="UTF-8"\?>""", patent)]


# In[ ]:

len(patent)


# In[46]:

start_index.append(len(patent)+1)
start_index


# In[47]:

text_list =[]
for start in range(1, len(start_index)):
    text_list.append(patent[start_index[start-1]:start_index[start]])


# In[48]:

len(text_list)


# In[54]:



for i in range(len(text_list)):
    patent_file = p_directory + "\\" + unzipped_name[-6:] + "_" + str(i+1) + ".xml"
    if not os.path.isfile(patent_file):
        with open(patent_file, "w") as f:
            f.write(text_list[i])
            f.close()


# In[ ]:



