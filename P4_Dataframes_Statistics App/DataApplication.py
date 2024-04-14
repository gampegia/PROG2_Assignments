from DataProcessor import DataProcessor
from Downloader import Downloader
 
class DataApplication:
    def __init__(self):
        self.downloader = Downloader()
        self.processor = DataProcessor(self.downloader)
 
    def run(self):
        self.downloader.download()
        data = self.processor.load_data()
        self.processor.calculate_statistics(data)
        self.processor.visualize_data(data)

    def inputmenu(self):
        print("1. Download data")
        print("2. Load data")
        print("3. Calculate statistics")
        print("4. Visualize data")
        print("5. Exit")
        return input("Enter your choice: ")
    def run(self):
        while True:
            choice = self.inputmenu()
            if choice == "1":
                self.downloader.download()
            elif choice == "2":
                data = self.processor.load_data()
            elif choice == "3":
                self.processor.calculate_statistics(data)
            elif choice == "4":
                self.processor.visualize_data(data)
            elif choice == "5":
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    app = DataApplication()
    app.run()
