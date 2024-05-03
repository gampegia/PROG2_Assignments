import requests
from dataclasses import dataclass
import json
from datetime import datetime

@dataclass(frozen=True)
class TrainConnection:
    """
    A class to represent train connections between two locations.

    Attributes:
        URL (str): The base URL of the Open Data Swiss Public Transport API.
    """

    URL = f"https://transport.opendata.ch/v1/connections"

    def TrainConnectionDownloader(self, start, destination):
        """
        Downloads train connections between two specified locations.

        Args:
            start (str): The starting location for the train journey.
            destination (str): The destination location for the train journey.

        Returns:
            list: A list of dictionaries representing train connections between the start and destination.
        """
        credentials = f"?from={start}&to={destination}"  # Constructing query parameters
        try:
            response = requests.get(self.URL + credentials)  # Making a GET request to the API
            response.raise_for_status()  # Raise an exception for non-2xx status codes
            api_content = response.content.decode("utf-8")  # Decoding API response content
            data = json.loads(api_content)  # Parsing JSON response
            return data.get('connections', [])  # Extracting 'connections' data from the response
        except Exception as e:
            print(f"An error occurred: {e}")  # Printing error message if an exception occurs
            return None  # Returning None if an error occurs

    @staticmethod
    def build_print_msg(array):

        departure_time = array[0]
        departure_delay = array[1]
        station_name_departure = array[2]
        platform_departure = array[3]
        journey_name = array[4]
        arrival_time = array[5]
        arrival_delay = array[6]
        station_name_arrival = array[7]
        platform_arrival = array[8]

        output_string = (
            f"{departure_time} {'+' + str(departure_delay) if departure_delay else '':<5}"
            f"{station_name_departure:<20}{platform_departure:<10}\n"
            f"           {journey_name}\n"
            f"{arrival_time} {'+' + str(arrival_delay) if arrival_delay else '':<5}"
            f"{station_name_arrival:<20}{platform_arrival:<10}"
        )
        return output_string
    @staticmethod
    def print_connection(str_connection_sections):

        for section in str_connection_sections:
            print(section)


    @staticmethod
    def get_journey_name(section):

        if section['journey'] == None:
            output = "Walk"
        else:
            output = str(section['journey']['category']+" "+section['journey']['number'])
        return output

    def sort_connections(self, connections):
        # Convert departure timestamps to datetime objects
        for conn in connections:
            try:
                conn['from']['departureTimestamp'] = datetime.fromtimestamp(conn['from']['departureTimestamp'])
            except KeyError:
                print(f"Invalid connection data: 'from.departureTimestamp' key not found for connection: {conn}")
                continue

        # Sort connections by departure time
        sorted_connections = sorted(connections, key=lambda x: x['from']['departureTimestamp'])
        return sorted_connections

    @staticmethod
    def print_header():
        # Print header
        print(f"{'Time':<10} {'Journey':<15} {'Platform':<10}")

    @staticmethod
    def get_connection_details(section):
        try:
            departure_timestamp = section['departure']['departureTimestamp']
            arrival_timestamp = section['arrival']['arrivalTimestamp']

            if isinstance(departure_timestamp, int):
                departure_time = datetime.fromtimestamp(departure_timestamp).strftime('%H:%M')
                arrival_time = datetime.fromtimestamp(arrival_timestamp).strftime('%H:%M')
            else:
                departure_time = departure_timestamp.strftime('%H:%M')
                arrival_time = arrival_timestamp.strftime('%H:%M')
        except (KeyError, AttributeError):
            print(f"Invalid section data: 'departure.departureTimestamp' "
                  f"key not found or invalid for section: {section}")

        station_name_departure = section['departure']['station']['name']
        station_name_arrival = section['arrival']['station']['name']
        platform_departure = section['departure']['platform'] or ''
        platform_arrival = section['arrival']['platform'] or ''

        departure_delay = section['departure']['delay'] if 'delay' in section['departure'] else ''
        arrival_delay = section['arrival']['delay'] if 'arrival' in section and 'delay' in section[
            'arrival'] else ''

        journey_name = TrainConnection.get_journey_name(section)
        conn_print_information = [departure_time,
                                  departure_delay,
                                  station_name_departure,
                                  platform_departure,
                                  journey_name,
                                  arrival_time,
                                  arrival_delay,
                                  station_name_arrival,
                                  platform_arrival]

        return conn_print_information


    def display_next_connection(self,connection):
        """
        Displays the next train connection between specified locations.
        """

        sorted_connections = self.sort_connections(connection)

        self.print_header()
        str_connection_sections = []
        if sorted_connections:
            next_conn = sorted_connections[0]
            for section in next_conn['sections']:
                conn_print_information = self.get_connection_details(section)

                str_connection_sections.append(self.build_print_msg(conn_print_information))

            self.print_connection(str_connection_sections)
        else:
            print("No connections found")


if __name__ == "__main__":
    start = "Visp"
    destination = "Milano"
    train_connection = TrainConnection()
    connection = train_connection.TrainConnectionDownloader(start, destination)
    train_connection.display_next_connection(connection)
