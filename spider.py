# pa chong https://pan.baidu.com/share/init?surl=pUZRD5wJOM7iUA4_O-TRSw fptt
# https://pan.baidu.com/s/1pUZRD5wJOM7iUA4_O-TRSw fptt

import sys
import requests
import time

import utils_boot

from bs4 import BeautifulSoup
from urllib import parse

def PrintHttpDetails(ret):
    print(ret.status_code)
    print(ret.headers)
    print(ret.text)

def GetCookieFromResponse(resp):
    str=""
    # print(resp.cookies)
    for i in resp.cookies:
        str = str + i.name + "=" + i.value + ";"
    return str[0:len(str)-1]

def TestSpider1():
    # proxy={'http':'http://127.0.0.1:8888', 'https':'https://127.0.0.1:8888'}
    proxy={}
    # url="https://pan.baidu.com/s/1pUZRD5wJOM7iUA4_O-TRSw"
    url="https://www.baidu.com"
    ret = requests.get(url=url, proxies=proxy,verify=False)
    ret.encoding = 'UTF-8'
    print(ret.text)

    print("------")
    soup = BeautifulSoup(ret.text, "html.parser")
    print(soup.prettify())

    print("------")
    links = soup.find_all(name="a")
    for l in links:
        print(l.get_text())

def TestSpider2():
    proxy={}

    # --s1 
    url="https://pan.baidu.com/s/1pUZRD5wJOM7iUA4_O-TRSw"
    headers = {
        "Host": "pan.baidu.com",
        "Connection": "keep-alive",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9"
    }
    resp = requests.get(url, headers=headers, allow_redirects=False)
    resp.encoding = 'UTF-8'
    # PrintHttpDetails(resp)

    # set redirect url
    if resp.status_code == 302 and 'Location' in resp.headers:
        url=resp.headers['Location']
    # print(url)    
    # --

    # --s2
    str = GetCookieFromResponse(resp)
    # print(str)
    headers = {
        "Host": "pan.baidu.com",
        "Connection": "keep-alive",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Cookie": str
    }
    resp = requests.get(url, headers=headers, allow_redirects=False)
    resp.encoding = 'UTF-8'
    # PrintHttpDetails(resp)
    # --

    # --s3: post pick_up_code request
    url2 = "https://pan.baidu.com/share/verify"
    surl = parse.parse_qs(parse.urlparse(url).query)['surl'][0]
    ts13 = int(time.time()*1000)
    ts10 = int(time.time())
    params = {
        # "surl": "pUZRD5wJOM7iUA4_O-TRSw",
        "surl": surl,
        # "t": "1559704493678",
        "t": ts13,
        "channel": "chunlei",
        "web": "1",
        "app_id": "250528",
        "bdstoken": "null",
        # "logid": "MTU1OTcwNDQ5MzY4MTAuNTM0OTc1MDYyNzc4NTI2OA==",
        "logid": "MTU1OTcwNDQ5MzY4MTAuNTM0OTc1MDYyNzc4NTI2OA==",
        "clienttype": "0"
    }
    print(params)

    headers = {
        "Host": "pan.baidu.com",
        "Connection": "keep-alive",
        "Content-Length": "26",
        "Accept": "*/*",
        "Origin": "https://pan.baidu.com",
        "X-Requested-With": "XMLHttpRequest",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        # "Referer": "https://pan.baidu.com/share/init?surl=pUZRD5wJOM7iUA4_O-TRSw",
        "Referer": url,
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9",
        # "Cookie": "PANWEB=1; BAIDUID=D85812618FC241EA800013BE1D970555:FG=1; Hm_lvt_7a3960b6f067eb0085b7f96ff5e660b0=1559660491; Hm_lpvt_7a3960b6f067eb0085b7f96ff5e660b0=1559660491"
        "Cookie": "PANWEB=1; BAIDUID=D85812618FC241EA800013BE1D970555:FG=1; Hm_lvt_7a3960b6f067eb0085b7f96ff5e660b0=1559660491; Hm_lpvt_7a3960b6f067eb0085b7f96ff5e660b0=1559660491"
    }
    print(headers)

    pick_up_code = "fptt"
    data = {
        # pwd=fptt&vcode=&vcode_str=
        "pwd": pick_up_code,
        "vcode": "",
        "vcode_str": ""
    }
    print(data)

    # resp = requests.post(url2, data=data, params=params, headers=headers)
    # resp.encoding = 'UTF-8'
    # PrintHttpDetails(resp)
    # --

if __name__ == "__main__":
    
    if sys.argv.__len__() > 1:
        if sys.argv[1] == "1":
            TestSpider1()
        elif sys.argv[1] == "2":
            TestSpider2()
    else:
        print("need input paramers")    
else:
    pass