import requests
from dataclasses import dataclass
import json



@dataclass(frozen=True)
class TrainConnection:

    URL = f"https://transport.opendata.ch/v1/connections"

    def TrainConnectionDownloader(self, start, destination):
        credentials = f"?from={start}&to={destination}"
        try:
            response = requests.get(self.URL + credentials)
            response.raise_for_status()  # Raise an exception for non-2xx status codes
            api_content = response.content.decode("utf-8")
            data = json.loads(api_content)
            return data.get('connections', [])
        except Exception as e:
            print(f"An error occurred: {e}")
            return None



if __name__ == "__main__":
    train_connection = TrainConnection()
    print(train_connection.TrainConnectionDownloader(start="St. Gallen", destination="Bern"))