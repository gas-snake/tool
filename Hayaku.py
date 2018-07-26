#!/usr/bin/python
#coding=utf-8 
import requests
from bs4 import BeautifulSoup as bs
import cchardet


url = "http://2017.wuxianshua.com:81/web1/"
#设置提交方式，使用session()包含cookies
r = requests.session()
print('session',r)
print('cookies',r.cookies.get_dict())
#提交链接，获取网页
req = r.get(url)
print('session',r)
print('cookies',r.cookies.get_dict())
print('content',req.content)
codetype=cchardet.detect(req.content)
print('codetype',codetype)
# 设置编码
req.encoding=codetype["encoding"]


#把网页进行分析
soup = bs(req.text,'html.parser')
print(soup.title)
# print(type(soup))
#找到对应的标签
div = soup.find(name='div',id='math')
#获取对应的值
divt=div.text
print(divt)
print(type(divt))
# print(type(divt.encode("utf-8")))
# s=divt
#eval可以将算术表达式进行计算
result=eval(divt)
# print(eval(divt))
# print (type(result))

#使用sessiong再次提交网页，使用POST方式，代入计算结果
req = r.post(url, data = {"res":result})
# 对结果编码
req.encoding=codetype["encoding"]
# 显示结果
print(req.text)

