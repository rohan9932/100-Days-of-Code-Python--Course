import requests
import os
from twilio.rest import Client

# api infos
OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = os.environ.get("OWM_API_KEY") # put the api key while running in ide

parameters = {
    "lat": 23.810331,
    "lon": 90.412521,
    "appid": api_key,
    "cnt": 4,
}

# making a request
response = requests.get(url=OWM_Endpoint, params=parameters)
response.raise_for_status()
data = response.json()

account_sid = "AC40aa9387a4c10bd325d9d18be2738407"
auth_token = os.environ.get("AUTH_TOKEN") # put the auth_code while running in ide

# checking the possibility of rain
will_rain = False
for forecast in data["list"]:
    weather_data = forecast["weather"]
    condition_code = int(weather_data[0]["id"])
    if condition_code < 600: # checking the id's
        will_rain = True

# send sms
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        from_="+17602786294",
        body="It's going to rain today. Bring an umbrella!☔️",
        to="+8801890317719",
    )
    print(message.status)

