#!/usr/bin/python
#coding=utf-8
import binascii
#a = 'asdf'
#a_bytes = bytes.fromhex(a)
#print('字符串转字节码',a_bytes)
##print (binascii.crc32('asdf'))
#print (bytes.fromhex(b'asdf'))
#print (binascii.crc32(bytes.fromhex('asdf')) & 0xffffffff)
crc1=0x7C2DF918
crc2=0x798A06C6
crc3=0x5246B5A8
s = ''
n = 0
#for i in range(33,127):
for i in range(47,127):
    if n == 0:
        #print (2)
        for j in range(47,127):
            if n == 0:
                #print (2)
                for k in range(47,127):
                    if n == 0:
                        #print (2)
                        for a in range(47,127):
                            if n == 0:
                                #print (2)
                                for b in range(47,127):
                                    if n == 0:
                                        #print (2)
                                        for c in range(47,127):
                                            s = chr(i)+chr(j)+chr(k)+chr(a)+chr(b)+chr(c)
                                            print (s)
                                            if crc1 == binascii.crc32(s.encode()):
                                                b = 1
                                                break
print(s)

#s = chr(49)+chr(55)+chr(70)+chr(79)+chr(110)+chr(115)
#print (s)
#print (binascii.crc32(s.encode()))
#print (type(binascii.crc32(s.encode())))
#print(crc1)
#print(type(crc1))