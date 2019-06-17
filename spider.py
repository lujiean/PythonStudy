# pa chong https://pan.baidu.com/share/init?surl=pUZRD5wJOM7iUA4_O-TRSw fptt
# https://pan.baidu.com/s/1pUZRD5wJOM7iUA4_O-TRSw fptt

import sys
import requests
import time
import execjs
import json
import os
import smtplib
import logging

from bs4 import BeautifulSoup
from urllib import parse
from utils import spiderutils
from email.mime.text import MIMEText
from email.header import Header

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

def TestSpider2(rootPath):

    #read config file
    if len(rootPath) == 0:
        print("input root path as arg 2")
        return
    else:
        cwd=rootPath
    # cfgFile = "./config/spider.cfg"
    cfgFile = cwd + "/config/usr/spider.json"
    if not os.path.isfile(cfgFile):
        with open(cfgFile, "w", encoding="UTF-8") as f:
            f.write("")
        print("not found config file. setup as " + cwd +"/config/usr/README do")
        return
    else:
        with open(cfgFile,"r", encoding="UTF-8") as f:
            cfgText = json.load(f)
        url = cfgText["url"]
        pick_up_code = cfgText["pickup"]
        username = cfgText["email"]["username"]
        passwd = cfgText["email"]["passwd"]
        receiver = cfgText["email"]["receiver"]

    #log file
    if not os.path.isdir(cwd + "/log"):
        os.makedirs(cwd + "/log")
    fh = logging.FileHandler(filename=cwd + "/log/spider.log", encoding="UTF-8")
    logging.basicConfig(level=logging.INFO, handlers=[fh])

    #pan.baidu.com config
    with open(cwd + "/config/pan.baidu.com/config.json", "r", encoding='UTF-8') as f:
        dupanConfig = json.load(f)
    #--
    logging.info("===spider2 start===")
    logging.info(time.asctime())

    # proxy={'http':'http://127.0.0.1:8888', 'https':'https://127.0.0.1:8888'}
    # proxy={}
    proxy=dupanConfig["proxy"]

    # --s1 
    # url="https://pan.baidu.com/s/1pUZRD5wJOM7iUA4_O-TRSw"
    # headers = {
    #     "Host": "pan.baidu.com",
    #     "Connection": "keep-alive",
    #     "Upgrade-Insecure-Requests": "1",
    #     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36",
    #     "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
    #     "Accept-Encoding": "gzip, deflate, br",
    #     "Accept-Language": "zh-CN,zh;q=0.9"
    # }
    curStep = "step1"
    if curStep in dupanConfig:
        dupanConfig[curStep]["url"] = url
        # headers = dupanConfig["step1"]["headers"]
        # allow_redirects = dupanConfig["step1"]["allow_redirects"]
        # resp = requests.get(url, proxies=proxy, headers=headers, allow_redirects=False)
        resp = requests.get(url=dupanConfig[curStep]["url"], 
                            proxies=dupanConfig["proxy"], 
                            headers=dupanConfig[curStep]["headers"], 
                            allow_redirects=dupanConfig[curStep]["allow_redirects"])
        resp.encoding = 'UTF-8'
    
        # PrintHttpDetails(resp)

        # set redirect url
        if resp.status_code == 302 and 'Location' in resp.headers:
            url3=resp.headers['Location']
        # print(url)    
        logging.info(resp.status_code)
    else:
        logging.info("No "+curStep)
    # --

    # --s2
    cookieDict = spiderutils.GetCookieDict(resp)
    cookie = spiderutils.GetCookieStrFromDict(cookieDict)
    # print(str)
    # headers = {
    #     "Host": "pan.baidu.com",
    #     "Connection": "keep-alive",
    #     "Upgrade-Insecure-Requests": "1",
    #     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36",
    #     "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
    #     "Accept-Encoding": "gzip, deflate, br",
    #     "Accept-Language": "zh-CN,zh;q=0.9",
    #     "Cookie": cookie
    # }
    curStep="step2"
    if curStep in dupanConfig:

        dupanConfig[curStep]["url"]=url3
        dupanConfig[curStep]["headers"]["Cookie"]=cookie
        # resp = requests.get(url3, proxies=proxy, headers=headers, allow_redirects=False)
        resp = requests.get(url=dupanConfig[curStep]["url"], 
                            proxies=dupanConfig["proxy"], 
                            headers=dupanConfig[curStep]["headers"], 
                            allow_redirects=dupanConfig[curStep]["allow_redirects"])
        resp.encoding = 'UTF-8'
    # PrintHttpDetails(resp)
        logging.info(resp.status_code)
    else:
        logging.info("No "+curStep)
    # --

    # --s3: post pick_up_code request
    curStep="step3"
    if curStep in dupanConfig:
        # url2 = "https://pan.baidu.com/share/verify"
        surl = parse.parse_qs(parse.urlparse(url3).query)['surl'][0]
        ts13 = str(int(time.time()*1000))
        ts10 = str(int(time.time()))

        with open(cwd + "/js/boot.js", "r", encoding="UTF-8") as f:
            content = f.read()
        ctx = execjs.compile(content)
        logid = ctx.call("Getlogid", cookieDict["BAIDUID"])

        dupanConfig[curStep]["params"]["surl"]=surl
        dupanConfig[curStep]["params"]["t"]=ts13
        dupanConfig[curStep]["params"]["logid"]=logid
    # params = {
    #     # "surl": "pUZRD5wJOM7iUA4_O-TRSw",
    #     "surl": surl,
    #     # "t": "1559704493678",
    #     "t": ts13,
    #     "channel": "chunlei",
    #     "web": "1",
    #     "app_id": "250528",
    #     "bdstoken": "null",
    #     # "logid": "MTU1OTcwNDQ5MzY4MTAuNTM0OTc1MDYyNzc4NTI2OA==",
    #     "logid": logid,
    #     "clienttype": "0"
    # }
    # print(params)

    # Hm_lvt_7a3960b6f067eb0085b7f96ff5e660b0=1559660491; Hm_lpvt_7a3960b6f067eb0085b7f96ff5e660b0=1559660491"
        cookieDict["Hm_lvt_7a3960b6f067eb0085b7f96ff5e660b0"]=ts10
        cookieDict["Hm_lpvt_7a3960b6f067eb0085b7f96ff5e660b0"]=ts10
        cookie = spiderutils.GetCookieStrFromDict(cookieDict)
        dupanConfig[curStep]["headers"]["Referer"]=url3
        dupanConfig[curStep]["headers"]["Cookie"]=cookie
    # headers = {
    #     "Host": "pan.baidu.com",
    #     "Connection": "keep-alive",
    #     "Content-Length": "26",
    #     "Accept": "*/*",
    #     "Origin": "https://pan.baidu.com",
    #     "X-Requested-With": "XMLHttpRequest",
    #     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36",
    #     "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    #     # "Referer": "https://pan.baidu.com/share/init?surl=pUZRD5wJOM7iUA4_O-TRSw",
    #     "Referer": url3,
    #     "Accept-Encoding": "gzip, deflate, br",
    #     "Accept-Language": "zh-CN,zh;q=0.9",
    #     # "Cookie": "PANWEB=1; BAIDUID=D85812618FC241EA800013BE1D970555:FG=1; Hm_lvt_7a3960b6f067eb0085b7f96ff5e660b0=1559660491; Hm_lpvt_7a3960b6f067eb0085b7f96ff5e660b0=1559660491"
    #     "Cookie": cookie
    # }
    # print(headers)

    # pick_up_code = "fptt"
        dupanConfig[curStep]["data"]["pwd"]=pick_up_code
    # data = {
    #     # pwd=fptt&vcode=&vcode_str=
    #     "pwd": pick_up_code,
    #     "vcode": "",
    #     "vcode_str": ""
    # }
    # print(data)

    # resp = requests.post(url2, proxies=proxy, data=data, params=params, headers=headers)
        resp = requests.post(url=dupanConfig[curStep]["url"], 
                             proxies=dupanConfig["proxy"], 
                             params=dupanConfig[curStep]["params"], 
                             headers=dupanConfig[curStep]["headers"],
                             data=dupanConfig[curStep]["data"])
        resp.encoding = 'UTF-8'
        # PrintHttpDetails(resp)
        randsk=json.loads(resp.text, encoding='UTF-8').get('randsk')
        logging.info(resp.status_code)
    else:
        logging.info("No "+curStep)
    # --

    # s4--
    curStep="step4"
    if curStep in dupanConfig:
        cookieDict["BDCLND"] = randsk
        cookie = spiderutils.GetCookieStrFromDict(cookieDict)
        dupanConfig[curStep]["url"]=url
        dupanConfig[curStep]["Referer"]=url3
        dupanConfig[curStep]["Cookie"]=cookie
        # headers = {
        #     "Host": "pan.baidu.com",
        #     "Connection": "keep-alive",
        #     "Upgrade-Insecure-Requests": "1",
        #     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36",
        #     "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
        #     # "Referer": "https://pan.baidu.com/share/init?surl=pUZRD5wJOM7iUA4_O-TRSw",
        #     "Referer": url3,
        #     "Accept-Encoding": "gzip, deflate, br",
        #     "Accept-Language": "zh-CN,zh;q=0.9",
        #     # "Cookie": "PANWEB=1; BAIDUID=D85812618FC241EA800013BE1D970555:FG=1; Hm_lvt_7a3960b6f067eb0085b7f96ff5e660b0=1559660491; Hm_lpvt_7a3960b6f067eb0085b7f96ff5e660b0=1559660491; BDCLND=hSsksGDHeTYSAu2txg7Kf2tiyhJe9jPOm5MgJ0N%2FwiI%3D"
        #     "Cookie": cookie
        # }

        # resp = requests.get(url, proxies=proxy, headers=headers)
        resp = requests.get(url=dupanConfig[curStep]["url"], 
                            proxies=dupanConfig["proxy"], 
                            headers=dupanConfig[curStep]["headers"])
        resp.encoding = 'UTF-8'
    else:
        logging.info("No "+curStep)
    # soup = BeautifulSoup(resp.text, "html.parser")
    # print(soup.prettify())
    # PrintHttpDetails(resp)
    # --

    # s5--
    curStep="step5"
    if curStep in dupanConfig:
        logid2 = ctx.call("Getlogid", cookieDict["BAIDUID"])
        dupanConfig[curStep]["params"]["logid"]=logid2
        # params = {
        #     "uk":"1862740414",
        #     "shareid":"136149483",
        #     "order":"other",
        #     "desc":"1",
        #     "showempty":"0",
        #     "web":"1",
        #     "page":"1",
        #     "num":"100",
        #     "dir":"/幪面超人Build",
        #     "t":"0.5237814128347804",
        #     "channel":"chunlei",
        #     "app_id":"250528",
        #     "bdstoken":"null",
        #     "logid":logid2,
        #     "clienttype": "0"
        # }

        cookieDict["cflag"] = "13%3A3"
        ts10_2 = str(int(time.time()))
        cookieDict["Hm_lpvt_7a3960b6f067eb0085b7f96ff5e660b0"]=ts10_2
        cookie = spiderutils.GetCookieStrFromDict(cookieDict)
        dupanConfig[curStep]["headers"]["Referer"]=url
        dupanConfig[curStep]["headers"]["Cookie"]=cookie
        # headers = {
        #     "Host": "pan.baidu.com",
        #     "Connection": "keep-alive",
        #     "Accept": "application/json, text/javascript, */*; q=0.01",
        #     "X-Requested-With": "XMLHttpRequest",
        #     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36",
        #     # "Referer": "https://pan.baidu.com/s/1pUZRD5wJOM7iUA4_O-TRSw",
        #     "Referer": url,
        #     "Accept-Encoding": "gzip, deflate, br",
        #     "Accept-Language": "zh-CN,zh;q=0.9",
        #     # "Cookie": "PANWEB=1; BAIDUID=D85812618FC241EA800013BE1D970555:FG=1; Hm_lvt_7a3960b6f067eb0085b7f96ff5e660b0=1559660491; BDCLND=hSsksGDHeTYSAu2txg7Kf2tiyhJe9jPOm5MgJ0N%2FwiI%3D; Hm_lpvt_7a3960b6f067eb0085b7f96ff5e660b0=1560172897; cflag=13%3A3"
        #     "Cookie": cookie
        # }

        # url4 = "https://pan.baidu.com/share/list"
        resp = requests.get(url=dupanConfig[curStep]["url"],
                            proxies=dupanConfig["proxy"],
                            params=dupanConfig[curStep]["params"],
                            headers=dupanConfig[curStep]["headers"])
        resp.encoding = 'UTF-8'

        # soup = BeautifulSoup(resp.text, "html.parser")
        # print(soup.prettify())
        # spiderutils.PrintHttpDetails(resp)
        # print(resp.status_code)
        logging.info(resp.status_code)
    else:
        logging.info("No "+curStep)
    #--

    #-- save JSON
    jsonDict = json.loads(resp.text,encoding="UTF-8")
    # del jsonDict['request_id']
    # del jsonDict['server_time']
    # for i in jsonDict.get('list')[:]:
    #     print(i["server_filename"])
    jPath = cwd + "/json"
    if not os.path.exists(jPath):
        os.makedirs(jPath)
    jFileName = jPath + "/outKRlist.json"

    # check old list
    if os.path.isfile(jFileName):
        # file exists
        with open(jFileName, "r", encoding="UTF-8") as f:
            jloadDict = json.load(f)
        #compare different
        # nfl = jsonDict["list"]
        difflist = []
        for i in jsonDict["list"]:
            if i not in jloadDict["list"]:
                difflist.append(i)
        #--
        
        if difflist.__len__() == 0:
            # print("No change")
            logging.info("No change")
        else:
            # print("Been changed")
            # logging.info("Been changed")
            logging.info("Been changed:{0}".format(difflist.__str__()))
            # logging.info("")
            subject = ""
            for i in difflist:
                subject = subject + i["path"] + ","
            #send notification email
            # with open("./config/spider.cfg","r", encoding="UTF-8") as f:
            #     cfgText = json.load(f)
            #     username = cfgText["email"]["username"]
            #     passwd = cfgText["email"]["passwd"]
            #     receiver = cfgText["email"]["receiver"]

            # try:
            smtp = smtplib.SMTP_SSL("smtp.163.com", 465)
            smtp.login(username, passwd)
            sender = username

            msg = MIMEText(difflist.__str__(),'plain','utf-8')
            msg['From'] = 'z136604<'+ sender + '>'
            msg['To'] = 'pyto<'+ receiver + '>'
            subject = 'DuPanUpdate: ' + subject
            msg['Subject'] = Header(subject,'utf-8') 

            smtp.sendmail(sender, receiver, msg.as_string())
            smtp.quit()

            #update file
            with open(jFileName, "w", encoding="UTF-8") as f:
                json.dump(jsonDict, f)
    else:
        # file not exists
        with open(jFileName, "w", encoding="UTF-8") as f:
            json.dump(jsonDict, f)

    # --
    logging.info("===spider2 end===")
    logging.info(time.asctime())
    return

if __name__ == "__main__":
    
    if sys.argv.__len__() > 1:
        if sys.argv[1] == "1":
            TestSpider1()
        elif sys.argv[1] == "2":
            TestSpider2(sys.argv[2])
    else:
        print("need input paramers")    
else:
    pass