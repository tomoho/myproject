#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
This file is helping to configure document structure and module top level config
it will use dict to define it 
'''
import os
import sys
CURRENT_DIR = os.getcwd()                         # define 当前工作目录     
FOLDER=[]                                         # 初始化文件列表
citys={}                                          #{city:[district1,district2...]...}
provincial_dict={}                                #{provience:[city1,city2]}

def getsubfolders():                              # 定义获取子目录的方法
  folders=[]
  listfiles=os.listdir()
  for i in listfiles:
    if '.' not in i:
      folders.append(i)
  return folders
      
FOLDER=getsubfolders()                              # get current dir folderlist FOLDER
Staticfiles={
'citylist':'China_citys.txt',
'msg_queue':'msg_queue.txt',
'carrier_list':'Carrier_List.txt'
}


  
