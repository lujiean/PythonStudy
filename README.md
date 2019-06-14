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

9. Python获取URL中参数的方法
https://blog.csdn.net/weixin_34179762/article/details/86943489

10. File "C:\Users\jiean.a.lu\AppData\Local\Programs\Python\Python37\lib\subprocess.py", line 939, in communicate
    stdout, stderr = self._communicate(input, endtime, timeout)
  File "C:\Users\jiean.a.lu\AppData\Local\Programs\Python\Python37\lib\subprocess.py", line 1261, in _communicate
    self._stdin_write(input)
  File "C:\Users\jiean.a.lu\AppData\Local\Programs\Python\Python37\lib\subprocess.py", line 873, in _stdin_write
    self.stdin.write(input)
  File "C:\Users\jiean.a.lu\AppData\Local\Programs\Python\Python37\lib\encodings\cp1252.py", line 19, in encode
    return codecs.charmap_encode(input,self.errors,encoding_table)[0]
UnicodeEncodeError: 'charmap' codec can't encode character '\uff01' in position 1324: character maps to <undefined>

https://blog.csdn.net/sergiojune/article/details/88423694
原因是有一个程序在使用TextIOWrapper 类创建对象时默认使用了cp936的编码，也就是gbk编码，读取不了utf-8的字符，
所以我们可以修改下 subprocess.py 文件的默认编码方式为utf-8即可

在代码行656有个初始化，直接修改默认即可，如下

11. python读写json文件
https://www.cnblogs.com/bigberg/p/6430095.html

12. python--自动创建文件和创建目录的方法
https://blog.csdn.net/liuyingying0418/article/details/84633603
https://www.cnblogs.com/jhao/p/7243043.html

13. python自动发邮件总结及实例说明
https://www.cnblogs.com/yufeihlf/p/5726619.html
https://blog.csdn.net/weixin_41789943/article/details/82348946

Reference Dic
1. https://2.python-requests.org/en/master/user/quickstart/#make-a-request
