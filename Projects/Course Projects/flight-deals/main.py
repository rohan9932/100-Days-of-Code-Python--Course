#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

from data_manager import DataManager
from flight_search import FlightSearch
import time

data_manager = DataManager()
sheet_data = data_manager.get_destination_data()
flight_search = FlightSearch()

# check for iatacodes
if len(sheet_data[0]["iataCode"]) == 0:
    for row in sheet_data:
        row["iataCode"] = flight_search.get_destination_code(row["city"])
        time.sleep(2)

data_manager.destination_data = sheet_data #update the data
data_manager.update_destination_code()

