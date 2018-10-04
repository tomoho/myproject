#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
conf file location  Staticfile.get('contact')
'''
fileaddress=r'C:\Users\mdong1\Downloads\myproject-master\myproject-master\myproject\static\contact.csv'
splitstyle='\t'
class Contact():
  def __init__(self):
    self.name='None'
    self.ID='None'
    self.cell='None'
    self.wechat='None'
    self.address=['None','None']                   # primary address will be defined by index
  def __str__(self):
    return self.name+self.ID
  def get(self):
    return [self.ID,self.name,self.cell,self.wechat,self.address[0],self.address[1]]

keys=['身份证号','姓名','电话号码','微信号','地址']    
contacts=[]                           # 定义载入的通讯录
def create(fileaddress):
  try:
    with open(fileaddress,'r')as f:
      f.close()
    return True
  except Exception:
    with open(fileaddress,'w',encoding='utf8') as f:
      title=splitstyle.join(keys)+'\n'
      f.write(title)
    f.close()
    return False
def loadcontact(fileaddress):
  # input contact.text file address to load file
  fileexisting=create(fileaddress)
  if not fileexisting:
    createcontact(fileaddress)
  with open(fileaddress,'r',encoding='utf8') as f:
    keys=f.readline().strip('\n').split(splitstyle)
    for line in f:
      try:
        x=Contact()
        x.name,x.ID,x.cell,x.wechat,*x.address=line.strip('\n').split(splitstyle)
        contacts.append(x)
      except Exception as e:
        print(e)
  f.close()
def appendcontact(fileaddress,contact):
  fileexisting=create(fileaddress)
  with open(fileaddress,'a+',encoding='utf8') as f:
    try:
      line=splitstyle.join(contact.get())+'\n'
      f.write(line)
      f.flush()
    except Exception as e:
      print(e)
  f.close()
def in_contact():
  contact=Contact()
  contact.name=input('请输入姓名，姓氏+名字，如韩梅梅：-->')
  contact.ID = input('请输入ID 号码：-->')
  contact.cell = input('请输入手机号码：-->')
  contact.wechat = input('请输入微信号码或备注名：-->')
  address=input('请输入地址,多个地址用逗号(,)隔开：-->')
  try:
    if ',' in address or '，'in address:
      contact.address=address.split(',')
    else:
      contact.address[0]=(address)
  except Exception as e:
    print(e)
  contacts.append(contact)
  return contact
def create_contact():
  contact=in_contact()
  appendcontact(fileaddress,contact)
    
  
  
  
