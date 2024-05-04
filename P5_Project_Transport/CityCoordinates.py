import requests

class CityCoordinates:
    def __init__(self, city_name):
        self.city_name = city_name.split(',')[0].strip()
        self.country_name = city_name.split(',')[-1].strip()

    def get_coordinates(self):
        url = f"https://nominatim.openstreetmap.org/search?city={self.city_name}&country={self.country_name}&format=json"
        response = requests.get(url)
        if response.status_code == 200 and response.content:
            data = response.json()
            if data:
                latitude = data[0]['lat']
                longitude = data[0]['lon']
                return latitude, longitude
        return None

    def get_city_coordinates(self):
        coordinates = self.get_coordinates()
        if coordinates:
            return coordinates
        else:
            return None

if __name__ == "__main__":
    city = input("City,Country:").lower()
    city_coordinates = CityCoordinates(city)
    print(city_coordinates.get_city_coordinates())
