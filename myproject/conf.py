#!/usr/bin/python
# -*- coding: utf-8 -*-

'''

'''
import os
import sys
CURRENT_DIR = os.getcwd()
FOLDER=[]
citys={}                                          #{city:[district1,district2...]...}
provincial_dict={}                                #{provience:[city1,city2]}

def getsubfolders():
  folders=[]
  listfiles=os.listdir()
  for i in listfiles:
    if '.' not in i:
      folders.append(i)
  return folders
      
FOLDER=getsubfolders()                              # get current dir folderlist FOLDER
localfiles={
'citylist':'China_citys.txt',
'msg_queue':'msg_queue.txt',
'carrier_list':'Carrier_List.txt'
}


  
