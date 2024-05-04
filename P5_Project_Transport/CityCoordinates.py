import requests


def get_coordinates(city_name, country_name):
    url = f"https://nominatim.openstreetmap.org/search?city={city_name}&country={country_name}&format=json"
    response = requests.get(url)
    if response.status_code == 200 and response.content:
        data = response.json()
        if data:
            latitude = data[0]['lat']
            longitude = data[0]['lon']
            return latitude, longitude
    return None


if __name__ == "__main__":
    country = "Österreich"
    city = "Wien"
    print(get_coordinates(city, country))