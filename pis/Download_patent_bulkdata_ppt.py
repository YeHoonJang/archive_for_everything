import urllib
import urllib3
import urllib.request
import requests

try:

    url_list = ["https://bulkdata.uspto.gov/data2/patent/application/redbook/2017/I20170706.tar",
                "https://bulkdata.uspto.gov/data2/patent/application/redbook/2017/I20170629.tar",
                "https://bulkdata.uspto.gov/data2/patent/application/redbook/2017/I20170622.tar",
                "https://bulkdata.uspto.gov/data2/patent/application/redbook/2017/I20170615.tar",
                "https://bulkdata.uspto.gov/data2/patent/application/redbook/2017/I20170608.tar",
                "https://bulkdata.uspto.gov/data2/patent/application/redbook/2017/I20170601.tar",
                "https://bulkdata.uspto.gov/data2/patent/application/redbook/2017/I20170525.tar",
                "https://bulkdata.uspto.gov/data2/patent/application/redbook/2017/I20170525.tar"]

    for i, j in enumerate(url_list):
        url = j
        name = "patent_"+url.split('/')[-1]
        print(i, "url:", url, ", name:", name)

        print("Downloading with urllib")
        urllib.request.urlretrieve(url, name)

except:
    print("Skip!")
