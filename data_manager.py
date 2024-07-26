import requests
from dotenv import load_dotenv
import os

load_dotenv()

SHEETY_END_POINT = os.getenv("SHEETY_END_POINT")
SHEETY_USERS_ENDPOINT = os.getenv("SHEETY_USERS_ENDPOINT")

sheety_headers = {
    "Authorization": os.getenv("SHEETY_AUTHORIZATION")
}


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.rows = self.get_rows()
        self.users = self.get_users()
    def get_rows(self):
        return requests.get(url=SHEETY_END_POINT, headers=sheety_headers).json()["prices"]

    def edit_row(self, row_id: str, data: str):
        body = {
            "price": {
                "iataCode": data
            }
        }
        requests.put(f"{SHEETY_END_POINT}/{row_id}", headers=sheety_headers, json=body)


    def get_users(self):
        return requests.get(url=SHEETY_USERS_ENDPOINT, headers=sheety_headers).json()["users"]

