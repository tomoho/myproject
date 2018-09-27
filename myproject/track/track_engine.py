#!/usr/bin/python
# -*- coding: utf-8 -*-
import urllib.request as request
import urllib.parse as parse
import re
import json
import logging
from datetime import datetime
Version     ='0.0'
Date    ='20180829'
logging.basicConfig(filename='logger.text',level=logging.CRITICAL)

class Tracker():
    '''
    the function of this class is to get query in same format 
    {
    }
    '''
    def __init__(self):
        self.header  = ('User-Agent','Mozilla/5.0 (Windows NT 10.0; Trident/7.0; Touch; rv:11.0) like Gecko')
        self.url     = {'tianma':'http://www.worldcps.com/Order/Track?TrackNo=',
                        'sifang':'http://us.transrush.com/track/search.json'}
    def get_url(self,reference,*args,**kargs):
        '''reference  if all number = tianma  if startwith US = sifang, will return dict''' 
        urlbase=self.url
        data = None
        try:
            if reference.startswith('US'):                              # sifang starts with US
                carrier = 'sifang'
                data={'number':reference}
                url = urlbase.get(carrier)
            else:
                carrier='tianma'
                url = urlbase.get(carrier)+str(reference)
        except Exception as e:                                          # if input int means tianma 
            url = urlbase.get(carrier)+str(reference)
        return {'carrier':carrier,
                'url':url,
                'data':data}
    def get_HTML(self,urlpars,*args,**kargs):
        '''input urldict return humen readable HTML which is dict'''
        header  = self.header
        carrier = urlpars.get('carrier')
        url = urlpars.get('url')
        data=urlpars.get('data')
        try:
            if data != None:                                        # sifang need submit data to url
                urldata=parse.urlencode(data,encoding='utf8')       # create string data 
                formdata=urldata.encode('utf8')
                req=request.Request(url,data=formdata)
            else:
                req = request.Request(url)
            req.add_header(header[0],header[1])
            html = request.urlopen(req)
            HTML=html.read().decode('utf-8')
        except Exception as e:
            logging.error('网页打开错误',e)
            return None
        return {'HTML':HTML,
                'carrier':carrier}
    def get_keyinfo(self,HTMLdict,*args,**kargs):
        '''input HTMLdict  return track result'''
        HTML = HTMLdict.get('HTML')
        carrier = HTMLdict.get('carrier')
        try: 
            if carrier == 'sifang':
                result=json.loads(HTML)
                details=result.get('data')[0]                        # result is a list with len==1,details is dict
                EndDeliverySupplierName=details.get('EndDeliverySupplierName')
                TrackingNumber=details.get('TrackingNumber')
                ReceiverID=details.get('ReceiverID')
                ReferenceNumber=details.get('ReferenceNumber')
                history=details.get('tracks')                       # history is a list with length based on result 
            elif carrier == 'tianma':
                pass                                                #======redefine it later======
        except Exception as e:
            logging.info('未大的节点',e)
            return None
        return {'receiver':ReceiverID,
                'ReferenceNumber':ReferenceNumber,
                'EndDeliverySupplierName':EndDeliverySupplierName,
                'TrackingNumber':TrackingNumber,
                'history':history}
    '''history example,just one element in the list 
    {'TrackID': '30629116', 'ItemID': '1478963', 'TrackStatusCode': 'CP', 
    'TrackDate': '2018-09-27 11:52:07', 'TrackLocation': '中国港口', 
    'TrackContent': '清关中', 'CreateDate': '2018-09-27 10:55:49',
    'UserIDCreate': '0', 'SyncFPX': '1'}'''
