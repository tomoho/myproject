#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
此模块用于接受网页查询结果，生成微信信息
'''
import os
CURRENT_ADDRESS = os.getcwd()                       # get current address
INQUEUE_MSG_FILE = "inqueue message.txt"            # define waitting queue file name
from exceptions import *                            # import customed exceptions

'''输入信息格式如下
{'receiver':ReceiverID,
 'ReferenceNumber':ReferenceNumber,
 'EndDeliverySupplierName':EndDeliverySupplierName,
 'TrackingNumber':TrackingNumber,
 'history':history
 }'''
class Message():
  def __init__(self):
    pass
  def Msg_NormalFormat(argv):
    # argv 为列表（快递单号，当前状态，历史记录，内容物）
    msg = '''
  --------------
  快递单号:{}
  **************
  当前状态:{}
  **************
  {}
  **************
  内容物:
  {}
  -------------
  '''.format(*argv)
    return msg
def FinalFormat(argv):
  # argv 是列表(快递单号，内容物，时间，目的地)
  msg = '''
--------------------
您的包裹快递单号:{}
内容物：
{}
********************
{}已经达到{}，正在派件
请您注意查收
  '''.format(*argv)
  return msg
def CHFormat(argv):
  # argv 内容物列表  [[数量，货品名称],....]
  # argv 历史记录列表[[日期，状态],........]
  for eachitem in argv:
    msg+="{}:{}\n".format(eachitem) 
  return msg
    

class Message():
    def __init__(self):
        self.inqueue_order    =[]                     # define msg list, inside list it is dict 
        self.static_address ='\\'.join([CURRENT_ADDRESS,INQUEUE_MSG_FILE])
                                                    # define static_file address to store in quere message
    def flush_msg(self):
        msglist=self.inqueue_order
        try:
            for eachmsg in msglist:
                msg='\t'.join([eachmsg['sender'],eachmsg['receiver']
                               eachmsg['subject'],eachmsg['content']])+'\n'
                                                # define msg format 
                f.write(eachmsg)                # add line into local file 
                f.flush()                       # flush to file avoid lose data
        except KeyError:
            print('message module key error for msg')
        except TypeError:
            print('message module msg Type Error, make sure str in msg')       
    def store_msg(self,msglist,**argus):           # define function to save msglist into file
        try:
            with open(self.static_address,'+a',encoding='utf8') as f:
                self.flush_msg(msglist,f)
        except FileNotFoundError:
            with open(self.static_address,'w',encoding='utf8') as f :
                self.flush_msg(msglist,f)
        f.close()




        

    def return_message(self,trackingnumber={}):
        try:
            print('信息内容已经生成')
            return self.__format_message__(trackingnumber)    # 返回信息内容
        except KeyError:
            print('未检测到合法输入，请确认输入参数是否正确')
            return '目前尚未查询到更新，请耐心等待'
            

