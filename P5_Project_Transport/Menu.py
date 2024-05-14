import pandas as pd
import TrainConnection
import countrymapping
import CityCoordinates
import Calculator

class TrainConnectionMenu:
    def __init__(self):
        self.start_city = None
        self.destination_city = None
        self.destination_country = None
        self.df = pd.read_csv('countrytrainmapping.csv')

    def input_route(self):
        self.start_city = input("Enter the start city: ")
        self.destination_city = input("Enter the destination city: ")
        self.destination_country = (input("Enter the destination country: ")).lower()

    def get_train_website(self):
        try:
            self.destination_country = str(self.destination_country).lower()
            website = self.df.loc[self.df['Country'] == self.destination_country, 'Website'].values[0]
            #print(f"Visit {website} for more information.")
            msg_visit_country_website = str(f"Visit {website} for more information.")
            TrainConnectionMenu.set_console_output(msg_visit_country_website)
        except:
            pass

    @staticmethod
    def set_console_output(msg):
        print(msg)

    def display_connection(self):
        if self.start_city and self.destination_city:
            msg_from_to = str(f"Train connection from {self.start_city} to {self.destination_city}")
            TrainConnectionMenu.set_console_output(msg_from_to)
            train_connection = TrainConnection.TrainConnection()
            connection = train_connection.TrainConnectionDownloader(self.start_city+self.destination_country, self.destination_city)
            if connection:
                train_connection.display_next_connection(connection)
            else:
                calculator = Calculator.Calculator()
                calculator.set_start_city(self.start_city, 'switzerland')
                calculator.set_destination_city(self.destination_city, self.destination_country)
                calculator.__post_init__()
                next_station = calculator.choose_transfer_station()
                #print(f"No direct connection found. The nearest station to {self.destination_city} is {next_station}.")
                #print(f"Finding connection to {next_station}...")
                msg_not_found = str(f"No direct connection found. The nearest station to {self.destination_city}"
                                    f" is {next_station}.")
                msg_finding_alternative = str(f"Finding connection to {next_station}...")
                TrainConnectionMenu.set_console_output(msg_not_found)
                TrainConnectionMenu.set_console_output(msg_finding_alternative)
                connection_to_next_station = train_connection.TrainConnectionDownloader(self.start_city, next_station)
                train_connection.display_next_connection(connection_to_next_station)
                train_connection.display_next_connection(connection)
        else:
            #print("Please input a valid route first.")
            msg_invalide_route = str("Please input a valid route first.")
            TrainConnectionMenu.set_console_output(msg_invalide_route)
 

if __name__ == "__main__":
    menu = TrainConnectionMenu()
    menu.input_route()
    menu.display_connection()
    menu.get_train_website()

