import requests
from datetime import datetime

APP_ID = "7ee77347"
API_KEY = "7abe580b584ead04fa52b4142a0960f5"
BEARER_TOKEN = "Helskdfehsidfhoad"

WEIGHT_KG = 78
HEIGHT_CM = 180.34
AGE = 19

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
exercise_text = input("Tell me which exercises you did?: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

exercise_params = {
    "query": exercise_text,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE,
}

response = requests.post(url=exercise_endpoint, json=exercise_params, headers=headers)
result = response.json()

print(result)

# saving data to google sheets
sheety_endpoint = "https://api.sheety.co/77831bea21aa80185bd147295978265c/myWorkouts/workouts"

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    bearer_headers = {
        "Authorization": f"Bearer {BEARER_TOKEN}"
    }
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"],
        }
    }
    add_row = requests.post(
        url=sheety_endpoint,
        json=sheet_inputs,
        headers=bearer_headers,
    )
    print(add_row.text)
