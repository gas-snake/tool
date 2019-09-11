#!/usr/bin/python
#coding=utf-8 
import time
import re
import IPy
# import numpy as np

IP = ""
print(IPy.IP('10.0.0.0/22') - IPy.IP('10.0.2.0/24'))
print(IPy.IP('192.168.1.0/28') - IPy.IP('192.168.1.4/30'))
IPS=IPy.IP('172.31.254.160/27') - IPy.IP('172.31.254.160/30')
print(IPS)
IPS=IPS - IPy.IP('172.31.254.164/30')
print(IPS)
IPS.add(IPy.IP('192.168.1.4/30'))
print(IPS)
IPS.add(IPy.IP('10.10.10.4/30'))
print(IPS)
print(IPy.IP('111.6.98.214/21',make_net=True))
IPS.add(IPy.IP('192.168.1.8/30'))
print(IPS)

print(IPy.IP('2409:8A44:9E40::/48'))
#得到IP类型
RealIP=IPy.IP('2409:8A44:9E40::/48',make_net=True)
#得到子网
Subnet = RealIP.strNormal(1)
print(Subnet)

#得到广播地址
Broadcast = RealIP.broadcast()
print(Broadcast)

IPND = ["2409:8A44:9E00::/48",
"2409:8A44:9E20::/48",
"2409:8A44:9E40::/48",
"2409:8A44:9E60::/48",
"2409:8A44:9E80::/48"]
IPNDM = "2409:8A44:9E00::/40"
# print(IPND)
# IPSv6 = IPy.IP(IPNDM)
# print(IPSv6)
# for ip in IPND:
#     IPSv6= IPSv6 - IPy.IP(ip)

# print(IPSv6)

print(IPy.IP('2409:8A44:9E00::/40') - IPy.IP('2409:8A44:9E80::/48'))
print(IPy.IP('2409:8A44:9E00::/40'))