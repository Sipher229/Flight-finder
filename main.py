import time

#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve
# the program requirements.

from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData
# from dotenv import load_dotenv
# from notification_manager import NotificationManager
# import os

# load_dotenv()

# FLIGHT_SEARCH_API_KEY = os.getenv("FLIGHT_SEARCH_API_KEY")
# FLIGHT_SEARCH_API_SECRET = os.getenv("FLIGHT_SEARCH_API_SECRET")
# FLIGHT_SEARCH_TOKEN_END_POINT = os.getenv("FLIGHT_SEARCH_TOKEN_END_POINT")


def find_flights(isnonstop: str = "false") -> list:
    try:
        data = flight_finder.get_flights(current_iata="YOW",
                                        destination_iata=item['iataCode'],non_stop=isnonstop)
    except Exception as error:
        print(error)
    else:
        return data


data_manager = DataManager()
sheet_rows = data_manager.rows
flight_finder = FlightSearch()

recursion_depth = 0

for item in sheet_rows:

    data = find_flights()
    if len(data) == 0:
        print(f"No direct flights to {item['city']} finding indirect flights")
        data = find_flights('true')

    print(FlightData.find_cheapest_flight(data))

    # if flight_data.destination != 'N/A':
    #     NotificationManager.send_sms(flight_data=flight_data, city=item['city'])
    # time.sleep(1)




