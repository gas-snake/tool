#!/usr/bin/python
#coding=utf-8 

import ofile
import os
#==============定义======================
#Fpath=os.path.dirname(__file__)  #当前路径  
Fpath=os.path.dirname(os.path.realpath(__file__))
Lpath=os.path.join(Fpath,'XlsFile')

print ('Lpath',Lpath)

#判断条件
Citys = ['济源','焦作']
print  (Citys)  
#判断列
CCol = 9
#表头行
RTitle = 1
XlsName = '合并.xls'
#=============读取文件=======================
#取指定文件夹里的所有文件
FileList = ofile.FileList(Lpath)     
print ('FileList',FileList)
#过滤出xls、xlsx文件组成新列表
XlsFileList=[] 
for fl in FileList:                       
    print (fl)
    if os.path.splitext(fl)[1] == '.xls' or os.path.splitext(fl)[1] == '.xlsx':
        XlsFileList.append(fl)
print (XlsFileList)
#从excel文件列表中巡环取出文件
#总表
XlsData = []
XlsN = 0
for XlsFile in XlsFileList:
    #当前文件读出的临时表
    Tfile = []
    #当前文件名
    Fname = os.path.basename(XlsFile)
    #判断是否是第一个文件，是的话取标题行，不是跳过
    if XlsN == 0 :
        Tfile = ofile.XlsReadTableAll(XlsFile,0,1)
        #给临时表加文件名列
        for i in range(RTitle,len(Tfile)):
            Tfile[i].append(Fname)
    else:
        Tfile =  ofile.XlsReadTableAll(XlsFile,0,1 + RTitle)
        #给临时表加文件名列
        for tl in Tfile:
            tl.append(Fname)
    #把临时表拼入主表
    XlsData = XlsData + Tfile
    XlsN = XlsN + 1
    
print  (XlsData)  
print(len(XlsData))

#给文件名加绝对路径
XlsName=os.path.join(Fpath, XlsName) 
#写入文件
ofile.XlsWrite(XlsData,XlsName)

'''
#=============取出需要的行=======================
#判断列的值
CData = ''
#定义新表
NXls = []
NXls.append(XlsData[0])
#遂行读取结果集
for Dr in XlsData:
    #取其中一行，判断是否合条件，是则加入新表
    CData = Dr[CCol-1]
    for City in Citys :
        # 判断该列是否能找到条件
        if CData.find(City) != -1:
            NXls.append(Dr)
print('=====================')
print  (NXls)  
print  (len(NXls))

#给文件名加绝对路径
XlsName=os.path.join(Fpath, XlsName) 
#写入文件
ofile.XlsWrite(XlsData,XlsName)
'''