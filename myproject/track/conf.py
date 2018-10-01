#!/usr/bin/python
# -*- coding: utf-8 -*-
import os,platform
'''
承运商数据定义在static文件中
'''
import logging
logging.basicConfig(filename='logger.log',level=logging.CRITICAL)
Version     ='0.0'
Date    = '20180829'
OS =platform.system
Timeout = (10,60)
User-Agent = 'Mozilla/5.0 (Windows NT 10.0; Trident/7.0; Touch; rv:11.0) like Gecko'
Url ={'天马':'http://www.worldcps.com/Order/Track?TrackNo=',
      '四方':'http://us.transrush.com/track/search.json'
     }
milestone={
          '天马':['订单创建','包裹出库','航班起飞','正在清关','国内配送'],
          '四方':['PU','LO','FT']
}

'''
TrackStatusCode -----> FT      =========> Flight Transport 
TrackStatusCode -----> LO      =========> Leave Overseas 
TrackStatusCode -----> OC      =========> Overseas warehouse Change  
TrackStatusCode -----> AO      =========> Arrive Oveseas warehouse
TrackStatusCode -----> PU      =========> Pick Up 
'''
Universial_milestone =['订单创建','包裹出库','航班起飞','正在清关','国内配送']




