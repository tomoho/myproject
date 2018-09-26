#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
使用时直接导入模块即可运行命令
ex.
   import tianmatrack
   track('trackingid')   will return current status and history

or
    import tianmatrack
    x=new_instance
    x.online_tracking('trackingid') will return current status and history
'''


from .track_engine import *



instanceList    =   []

def new_instance():
    newInstance     =   Track()
    instanceList.append(newInstance)
    return newInstance

originInstance =    new_instance()

track           =   originInstance.track

'''
result = {
         'tracknumber':'',
         'current':[date,time,comments],
         'details':[[date,time,comments],.........],
         'current_city':[date,time,city],
         'carrier':[date,time,carrier],
         'op_date':[date,time,location],
         'cl_date':[date,time,location]}
'''

