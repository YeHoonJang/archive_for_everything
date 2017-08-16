
# coding: utf-8

# In[1]:


import requests
import urllib
import queue
import threading
import zipfile
import os
import sys
from bs4 import BeautifulSoup


# In[3]:


class FileWorker(threading.Thread):
    def __init__(self,id,dataQueue):
        threading.Thread.__init__(self)
        self.id = id
        self.dataQueue = dataQueue

    def run(self):
        while True:
            data = self.dataQueue.get()
            print("data",data, "type", type(data))
            print("[" + str(self.id)+" : " + str(data) + "]\n")
            fileName = data.split('/')[-1]
            fileSave = open(fileName,"wb")
            urlFile = urllib.request.urlopen(data)
            print(urlFile)
            print(fileName)
            if "Content-Length" in urlFile.headers:
                urlFileByteSize = int(urlFile.headers["Content-Length"])
                print(urlFileByteSize)
                fileFlag = True
                fileDownSize = 0;
                blockSize = 8192
                while fileFlag:
                    buffer = urlFile.read(blockSize)
                    if not buffer:
                        fileFlag = False
                    fileDownSize +=len(buffer)
                    fileSave.write(buffer)
                fileSave.close()
                #filePath = os.getcwd()+fileName
                #print(filePath)
            self.dataQueue.task_done()


# In[ ]:


def main():
    url = 'https://www.google.com/googlebooks/uspto-patents-applications-text.html'
    source = requests.get(url, allow_redirects=False)
    pText = source.text
    soup  = BeautifulSoup(pText,'html.parser')

    urlQueue = queue.Queue()

    worker1 = FileWorker("worker1", urlQueue)
    worker1.setDaemon(True)
    worker2 = FileWorker("worker2", urlQueue)
    worker2.setDaemon(True)
    worker3 = FileWorker("worker3", urlQueue)
    worker3.setDaemon(True)

    worker1.start()
    worker2.start()
    worker3.start()

    number =0
    for link in soup.findAll('a'):
        href = link.get('href')
        if(number >2):
            break
        if href.endswith('zip'):
            number = number +1
            urlQueue.put(href)

    worker1.dataQueue.join()
    worker2.dataQueue.join()
    worker3.dataQueue.join()

if __name__ == "__main__":
    main()


# In[ ]:





# In[ ]:




