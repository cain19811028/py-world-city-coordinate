import json
import requests

URL = "https://maps.googleapis.com/maps/api/geocode/json?address="
KEY = "AIzaSyClwxv44r572Vkcj_MCAfmREF6jdCNZIxA"
HEADERS = {'User-Agent': 'Mozilla/5.0'}

def getGeoInfo(city):
    url = URL + city + "&key=" + KEY
    response = requests.get(url, headers = HEADERS)
    result = json.loads(response.text)
    return result

"""
Main
"""
if __name__ == "__main__":
    city = input("please input a city name : ")
    info = getGeoInfo(city)
    print(info)