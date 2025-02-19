import requests
import time
from datetime import datetime

def is_iss_overhead():
    """Makes a request to 'ISS Current Position API' and compares it with my position"""
    iss_response = requests.get(url="http://api.open-notify.org/iss-now.json")
    iss_response.raise_for_status()
    iss_data = iss_response.json()
    iss_longitude = float(iss_data["iss_position"]["longitude"])
    iss_latitude = float(iss_data["iss_position"]["latitude"])
    if  LAT - 5 <= iss_latitude <= LAT + 5 and LNG - 5 <= iss_longitude <= LNG + 5: #+-5 degrees
        return True

def is_dark():
    """Makes a request to 'Sunset and sunrise times API' and compares my current hour with the sunset and the sunrise hours"""
    parameters = {
        "lat": LAT,
        "lng": LNG,
        "formatted": 0,
        "tzid": timezone
    }

    response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    if sunrise <= time_now.hour <= sunset:
        return True

#Latitute, longitude and timezone are set for Bucharest
LAT = 44.426765
LNG = 26.102537
timezone = "Europe/Bucharest"

while True:
    time_now = datetime.now()
    time.sleep(60) #Run every 60 seconds
    print(f"{time_now}: searching...")
    if is_dark() and is_iss_overhead():
        print(f"{time_now}: the ISS is above you.")
    elif not is_dark() and is_iss_overhead():
        print(f"{time_now}: the ISS is above you, but it is day outside.")