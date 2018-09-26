#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
承运商数据定义在static文件中
'''
import logging
logging.basicConfig(filename='logger.log',level=logging.CRITICAL)
Version     ='0.0'
Date    ='20180829'

Universial_milestone =['订单创建','包裹出库','航班起飞','正在清关','国内配送']
milestone={
          '天马':['订单创建','包裹入库']
}
