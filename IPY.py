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