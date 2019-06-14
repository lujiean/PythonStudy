a,b=1,2
print(a+b)

if a < 1:
    print(a,"<1")
else:
    print(a,">1")

print("------")
for n in range(1, 4):
    if n == 2 :
        print("this is 2")
        break
    else:
        print("this is not 2 ->", n)
else:
    print("this is for else")

print("------")
for n in range(1, 4):
    if n == 2 :
        print("this is 2")
        # continue
    print("this is not 2 ->", n)
else:
    print("this is for else")

print("------")
def sum(a,b,c):
    print("in sum")
    return a+b+c

sn=sum(1,2,3)
print(sn)
# function must upper than call
# sn=sum2(1,2,3)

# def sum2(a,b,c):
#     print("in sum2")
#     return a+b+c
print("-annotations-----")
# def func2(c[iput var name]: str[type], d: str = 'gg'[default value]) -> str[return type]:
def func2(c: str, d: str = 'gg') -> str:
    # str=print("value a = ", a, "value b = ", b)
    str="value a = " + c + " value b = " + d  #can not use + to concat String + Int
    print(str)
    return str

# print("func2 1 input param: ", func2(3))
# print("func2 2 input param: ", func2(8, "kk"))
print("func2 1 input param: ", func2("3"))
print("func2 2 input param: ", func2("8", "kk"))
print(func2.__annotations__)
print(type("bb"))

print("-list-----")
list_a = [56, 34 ,6]
list_a.append(89)
list_a.append(6)
for i in list_a:
    print(i)

print("-set-----")
set_a = {"a", "b", "a"}
print(set_a)

print("-moduls-----")
import testutils
testutils.CommFunc1(4,6)

newNameCommFunc1 = testutils.CommFunc1
newNameCommFunc1(7,0)

print("-main func-----")

if __name__ == "__main__":
    import sys
    # newNameCommFunc1(int(sys.argv[1]), int(sys.argv[2]))

print("-pkg test-----")
# import pkg1.innerpkg1.pkg1utils
# pkg1.innerpkg1.pkg1utils.pkg1CommFunc1(77)

# import pkg1.innerpkg1.  #cannot run this
# from pkg1.innerpkg1 import *

# pkg1.innerpkg1.pkg1utils.pkg1CommFunc1(88)
# pkg1.innerpkg1.pkg1utils2.pkg2Commfunc2("hah")

print("-dict test-----")
dict1 = { 
    "name1":"hello",
    "name2":"what?",
    "nameList1": [{
            "listName1": "not",
            "listName2": "bb"
        },
        {
            "list2Name1": "struck",
            "list2Name2": "brown"
        }]
    }
print(dict1["nameList1"][0])

dict2common = {
    "name1":"kk"
}
print(dict2common)

dict3 = [{
    "name2": "conbine"
},
{
    "name3": "haha"
}]
print(dict3)
print(dict3[0]["name2"])

dict4 = {
    "name2": "conbine"
}

# dict4 add dict2common data
for k, v in dict2common.items():
    dict4[k]=v
    # print("k = " + k + ", v = " + v)

print(dict4)

print("-Formatted String Literals-----")
str="ljj"
print(f'{str} is a good boy')
# print(f'{str:-9s} is a good girl')
f'{str:9s} is a good girl'

for k, v in dict4.items():
    print(f'{k:10s} ==> {v:20s}|')
    # print('{:10} ==> {v:20}'.format(k,v))

# Reading and Writing Files
print("-Reading and Writing Files-----")
f=open('testutils.py', 'r')
print(f.read())
f.close()
with open('testutils.py', 'r') as f:
    str = f.read()
    print(str)

f=open('wf2.log','w')
f.write("this is a writed line.")
f.close()
with open('wf3.log', 'w') as f:
    f.write('hello nboy')

import json
# json.lo

print("-test execjs-----")
import execjs

with open("./js/test.js", "r", encoding="UTF-8") as f:
    content = f.read()
ctx = execjs.compile(content)
print(ctx.call("testJSFunc1", "a", "b"))
# print(content)

# with open("./js/boot.js", "r", encoding="UTF-8") as f:
#     content = f.read()
# ctx = execjs.compile(content)
# print(ctx.call("Getlogid", "Getlogid"))

print("-test beauti-----")
# s="'\n{"errno":0,"err_msg":"","request_id":249609282089505580,"randsk":"hSsksGDHeTYSAu2txg7Kf2tiyhJe9jPOm5MgJ0N%2FwiI%3D"}'
# "

print("--test json---")
text = '{"errno":0,"request_id":292024594349675781,"server_time":1560244778,"list":[{"category":6,"fs_id":619574849322546,"isdir":0,"local_ctime":1560192083,"local_mtime":1560192134,"md5":"5a49496b33de79a64e6fc229210ffca7","path":"\/\u5e6a\u9762\u8d85\u4ebaBuild\/KR Build 22.rar","server_ctime":1560192276,"server_filename":"KR Build 22.rar","server_mtime":1560192276,"size":454999665},{"category":6,"fs_id":239218870938,"isdir":0,"local_ctime":1560192010,"local_mtime":1560192062,"md5":"7da53be1c00ab850fb182357fb619d93","path":"\/\u5e6a\u9762\u8d85\u4ebaBuild\/KR Build 21.rar","server_ctime":1560192502,"server_filename":"KR Build 21.rar","server_mtime":1560192502,"size":460985481},{"category":6,"fs_id":683425561114142,"isdir":0,"local_ctime":1560191946,"local_mtime":1560192000,"md5":"012d2c63bcf0b28e7047e7246257808b","path":"\/\u5e6a\u9762\u8d85\u4ebaBuild\/KR Build 20.rar","server_ctime":1560192390,"server_filename":"KR Build 20.rar","server_mtime":1560192390,"size":455928623},{"category":6,"fs_id":388224428069460,"isdir":0,"local_ctime":1558336313,"local_mtime":1558336368,"md5":"2ea6a321bb147a46f9b45b852bca7064","path":"\/\u5e6a\u9762\u8d85\u4ebaBuild\/KR Build 19.rar","server_ctime":1558336544,"server_filename":"KR Build 19.rar","server_mtime":1558336544,"size":455843920},{"category":6,"fs_id":695560020740384,"isdir":0,"local_ctime":1558336249,"local_mtime":1558336295,"md5":"2900a67b3ab5b4db4c4104a2045e3753","path":"\/\u5e6a\u9762\u8d85\u4ebaBuild\/KR Build 18.rar","server_ctime":1558336431,"server_filename":"KR Build 18.rar","server_mtime":1558336431,"size":462236107},{"category":6,"fs_id":284003628981352,"isdir":0,"local_ctime":1556217947,"local_mtime":1556218012,"md5":"4fcd6d52d194b49163b1e1279fce064a","path":"\/\u5e6a\u9762\u8d85\u4ebaBuild\/KR Build 17.rar","server_ctime":1556218292,"server_filename":"KR Build 17.rar","server_mtime":1556218292,"size":455003824},{"category":6,"fs_id":102056035236058,"isdir":0,"local_ctime":1555695976,"local_mtime":1555696029,"md5":"ed0dfe0c915fa8136214ec703083a02a","path":"\/\u5e6a\u9762\u8d85\u4ebaBuild\/KR Build 16.rar","server_ctime":1555696911,"server_filename":"KR Build 16.rar","server_mtime":1555696911,"size":458265524},{"category":6,"fs_id":528858968613856,"isdir":0,"local_ctime":1554930201,"local_mtime":1554930246,"md5":"4a80c747fd3bb200965c2ed5902cef20","path":"\/\u5e6a\u9762\u8d85\u4ebaBuild\/KR Build 15.rar","server_ctime":1554930631,"server_filename":"KR Build 15.rar","server_mtime":1555696099,"size":450226629},{"category":6,"fs_id":637933013145740,"isdir":0,"local_ctime":1554228385,"local_mtime":1554228430,"md5":"302b986f0db7a896482b6d100454ea76","path":"\/\u5e6a\u9762\u8d85\u4ebaBuild\/KR Build 14.rar","server_ctime":1554228783,"server_filename":"KR Build 14.rar","server_mtime":1554228783,"size":462274552},{"category":6,"fs_id":527314914003346,"isdir":0,"local_ctime":1553583167,"local_mtime":1553583212,"md5":"48378ecb40974f376bfe434834fec0b5","path":"\/\u5e6a\u9762\u8d85\u4ebaBuild\/KR Build 13.rar","server_ctime":1553584755,"server_filename":"KR Build 13.rar","server_mtime":1553584755,"size":450762760},{"category":6,"fs_id":335224282127645,"isdir":0,"local_ctime":1553148237,"local_mtime":1553148285,"md5":"f949efda3d66f28938c35d29185dec68","path":"\/\u5e6a\u9762\u8d85\u4ebaBuild\/KR Build 12.rar","server_ctime":1553148497,"server_filename":"KR Build 12.rar","server_mtime":1553148497,"size":453173497},{"category":6,"fs_id":932570894457543,"isdir":0,"local_ctime":1552369698,"local_mtime":1552369742,"md5":"4f8c6b50267074cadda5dc81b15ca2a9","path":"\/\u5e6a\u9762\u8d85\u4ebaBuild\/KR Build 11.rar","server_ctime":1552369857,"server_filename":"KR Build 11.rar","server_mtime":1552369857,"size":452176886},{"category":6,"fs_id":284630719561164,"isdir":0,"local_ctime":1552369608,"local_mtime":1552369654,"md5":"ec95f821dcd4760382f0f28ff704f08d","path":"\/\u5e6a\u9762\u8d85\u4ebaBuild\/KR Build 10.rar","server_ctime":1552369967,"server_filename":"KR Build 10.rar","server_mtime":1552369967,"size":449501153},{"category":6,"fs_id":403971492624543,"isdir":0,"local_ctime":1551803203,"local_mtime":1551803256,"md5":"05640c6f7fe16fb9e984909d77db17be","path":"\/\u5e6a\u9762\u8d85\u4ebaBuild\/KR Build 09.rar","server_ctime":1551803482,"server_filename":"KR Build 09.rar","server_mtime":1551803482,"size":468332179},{"category":6,"fs_id":630162947854527,"isdir":0,"local_ctime":1551803119,"local_mtime":1551803172,"md5":"c87c01c0fd51314451c0e1fef9c37677","path":"\/\u5e6a\u9762\u8d85\u4ebaBuild\/KR Build 08.rar","server_ctime":1551803715,"server_filename":"KR Build 08.rar","server_mtime":1551803715,"size":457782443},{"category":6,"fs_id":554072298841361,"isdir":0,"local_ctime":1551803054,"local_mtime":1551803115,"md5":"2bc67219290389c6fbc0400b8e4fc631","path":"\/\u5e6a\u9762\u8d85\u4ebaBuild\/KR Build 07.rar","server_ctime":1551803601,"server_filename":"KR Build 07.rar","server_mtime":1551803601,"size":488326222},{"category":6,"fs_id":740731871900287,"isdir":0,"local_ctime":1550073323,"local_mtime":1550073375,"md5":"52f3845f7aac745ae362beeb79a8504b","path":"\/\u5e6a\u9762\u8d85\u4ebaBuild\/KR Build 06.rar","server_ctime":1550073652,"server_filename":"KR Build 06.rar","server_mtime":1550073652,"size":456855034},{"category":6,"fs_id":598809886719466,"isdir":0,"local_ctime":1548959437,"local_mtime":1548959485,"md5":"929a28cbac931534443b1debbe614c24","path":"\/\u5e6a\u9762\u8d85\u4ebaBuild\/KR Build 05.rar","server_ctime":1548959657,"server_filename":"KR Build 05.rar","server_mtime":1548959657,"size":456134932},{"category":6,"fs_id":64080622093001,"isdir":0,"local_ctime":1548959357,"local_mtime":1548959403,"md5":"e71894cd2cb013f002d0421a5571d9c7","path":"\/\u5e6a\u9762\u8d85\u4ebaBuild\/KR Build 04.rar","server_ctime":1548959547,"server_filename":"KR Build 04.rar","server_mtime":1548959547,"size":447161317},{"category":6,"fs_id":670229686242822,"isdir":0,"local_ctime":1547573936,"local_mtime":1547573982,"md5":"38d13bc3e038b6d00f15143a5aae4828","path":"\/\u5e6a\u9762\u8d85\u4ebaBuild\/KR Build 03.rar","server_ctime":1547574125,"server_filename":"KR Build 03.rar","server_mtime":1547574125,"size":458796008},{"category":6,"fs_id":198353047368289,"isdir":0,"local_ctime":1546827162,"local_mtime":1546827223,"md5":"981a5263199d530ebbb453099fede530","path":"\/\u5e6a\u9762\u8d85\u4ebaBuild\/KR Build 02.rar","server_ctime":1546827558,"server_filename":"KR Build 02.rar","server_mtime":1546827558,"size":445292600},{"category":6,"fs_id":113786982950592,"isdir":0,"local_ctime":1546827235,"local_mtime":1546827289,"md5":"7364b8c043859566e1e538b5c5238664","path":"\/\u5e6a\u9762\u8d85\u4ebaBuild\/KR Build 01.rar","server_ctime":1546827450,"server_filename":"KR Build 01.rar","server_mtime":1546827450,"size":458469786}]}'
jsontext = json.loads(text,encoding="UTF-8")
list1 = jsontext.get('list')

for i in list1[:]:
    print(i["server_filename"])

print("-test folder-----")
import os
if not os.path.exists("./folder1"):
    os.makedirs("./folder1")
with open("./folder1/1.log",'w') as f:
    f.write("hello, in folder files")

# with open("./outKRlist.json","r") as f:
#     jsontext = json.load(f)
# jsontext = jsontext["list"]
# for i in jsontext.items():
#     print([""])

with open("./config/spider.cfg", "r", encoding="UTF-8") as f:
    text = json.load(f)
print(text)

print("--test send email-----")
import smtplib
from email.mime.text import MIMEText
from email.header import Header

with open("./config/spider.cfg","r", encoding="UTF-8") as f:
    cfgText = json.load(f)
    username = cfgText["email"]["username"]
    passwd = cfgText["email"]["passwd"]
    receiver = cfgText["email"]["receiver"]

# try:
smtp = smtplib.SMTP_SSL("smtp.163.com", 465)
# smtp.connect('smtp.163.com,25')
# smtp.connect(host="smtp.163.com",port=25)
smtp.login(username, passwd)
sender = username

msg = MIMEText('Karman rider update','plain','utf-8')
msg['From'] = 'KrBuildUpdate<'+ sender + '>'
msg['To'] = 'pyto<'+ receiver + '>'
subject = 'Karmen Rider update'
msg['Subject'] = Header(subject,'utf-8') 

smtp.sendmail(sender, receiver, msg.as_string())
smtp.quit()
# except Exception:
#     pass
