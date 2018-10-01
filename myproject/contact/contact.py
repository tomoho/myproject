#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
conf file location  Staticfile.get('contact')
'''
class Contact():
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
      print(line)
      x.name,x.ID,x.cell,x.wechat,*x.address=line.strip('\n').split('\t')
      contacts.append(x)
  f.close()
def appendcontact(fileaddress,contact):
  with open(fileaddress,'a+',encoding='utf8') as f:
    line='{}\t{}\t{}\t{}\t{}\t{}\t{}'.format(contact.name,contact.ID,contact.cell,contact.wechat,contact.address)
    f.write()
    f.flush()
  f.close()
def in_contact():
  contact=Contact()
  contact.name=input('请输入姓名，姓氏+名字，如韩梅梅：-->')
  contact.ID = input('请输入ID 号码：-->')
  contact.cell = input('请输入手机号码：-->')
  contact.wechat = input('请输入微信号码或备注名：-->')
  addressnumber = int(input('请输如地址的数量：-->'))
  for i in range(addressnumber):
    address=input('请输入第%s个地址：-->'%(addressnumber))
    contact.address.append(address)
  return contact
def create_contact():
  contact=in_contact()
  appendcontact(fileaddress,contact)
    
  
  
  
