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
def GetIpInfo (IP='',GateTpye='F'): #GateTpye网关类型，F为第一个，L为最后一个
    #定义输出的结果集
    IpInfo = {
        'Subnet':'',
        'Broadcast':'',
        'First':'',
        'Last':'',
        'Num':'',
        'Gate':'',
        'Mask':'',
        'Wildmask':'',
    }
    Subnet = '' 
    Broadcast = ''
    First = ''
    Last = ''
    Num = 0
    Gate = ''
    Mask = ''
    Wildmask = ''
    #得到IP类型
    RealIP=IPy.IP(IP,make_net=True)
    #得到子网
    Subnet = RealIP.strNormal(1)
    #得到广播地址
    Broadcast = RealIP.broadcast()
    #得到子网IP的整形数
    SubnetN =  RealIP.int()
    #得到广播地址的整形数
    BroadcastN = Broadcast.int()
    #得到首地址的整形数
    FirstN = SubnetN +1 
    #得到尾地址的整形数
    LastN = BroadcastN -1
    #得到首地址
    First = IPy.IP(FirstN)
    #得到尾地址
    Last = IPy.IP(LastN)
    #得到子网IP数
    Num = len(RealIP)
    #得到掩码
    Mask = RealIP.netmask()
    #得到掩码的整形数
    MaskN = Mask.int()
    #得到反掩码的整形数
    WildmaskN = IPy.IP('255.255.255.255',make_net=True).int() - MaskN
    #得到反掩码
    Wildmask = IPy.IP(WildmaskN)
    IpInfo['Subnet'] = Subnet
    IpInfo['Broadcast'] = Broadcast
    IpInfo['First'] = First
    IpInfo['Last'] = Last
    IpInfo['Num'] = Num
    # dict['Gate'] =
    IpInfo['Mask'] = Mask
    IpInfo['Wildmask'] = Wildmask

    return IpInfo 
def DisplayIpInfo():
    IpInfo = GetIpInfo(IP,'F')
    print ('==========================')
    print ('子    网:',IpInfo['Subnet'])
    print ('掩    码:',IpInfo['Mask'])
    print ('反 掩 码:',IpInfo['Wildmask'])
    print ('首 地 址:',IpInfo['First'])
    print ('尾 地 址:',IpInfo['Last'])
    print ('广播地址:',IpInfo['Broadcast'])
    print ('网段IP数:',IpInfo['Num'])
    print ('==========================')
    return

# IPS = input("请输入：")
while 1 == 1 :
    IPS = input("请输入：")
    print(IPS)
    if IPS == 'n':
        print('break')
        break
    IPM = IPS.split()
    print ('IPM')
    if len(IPM) >1 :
        IP = IPM[0]+'/'+IPM[1]
    else:
        IP = IPM[0]
    DisplayIpInfo()


# print (IP)
""" 
ipt = IPy.IP(IP,make_net=1)
iptn =  ipt.int()
Iptnf = IPy.IP(IP,make_net=1).int()-iptn
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
print(ipt.netmask()) #输出其网络掩码 """


