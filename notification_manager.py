
import os
from twilio.rest import Client
from dotenv import load_dotenv
from flight_data import FlightData

load_dotenv()

TWILIO_AUTH_TOKEN = os.environ['TWILIO_AUTH_TOKEN']
ACCOUNT_SID = os.environ['ACCOUNT_SID']


class NotificationManager:
    def __int__(self):
        self.message = "The following cheapest flight was found: \n"

    @staticmethod
    def send_sms(flight_data: FlightData, city: str):
        client = Client(ACCOUNT_SID, TWILIO_AUTH_TOKEN)
        message = client.messages.create(
            from_='+16672919103',
            to='+13434628385',
            body=f"The following cheapest flight to {city} was found: \n" + str(flight_data)
        )
        print(message.status)





