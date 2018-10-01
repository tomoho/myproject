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
    self.address=[]                         #
  @property  self.name,self.ID,self.address,self.cell
  
 
contacts=[]
  
def loadcontact(fileaddress):
  # input contact.text file address to load file 
  with open('fileaddress','r',encod='utf8') as f:
    for line in f:
      contactinfo=f.readline()
      name,ID,cell,wechat,*address=contactinfo.strip('\n').split('\t')
      contacts.append(Contact(name,ID,cell,wechat,*address))
      
  
  
