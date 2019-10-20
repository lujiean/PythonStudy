import requests

from bs4 import BeautifulSoup

header={
    "Host": "www.ktkkt.com",
    "Connection": "keep-alive",
    "Cache-Control": "max-age=0",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9"
}

resp = requests.get(
    url="http://www.ktkkt.com/y/index.html",
    headers=header
)
resp.encoding = 'gb2312'
# print(resp.text)

soup = BeautifulSoup(resp.text, "html.parser")
print(soup.prettify())
print("------")
# print(soup.find_all('ul')[0].find_all('a'))
for r in soup.find_all('ul'):
    for s in r.find_all('strong'):
        for t in s.find_all('a'):
            print(t.get('title'))
print("------")
# l=soup.find_all('ul')
# htext=l[0]
# soup1 = BeautifulSoup(htext, "html.parser")
# print(soup1.find_all('ul'))
# for i in soup.find_all('a', 'class'):
#     print(i.get('title'))