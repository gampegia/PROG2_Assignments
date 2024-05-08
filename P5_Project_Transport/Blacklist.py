import csv
import datetime
from dataclasses import dataclass

@dataclass
class Blacklist:

    @staticmethod
    def __timestamp():
        """
        Generate a timestamp in the format "YYYY-MM-DD HH:MM:SS" for the current time.

        Returns:
            str: A string representing the current timestamp.
        """
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return timestamp

    def check_blacklist(self, start_city, start_country, destination_city, destination_country):
        """
        Check if a given route (start_city, start_country, destination_city, destination_country) is present in the blacklist CSV file.
        The comparison is case-insensitive.

        Args:
            start_city (str): The starting city of the route.
            start_country (str): The starting country of the route.
            destination_city (str): The destination city of the route.
            destination_country (str): The destination country of the route.

        Returns:
            bool: True if the route is in the blacklist, False otherwise.
        """
        with open('Blacklist.csv', 'r', encoding='utf-8') as csvfile:
            csvreader = csv.reader(csvfile)
            for row in csvreader:
                # Convert both existing entry and new entry to lowercase for case-insensitive comparison
                if row[:4] == [start_city.lower(), start_country.lower(), destination_city.lower(), destination_country.lower()]:
                    return True
        return False

    def write_to_blacklist(self, start_city, start_country, destination_city, destination_country):
        """
        Write a new route (start_city, start_country, destination_city, destination_country) to the blacklist CSV file if it doesn't already exist.
        The entries are written in lowercase for case-insensitive comparison.

        Args:
            start_city (str): The starting city of the route.
            start_country (str): The starting country of the route.
            destination_city (str): The destination city of the route.
            destination_country (str): The destination country of the route.
        """
        if not self.check_blacklist(start_city, start_country, destination_city, destination_country):
            with open('Blacklist.csv', 'a', newline='', encoding='utf-8') as csvfile:
                csvwriter = csv.writer(csvfile)
                # Write lowercase entries to the CSV file
                row = [start_city.lower(), start_country.lower(), destination_city.lower(), destination_country.lower(), self.__timestamp()]
                csvwriter.writerow(row)


if __name__ == "__main__":
    blacklist = Blacklist()
    blacklist.write_to_blacklist("Zürich", "Switzerland", "Turin", "Italy")