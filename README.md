# PythonStudy
Python Study

current learning chapter:
https://docs.python.org/3/tutorial/inputoutput.html

Note:
1. upgread pythone pip

You are using pip version 9.0.3, however version 19.1.1 is available.
You should consider upgrading via the 'python -m pip install --upgrade pip' command.

2. install request package
PS C:\Users\sqpz\Documents\PythonStudy> pip --trusted-host pypi.org --trusted-host files.pythonhosted.org install requests

3. install pylint
PS C:\Users\sqpz\Documents\PythonStudy> pip --trusted-host pypi.org --trusted-host files.pythonhosted.org install pylint

4. when catch SSLerror, the reason is fiddler is opening using proxy[for item 3,4]

5. 在爬虫中使用proxy 可以同时使用Fiddler4 和爬虫
http://baijiahao.baidu.com/s?id=1599906763166379926&wfr=spider&for=pc

6. test case
链接: https://pan.baidu.com/s/1MtzzoarNAZbQGv92zlZyCg 提取码: rxks 复制这段内容后打开百度网盘手机App，操作更方便哦

7. flow
发送request
—> 
收到response，分析获取数据
-> 
再发送request
-> 
再收到response，分析获取数据
...
直到获取了自己需要的信息

8. avoid requests auto redirect.
ret = requests.get(url=url, headers=headers, allow_redirects=False)

Reference Dic
1. https://2.python-requests.org/en/master/user/quickstart/#make-a-request
