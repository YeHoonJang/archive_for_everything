
# coding: utf-8

# In[2]:

import requests
from bs4 import BeautifulSoup
import urllib
from urllib import request
import zipfile
import re


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

file_list = []

for url in my_url[:2]:
    file_name = url.get('href').split('/')[-1]
    file_list.append(file_name)
    
    urllib.request.urlretrieve(url.get('href'), file_name)
    print("Downloading '"+file_name+"' is done\n")


# In[7]:

import os

if not os.path.isdir("C:/workspace/code_for_study/pis/patent_file/"):
    os.mkdir("C:/workspace/code_for_study/pis/patent_file/")

unzipped_list = []

for i in file_list:
    
    file_path = "C:\workspace\code_for_study\pis" + "\\" + str(i)
    
    unzipped_name = i.split('.')[0]
    pd_name = unzipped_name[-6:]
    pd_path = "C:/workspace/code_for_study/pis/patent_file/" + pd_name
    
    if not os.path.isdir(pd_path):
        os.mkdir(pd_path)
    
    unzipped_file = unzipped_name + ".xml"
    unzipped_list.append(unzipped_file)
    
    full_patent = pd_path + "/" + str(pd_name+".xml")

#     unzipped_file_path = "C:/workspace/code_for_study/pis/patent_file"
    
    patent_zip = zipfile.ZipFile(file_path)
    patent_zip.extract(unzipped_file, pd_path)
    
    patent_zip.close()


# In[19]:

patent_text_list = []

for i in unzipped_list:
    patent_text = "C:/workspace/code_for_study/pis/patent_file" +"\\" + str(i)
#     patent_file_list.append(patent_text)
    

    f = open(patent_text, "r")
    patent = ''
    
    print("1")
    while True:
        line = f.readline()
        patent += line
        if not line: break
    f.close()
    print("2")
    
    start_index = [i.start() for i in re.finditer("""\<\?xml version="1.0" encoding="UTF-8"\?>""", patent)]
    start_index.append(len(patent)+1)
    
    text_list =[]
    for start in range(1, len(start_index)):
        text_list.append(patent[start_index[start-1]:start_index[start]])
        
    for i in range(len(text_list)):
        patent_file = "patent_" + str(i) + ".xml"
        with open(patent_file, "w") as f:
            f.write(text_list[i])
            f.close()



# In[ ]:



