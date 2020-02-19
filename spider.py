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
import re

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

def TestSpider2(configFile):

    #read config file
    if len(configFile) == 0:
        print("input root path as arg 2")
        return
    else:
        cfgFile=configFile
    # cfgFile = "./config/spider.cfg"
    # cfgFile = cwd + "/config/usr/spider.json"
    if not os.path.isfile(cfgFile):
        with open(cfgFile, "w", encoding="UTF-8") as f:
            f.write("")
        print("not found config file. setup as /config/usr/README do")
        return
    else:
        with open(cfgFile,"r", encoding="UTF-8") as f:
            cfgText = json.load(f)
        title = cfgText["title"]
        url = cfgText["url"]
        pick_up_code = cfgText["pickup"]
        username = cfgText["email"]["username"]
        passwd = cfgText["email"]["passwd"]
        receiver = cfgText["email"]["receiver"]
        jsPath = cfgText["jsPath"]
        logFile = cfgText["logFile"]
        configFile = cfgText["configFile"]
        outFile = cfgText["outFile"]

    #log file
    if not os.path.isdir(os.path.dirname(logFile)):
        os.makedirs(os.path.dirname(logFile))
    fh = logging.FileHandler(filename=logFile, encoding="UTF-8")
    logging.basicConfig(level=logging.INFO, handlers=[fh])

    #pan.baidu.com config
    with open(configFile, "r", encoding='UTF-8') as f:
        dupanConfig = json.load(f)
    #--
    logging.info("===" + title +" start===")
    logging.info(time.asctime())
    logging.info("logFile: " + logFile)
    logging.info("outFile: " + outFile)

    # proxy={'http':'http://127.0.0.1:8888', 'https':'https://127.0.0.1:8888'}

    # --s1 first request
    curStep = "step1"
    if curStep in dupanConfig:
        dupanConfig[curStep]["url"] = url
        resp = requests.get(url=dupanConfig[curStep]["url"], 
                            proxies=dupanConfig["proxy"], 
                            headers=dupanConfig[curStep]["headers"], 
                            allow_redirects=dupanConfig[curStep]["allow_redirects"])
        resp.encoding = 'UTF-8'

        # set redirect url
        if resp.status_code == 302 and 'Location' in resp.headers:
            url3=resp.headers['Location']
        cookieDict = spiderutils.GetCookieDict(resp)
        cookie = spiderutils.GetCookieStrFromDict(cookieDict)
        logging.info(resp.status_code)
    else:
        logging.info("No "+curStep)
    # --

    # --s2
    curStep="step2"
    if curStep in dupanConfig:

        dupanConfig[curStep]["url"]=url3
        dupanConfig[curStep]["headers"]["Cookie"]=cookie
        
        resp = requests.get(url=dupanConfig[curStep]["url"], 
                            proxies=dupanConfig["proxy"], 
                            headers=dupanConfig[curStep]["headers"], 
                            allow_redirects=dupanConfig[curStep]["allow_redirects"])
        resp.encoding = 'UTF-8'

        logging.info(resp.status_code)
    else:
        logging.info("No "+curStep)
    # --

    # --s3: post pick_up_code request
    curStep="step3"
    if curStep in dupanConfig:
        
        surl = parse.parse_qs(parse.urlparse(url3).query)['surl'][0]
        ts13 = str(int(time.time()*1000))
        ts10 = str(int(time.time()))

        with open(jsPath + "/boot.js", "r", encoding="UTF-8") as f:
            content = f.read()
        ctx = execjs.compile(content)
        logid = ctx.call("Getlogid", cookieDict["BAIDUID"])

        #params
        dupanConfig[curStep]["params"]["surl"]=surl
        dupanConfig[curStep]["params"]["t"]=ts13
        dupanConfig[curStep]["params"]["logid"]=logid

        #headers
        cookieDict["Hm_lvt_7a3960b6f067eb0085b7f96ff5e660b0"]=ts10
        cookieDict["Hm_lpvt_7a3960b6f067eb0085b7f96ff5e660b0"]=ts10
        cookie = spiderutils.GetCookieStrFromDict(cookieDict)
        dupanConfig[curStep]["headers"]["Referer"]=url3
        dupanConfig[curStep]["headers"]["Cookie"]=cookie

        #data
        dupanConfig[curStep]["data"]["pwd"]=pick_up_code

        resp = requests.post(url=dupanConfig[curStep]["url"], 
                             proxies=dupanConfig["proxy"], 
                             params=dupanConfig[curStep]["params"], 
                             headers=dupanConfig[curStep]["headers"],
                             data=dupanConfig[curStep]["data"])
        resp.encoding = 'UTF-8'
        
        randsk=json.loads(resp.text, encoding='UTF-8').get('randsk')
        logging.info(resp.status_code)
    else:
        logging.info("No "+curStep)
    # --

    # s4--
    cookieDict["BDCLND"] = randsk
    cookie = spiderutils.GetCookieStrFromDict(cookieDict)

    curStep="step4"
    if curStep in dupanConfig:
        # cookieDict["BDCLND"] = randsk
        # cookie = spiderutils.GetCookieStrFromDict(cookieDict)
        dupanConfig[curStep]["url"]=url
        dupanConfig[curStep]["headers"]["Referer"]=url3
        dupanConfig[curStep]["headers"]["Cookie"]=cookie
        
        resp = requests.get(url=dupanConfig[curStep]["url"], 
                            proxies=dupanConfig["proxy"], 
                            headers=dupanConfig[curStep]["headers"])
        resp.encoding = 'UTF-8'
        logging.info(resp.status_code)

        #--
        soup = BeautifulSoup(resp.text, "html.parser")
        links = soup.find_all(name="script", attrs={"type": "text/javascript"})
        jsAssignDict={}
        for l in links:
            li=re.findall(r'yunData.SHARE_UK = .*;',l.get_text())
            if len(li) > 0:
                li = li[0].replace("=","").replace("\\","").split('"')
                jsAssignDict[li[0].strip()]=li[1].strip()
            li=re.findall(r'yunData.SHARE_ID = .*;',l.get_text())
            if len(li) > 0:
                li = li[0].replace("=","").replace("\\","").split('"')
                jsAssignDict[li[0].strip()]=li[1].strip()
            li=re.findall(r'yunData.PATH = .*;',l.get_text())
            if len(li) > 0:
                # li = li[0].replace("=","").replace("\\","").split('"')
                li = li[0].replace("=","").replace("\\","").replace("x27","'").split('"')
                jsAssignDict[li[0].strip()]=li[1].strip()

        # print(jsAssignDict)
    else:
        logging.info("No "+curStep)
    # --

    # s5--list all files.
    curStep="step5"
    if curStep in dupanConfig:
        #--params
        logid2 = ctx.call("Getlogid", cookieDict["BAIDUID"])
        dupanConfig[curStep]["params"]["logid"]=logid2

        dupanConfig[curStep]["params"]["uk"]=jsAssignDict["yunData.SHARE_UK"]
        dupanConfig[curStep]["params"]["shareid"]=jsAssignDict["yunData.SHARE_ID"]
        dupanConfig[curStep]["params"]["dir"]=jsAssignDict["yunData.PATH"]

        #--headers
        cookieDict["cflag"] = "13%3A3"
        ts10_2 = str(int(time.time()))
        cookieDict["Hm_lpvt_7a3960b6f067eb0085b7f96ff5e660b0"]=ts10_2
        cookie = spiderutils.GetCookieStrFromDict(cookieDict)
        dupanConfig[curStep]["headers"]["Referer"]=url
        dupanConfig[curStep]["headers"]["Cookie"]=cookie

        resp = requests.get(url=dupanConfig[curStep]["url"],
                            proxies=dupanConfig["proxy"],
                            params=dupanConfig[curStep]["params"],
                            headers=dupanConfig[curStep]["headers"])
        resp.encoding = 'UTF-8'
        logging.info(resp.status_code)
    else:
        logging.info("No "+curStep)
    #--

    #-- save JSON
    jsonDict = json.loads(resp.text,encoding="UTF-8")

    if not os.path.exists(os.path.dirname(outFile)):
        os.makedirs(os.path.dirname(outFile))

    # check old list
    if os.path.isfile(outFile):
        # file exists
        with open(outFile, "r", encoding="UTF-8") as f:
            jloadDict = json.load(f)
        #compare different
        difflist = []
        # for i in jsonDict["list"]:
        for i in range(jsonDict["list"].__len__()):
            i_new_server_filename=jsonDict["list"][i]["server_filename"]
            # if i not in jloadDict["list"]:
            for j in range(jloadDict["list"].__len__()):
                if i_new_server_filename == jloadDict["list"][j]["server_filename"]:
                    break
            else:
                difflist.append(i_new_server_filename)
        #--
        
        if difflist.__len__() == 0:
            # print("No change")
            logging.info("No change")
        else:
            # print("Been changed")
            logging.info("Been changed:{0}".format(difflist.__str__()))
            subject = ""
            for i in difflist:
                # subject = subject + i["path"] + ","
                if len(subject) == 0:
                    subject = i
                else:
                    subject = subject + "," + i
            #send notification email
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
            with open(outFile, "w", encoding="UTF-8") as f:
                json.dump(jsonDict, f)
    else:
        # file not exists
        with open(outFile, "w", encoding="UTF-8") as f:
            json.dump(jsonDict, f)

    # --
    logging.info("===" + title + " end===")
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