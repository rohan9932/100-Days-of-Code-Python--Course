import requests
from datetime import datetime

# response = requests.get(url="http://api.open-notify.org/iss-now.json")

# '''
# Response codes
# 1XX - Hold on. Not finished yet.
# 2XX - Here you go with the data.
# 3XX - You don't have permission to view this.
# 4XX - You screwed up or the data doesn't even exist.
# 5XX - I(Server) screwed up.
# '''

# response.raise_for_status() # for showing errors 
# print(response.status_code)

# data = response.json()
# longitude = data["iss_position"]["longitude"]
# latitude = data["iss_position"]["latitude"]
# position = (longitude, latitude)
 
# print(position)

MY_LAT = 23.765844
MY_LONG = 90.358360

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0, 
}

response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]
print(sunrise)


time_now = datetime.now()
print(time_now.hour)

