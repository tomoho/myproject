#!/usr/bin/python
# -*- coding: utf-8 -*-

'''

'''
import os
import sys
CURRENT_DIR = os.getcwd()
FOLDER=[]

def getfolders():
  folders=[]
  listfiles=os.listdir()
  for i in listfiles:
    if '.' not in i:
      folders.append(i)
  return folders
      
FOLDER=getfolders()                              # get current dir folderlist FOLDER


  
