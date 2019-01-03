#!/usr/bin/python
#coding=utf-8 
import time
import re
import IPy

IP = ""
print(IPy.IP('10.0.0.0/22') - IPy.IP('10.0.2.0/24'))
print(IPy.IP('192.168.1.0/28') - IPy.IP('192.168.1.4/30'))
IPS=IPy.IP('192.168.1.0/27') - IPy.IP('192.168.1.4/30')
print(IPS)
IPS=IPS - IPy.IP('192.168.1.8/30')
print(IPS)
IPS.add(IPy.IP('192.168.1.4/30'))
print(IPS)
IPS.add(IPy.IP('10.10.10.4/30'))
print(IPS)
print(IPy.IP('111.6.98.214/21',make_net=True))
IPS.add(IPy.IP('192.168.1.8/30'))
print(IPS)
'''
子网号
掩码
反掩码
广播地址
第一个地址
最后一个地址
可用个数
网关
可用个数
'''
IP = input("请输入：")
ipt = IPy.IP(IP,make_net=1)
iptn =  ipt.int()
Iptnf = IPy.IP("255.255.255.255",make_net=1).int()-iptn
print("子网号",ipt.strNormal(1))
print("广播地址",ipt.broadcast())
print("第一个地址",IPy.IP(iptn+1))
print('最后一个地址',IPy.IP(Iptnf))

print(ipt.reverseNames()) #返回IP的反向地址解析模式 
print(ipt.iptype()) #返回IP地址的类型 
print(ipt.int()) #将IP地址转换为整数格式 
print(ipt.strHex()) #将IP地址转换为16进制格式 
print(ipt.strBin()) #将IP地址转换为二进制格式 
print(ipt.net()) #输出其网络地址 
print(ipt.netmask()) #输出其网络掩码
