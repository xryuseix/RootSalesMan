# // https://www.google.com/maps/dir/?api=1&origin=横浜駅&destination=東京駅&waypoints=川崎駅|品川駅&travelmode=driving

import requests
import csv
from time import sleep

# APIリクエストを送信
def getPosition(pos):
    with open('./config.txt') as f:
        API_KEY = f.read()
    url = 'https://maps.googleapis.com/maps/api/place/findplacefromtext/json'
    requestString = '{}?language=ja&key={}&input={}&inputtype={}&fields=geometry'.format(url, API_KEY, pos, 'textquery')
    data = requests.get(requestString).json()
    print(data)
    ido = data['candidates'][0]['geometry']['location']['lat'] if data['status']=='OK' else -1
    keido = data['candidates'][0]['geometry']['location']['lng'] if data['status']=='OK' else -1
    return ido, keido

def readCSV():
    arr = []
    with open('./destination.csv', 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            arr.append(row)
    return arr
     
def writeCSV(arr):
    with open('./destination.csv', 'w') as f:
        writer = csv.writer(f, lineterminator='\n')
        writer.writerows(arr)

