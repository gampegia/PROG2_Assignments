import CityCoordinates
from dataclasses import dataclass


@dataclass
class Calculator:
    __start_city: str = None
    __destination_city: str = None

    def set_start_city(self, start_city):
        self.__start_city = start_city

    def get_start_city(self):
        return self.__start_city

    def set_destination_city(self, destination_city):
        self.__destination_city = destination_city

    def get_destination_city(self):
        return self.__destination_city



if __name__ == "__main__":
    calculator = Calculator()
    calculator.set_start_city("Männedorf")
    print(calculator.get_start_city())
    calculator.set_destination_city("Meilen")
    print(calculator.get_destination_city())
    print(CityCoordinates.get_coordinates("Männedorf, Switerland"))



