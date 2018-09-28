#!/usr/bin/python
# -*- coding: utf-8 -*-
import urllib.request as request
import urllib.parse as parse
import json
from datetime import datetime

url= http://www.ems.com.cn/serviceguide/you_bian_cha_xun.html
  
country=http://www.ems.com.cn/ems/tool/rpq/countries  
{"model":{"selectedCountry":[{"countryName":"TNT公司","countryCode":"WW"},....
                            ]
         },
 "cleard":false
}
provience = http://www.ems.com.cn/ems/tool/rpq/provinces
{"model":{"selectedProv":[{"provName":"河北","provCode":"13"},...
                         ]
         },
 "cleared":false
}
city=http://www.ems.com.cn/ems/tool/rpq/cities?province=11

{"model":{"selectedCity":[{"cityName":"安丘市","cityCode":"370784"},....
                         ]
         },
 "cleared":false
}  
  
'''
return data type :

'''
