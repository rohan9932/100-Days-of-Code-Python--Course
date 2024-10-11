import os
import requests
from dotenv import load_dotenv

load_dotenv()

class FlightSearch:
    def __init__(self):
        self._api_key = os.environ["AMEDEUS_API_KEY"]
        self._api_secret = os.environ["AMEDEUS_API_SECRET"]
        self._token = self.get_new_token()

    def get_new_token(self):
        header = {
            "Content-Type": "application/x-www-form-urlencoded",
        }
        body = {
            "grant_type": "client_credentials",
            "client_id": self._api_key,
            "client_secret": self._api_secret
        }
        response = requests.post(
            url="https://test.api.amadeus.com/v1/security/oauth2/token",
            headers=header,
            data=body
        )
        token = response.json()["access_token"]
        return token

    def get_destination_code(self, city_name):
        """
        Retrieves the IATA code for a specified city using the Amadeus Location API.
        Parameters:
        city_name (str): The name of the city for which to find the IATA code.
        Returns:
        str: The IATA code of the first matching city if found; "N/A" if no match is found due to an IndexError,
        or "Not Found" if no match is found due to a KeyError.

        The function sends a GET request to the IATA_ENDPOINT with a query that specifies the city
        name and other parameters to refine the search. It then attempts to extract the IATA code
        from the JSON response.
        - If the city is not found in the response data (i.e., the data array is empty, leading to
        an IndexError), it logs a message indicating that no airport code was found for the city and
        returns "N/A".
        - If the expected key is not found in the response (i.e., the 'iataCode' key is missing, leading
        to a KeyError), it logs a message indicating that no airport code was found for the city
        and returns "Not Found".
        """
        headers = {
            "Authorization": f"Bearer {self._token}"
        }
        query = {
            "keyword": city_name,
            "max": "2",
            "include": "AIRPORTS"
        }
        response = requests.get(
            url="https://test.api.amadeus.com/v1/reference-data/locations/cities",
            headers=headers,
            params=query
        )
        # print(f"Status Code: {response.status_code} Iata: {response.text}")
        try:
            code = response.json()["data"][0]["iataCode"]
        except IndexError:
            print(f"IndexError: No airport code found for {city_name}")
            return "N/A"
        except KeyError:
            print(f"KeyError: No airport code found for {city_name}")
            return "Not Found"

        return code


