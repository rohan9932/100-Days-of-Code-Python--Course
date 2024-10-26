import requests
from datetime import datetime

USERNAME = "rohan932"
TOKEN = "AdfbeidhfggelhkH"
GRAPH_ID = "graph01"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# setup account
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Coding Graph",
    "unit": "hours",
    "type": "float",
    "color": "sora",
}

headers = {
    "X-USER-TOKEN": TOKEN,
}

# create a graph
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

# create a pixel
create_pixel_endpoint = f"{graph_endpoint}/{GRAPH_ID}"

today = datetime.now()

pixel_config = {
    "date": today.strftime("%Y%m%d"), # to get date as "20240908(08 Sep 24)" method
    "quantity": input("How many hours did you code today?: "),
}

response = requests.post(url=create_pixel_endpoint, json=pixel_config, headers=headers)
print(response.text)

# update the data
# update_data_endpoint = f"{create_pixel_endpoint}/{today.strftime('%Y%m%d')}"
#
# update_config = {
#     "quantity": "2.0",
# }
#
# response = requests.put(url=update_data_endpoint, json=update_config, headers=headers)
# print(response.text)

# delete a pixel
# delete_pixel_endpoint = f"{create_pixel_endpoint}/{today.strftime('%Y%m%d')}"
#
# response = requests.delete(url=delete_pixel_endpoint, headers=headers)
# print(response.text)
