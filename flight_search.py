from dotenv import load_dotenv
import os
import requests
import datetime

load_dotenv()

date = datetime.datetime.now() + datetime.timedelta(days=180.0)

return_date = date.strftime("%Y-%m-%d")

tomorrow = (datetime.datetime.now() + datetime.timedelta(hours=24.0)).strftime("%Y-%m-%d")

class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self._api_key: str = os.getenv("FLIGHT_SEARCH_API_KEY")
        self._api_secret: str = os.getenv("FLIGHT_SEARCH_API_SECRET")
        self._token: str = self._get_new_token()
        self._headers: dict = {
            "authorization": f"Bearer {self._token}"
        }

    def get_iata(self, city_name: str) -> str:
        url = "https://test.api.amadeus.com/v1/reference-data/locations/cities"
        headers = {
            "authorization": f"Bearer {self._token}"
        }
        body = {
            'keyword': city_name
        }
        try:
            response = requests.get(url=url, headers=headers, params=body)
        except Exception:
            raise Exception('Error while fetching city iata')



        return response.json()['data'][0]['iataCode']


    def _get_new_token(self) -> str:
        headers = {
            "content-type": 'application/x-www-form-urlencoded',

        }
        body = {
            "grant_type": "client_credentials",
            "client_id": self._api_key,
            "client_secret": self._api_secret
        }
        try:
            response = requests.post(url=os.getenv("FLIGHT_SEARCH_TOKEN_END_POINT"), headers=headers, data=body)
        except Exception:
            raise Exception("Error while fetching token")

        # print(f"Your token is {response.json()['access_token']}")
        # print(f"Your token expires in {response.json()['expires_in']} seconds")
        return response.json()['access_token']

    def get_flights(self, current_iata: str, destination_iata: str, departure_date: str = tomorrow,
                    adults: str = "1", non_stop: str = 'true', max_count: int = 5) -> list:
        url = "https://test.api.amadeus.com/v2/shopping/flight-offers"

        body = {
            'originLocationCode': current_iata,
            'destinationLocationCode': destination_iata,
            'departureDate': departure_date,
            'returnDate': return_date,
            'adults': adults,
            'currencyCode': 'USD',
            'nonStop': non_stop,
            'max': max_count

        }
        try:

            response = requests.get(url=url, params=body, headers=self._headers)
        except Exception:
            raise Exception("Could not get flights")
        else:
            if response.status_code != 200:
                print( response.json())
                return []
            return response.json()['data']





