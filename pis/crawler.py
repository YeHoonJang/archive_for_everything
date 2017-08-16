import urllib
from urllib import request
import zipfile
import os
import re
import utils as utls

class PatentDownload:
    def __init__(self, url_data):
        self.url_data = url_data

    def run(self):

        url_data = self.url_data
        zipfile_name = url_data.split('/')[-1]

        parent_dir = utls.make_subdir(utls.CUR_DIR, "patents")
        pat_type_dir = utls.make_subdir(parent_dir, utls.is_grant_or_app(zipfile_name))
        pat_dir = utls.make_subdir(pat_type_dir, zipfile_name.split('.')[0])
        print("\n'" + zipfile_name + "' patent data will be downloaded at \n<" + pat_dir + ">.\n")

        print("Start to download...")
        zipfile_dir = os.path.join(pat_dir, zipfile_name)
        urllib.request.urlretrieve(url_data, zipfile_dir)
        print("Downloading is complete.\n")

        return [pat_dir, zipfile_name, zipfile_dir]



def unzip(pat_dir, zipfile_name, zipfile_dir):
    print("Start to unzip...")
    unzipfile_name = zipfile_name.split('.')[0] + '.xml'

    zipped_pat = zipfile.ZipFile(zipfile_dir)
    zipped_pat.extract(unzipfile_name, pat_dir)
    zipped_pat.close()
    print("Unzipping is complete.\n")

    return unzipfile_name



class PatentFoldering:
    def __init__(self, pat_dir, unzipfile_name, save_xml):
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
        print("\nStart to save the file as list...")
        pat_dir = self.pat_dir
        unzipfile_name = self.unzipfile_name
        pat_text = utls.make_subdir(pat_dir, unzipfile_name)

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
        print("Saving the file as list is complete.\n")

        # 파일 저장 code
        if self.save_xml == True:
            print("Start to split the file as xml...")
            for i in range(len(start_list)):
                pat_xmlfile = unzipfile_name.split('.')[0] + "_" + str(i + 1) + ".xml"
                pat_file = os.path.join(pat_dir, pat_xmlfile)
                if not os.path.isfile(pat_file):
                    with open(pat_file, "w") as f:
                        f.write(start_list[i])
                        f.close()
            print("File splitting is complete.\n")


def main():

    url = 'http://storage.googleapis.com/patents/grant_full_text/2015/ipg150106.zip'
    url_file = urllib.request.urlopen(url)

    is_download = ''
    if "Content-Length" in url_file.headers:
        url_file_byte = int(url_file.headers["Content-Length"])
        url_file_size = utls.byte_unit_converter(url_file_byte)

        is_download = utls.is_file_download(url_file_size)


    if is_download == True:

        download = PatentDownload(url)
        pat_dir, zipfile_name, zipfile_dir = download.run()

        unzipfile_name = unzip(pat_dir, zipfile_name, zipfile_dir)

        save_answer = PatentFoldering.is_yes_or_no()
        folder_maker = PatentFoldering(pat_dir, unzipfile_name, save_answer)
        folder_maker.run()

        print("Thank you for using our program!")

    else:
        print("Thank you for using our program!")


if __name__ == "__main__":
    main()
