#!/usr/bin/python
#coding=utf-8 
import requests
import cchardet
from bs4 import BeautifulSoup as bs
# 设置URL
url = "https://jianguan.dianhua.cn"
def GetHtml (url,Htype='get',data={}):
    #设置提交方式，使用session()包含cookies
    r = requests.session()
    print('session',r)
    print('cookies',r.cookies.get_dict())
    #提交链接，获取网页
    if Htype == 'get' :
        req = r.get(url)
    elif Htype == 'post':
        req = r.get(url,data)
    # 判断编码
    codetype=cchardet.detect(req.content)
    # 设置编码
    req.encoding=codetype["encoding"]
    return req.text




def Htmlread(HTXT='',hname='',hid=''):
    print('HTXT',HTXT)
    #把网页进行分析
    soup = bs(HTXT,'html.parser')
    print(soup.title)
    #找到对应的标签
    
    div = soup.find(name=hname,id=hid)
    print (div)
    divt=''
    if div != None:
        divt=div.text
    return divt


#测试数据
htxt= GetHtml(url,'get',)
print ('dddddddddddddd')
print (htxt)
soup = bs(htxt,'html.parser')
print (soup.title)
print ('soup',soup)
# inputs = soup.findall(name='input')
# print (inputs)
# print (type(inputs))
# print (Htmlread(htxt,'div','math'))
'''
    print('session',r)
    print('cookies',r.cookies.get_dict())
    print('cookies',r.cookies.get_dict())
    
soup = BeautifulSoup('<option value="28">电子零组件业</option>', 'lxml')
data = soup.findall('option')[0]  # findall返回列表，因为只有一个，所以索引0
text = data.text
value = data['value']  # 注意这个是字符串不是数字
print "text:%s value:%s" % （text, value）  

http://dhcl.12321.cn/fraud/needtodo?reportPhoneOperator=0&reportPhoneProvince=0&reportPhoneCity=0&reportedPhoneOperator=1&reportedPhoneProvince=16&reportedPhoneCity=325&startTime=2018-06-29&endTime=2018-07-29&reportedPhoneType=0&phoneType=report_phone&phone=&retrieve=id&words=&limit=20
http://dhcl.12321.cn/fraud/needtodo/s/%2Ffraud%2Fneedtodo/reportPhoneOperator/0/reportPhoneProvince/0/reportPhoneCity/0/reportedPhoneOperator/1/reportedPhoneProvince/16/reportedPhoneCity/0/startTime/2018-06-29/endTime/2018-07-29/reportedPhoneType/0/phoneType/report_phone/phone//retrieve/id/words//limit/20/page/2?reportPhoneOperator=0&reportPhoneProvince=0&reportPhoneCity=0&reportedPhoneOperator=1&reportedPhoneProvince=16&reportedPhoneCity=0&startTime=2018-06-29&endTime=2018-07-29&reportedPhoneType=0&phoneType=report_phone&phone=&retrieve=id&words=&limit=500
http://dhcl.12321.cn/fraud/needtodo?reportPhoneOperator=0&reportPhoneProvince=0&reportPhoneCity=0&reportedPhoneOperator=1&reportedPhoneProvince=16&reportedPhoneCity=149&startTime=2018-06-29&endTime=2018-07-29&reportedPhoneType=0&phoneType=report_phone&phone=&retrieve=id&words=&limit=500
#被举报，移动 河南 济源
reportPhoneOperator:0
reportPhoneProvince:0
reportPhoneCity:0
reportedPhoneOperator:1
reportedPhoneProvince:16
reportedPhoneCity:325
startTime:2018-06-29
endTime:2018-07-29
reportedPhoneType:0
phoneType:report_phone
phone:
retrieve:id
words:
limit:20
#被举报，移动 河南 不限
reportPhoneOperator:0
reportPhoneProvince:0
reportPhoneCity:0
reportedPhoneOperator   :1
reportedPhoneProvince:16
reportedPhoneCity:0
startTime:2018-06-29
endTime:2018-07-29
reportedPhoneType:0
phoneType:report_phone
phone:
retrieve:id
words:
limit:20

  '''