
# coding: utf-8

# In[54]:


import requests
from bs4 import BeautifulSoup
import urllib
from urllib import request
import zipfile
import os

url_data_list  = []
for i in range(54):
    if len(str(i)) == 1:
        i = "00" + str(i)
        url_data = 'http://www.med.harvard.edu/aanlib/cases/case9/mr1-tc1/' + i + '.html'
        url_data_list.append(url_data)
    elif len(str(i)) == 2:
        i = "0" + str(i)
        url_data = 'http://www.med.harvard.edu/aanlib/cases/case9/mr1-tc1/' + i + '.html'
        url_data_list.append(url_data)
    elif len(str(i)) ==3:
        i = str(i)
        url_data = 'http://www.med.harvard.edu/aanlib/cases/case9/mr1-tc1/' + i + '.html'
        url_data_list.append(url_data)


for j in url_data_list:
    req = requests.get(j)
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')
    my_url = soup.select('body > table > tr > td > table > tr > td > a > img')
    
    print("Start Downloading...\n")

    file_name_list = []

    for url in my_url[:1]:

        file_name = url.get('src').split('/')[-1]

        file_name_list.append(file_name)
    
    a=''
    for i in url.get('src').split('/')[1:]:
        a+="/"+i
        
    file_path ="http://www.med.harvard.edu/aanlib/cases/case9" + a

    urllib.request.urlretrieve(file_path, os.path.join(os.getcwd(),file_name))
    print("Downloading '"+file_name+"' is done\n")

