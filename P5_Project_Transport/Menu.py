import pandas as pd
import TrainConnection
import Blacklist
import countrymapping

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
        website = self.df.loc[self.df['Country'] == self.destination_country, 'Website'].values[0]
        print(f"Visit {website} for more information.")

    def display_connection(self):
        if self.start_city and self.destination_city:
            print(f"Train connection from {self.start_city} to {self.destination_city}")
            train_connection = TrainConnection.TrainConnection()
            connection = train_connection.TrainConnectionDownloader(self.start_city, self.destination_city)
            #print(connection) # DEBUG Statement
            train_connection.display_next_connection(connection)
        else:
            print("Please input a valid route first.")

    def check_blacklist(self):
        blacklist = Blacklist.Blacklist()
        if blacklist.is_blacklisted(self.destination):
            print(f"{self.destination} is blacklisted.")
        else:
            print(f"{self.destination} is not blacklisted.")

if __name__ == "__main__":
    menu = TrainConnectionMenu()
    menu.input_route()
    menu.display_connection()
    menu.get_train_website()
