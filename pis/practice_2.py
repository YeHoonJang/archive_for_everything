import requests
from bs4 import BeautifulSoup
import urllib
from urllib import request
import zipfile
import os
import threading
import queue
import re

class PatentDownload(threading.Thread):

    def __init__(self, id, dataQueue, saveXml):
        threading.Thread.__init__(self)
        self.id = id
        self.dataQueue = dataQueue
        self.saveXml = saveXml


    def isYesOrNo():
        save_question = input("Do you want to save the file as xml? [y/n] : ")
        save_answer = save_question.upper()
        save_flag = True

        while save_flag == True:
            if save_answer in ["Y", "YES"]:
                saveXml = True
                save_flag = False
                return saveXml

            elif save_answer in ["N", "NO"]:
                saveXml = False
                save_flag = False
                return saveXml

            else:
                print("Wrong input, Input Again.")
                save_question = input("Do you want to save the file as xml? [y/n] : ")
                save_answer = save_question.upper()





    def run(self):

        while True:
            url_data = self.dataQueue.get()
            print("url_data", url_data)
            str_url = url_data.get('href')
            zipfile_name = str_url.split('/')[-1]
            print(str(self.id) + " : [" + str(url_data) + "]\n")

            parent_path = os.path.join(os.getcwd(), "patents")

            if 'ipg' in zipfile_name.split('.')[0]:
                pat_type = 'grants'

            elif 'ipa' in zipfile_name.split('.')[0]:
                pat_type = 'applications'

            try:
                pat_type_path = os.path.join(parent_path, pat_type)
                if not os.path.exists(pat_type_path):
                    os.mkdir(pat_type_path)
            except:
                pass

            pat_path = os.path.join(pat_type_path, zipfile_name.split('.')[0])
            print(str(
                self.id) + " : " + "Your '" + zipfile_name + "' patent data is downloaded at <" + pat_path + ">.\n")

            if not os.path.exists(pat_path):
                os.mkdir(pat_path)

            zipfile_path = os.path.join(pat_path, zipfile_name)
            print("zipfile_path:",zipfile_path)
            urllib.request.urlretrieve(str_url, zipfile_path)

            unzipfile_name = zipfile_name.split('.')[0] + '.xml'

            pat_zip = zipfile.ZipFile(zipfile_path)
            pat_zip.extract(unzipfile_name, pat_path)
            pat_zip.close()

            pat_text = os.path.join(pat_path, unzipfile_name)

            f = open(pat_text, "r")
            pat_lines = ''
            while True:
                line = f.readline()
                pat_lines += line
                if not line: break
            f.close()

            start_index = [i.start() for i in re.finditer("""\<\?xml version="1.0" encoding="UTF-8"\?>""",
                                                          pat_lines)]
            start_index.append(len(pat_lines) + 1)

            start_list = []
            for start in range(1, len(start_index)):
                start_list.append(pat_lines[start_index[start - 1]:start_index[start]])

            # 파일 저장 code
            if self.saveXml == True:
                print(str(self.id) + " : " + "Start to split the whole file into individual xml files... \n")
                for i in range(len(start_list)):
                    pat_xmlfile = zipfile_name.split('.')[0] + "_" + str(i + 1) + ".xml"
                    pat_file = os.path.join(pat_path, pat_xmlfile)
                    if not os.path.isfile(pat_file):
                        with open(pat_file, "w") as f:
                            f.write(start_list[i])
                            f.close()
                print(str(self.id) + " : " + "File splitting is complete.\n")

            self.dataQueue.task_done()






def main():

    url = 'https://www.google.com/googlebooks/uspto-patents-applications-text.html'
    req = requests.get(url)
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')


    parent_path = os.path.join(os.getcwd(), "patents")
    if not os.path.exists(parent_path):
        os.mkdir(parent_path)


    urlQueue = queue.Queue()
    save_answer = PatentDownload.isYesOrNo()



    print("Start to Download...\n")

    worker1 = PatentDownload("worker1", urlQueue, save_answer)
    worker1.setDaemon(True)
    worker2 = PatentDownload("worker2", urlQueue, save_answer)
    worker2.setDaemon(True)
    worker3 = PatentDownload("worker3", urlQueue, save_answer)
    worker3.setDaemon(True)
    worker4 = PatentDownload("worker4", urlQueue, save_answer)
    worker4.setDaemon(True)
    # worker5 = PatentDownload("worker5", urlQueue, save_answer)
    # worker5.setDaemon(True)
    # worker6 = PatentDownload("worker6", urlQueue, save_answer)
    # worker6.setDaemon(True)
    # worker7 = PatentDownload("worker7", urlQueue, save_answer)
    # worker7.setDaemon(True)
    # worker8 = PatentDownload("worker8", urlQueue, save_answer)
    # worker8.setDaemon(True)

    worker1.start()
    worker2.start()
    worker3.start()
    worker4.start()
    # worker5.start()
    # worker6.start()
    # worker7.start()
    # worker8.start()


    href = soup.select('body > a')
    for i in href[:20]:
        urlQueue.put(i)

    # href = soup.select('body > a')
    #
    # try:
    #    for i in range(2014, 2016):
    #        for j in href:
    #            year = j.get('href').split('/')[-2]
    #            if year == i:
    #                print(year)
    #                urlQueue.put(href)
    #            else:
    #                pass
    # except:
    #     pass

    worker1.dataQueue.join()
    worker2.dataQueue.join()
    worker3.dataQueue.join()
    worker4.dataQueue.join()
    # worker5.dataQueue.join()
    # worker6.dataQueue.join()
    # worker7.dataQueue.join()
    # worker8.dataQueue.join()
    print("Downloading is complete.")


if __name__ == "__main__":
    main()
