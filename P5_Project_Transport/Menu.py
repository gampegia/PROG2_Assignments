from datetime import datetime
import TrainConnection


class TrainConnectionMenu:
    def __init__(self, connections):
        self.connections = connections

    def display_next_connection(self):
        # Convert departure timestamps to datetime objects
        for conn in self.connections:
            try:
                conn['from']['departureTimestamp'] = datetime.fromtimestamp(conn['from']['departureTimestamp'])
            except KeyError:
                print(f"Invalid connection data: 'from.departureTimestamp' key not found for connection: {conn}")
                continue

        # Sort connections by departure time
        sorted_connections = sorted(self.connections, key=lambda x: x['from']['departureTimestamp'])

        # Print the next connection
        if sorted_connections:
            next_conn = sorted_connections[0]
            for section in next_conn['sections']:
                try:
                    departure_timestamp = section['departure']['departureTimestamp']
                    arrival_timestamp = section['journey']['passList'][-1]['arrivalTimestamp']
                    delay_timestamp = section['journey']['passList'][-1]['delay']

                    if delay_timestamp is not None:  # Check if delay_timestamp is not None
                        if delay_timestamp > 0:  # Compare delay_timestamp with 0
                            delay = f"(+{delay_timestamp})"
                        else:
                            delay = ""
                    else:
                        delay = ""

                    if isinstance(departure_timestamp, int):
                        departure_time = datetime.fromtimestamp(departure_timestamp).strftime('%H:%M')
                        arrival_time = datetime.fromtimestamp(arrival_timestamp).strftime('%H:%M')
                    else:
                        departure_time = departure_timestamp.strftime('%H:%M')
                        arrival_time = arrival_timestamp.strftime('%H:%M')
                except (KeyError, AttributeError):
                    print(f"Invalid section data: 'departure.departureTimestamp' key not found or invalid for section: {section}")
                    continue

                station_name_departure = section['departure']['station']['name']
                station_name_arrival = section['arrival']['station']['name']
                platform_departure = section['departure']['platform'] or '-'
                platform_arrival = section['arrival']['platform'] or '-'


                if 'journey' in section and section['journey']:
                    journey_name = section['journey']['name']
                    print(f"{departure_time} {delay}   {station_name_departure:<20}{platform_departure}")
                    print(f"         {journey_name}")
                    print(f"{arrival_time}    {station_name_arrival:<20}{platform_arrival}")
                else:
                    arrival_time = section['arrival']['arrivalTimestamp'].strftime('%H:%M')
                    arrival_delay = section['arrival']['delay'] if 'delay' in section['arrival'] and section['arrival']['delay'] else ''
                    print(f"{departure_time} {station_name_departure:<20}{platform_departure}")
                    print(f"{arrival_time} +{arrival_delay} {section['arrival']['station']['name']}")
        else:
            print("No connections found")

if __name__ == "__main__":
    start = "Davos"
    destination = "Genève"

    downloader = TrainConnection.TrainConnection()
    connections = downloader.TrainConnectionDownloader(start, destination)

    menu = TrainConnectionMenu(connections)
    menu.display_next_connection()

