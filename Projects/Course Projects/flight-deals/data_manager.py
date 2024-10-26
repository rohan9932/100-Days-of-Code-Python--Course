import os
import requests
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv

# load environment variables from .env file
load_dotenv()

SHEETY_PRICES_ENDPOINT = "https://api.sheety.co/77831bea21aa80185bd147295978265c/flightDeals/prices"


class DataManager:
    def __init__(self):
        self.user = os.environ["SHEETY_USERNAME"]
        self.password = os.environ["SHEETY_PASSWORD"]
        self.authorization = HTTPBasicAuth(self.user, self.password)
        self.destination_data = []

    def get_destination_data(self):
        response = requests.get(url=SHEETY_PRICES_ENDPOINT, auth=self.authorization)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def update_destination_code(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"],
                }
            }
            response = requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/{city["id"]}",
                json= new_data,
                auth=self.authorization
            )



