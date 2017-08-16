
import requests
from bs4 import BeautifulSoup
import urllib
from urllib import request
import zipfile
import os


req = requests.get('http://www.med.harvard.edu/aanlib/cases/case9/mr1-tc1/020.html')
html = req.text
soup = BeautifulSoup(html, 'html.parser')




# html에서 parser할 태그 확인 → copy selector<br>
# container > a:nth-child(18)


my_url = soup.select('body > table > tbody > tr:nth-child(1) > td > table > tbody > tr > td:nth-child(1) > a > img')
print("Start Downloading...\n")

file_name_list = []

for url in my_url[:1]:
    print(url, type(url))
    file_name = url.get('src').split('/')[-1]
    file_name_list.append(file_name)
    print(file_name)
    print(file_name_list)

    urllib.request.urlretrieve(url.get('src'), file_name)
    print("Downloading '"+file_name+"' is done\n")
#
# cur_dir = os.getcwd()
# if not os.path.isdir(cur_dir + "/patent_file/"):
#     os.mkdir(cur_dir + "/patent_file/")
#
# unzipped_file_list = []
#
# for i in file_name_list:
#
#     # file_path = cur_dir + "/patent_file/" + str(i)
#     # print("filepath", file_path)
#
#     unzipped_name = i.split('.')[0]
#     p_directory = cur_dir + "/patent_file/" + unzipped_name[-6:]
#     file_path = cur_dir + "/patent_file/"
#
#     if not os.path.isdir(p_directory):
#         os.mkdir(p_directory)
#
#     unzipped_file_name = unzipped_name + ".xml"
#
#     unzipped_file_list.append(unzipped_file_name + str(".xml"))
#     print(unzipped_file_name, unzipped_file_list, unzipped_name)
#
#
#     patent_text = p_directory + "/" + str(unzipped_name[-6:]+".xml")
#
#     #     unzipped_file_path = "C:/workspace/code_for_study/pis/patent_file"
#
#     patent_zip = zipfile.ZipFile(os.path.join(cur_dir, file_name))
#     patent_zip.extract(unzipped_file_name,os.path.join(file_path,unzipped_name))
#     a = os.path.join(file_path,unzipped_name)
#
#     patent_zip.close()
#
#
#
#
#     p_directory = cur_dir + "/patent_file/" + unzipped_name[-6:]
#     patent_text = os.path.join(a, str(unzipped_name+".xml"))
#
#     f = open(patent_text, "r")
#     patent = ''
#     while True:
#         line = f.readline()
#         patent += line
#         if not line: break
#
#     f.close()
#
#
# import re
#
#
# start_index = [i.start() for i in re.finditer("""\<\?xml version="1.0" encoding="UTF-8"\?>""", patent)]
#
# len(patent)
#
#
# start_index.append(len(patent)+1)
#
#
# text_list =[]
# for start in range(1, len(start_index)):
#     text_list.append(patent[start_index[start-1]:start_index[start]])
#
#
#
# len(text_list)
#
#
# for i in range(len(text_list)):
#     patent_file = p_directory + "\\" + unzipped_name[-6:] + "_" + str(i+1) + ".xml"
#     if not os.path.isfile(patent_file):
#         with open(patent_file, "w") as f:
#             f.write(text_list[i])
#             f.close()
