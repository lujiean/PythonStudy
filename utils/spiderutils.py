def PrintHttpDetails(ret):
    print("------response status code-------")
    print(ret.status_code)
    print("-------response headers-----")
    print(ret.headers)
    print("-------response text-----")
    print(ret.text)

def GetCookieStrFromDict(dict):
    str=''
    # print(resp.cookies)
    for k,v in dict.items():
        str = str + k + "=" + v + ";"
        # str = print("{0}{1}={2};".format(str, k, v))
    return str[0:len(str)-1]

def GetCookieDict(resp):
    dict={}
    for i in resp.cookies:
        dict[i.name]=i.value
    return dict