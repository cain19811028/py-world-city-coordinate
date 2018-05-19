def getGeoInfo(city):
    return city

"""
Main
"""
if __name__ == "__main__":
    city = input("please input a city name : ")
    info = getGeoInfo(city)
    print(info)