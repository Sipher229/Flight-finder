
class FlightData:
    def __init__(self, price: float | str | int = 'N/A',
                 destination_iata: str = 'N/A',
                 origin_iata: str = 'N/A',
                 out_date: str = 'N/A',
                 return_date: str = 'N/A',
                 stops: int = 0
                 ):

        self.price: str = price
        self.origin: str = origin_iata
        self.destination: str = destination_iata
        self.leave_date: str = out_date
        self.return_date: str = return_date
        self.stops: int = 0

    @staticmethod
    def find_cheapest_flight(data: list[dict]):
        if len(data) == 0:
            print("Empty data list")
            return FlightData()

        flight_item = data[0]
        stops = len(flight_item['itineraries'][1]['segments'])
        lowest_price = float(flight_item['price']['grandTotal'])
        origin = flight_item['itineraries'][0]['segments'][0]['departure']['iataCode']
        destination = flight_item['itineraries'][0]['segments'][-1]['arrival']['iataCode']
        leave_date = flight_item['itineraries'][0]['segments'][0]['departure']['at']
        return_date = flight_item['itineraries'][1]['segments'][0]['arrival']['at']

        cheapest_flight = FlightData(price=lowest_price,
                                     origin_iata=origin,
                                     destination_iata=destination,
                                     out_date=leave_date,
                                     return_date=return_date,
                                     stops=stops)

        for item in data[1:]:
            item_price = float(item['price']['grandTotal'])
            if item_price < lowest_price:
                lowest_price = item_price
                stops = len(item['itineraries'][1]['segments'])
                origin = item['itineraries'][0]['segments'][0]['departure']['iataCode']
                destination = item['itineraries'][0]['segments'][-1]['arrival']['iataCode']
                leave_date = item['itineraries'][0]['segments'][0]['departure']['at'].split('T')
                return_date = item['itineraries'][1]['segments'][0]['arrival']['at'].split('T')
                cheapest_flight = FlightData(price=lowest_price,
                                             origin_iata=origin,
                                             destination_iata=destination,
                                             out_date=leave_date,
                                             return_date=return_date,
                                             stops=stops)

        return cheapest_flight

    def __str__(self):
        return f"Flight data: \n Price: ${self.price} \n Origin: {self.origin} \n"\
                     f" Destination: {self.destination} \n Leave on: {self.leave_date} \n"\
                     f" Return on: {self.return_date}\n Stops: {self.stops}\n\n"


