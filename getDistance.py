import requests
import csv

# APIリクエストを送信
def getDistance(places):
    with open('./config.txt') as f:
        API_KEY = f.read()
    url = 'https://maps.googleapis.com/maps/api/distancematrix/json'
    placeString = '|'.join(places)
    requestString = '{}?language=ja&key={}&origins={}&destinations={}&mode=walking&units=metric'.format(url, API_KEY, placeString, placeString)
    data = requests.get(requestString).json()
    resData = []
    for i in data['rows']:
        row = []
        for j in i['elements']:
            row.append(j['distance']['value'])
        resData.append(row)
    return resData

def readCSV():
    arr = []
    with open('./destination.csv', 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            arr.append(row)
    return arr

def writeCSV(arr):
    with open('./distance.csv', 'w') as f:
        writer = csv.writer(f, lineterminator='\n')
        writer.writerows(arr)

distances = getDistance(readCSV()[0])
writeCSV(distances)