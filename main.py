# // https://www.google.co.jp/maps/dir/
# // https://www.google.co.jp/maps/dir/

# // 34.9985249,135.9609779/%E3%80%92525-0050+%E6%BB%8B%E8%B3%80%E7%9C%8C%E8%8D%89%E6%B4%A5%E5%B8%82%E5%8D%97%E8%8D%89%E6%B4%A5%EF%BC%91%E4%B8%81%E7%9B%AE+%E5%8D%97%E8%8D%89%E6%B4%A5%E9%A7%85/34.991564,135.9654411/
# // 34.9985249,135.9609779/%E3%80%92525-0050+%E6%BB%8B%E8%B3%80%E7%9C%8C%E8%8D%89%E6%B4%A5%E5%B8%82%E5%8D%97%E8%8D%89%E6%B4%A5%EF%BC%91%E4%B8%81%E7%9B%AE+%E5%8D%97%E8%8D%89%E6%B4%A5%E9%A7%85/34.991564,135.9654411/

# // %E3%82%BB%E3%83%96%E3%83%B3%E2%80%90%E3%82%A4%E3%83%AC%E3%83%96%E3%83%B3+%E8%8D%89%E6%B4%A5%E3%83%91%E3%83%8A%E3%82%BD%E3%83%8B%E3%83%83%E3%82%AF%E5%89%8D%E5%BA%97/

# // @34.9879427,135.9515365,15z
# // @34.9879427,135.9515365,15z

# // /data=!4m10!4m9!1m0!1m5!1m1!1s0x6001727b52eb86b9:0xf401e6a15a29cd9d!2m2!1d135.9472318!2d35.0037471!1m0!3e2?hl=ja
# // /data=!4m16!4m15!1m0!1m5!1m1!1s0x6001727b52eb86b9:0xf401e6a15a29cd9d!2m2!1d135.9472318!2d35.0037471!1m0!1m5!1m1!1s0x60016d8f9ff5d227:0x6dcc975cceeebeb0!2m2!1d135.9527086!2d34.9906572!3e2?hl=ja


# // https://www.google.com/maps/dir/?api=1&origin=横浜駅&destination=東京駅&waypoints=川崎駅|品川駅&travelmode=driving

# // result[0].geometry.location.lat lng

import requests

with open('./config.txt') as f:
    API_KEY = f.read()

url = 'https://maps.googleapis.com/maps/api/place/textsearch/json'
requestString = '{}?language=ja&key={}&input={}&inputtype={}'.format(url, API_KEY, 'Ritsumeikan', 'textquery')

print(requestString)

# APIリクエストを送信
data = requests.get(requestString).json()
print(data)

# https://maps.googleapis.com/maps/api/place/findplacefromtext/json?input=Museum%20of%20Contemporary%20Art%20Australia&inputtype=textquery&fields=photos,formatted_address,name,rating,opening_hours,geometry&key=YOUR_API_KEY
