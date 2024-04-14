import pandas as pd
import matplotlib.pyplot as plt
from dataclasses import dataclass
from Downloader import Downloader

@dataclass(frozen=True)
class DataProcessor:
    downloader: Downloader

    def load_data(self):
        try:
            data = pd.read_csv(self.downloader.FILENAME)
            print(f"'{self.downloader.FILENAME}' loaded successfully!")
            return data
        except Exception as e:
            print(f"An error occurred: {e}")
            return None

    def calculate_statistics(self, data):
        if data is not None:
            # Calculate the mean, median, and standard deviation of the values
            print(f"Mean: {data['water_temperature'].mean()}")
            print(f"Median: {data['water_temperature'].median()}")
            print(f"Standard deviation: {data['water_temperature'].std()}")


    def visualize_data(self, data):
        if data is not None:
            # Visualize the distribution of values
            data.hist(bins=50, figsize=(20,15))
            plt.show()


if __name__ == "__main__":
    downloader = Downloader()
    downloader.download()

    processor = DataProcessor(downloader)
    data = processor.load_data()
    processor.calculate_statistics(data)
    processor.visualize_data(data)