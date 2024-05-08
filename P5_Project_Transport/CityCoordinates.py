import requests


def get_coordinates(city_name, country_name):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                             '(KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'}
    url = f"https://nominatim.openstreetmap.org/search?city={city_name}&country={country_name}&format=json"
    response = requests.get(url, headers=headers)
    if response.status_code == 200 and response.content:
        data = response.json()
        if data:
            latitude = float(data[0]['lat'])
            longitude = float(data[0]['lon'])
            return latitude, longitude
    return None


if __name__ == "__main__":
    country = "Balzers"
    city = "Schweiz"
    print(get_coordinates(city, country))
