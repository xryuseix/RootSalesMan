import requests
import csv
import json

# APIリクエストを送信
def getDistance(places):
    with open("./config.txt") as f:
        API_KEY = f.read()
    url = "https://maps.googleapis.com/maps/api/distancematrix/json"
    placeString = "|".join(places)
    requestString = "{}?language=ja&key={}&origins={}&destinations={}&mode=walking&units=metric".format(
        url, API_KEY, placeString, placeString
    )
    # with open("./tmp.json") as f:
    #     requestString = f.read()
    data = requests.get(requestString).json()
    # data = json.loads(requestString)
    resData = []
    notFoundSpot = []
    # print(data)
    for spot1, i in zip(places, data["rows"]):
        row = []
        nf_count = 0
        for j in i["elements"]:
            if j["status"] == "OK":
                row.append(j["distance"]["value"])
            else:
                nf_count += 1
        resData.append(row)
        if nf_count == len(places):
            notFoundSpot.append(spot1)
    notFoundSpot = list(set(notFoundSpot))
    for s in notFoundSpot:
        print("{} is NOT FOUND!!".format(s))
    return resData, notFoundSpot


def readCSV():
    arr = []
    with open("./destination.csv", "r") as f:
        reader = csv.reader(f)
        for row in reader:
            arr.append(row)
    return arr


def writeCSV(arr):
    with open("./distance.csv", "w") as f:
        writer = csv.writer(f, lineterminator="\n")
        writer.writerows(arr)


distances, notFoundSpot = getDistance(readCSV()[0][:10])

if notFoundSpot:
    print("can't calculate :(")
else:
    writeCSV(distances)
