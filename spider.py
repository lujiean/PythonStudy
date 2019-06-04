# pa chong https://pan.baidu.com/share/init?surl=pUZRD5wJOM7iUA4_O-TRSw fptt
# https://pan.baidu.com/s/1pUZRD5wJOM7iUA4_O-TRSw fptt

import requests
from bs4 import BeautifulSoup

def PrintHttpDetails(ret):
    print(ret.status_code)
    print(ret.headers)
    print(ret.text)

def GetCookieFromResponse(resp):
    str=""
    print(resp.cookies)
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
    PrintHttpDetails(resp)
    # --

if __name__ == "__main__":
    import sys
    if sys.argv.__len__() > 1:
        if sys.argv[1] == "1":
            TestSpider1()
        elif sys.argv[1] == "2":
            TestSpider2()
    else:
        print("need input paramers")    
else:
    pass