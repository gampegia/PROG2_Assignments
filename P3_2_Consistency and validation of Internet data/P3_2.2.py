import requests  # Importing the requests library to make HTTP requests
import backoff  # Importing backoff library for exponential backoff strategy
import json  # Importing json library for JSON parsing

class BOMService:
    """
    Class to handle Bill of Materials (BOM) service.

    Attributes:
        base_url (str): Base URL of the BOM service.
    """

    def __init__(self, base_url):
        """
        Initializes the BOMService with the base URL.

        Args:
            base_url (str): Base URL of the BOM service.
        """
        self.base_url = base_url  # Storing the base URL for the BOM service

    @staticmethod
    def get_bom_total_price(data):
        """
        Computes the total price from the given BOM data.

        Args:
            data (dict): BOM data containing items and their prices.

        Returns:
            float: Total price of all items.
        """
        total_price = sum(list(data.values()))  # Summing up the prices in the BOM data
        return total_price

    @staticmethod
    def get_max_width_item(data):
        """
        Computes the maximum width of items in the BOM data.

        Args:
            data (dict): BOM data containing items and their prices.

        Returns:
            int: Maximum width of items.
        """
        width = max(len(str(item)) for item in data.keys())  # Finding the maximum width of items
        return width

    @staticmethod
    def get_max_width_price(data):
        """
        Computes the maximum width of prices in the BOM data.

        Args:
            data (dict): BOM data containing items and their prices.

        Returns:
            int: Maximum width of prices.
        """
        width = max(len(str(item)) for item in data.values())  # Finding the maximum width of prices
        return width

    @backoff.on_exception(backoff.expo,
                          (requests.exceptions.Timeout,
                           requests.exceptions.HTTPError,
                           requests.exceptions.ConnectionError))
    def get_bom_data(self):
        """
        Retrieves BOM data from the specified URL.

        Returns:
            dict: Parsed BOM data.
        """
        response = requests.get(self.base_url)  # Making a GET request to fetch BOM data
        response.raise_for_status()  # Raise an exception for non-2xx status codes
        data = response.text  # Extracting the response text
        return self.parse_bom_data(data)  # Parsing the received data

    def parse_bom_data(self, data):
        """
        Parses the raw BOM data and corrects decoding issues.

        Args:
            data (str): Raw BOM data in string format.

        Returns:
            dict: Parsed and corrected BOM data.
        """
        decoded_data = json.loads(data)  # Decoding the JSON data
        return self.decoding_correction(decoded_data)  # Correcting any decoding issues

    def decoding_correction(self, data):
        """
        Corrects any decoding issues in the BOM data.

        Args:
            data (dict): Parsed BOM data.

        Returns:
            dict: BOM data with corrected keys.
        """
        for item in list(data.keys()):  # Iterating through the keys in the data
            corrected_key = item.encode('latin-1').decode('utf-8')  # Correcting the encoding issue
            if corrected_key != item:  # Checking if the key was corrected
                data.update({corrected_key: data[item]})  # Updating the data with corrected key
                data.pop(item)  # Removing the original key
        return self.validation(data)  # Validating the corrected data

    def validation(self, data):
        """
        Validates the BOM data, removing any non-numeric entries.

        Args:
            data (dict): BOM data to be validated.

        Returns:
            dict: Validated BOM data.
        """
        for item in list(data.keys()):  # Iterating through the keys in the data
            if not str(data[item]).isnumeric():  # Checking if the value is numeric
                data.pop(item)  # Removing non-numeric entries
        return self.print_bom(data)  # Printing the validated BOM data

    def print_bom(self, data):
        """
        Prints the BOM data in a formatted table.

        Args:
            data (dict): BOM data to be printed.
        """
        item_width = BOMService.get_max_width_item(data)  # Getting the maximum width of items
        price_width = BOMService.get_max_width_price(data)  # Getting the maximum width of prices
        total_price = BOMService.get_bom_total_price(data)  # Getting the total price
        print(f"BOM fetched from:{self.base_url}")  # Printing the source of BOM data
        print("=".ljust(item_width + price_width + 3, "="))  # Printing the header separator
        for item, price in data.items():  # Iterating through the items and prices
            print(f"|{str(item).ljust(item_width)}|{str(price).ljust(price_width)}|")  # Printing each item and price
        print("|" + "-".ljust(item_width, "-") + "|" + "-".ljust(price_width, "-") + "|")  # Printing the separator line
        print(f"|{str('Total Price').ljust(item_width)}|{str(total_price).ljust(price_width)}|")  # Printing the total price
        print("=".ljust(item_width + price_width + 3, "="))  # Printing the footer separator

if __name__ == "__main__":
    URL = "http://160.85.252.148/"  # URL of the BOM service
    bom1 = BOMService(URL)  # Creating an instance of BOMService
    bom1.get_bom_data()  # Fetching and processing the BOM data
