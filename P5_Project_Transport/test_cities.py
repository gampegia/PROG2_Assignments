import csv
from TrainConnection import TrainConnection

def check_train_connections(file_name):
    train_connection = TrainConnection()

    # create lists to store cities with and without connection
    no_connection = []
    has_connection = []

    # Read csv
    with open(file_name, 'r') as file:
        reader = csv.reader(file)
        cities = [row[0] for row in reader]

    # check for connections
    for i in range(len(cities)):
        for j in range(i+1, len(cities)):
            start = cities[i+1]
            destination = cities[j]
            connection = train_connection.TrainConnectionDownloader(start, destination)
            if connection:
                has_connection.append((start, destination))
            else:
                no_connection.append((start, destination))

    
if __name__ == "__main__":
    check_train_connections('CityCoordinates.csv')
    print(f"Cities with connection: {has_connection}")
    print(f"Cities without connection: {no_connection}")

