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

history=result.get['data']
