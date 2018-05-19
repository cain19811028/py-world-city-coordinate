import requests

URL = "https://maps.googleapis.com/maps/api/geocode/json?address="
HEADERS = {'User-Agent': 'Mozilla/5.0'}

def getGeoInfo(city):
    url = URL + city
    response = requests.get(url, headers = HEADERS)
    return response

"""
Main
"""
if __name__ == "__main__":
    city = input("please input a city name : ")
    info = getGeoInfo(city)
    print(info)