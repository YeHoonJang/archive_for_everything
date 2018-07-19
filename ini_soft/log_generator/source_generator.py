import os
import time
import datetime
import random
from time import gmtime, strftime

file_names = ["/video.mp4","/vidoe.m3u8","/video.wmv","/video.flv","/video.avi"]
ips = ["123.221.14.56","16.180.70.237","10.182.189.79","218.193.16.244",
       "198.122.118.164","114.214.178.92","233.192.62.103","244.157.45.12",
       "81.73.150.239","237.43.24.118","192.168.10.190","192.168.10.108",
       "192.168.10.37","192.9.64.65","192.9.66.224","192.9.64.102"]
resources = ["http://google.com","http://naver.com","http://daum.net"]
useragents = ["Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1944.0 Safari/537.36",
            "Mozilla/5.0 (Linux; U; Android 2.3.5; en-us; HTC Vision Build/GRI40) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
            "Mozilla/5.0 (iPad; CPU OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10A5355d Safari/8536.25",
            "Mozilla/5.0 (Windows; U; Windows NT 6.1; rv:2.2) Gecko/20110201","Mozilla/5.0 (Windows NT 5.1; rv:31.0) Gecko/20100101 Firefox/31.0",
            "Mozilla/5.0 (Windows; U; MSIE 9.0; WIndows NT 9.0; en-US))"]
methods = ["GET", "POST", "PUT", "DELETE"]
error_codes = ["200", "301", "404", "500"]

now = datetime.datetime.now().strftime('%Y-%m-%d_%H_%M_%S')
otime = time.time()
end_time = otime + 1

log_name = "log_"+now+".log"
f = open(log_name, 'w')

while otime < end_time:
    ms_unit = random.randint(1, 10000)
    otime = otime + ms_unit*0.000001
    url = random.choice(resources)
    ip = random.choice(ips)
    useragent = random.choice(useragents)
    file_name = random.choice(file_names)
    method = random.choice(methods)
    error_code = random.choice(error_codes)
    f.write('%s - - [%s] %s "%s HTTP/1.0" %s %s "%s" "%s"\n' % (ip, datetime.datetime.fromtimestamp(otime).strftime('%d/%b/%Y:%H:%M:%S.%f +0100')[:-3], method, url, error_code, random.randint(2000,5000), file_name, useragent))
