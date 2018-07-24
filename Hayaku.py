#!/usr/bin/python
#coding=utf-8 
import requests
from bs4 import BeautifulSoup as bs
import xml.sax
#提交链接，获取网页r
r = requests.get('http://2017.wuxianshua.com:81/web1/')
r.encoding='gb2312'
# s=52347*(80161+38740)-(64690+16422)*80
# s = int(s)
# print(r.text)
# print (s)
# soup = ''
#把网页进行分析
soup = bs(r.text,'html.parser')
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
result=eval(divt)
# print(eval(divt))
# print (type(result))
r3=requests.session()
r2 = r3.post('http://2017.wuxianshua.com:81/web1/', data = {"res":result})
r2.encoding='gb2312'
print(r2.text)
# print (53742*(62747+47219))
# print ((23555+88140)*80)
# print (5909792772-8935600)