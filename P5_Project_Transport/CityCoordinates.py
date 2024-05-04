import requests

class CityCoordinates:
    def __init__(self, city_name_country):
        self.city_name_country = city_name_country

    def get_coordinates(self):
        url = f"https://nominatim.openstreetmap.org/search?q={self.city_name_country}&format=json"
        response = requests.get(url)
        data = response.json()
        if data:
            latitude = data[0]['lat']
            longitude = data[0]['lon']
            return latitude, longitude
        else:
            return None, None

    def get_city_coordinates(self):
        coordinates = self.get_coordinates()
        if coordinates:
            return coordinates
        else:
            return None, None

if __name__ == "__main__":
    city = input("City:")
    city_coordinates = CityCoordinates(city)
    print(city_coordinates.get_city_coordinates())