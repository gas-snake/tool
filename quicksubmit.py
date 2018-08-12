#!/usr/bin/python
#coding=utf-8 
import requests
import cchardet
from bs4 import BeautifulSoup as bs
# 设置URL
# url = "https://jianguan.dianhua.cn"
url = "http://2017.wuxianshua.com:81/web1/"
r = requests.session()
def GetHtml (url,Htype='get',data={}):
    #设置提交方式，使用session()包含cookies
    # r = requests.session()
    print('session',r)
    print('cookies',r.cookies.get_dict())
    #提交链接，获取网页
    if Htype == 'get' :
        req = r.get(url)
    elif Htype == 'post':
        req = r.post(url,data)
    # 判断编码
    codetype=cchardet.detect(req.content)
    # 设置编码
    req.encoding=codetype["encoding"]
    return req.text



#HTML查找函数，HTXT为输入的HTML文件，hname为需要找的TAG名称，att为其它属性条件，如{"class": "token","name":'token','type':"hidden"}
def HtmlSearch(HTXT='',hname='',att={}):
    # print('HTXT',HTXT)
    #把网页进行分析
    soup = bs(HTXT,'html.parser')
    # print(soup.title)
    # print(soup.head)
    #找到对应的标签
    
    rows = soup.find_all(name=hname,attrs=att)
    print (rows)
    return rows
#标签解读函数，att="text"时输出TEXT，att="id"等属性时输出对应的value值
def HtmlRead(Htxt,att='text'):
    if att =='text':
        return Htxt.text
    else:
        return Htxt[att]
'''
#测试数据
htxt= GetHtml(url,'get',)
print ('dddddddddddddd')
print (htxt)
soup = bs(htxt,'html.parser')
print ('dddddddddddddd')
print (soup.div)
print ('dddddddddddddd')
print (soup.head)
print ('soup',soup)
# inputs = soup.find_all(name='input',type = "hidden")
at=['login_txtbx password','password']#传入attr的参数可以是LSIT，也可以是字典
at2={"class": "token","name":'token','type':"hidden"}
at3={"id":"math"}
inputs = soup.find_all('div',at3)
# inputs = soup.find_all('input',at2)
soup.find()
print ('inputs',inputs)

for ins in inputs:
    print (type(ins))
#     pass
# print (type(inputs))
# print (Htmlread(htxt,'div','math'))
'''
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