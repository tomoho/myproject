#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
conf file location  Staticfile.get('contact')
'''
Class Contact(self):
  def __init__(self):
    self.name=''
    self.ID=''
    self.cell=''
    self.wechat=''
    self.address=[]                   # primary address will be defined by index   

    
contacts=[]                           # 定义载入的通讯录
fileaddress='contact.txt'  
def loadcontact(fileaddress):
  # input contact.text file address to load file 
  with open(fileaddress,'r',encoding='utf8') as f:
    for line in f:
      x=Contact()
      x.name,x.ID,x.cell,x.wechat,*x.address=contactinfo.strip('\n').split('\t')
      contacts.append(x)
  f.close()
def appendcontact(fileaddress,contact):
  with open(fileaddress,'a+',encoding='utf8') as f:
    line='{}\t{}\t{}\t{}\t{}\t{}\t{}'.format(contact.name,contact.ID,contact.cell,contact.wechat,contact.address)
    f.write()
    f.flush()
  f.close()
  
  
  
