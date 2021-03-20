import threading
import queue
import requests
import urllib
from urllib import request
import zipfile
import os
from bs4 import BeautifulSoup

from alquimista import alquimista
import utils as utls
import worker as wkr

class PatCrawling:
    def __init__(self, id, url):
        self.id = id
        self.url = url

    def crawl_url(url):

        url_data = url
        req = requests.get(url_data)
        html = req.text
        soup = BeautifulSoup(html, "lxml")

        return soup

class PatentDownload(threading.Thread):
    def __init__(self, id, url_data):
        threading.Thread.__init__(self)
        self.url_data = url_data
        self.id = id

    def run(self):
        id = self.id
        url_data = self.url_data
        zipfile_name = url_data.split('/')[-1]

        parent_dir = utls.make_subdir(utls.CUR_DIR, "patents")
        pat_type_dir = utls.make_subdir(parent_dir, utls.is_grant_or_app(zipfile_name))
        pat_dir = utls.make_subdir(pat_type_dir, zipfile_name.split('.')[0])
        print(id, ":\n'" + zipfile_name + "' patent data will be downloaded at \n<" + pat_dir + ">.\n")

        print(id, ": Start to download...")
        zipfile_dir = os.path.join(pat_dir, zipfile_name)
        urllib.request.urlretrieve(url_data, zipfile_dir)
        print(id, ": Downloading is completed.\n")

        return [pat_dir, zipfile_name, zipfile_dir]



class Unzipping(threading.Thread):
    def __init__(self, id, pat_dir, zipfile_name, zipfile_dir):
        threading.Thread.__init__(self)
        self.id = id
        self.pat_dir = pat_dir
        self.zipfile_name = zipfile_name
        self.zipfile_dir = zipfile_dir

    def unzip(self):
        id = self.id
        print(id, ": Start to unzip...")
        unzipfile_name = self.zipfile_name.split('.')[0] + '.xml'

        zipped_pat = zipfile.ZipFile(self.zipfile_dir)
        zipped_pat.extract(unzipfile_name, self.pat_dir)
        zipped_pat.close()
        print("\n",id, ": Unzipping is completed.\n")

        return unzipfile_name



class PatentFileMaking(threading.Thread):
    def __init__(self, id, pat_dir, unzipfile_name, save_xml):
        threading.Thread.__init__(self)
        self.id = id
        self.pat_dir = pat_dir
        self.unzipfile_name = unzipfile_name
        self.save_xml = save_xml


    def is_yes_or_no():
        save_question = input("Do you want to save the file as xml? [y/n] : ")
        save_answer = save_question.upper()
        save_flag = True

        while save_flag == True:
            if save_answer in ["Y", "YES"]:
                save_xml = True
                save_flag = False
                return save_xml

            elif save_answer in ["N", "NO"]:
                save_xml = False
                save_flag = False
                return save_xml

            else:
                print("Wrong input, Input again.")
                save_question = input("Do you want to save the file as xml? [y/n] : ")
                save_answer = save_question.upper()


    def run(self):
        id = self.id
        pat_dir = self.pat_dir
        unzipfile_name = self.unzipfile_name

        print(id, ": Start to parsing and to make at DB...")
        wkr.worker(os.path.join(pat_dir, unzipfile_name), self.save_xml)

        print(id, ": Parsing and Making DB are completed.")



class RunDownloader(threading.Thread):
    def __init__(self, id, data_queue):
        threading.Thread.__init__(self)
        self.id = id
        self.data_queue = data_queue

    def run(self):

        id = self.id
        href = self.data_queue.get().get('href')
        url_file = urllib.request.urlopen(href)

        if "Content-Length" in url_file.headers:
            url_file_byte = int(url_file.headers["Content-Length"])
            url_file_size = utls.byte_unit_converter(url_file_byte)
            print("\n", id, ": The file's size is about " + url_file_size + ".\n")

            download = PatentDownload(id, href)
            pat_dir, zipfile_name, zipfile_dir = download.run()

            unzipping = Unzipping(id, pat_dir, zipfile_name, zipfile_dir)
            unzipfile_name = unzipping.unzip()

            save_answer = PatentFileMaking.is_yes_or_no()
            file_maker = PatentFileMaking(id, pat_dir, unzipfile_name, save_answer)
            file_maker.run()

            print(id, ": Thank you for using our program!")

        self.data_queue.task_done()




def main():

    url = alquimista()
    soup = PatCrawling.crawl_url(url)
    href = soup.select('body > a')

    url_queue = queue.Queue()

    worker1 = RunDownloader("worker1", url_queue)
    worker1.setDaemon(True)
    worker2 = RunDownloader("worker2", url_queue)
    worker2.setDaemon(True)
    # worker3 = RunDownloader(url_queue)
    # worker3.setDemon(True)
    # worker4 = RunDownloader(url_queue)
    # worker4.setDemon(True)
    # worker5 = RunDownloader(url_queue)
    # worker5.setDemon(True)
    # worker6 = RunDownloader(url_queue)
    # worker6.setDemon(True)
    # worker7 = RunDownloader(url_queue)
    # worker7.setDemon(True)
    # worker8 = RunDownloader(url_queue)
    # worker8.setDemon(True)

    worker1.start()
    worker2.start()
    # worker3.start()
    # worker4.start()
    # worker5.start()
    # worker6.start()
    # worker7.start()
    # worker8.start()


    for i in href:
        url_queue.put(i)



    worker1.data_queue.join()
    # worker2.dataQueue.join()
    # worker3.dataQueue.join()
    # worker4.dataQueue.join()
    # worker5.dataQueue.join()
    # worker6.dataQueue.join()
    # worker7.dataQueue.join()
    # worker8.dataQueue.join()

if __name__ == "__main__":
    main()