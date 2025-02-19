This application will tell you when the International Space Station is above you.

Requirements:
- latest version of Python (app was created with version 3.13)
- requests library (run 'pip install requests' in the terminal)

This app calls 2 APIs:
- International Space Station Current Location API (http://open-notify.org/Open-Notify-API/ISS-Location-Now/)
- Sunset and sunrise times API (http://open-notify.org/Open-Notify-API/ISS-Location-Now/)

Run main.py to start the app and every 60 seconds it will search for the ISS position and notify you if it is close to your location (change LAT and LNG variables to correspond with your location - use https://www.latlong.net).
