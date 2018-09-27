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

class Tracking():
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
        # tracking id is string format 
        urlbase=self.url
        carrier=self.carrier
        data = None
        try:
            if reference.startswith('US'):                              # sifang starts with US
                carrier = 'sifang'
                data={'number':reference}
                url = urlbase.get(carrier)+reference
            else:
                carrier='tianma'
                url = urlbase.get(carrier)+str(reference)
        except Exception as e:                                          # if input int means tianma 
            url = urlbase.get(carrier)+str(reference)
        return {'carrier':carrier,
                'url':url,
                'data':data}
    def url_open(self,urlpars,*args,**kargs):
        '''input urlpars return humen readable HTML'''
        header  = self.header
        carrier = urlpars.get('carrier')
        url = urlpars.get('url')
        data=urlpars.get('data')
        try:
            if data != None:                                        # sifang need submit data to url
                urldata=parse.urlencode(data,encoding='utf8')       # create string data 
                formdata=urldata.encode('utf8')
                req=urllib.request.Request(url,data=formdata)
            else:
                req = request.Request(url)
            req.add_header(header[0],header[1])
            html = request.urlopen(req)
            HTML=html.read().decode('utf-8')
        except Exception as e:
            logging.error('网页打开错误',e)
            return None
        return {'HTML':HTML,
                'carrier':carrier
                }
    def HTML_keyinfo(self,HTMLdict,*args,**kargs):
        HTML = HTMLdict.get('HTML')
        carrier = HTMLdict.get('carrier')
        try:
            stepinfo = re.findall(r'<ul class="stepdetail  clearfix tc ml20">(.*?)</ul>',Html,re.M|re.S)[0]
        except Exception as e:
            logging.info('未大的节点',e)
            return None
        return stepinfo
    def get_trans_in_Html(self,Html,*args,**kargs):
        try:
            trans_info  =   re.findall(r'<ul class="trans_info  clearfix tl ml20 ">(.*?)</ul>',Html,re.M|re.S)[0]
        except Exception as e:
            logging.info('未查询到大的节点',e)
            return None
        return trans_info
    def get_step_detail(self,stepinfo,*args,**kargs):
        '''爬取网页信息，当前状态的日期和时间'''
        status  = 'open'
        try:
            statuslist  = re.findall(r'<div class="c33 fb f14">(.*?)</div>',stepinfo,re.M|re.S)
            datelist    = re.findall(r'<p class="c66 f12">(.*?)<br>',stepinfo,re.M|re.S)
            timelist    = re.findall(r'<br>(.*?)</p>',stepinfo,re.M|re.S)
            length      = len(datelist)
            if len(statuslist)==(length):
                status  = 'closed'
            else:
                statuslist  = statuslist[:length]
            details={'status':status,
                     'statuslist':statuslist,
                     'datelist':datelist,
                     'timelist':timelist}        
        except Exception as e:
            logging.info('未查询到大的节点详细信息',e)
            return None
        return details
    def get_trans_detail(self,trans_info,*args,**kargs):
        '''获取运输详细记录'''
        detailcommentlist=[]
        try:
            detailtimelist  =   re.findall(r'<p class="c33 f14  trans_time pr fl">(.*?)</p>',trans_info,re.M|re.S)
            comments        =   re.findall(r'<p class="c66 f14  ml20 trans_d pr fl(.*?)">(.*?)</p>',trans_info,re.M|re.S)
            # 最后状态中有设置字体颜色，匹配结果为二元数组
            for each in comments:
                detailcommentlist.append(each[1])
            detailtimelist.reverse()
            detailcommentlist.reverse()
            details = {'detailtimelist':detailtimelist,
                       'detailcommentlist':detailcommentlist}
        except Exception as e:
            logging.info('查询详细记录出错了')
            return None
        return details            

    def get_carrier(self,comments):
        carrierlist=self.carrierlist
        carrier=None
        pattern ='包裹已转(.*?)配送'
        try:
            for eachcomment in comments:
                try:
                    carrier=re.findall(pattern,eachcomment)[0]
                    break
                except IndexError:
                    pass
        except Exception :
            logging.debug('出错了')
        
        if carrier not in carrierlist:
            carrierlist.append(carrier)
        return carrier
    def prov_match(self,string,*args,**kwargs):
        provlist=list(self.city_dict.keys())
        try:
            for prov in provlist:
                try:
                    re.findall(prov,string)[0]
                    return prov
                    break
                except Exception :
                    pass
        except Exception as e:
            logging.error('省会未匹配成功，程序报错',e)
            pass
        
    def city_match(self,string,prov,*args,**kwargs):
        try:
            citylist    =   self.city_dict[prov]
        except Exception as e:
            logging.error('请确认省份输入正确',e)
        try:
            for city in citylist:
                try:
                    re.findall(city,string)[0]
                    return city
                    break
                except Exception:
                    pass
        except Exception:
            logging.debug('城市清单未定义')
    def hard_city_match(self,comments):
        city_dict   =   self.city_dict
        if comments!=None:
            commentscopy=comments[:]
            commentscopy.reverse()
            try:
                for string in commentscopy:
                    for prov in self.city_dict.keys():
                        for city in city_dict[prov]:
                        
                            try:
                                if '市' in city:
                                    pattern=city[:-1]
                                else:
                                    pattern=city[:-3]
                                re.findall(pattern,string)[0]
                                return {'prov':prov,
                                        'city':city} 
                                break
                            except Exception :
                                pass
            except Exception as e:
                logging.error('省会未匹配成功，程序报错',e)
                pass

    def get_citys(self,comments):
        from_city   =   None
        mid_city    =   None
        dest_prov   =   None
        dest_city   =   None
        try:
            for each in comments:
                try:
                    if from_city ==None:
                        try:
                            if '门店揽收'in each :
                                from_city=re.findall('\[(.*?)]门店揽收',each)[0]
                            else:
                                from_city=re.findall('\[(.*?)]仓库扣款',each)[0]
                                mid_city = from_city
                        except Exception:
                            pass
                             
                    elif mid_city == None:
                        try:
                            if '包裹入库'in each: 
                                mid_city=re.findall('\[(.*?)]包裹入库',each)[0]
                        except Exception:
                            pass
                                            
                    else:# 匹配终点城市
                        pass
                        '''
                        try:
                            prov = self.prov_match(each)
                            if prov != None:
                                dest_prov   =   prov
                                city = self.city_match(each,dest_prov)
                                if city !=None:
                                    dest_city   =   city
                        except Exception:
                            logging.error('省会城市未找到')
                            pass
                        '''
                except Exception:
                    logging.debug('城市匹配报错了')
        except Exception as e:
            logging.debug('寻找城市出错了')
            print(e)
        if dest_city==None:
            try:
                hard_city_result=self.hard_city_match(comments)
                dest_prov=hard_city_result['prov']
                dest_city=hard_city_result['city']
            except Exception:
                pass
        citys   = {'from_city':from_city,
                   'mid_city':mid_city,
                   'dest_prov':dest_prov,
                   'dest_city':dest_city}
        return citys
    def get_month(self,stepdetail):
        try:
            datelist=stepdetail['datelist']
            date    =datelist[1]# 获取运单真实开始时间，门店揽收
            return date[0:7]# 返回2018-01 年份加月份
        except Exception:
            pass
    def get_duration(self,transdetail):
        try:
            datelist=transdetail['detailtimelist']
            initial = datelist[1].split(' ')[0]
            final = datelist[-1].split(' ')[0]
            Di      = datetime.strptime(initial,'%Y-%m-%d')
            Df      = datetime.strptime(final,'%Y-%m-%d')
            return (Df-Di).days
        except Exception:
            pass
    def track_order(self,trackingid):
        '''运行查单，返回主要步骤信息，和运输详细记录，返回字典'''
        url         = self.get_url(trackingid)
        Html        = self.url_open(url)
        
        transinfo   = self.get_trans_in_Html(Html)
        stepinfo    = self.get_step_in_Html(Html)
        
        stepdetail  = self.get_step_detail(stepinfo)
        transdetail = self.get_trans_detail(transinfo)
        # 上面的赋值要么有结果，要么是None
        comments    = transdetail['detailcommentlist']
        citys       = self.get_citys(comments)
        carrier     = self.get_carrier(comments)
        month       = self.get_month(stepdetail)
        duration    = self.get_duration(transdetail)
        result = {'stepdetail':stepdetail,
                  'transdetail':transdetail,
                  'citys':citys,
                  'carrier':carrier,
                  'month':month,
                  'duration':duration}
        return result
            
if __name__=='__main__':
    cityfile=open('citys.txt',encoding='utf8')
    city_dict={}
    citylist=[]
    cityfile.readline()
    for i in range(300):
        try:
            city,provience=cityfile.readline().strip('\n').split('\t')
            if city !='':
                city_dict[provience].append(city)
                citylist.append(city)
            else:
                cityfile.close()
                break
        except KeyError:
            city_dict[provience]=[]
            city_dict[provience].append(city)
            
        except ValueError:
            pass

        
    x=Tracking()
    x.city_dict=city_dict
    x.citylist=citylist
    trackingid = 10000368529
    for i in range(3):
        result=x.track_order(trackingid)
        print(trackingid,result['carrier'],result['citys']['dest_city'])
        trackingid+=1
        
    

