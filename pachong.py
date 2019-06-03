# pa chong https://pan.baidu.com/share/init?surl=pUZRD5wJOM7iUA4_O-TRSw fptt
# https://pan.baidu.com/s/1pUZRD5wJOM7iUA4_O-TRSw fptt

import requests
from bs4 import BeautifulSoup

# proxy={'http':'http://127.0.0.1:8888', 'https':'https://127.0.0.1:8888'}
proxy={}
url="https://pan.baidu.com/s/1pUZRD5wJOM7iUA4_O-TRSw"
ret = requests.get(url=url, proxies=proxy,verify=False)
ret.encoding = 'UTF-8'
print(ret)

print("------")
soup = BeautifulSoup(ret.text, "html.parser")
# print(soup.prettify())

# print("------")
# links = soup.find_all(name="div")
# for l in links:
#     print(l.get_text())
