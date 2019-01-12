#!/usr/bin/python
#coding=utf-8 
import quicksubmit as qs
#登录入口
url = "https://jianguan.dianhua.cn"
url2="https://jianguan.dianhua.cn/login?redirect_url=%2F%2Fjianguan.dianhua.cn%2F"
#登录信息jianguan.dianhua.cn/data/report/harass/issue?phone_province_id=0&report_phone_province_id=16&report_phone_city_id=325&operator=0&reported_operator=1&startDate=2018-06-26&endDate=2018-07-26&report_phone_type=0&bad_type=-2&harass_type=0&phone_type=&phone_value=&retrieve_k=&retrieve_v=&page_size=
user_login={'username':'henanyidong','password':'qwe12345','token':''}
#登录页面TOKEN值查找条件
attrToken={'type':"hidden",'class':"token",'name':"token"}
#获取首页
H1 = qs.GetHtml(url2,"get",)
#判断TITLE是否是首页<title>登录 -- 12321电话举报平台</title>
# HAS=qs.HtmlSearch(H1,'div',{'id':'math'})
Htitle=qs.HtmlSearch(H1,'title',)
Ttitle=qs.HtmlRead(Htitle[0],'text')
print ('title=>',Ttitle)
if Ttitle=='登录 -- 12321电话举报平台' :
    Htoken=qs.HtmlSearch(H1,'input',attrToken)
    Vtoken=qs.HtmlRead(Htoken[0],'value')
    user_login['token']=Vtoken
    print ('user_login=>',user_login)
    H2 = qs.GetHtml(url2,"post",user_login)
    print ("H2=>",H2)

    
# if expression:
#     pass

# print (qs.HtmlRead(HAS[0],'id'))

# print (HAS2[0].text)