#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
此模块用于生成信息，并保存已经发送的信息
'''
import os
CURRENT_ADDRESS = os.getcwd()                       # get current address
INQUEUE_MSG_FILE = "inqueue message.txt"            # define waitting queue file name


from exceptions import *                            # import customed exceptions

def Format(**argv)
  msg = '''
    
  '''


class Message():
    def __init__(self):
        self.inqueue_msg    =[]                     # define msg list, inside list it is dict 
        self.static_address ='\\'.join([CURRENT_ADDRESS,INQUEUE_MSG_FILE])
                                                    # define static_file address to store in quere message
    def flush_msg(self,msglist):
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
            

