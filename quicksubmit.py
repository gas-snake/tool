#!/usr/bin/python
#coding=utf-8 
import requests
import cchardet
from bs4 import BeautifulSoup as bs
# 设置URL
url = "http://2017.wuxianshua.com:81/web1/"
def GetHtml (url,Htype='get',data={})
    r = requests.session()
    print('session',r)
    print('cookies',r.cookies.get_dict())
    #提交链接，获取网页
    if Htype = 'get' :
        req = r.get(url)
    elif Htype = 'post':
        req = r.get(url)
    return req
'''
def 
    print('session',r)
    print('cookies',r.cookies.get_dict())
    print('cookies',r.cookies.get_dict())
    '''