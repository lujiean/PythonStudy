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
import utils
utils.CommFunc1(4,6)

newNameCommFunc1 = utils.CommFunc1
newNameCommFunc1(7,0)

print("-main func-----")

if __name__ == "__main__":
    import sys
    newNameCommFunc1(int(sys.argv[1]), int(sys.argv[2]))

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
f=open('utils.py', 'r')
print(f.read())
f.close()
with open('utils.py', 'r') as f:
    str = f.read()
    print(str)

f=open('wf2.log','w')
f.write("this is a writed line.")
f.close()
with open('wf3.log', 'w') as f:
    f.write('hello nboy')

import json
# json.lo