from CityCoordinates import get_coordinates
from dataclasses import dataclass
import math



@dataclass
class Calculator:
    __start_city: list = None
    __destination_city: list = None
    __start_city_coordinates: tuple = None
    __destination_city_coordinates: tuple = None

    def __post_init__(self):
        if self.__start_city:
            coordinates = get_coordinates(self.__start_city[0], self.__start_city[1])
            if coordinates:
                self.__start_city_coordinates = tuple(coordinates)

        if self.__destination_city:
            coordinates = get_coordinates(self.__destination_city[0], self.__destination_city[1])
            if coordinates:
                self.__destination_city_coordinates = tuple(coordinates)

    def set_start_city(self, start_city, start_country):
        self.__start_city = [start_city, start_country]

    def get_start_city(self):
        return self.__start_city

    def set_destination_city(self, destination_city, destination_country):
        self.__destination_city = [destination_city, destination_country]

    def get_destination_city(self):
        return self.__destination_city

    def get_distance(self):
        # haversine distance calculator

        lat1 = self.__start_city_coordinates[0]
        lat2 = self.__destination_city_coordinates[0]
        lon1 = self.__start_city_coordinates[1]
        lon2 = self.__destination_city_coordinates[1]

        # Convert decimal degrees to radians
        lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])

        # Haversine formula
        dlon = lon2 - lon1
        dlat = lat2 - lat1
        a = math.sin(dlat / 2) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2) ** 2
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
        radius = 6371  # Radius of Earth in kilometers

        return c * radius


if __name__ == "__main__":
    calculator = Calculator()
    calculator.set_start_city("Männedorf", "Switzerland")
    print(calculator.get_start_city())
    calculator.set_destination_city("Meilen", "Switzerland")
    print(calculator.get_destination_city())
    print(get_coordinates("Männedorf", "Switzerland"))
    print(calculator.get_distance())
