import csv
from TrainConnection import TrainConnection

def check_train_connections(file_name):
    # Erstellen Sie eine Instanz von TrainConnection
    train_connection = TrainConnection()

    # Erstellen Sie Listen für Städte mit und ohne Verbindung
    no_connection = []
    has_connection = []

    # Lesen Sie die CSV-Datei ein
    with open(file_name, 'r') as file:
        reader = csv.reader(file)
        cities = [row[0] for row in reader]

    # Überprüfen Sie die Zugverbindungen zwischen allen Städten
    for i in range(len(cities)):
        for j in range(i+1, len(cities)):
            start = cities[i]
            destination = cities[j]
            connection = train_connection.TrainConnectionDownloader(start, destination)
            if connection:
                has_connection.append((start, destination))
            else:
                no_connection.append((start, destination))

    # Drucken Sie die Listen
    print(f"Städte mit Verbindung: {has_connection}")
    print(f"Städte ohne Verbindung: {no_connection}")

if __name__ == "__main__":
    check_train_connections('CityCoordinates.csv')
