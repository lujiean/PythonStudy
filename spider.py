# pa chong https://pan.baidu.com/share/init?surl=pUZRD5wJOM7iUA4_O-TRSw fptt
# https://pan.baidu.com/s/1pUZRD5wJOM7iUA4_O-TRSw fptt

import requests
from bs4 import BeautifulSoup

def testSpider1():
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

def testSpider2():
    proxy={}
    url="https://pan.baidu.com/s/1pUZRD5wJOM7iUA4_O-TRSw"

    ret = requests.get(url=url, proxies=proxy,verify=False)
    ret.encoding = 'UTF-8'
    print(ret.text)

if __name__ == "__main__":
    import sys
    if sys.argv.__len__() > 1:
        if sys.argv[1] == "a":
            testSpider1()
        elif sys.argv[1] == "b":
            testSpider2()
    else:
        print("need input paramers")    
else:
    pass