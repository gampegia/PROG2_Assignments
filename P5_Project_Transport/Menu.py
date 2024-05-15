import pandas as pd
import TrainConnection
import countrymapping
import CityCoordinates
import Calculator
import Blacklist

class TrainConnectionMenu:
    def __init__(self):
        """
        Initialize the TrainConnectionMenu class with default values.
        """
        self.start_city = None
        self.start_country = None
        self.destination_city = None
        self.destination_country = None
        try:
            self.df = pd.read_csv('countrytrainmapping.csv')
        except FileNotFoundError:
            msg_file_404 = "Error: 'countrytrainmapping.csv' file not found."
            TrainConnectionMenu.set_console_output(msg_file_404)
            self.df = pd.DataFrame(columns=['Country', 'Website'])

    def input_route(self):
        """
        Get input from the user for start city, destination city, and destination country.
        """
        print("Enter all entries in English or the exact name of the destination!")
        self.start_city = input("Enter the start city: ")
        self.start_country = input("Enter the start country: ").lower()
        self.destination_city = input("Enter the destination city: ")
        self.destination_country = input("Enter the destination country: ").lower()

    def get_train_website(self):
        """
        Get the website for train connections based on the destination country.
        """
        try:
            website = self.df.loc[self.df['Country'] == self.destination_country, 'Website'].values[0]
            msg_visit_country_website = f"Visit {website} for more information."
            TrainConnectionMenu.set_console_output(msg_visit_country_website)
        except IndexError:
            msg_index_error = f"Error: No website found for country '{self.destination_country}'."
            TrainConnectionMenu.set_console_output(msg_index_error)
        except Exception as e:
            msg_exception = f"An unexpected error occurred: {e}"
            TrainConnectionMenu.set_console_output(msg_exception)

    @staticmethod
    def set_console_output(msg):
        """
        Static method to print messages to the console.
        """
        print(msg)

    def display_connection(self):
        """
        Display the train connection from the start city to the destination city.
        If no direct connection is found, suggest the nearest station and find connections to it.
        """
        if self.start_city and self.destination_city and self.destination_country:
            blacklist_checker = Blacklist.Blacklist()
            if blacklist_checker.check_blacklist(self.start_city, self.start_country, self.destination_city, self.destination_country):
                msg_blacklist = (f"The Route from {self.start_city} to "
                                 f"{self.destination_city} is inexistent and on the blacklist, try another one.")
                TrainConnectionMenu.set_console_output(msg_blacklist)
            else:
                try:
                    msg_from_to = f"Train connection from {self.start_city} to {self.destination_city}"
                    TrainConnectionMenu.set_console_output(msg_from_to)

                    train_connection = TrainConnection.TrainConnection()
                    connection = train_connection.TrainConnectionDownloader(
                        self.start_city + " " + self.start_country, self.destination_city)

                    if connection:
                        train_connection.display_next_connection(connection)
                    else:
                        calculator = Calculator.Calculator()
                        calculator.set_start_city(self.start_city, self.start_country)
                        calculator.set_destination_city(self.destination_city, self.destination_country)
                        calculator.__post_init__()

                        next_station = calculator.choose_transfer_station()

                        if next_station is None:
                            blacklist_checker.write_to_blacklist(self.start_city, self.start_country, self.destination_city, self.destination_country)
                            msg_blacklisted = f"The requested route from {self.start_city} to {self.destination_city} does not exist and has been blacklisted"
                            TrainConnectionMenu.set_console_output(msg_blacklisted)

                        else:
                            msg_not_found = (f"No direct connection found. The nearest station to "
                                             f"{self.destination_city} is {next_station}.")
                            msg_finding_alternative = f"Finding connection to {next_station}..."
                            TrainConnectionMenu.set_console_output(msg_not_found)
                            TrainConnectionMenu.set_console_output(msg_finding_alternative)

                            connection_to_next_station = train_connection.TrainConnectionDownloader(self.start_city, next_station)
                            train_connection.display_next_connection(connection_to_next_station)
                            train_connection.display_next_connection(connection)
                except Exception as e:
                    msg_invalid_route = f"An unexpected error occurred while displaying the connection: {e}"
                    TrainConnectionMenu.set_console_output(msg_invalid_route)
        else:
            msg_invalid_route = "Please input a valid route first."
            TrainConnectionMenu.set_console_output(msg_invalid_route)


if __name__ == "__main__":
    menu = TrainConnectionMenu()
    menu.input_route()
    menu.display_connection()
    menu.get_train_website()
