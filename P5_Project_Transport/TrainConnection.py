import requests
from dataclasses import dataclass
import json

@dataclass(frozen=True)
class TrainConnection:
    """
    A class to represent train connections between two locations.

    Attributes:
        URL (str): The base URL of the Open Data Swiss Public Transport API.
    """

    URL = f"https://transport.opendata.ch/v1/connections"

    def TrainConnectionDownloader(self, start, destination):
        """
        Downloads train connections between two specified locations.

        Args:
            start (str): The starting location for the train journey.
            destination (str): The destination location for the train journey.

        Returns:
            list: A list of dictionaries representing train connections between the start and destination.
        """
        credentials = f"?from={start}&to={destination}"  # Constructing query parameters
        try:
            response = requests.get(self.URL + credentials)  # Making a GET request to the API
            response.raise_for_status()  # Raise an exception for non-2xx status codes
            api_content = response.content.decode("utf-8")  # Decoding API response content
            data = json.loads(api_content)  # Parsing JSON response
            return data.get('connections', [])  # Extracting 'connections' data from the response
        except Exception as e:
            print(f"An error occurred: {e}")  # Printing error message if an exception occurs
            return None  # Returning None if an error occurs


if __name__ == "__main__":
    train_connection = TrainConnection()
    print(train_connection.TrainConnectionDownloader(start="Davos", destination="st moritz"))
