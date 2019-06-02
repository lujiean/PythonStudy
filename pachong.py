# pa chong https://pan.baidu.com/share/init?surl=pUZRD5wJOM7iUA4_O-TRSw fptt

import requests

proxy={'http':'http://127.0.0.1:8888', 'https':'https://127.0.0.1:8888'}
url="https://www.baidu.com/"
ret = requests.get(url=url, proxies=proxy,verify=False)
ret.encoding = 'UTF-8'
print(ret.text)

