import re
import urllib.request
import json

number=input('please input number:')        # 'US18091743239'
url='http://us.transrush.com/track/search.json'
data={'number':number}

urldata=urllib.parse.urlencode(data,encoding='utf8')  # create string data 
formdata=urldata.encode('utf8')
header=('User-Agent','Mozilla/5.0 (Windows NT 10.0; Trident/7.0; Touch; rv:11.0) like Gecko')
req=urllib.request.Request(url,data=formdata)
req.add_header(header[0],header[1])
html=urllib.request.urlopen(req)
HTML=html.read().decode('utf8')

result=json.loads(HTML)

details=result.get('data')             # details is a list with len==1
details=details[0]                    # details is dict 
EndDeliverySupplierName=details.get('EndDeliverySupplierName')
TrackingNumber=details.get('TrackingNumber')
ReceiverID=details.get('ReceiverID')
ReferenceNumber=details.get('ReferenceNumber')

'''['ItemID', 'ReferenceNumber', 'TrackingNumber', 'EndDeliverySupplierCode',
'ChannelCode', 'ReceiverID', 'SourceCode', 'TraceSourceNumber', 
'EndDeliverySupplierName', 'is_use_idCode', 'tracks']
'''
history=details.get('tracks')         # history is a list with length based on result 
                                      # each item is dict with key 
'''['TrackID', 'ItemID', 'TrackStatusCode', 'TrackDate', 'TrackLocation', 
'TrackContent', 'CreateDate', 'UserIDCreate', 'SyncFPX']

TrackID 29773742
ItemID 1478963
TrackStatusCode FT
TrackDate 2018-09-22 02:24:51
TrackLocation 芝加哥
TrackContent 起飞
CreateDate 2018-09-22 02:28:41
UserIDCreate 1588
SyncFPX 1
'''
                   
return {
        'receiver':ReceiverID,
        'ReferenceNumber':ReferenceNumber,
        'EndDeliverySupplierName':EndDeliverySupplierName,
        'TrackingNumber':TrackingNumber,
        'history':history        
}
                   
                   


