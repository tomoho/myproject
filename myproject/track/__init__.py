
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


from .tianmatrack import *



instanceList    =   []

def new_instance():
    newInstance     =   Tracking()
    instanceList.append(newInstance)
    return newInstance

originInstance =    new_instance()

track           =   originInstance.track_order

'''
        result = {'stepdetail':stepdetail,
                  'transdetail':transdetail,
                  'citys':citys,
                  'carrier':carrier,
                  'month':month,
                  'duration':duration}
        return result
'''

