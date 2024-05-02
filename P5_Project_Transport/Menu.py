from datetime import datetime
import TrainConnection


class TrainConnectionMenu:
    """
    A class to represent a menu for displaying train connections.

    Attributes:
        connections (list): A list of dictionaries representing train connections.
    """

    def __init__(self, connections):
        """
        Initializes a TrainConnectionMenu object with connections data.

        Args:
            connections (list): A list of dictionaries representing train connections.
        """
        self.connections = connections


    @staticmethod
    def print_connection(departure_time,departure_delay,station_name_departure,platform_departure,journey_name,
                         arrival_time,arrival_delay,station_name_arrival,platform_arrival):

        print(f"{departure_time} {'+' + str(departure_delay) if departure_delay else '':<5}"
              f"{station_name_departure:<20}{platform_departure:<10}")
        print(f"{journey_name:>17}")
        print(f"{arrival_time} {'+' + str(arrival_delay) if arrival_delay else '':<5}"
              f"{station_name_arrival:<20}{platform_arrival:<10}")


    @staticmethod
    def get_journey_name(section):

        if section['journey'] == None:
            output = "Walk"
        else:
            output = section['journey']['name']
        return output
    def display_next_connection(self):
        """
        Displays the next train connection between specified locations.
        """
        # Convert departure timestamps to datetime objects
        for conn in self.connections:
            try:
                conn['from']['departureTimestamp'] = datetime.fromtimestamp(conn['from']['departureTimestamp'])
            except KeyError:
                print(f"Invalid connection data: 'from.departureTimestamp' key not found for connection: {conn}")
                continue

        # Sort connections by departure time
        sorted_connections = sorted(self.connections, key=lambda x: x['from']['departureTimestamp'])

        # Print header
        print(f"{'Time':<10} {'Journey':<15} {'Platform':<10}")

        # Print the next connection
        if sorted_connections:
            next_conn = sorted_connections[0]
            for section in next_conn['sections']:
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
                    continue

                station_name_departure = section['departure']['station']['name']
                station_name_arrival = section['arrival']['station']['name']
                platform_departure = section['departure']['platform'] or ''
                platform_arrival = section['arrival']['platform'] or ''

                departure_delay = section['departure']['delay'] if 'delay' in section['departure'] else ''
                arrival_delay = section['arrival']['delay'] if 'arrival' in section and 'delay' in section[
                    'arrival'] else ''

                journey_name = TrainConnectionMenu.get_journey_name(section)
                TrainConnectionMenu.print_connection(departure_time,
                                                     departure_delay,
                                                     station_name_departure,
                                                     platform_departure,
                                                     journey_name,
                                                     arrival_time,
                                                     arrival_delay,
                                                     station_name_arrival,
                                                     platform_arrival)

        else:
            print("No connections found")


if __name__ == "__main__":
    start = "Köniz"
    destination = "Bern"

    downloader = TrainConnection.TrainConnection()
    connections = downloader.TrainConnectionDownloader(start, destination)
    #print(connections)
    menu = TrainConnectionMenu(connections)
    menu.display_next_connection()
