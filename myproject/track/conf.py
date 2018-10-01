#!/usr/bin/python
# -*- coding: utf-8 -*-
import os,platform
'''
承运商数据定义在static文件中
'''
import logging
logging.basicConfig(filename='logger.log',level=logging.CRITICAL)
VERSION     ='0.0'
DATE    = '20180829'
OS =platform.system
TIMEOUT = (10,60)
USER_AGENT = ''

Universial_milestone =['订单创建','包裹出库','航班起飞','正在清关','国内配送']
milestone={
          '天马':['订单创建','包裹入库']
}

