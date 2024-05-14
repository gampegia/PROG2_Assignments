import pandas as pd
import TrainConnection
import Blacklist
import countrymapping

class TrainConnectionMenu:
    def __init__(self):
        self.start = None
        self.destination = None
        self.destination_country = None
        self.df = pd.read_csv('countrytrainmapping.csv')

    def input_route(self):
        self.start = input("Enter the start city: ")
        self.destination = input("Enter the destination city: ")
        self.destination_country = (input("Enter the destination country: ")).lower()

    def get_train_website(self):
        website = self.df.loc[self.df['Country'] == self.destination_country, 'Website'].values[0]
        print(f"Visit {website} for more information.")

    def display_connection(self):
        if self.start and self.destination:
            print(f"Train connection from {self.start} to {self.destination}")
            train_connection = TrainConnection.TrainConnection()
            connection = train_connection.TrainConnectionDownloader(self.start, self.destination)
            #print(connection) # DEBUG Statement
            train_connection.display_next_connection(connection)
        else:
            print("Please input a valid route first.")

if __name__ == "__main__":
    menu = TrainConnectionMenu()
    menu.input_route()
    menu.display_connection()
    menu.get_train_website()
