import csv
from TrainConnection import TrainConnection
import pandas as pd

"""
Functions:
    - read_csv_pandas: Reads a CSV file using pandas.
    - read_csv: Reads a CSV file using Python's csv module.
    - printcities: Prints all cities in the given list.
    - check_has_connection: Checks if a train connection exists between two cities.
    - backtest: Tests multiple cities for train connections.
"""

def read_csv_pandas(filename):
    """
    Reads a CSV file using pandas and returns a DataFrame.

    Args:
        filename (str): Path to the CSV file.

    Returns:
        pd.DataFrame: DataFrame containing the CSV data.
    """
    df = pd.read_csv(filename, header=0)
    return df

def read_csv(filename):
    """
    Reads a CSV file using Python's csv module and extracts the first column (assumed to be city names).

    Args:
        filename (str): Path to the CSV file.

    Returns:
        list: List of city names.
    """
    with open(filename, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header row
        cities = [row[0] for row in reader]
    return cities

def printcities(city_list):
    """
    Prints all cities in the given list.

    Args:
        city_list (list): List of city names.
    """
    for row in city_list:
        print(row)

def check_has_connection(start, destination):
    """
    Checks if there is a train connection between two cities.

    Args:
        start (str): Name of the starting city.
        destination (str): Name of the destination city.

    Returns:
        bool: True if a direct train connection exists, otherwise False.
    """
    train_connection = TrainConnection()
    connection = train_connection.TrainConnectionDownloader(start, destination)
    connection_flag, destination_city = train_connection.has_connection(connection)

    print(train_connection.has_connection(connection))
    destination = destination.replace("-", " ")

    result = False  # Initialize `result` to a default value

    if connection_flag:
        destination_city = destination_city.replace(",", "")
        if destination_city == destination:
            result = True
            print("HAS A CONNECTION")
    else:
        print("NO Connection Available")
    return result

def backtest(city_list):
    """
    Tests multiple cities for train connections from a fixed starting point (Zürich HB).

    Args:
        city_list (list): List of city names.

    Returns:
        tuple: (has_connection, no_connection)
            - has_connection (int): Number of cities with a direct train connection.
            - no_connection (int): Number of cities without a direct train connection.
    """
    start = "Zürich HB"
    no_connection = 0
    has_connection = 0
    for city in city_list:
        destination = city
        print(city)
        #print(has_connection, no_connection)
        if check_has_connection(start, destination):
            has_connection += 1
        else:
            no_connection += 1
    return has_connection, no_connection

if __name__ == "__main__":
    # Read the list of cities from a CSV file and perform backtesting
    test = read_csv("cities.csv")
    print(backtest(test))
