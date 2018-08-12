#!/usr/bin/python
#coding=utf-8 
# 一对兔子，从第三个月起每月下一对兔子，新兔子也从第二个月起每月下一对兔子
def rabbit (n=0):
    if n ==1 or n ==2  :
        return 1
    else  :
        return rabbit(n-1) + rabbit(n-2)

for d in range(1,10):
    print (rabbit(d))

str1 = '0123456789'
print (str1[0:3]) #截取第一位到第三位的字符
print (str1[:]) #截取字符串的全部字符
print (str1[6:]) #截取第七个字符到结尾
print (str1[:-3]) #截取从头开始到倒数第三个字符之前
print (str1[2]) #截取第三个字符
print (str1[-1]) #截取倒数第一个字符
print (str1[::-1]) #创造一个与原字符串顺序相反的字符串
print (str1[-3:-1]) #截取倒数第三位与倒数第一位之前的字符
print (str1[-3:]) #截取倒数第三位到结尾
print (str1[:-5:-3]) #逆序截取，具体啥意思没搞明白？
print (11//3)
print (11%3)
print ((2)and(-2))

#打印九九乘法表

s9=[]

for i in range(1,10):
    print ('i=',i)
    st=[]
    for j in range(1,i+1):
#        print ('j=',j)
        s1=str(j)+"X"+str(i)+'='+str(i*j)
        print (s1,end=' ')
        st.append(s1)
    s9.append(st)
print(s9)

for ss9 in s9:
    print (ss9)

#N*N的矩阵，不使用缓存矩阵，把矩阵顺时针转90度

image1=[]
image2=[]

for i in range(0,10):
    imaget1=[]
    imaget2=[]
    for j in range(0,10):
        imaget1.append(j+i*10)
        imaget2.append('')
    image1.append(imaget1)
    image2.append(imaget2)
print (image1)
print (image2)

for i in range(0,10):
    for j in range(0,10):
        image2[j][10-1-i]=image1[i][j]

for im in image2:
    print (im)

for j in range(0,10):
    print ('',end='\n')
    for i in range(0,10):
        print (image1[10-1-i][j],end=' ')