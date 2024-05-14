import pandas as pd
import TrainConnection
import Blacklist

class TrainConnectionMenu:
    def __init__(self):
        self.start_city = None
        self.destination_city = None
        self.destination_country = None

    def input_route(self):
        self.start_city = input("Enter the start city: ")
        self.destination_city = input("Enter the destination city: ")
        self.destination_country = input("Enter the destination country: ")

    def get_train_website(self):
        website = self.df.loc[self.df['Country'] == self.destination_country, 'Website'].values[0]
        return website

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
