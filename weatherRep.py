# -*- coding: utf-8 -*-

from twilio.rest import Client
import urllib.request

import json
import gzip

cityname = "上海"
# 访问的url，其中urllib.parse.quote是将城市名转换为url的组件
url = 'http://wthrcdn.etouch.cn/weather_mini?city=' + urllib.parse.quote(cityname)
# 发出请求并读取到weather_data
weather_data = urllib.request.urlopen(url).read()
# 以utf-8的编码方式解压数据
weather_data = gzip.decompress(weather_data).decode('utf-8')
# 将json数据转化为dict数据
weather_dict = json.loads(weather_data)
forecast = weather_dict.get('data').get('forecast')
startoday = '早上好！天气播报!\n' \
            + '今天是' + forecast[0].get('date') + '!\n' \
            +weather_dict.get('data').get('city') \
            + '今天' + forecast[0].get('high') + '\n' \
            + forecast[0].get('low') + '\n' \
            + '天气是：' + forecast[0].get('type') + '\n' \
            + '提示：' + weather_dict.get('data').get('ganmao') + '\n'

print(startoday)
#send message
account_sid = '###'
auth_token = '###'
client = Client(account_sid, auth_token)

message = client.messages.create(
    from_='###',
    body= startoday,
    to='###'
)


