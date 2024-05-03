import TrainConnection


class TrainConnectionMenu:
    def __init__(self):
        self.start = None
        self.destination = None

    def input_route(self):
        self.start = input("Enter the start station: ")
        self.destination = input("Enter the destination station: ")

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
