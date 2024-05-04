import requests

class CityCoordinates:
    def __init__(self, city_name):
        self.city_name = city_name

    def get_coordinates(self):
        url = f"https://nominatim.openstreetmap.org/search?q={self.city_name}&format=json"
        try:
            response = requests.get(url)
            data = response.json()
            if data:
                latitude = data[0]['lat']
                longitude = data[0]['lon']
                return latitude, longitude
            else:
                return None, None
        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")
            return None, None
        except (KeyError, IndexError):
            print("Error: Unable to parse response data")
            return None, None

    def get_city_coordinates(self):
        coordinates = self.get_coordinates()
        return coordinates

if __name__ == "__main__":
    city = input("City:")
    city_coordinates = CityCoordinates(city)
    print(city_coordinates.get_city_coordinates())
