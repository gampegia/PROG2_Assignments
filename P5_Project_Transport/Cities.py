
import pandas as pd
import requests
from CityCoordinates import CityCoordinates

# Ihre Daten
data = {
    'City': ['Altach', 'Altstätten', 'Arbon', 'Au', 'Balzers', 'Basel', 'Bregenz', 'Buchs', 'Diepoldsau', 'Dornbirn', 'Eichberg', 'Feldkirch', 'Friedrichshafen', 'Gams', 'Haag', 'Heerbrugg', 'Koblach', 'Konstanz', 'Kreuzlingen', 'Kriessern', 'Küssaberg', 'Lindau', 'Lörrach', 'Lustenau', 'Mäder', 'Montlingen', 'Mulhouse', 'Oberriet', 'Rankweil', 'Rheinfelden', 'Romanshorn', 'Rorschach', 'Rüthi', 'Rüthi', 'Saint-Louis', 'SanktGallen', 'Sargans', 'Schaan', 'Schaffhausen', 'Sevelen', 'Singen', 'St.Margrethen', 'Überlingen', 'Vaduz', 'Waldshut-Tiengen', 'WeilamRhein', 'Widnau', 'Mailand', 'Como'],
    'Country': ['Österreich', 'Schweiz', 'Schweiz', 'Schweiz', 'Liechtenstein', 'Schweiz', 'Österreich', 'Schweiz', 'Schweiz', 'Österreich', 'Schweiz', 'Österreich', 'Deutschland', 'Schweiz', 'Schweiz', 'Schweiz', 'Österreich', 'Deutschland', 'Schweiz', 'Schweiz', 'Deutschland', 'Deutschland', 'Deutschland', 'Österreich', 'Österreich', 'Schweiz', 'Frankreich', 'Schweiz', 'Österreich', 'Schweiz', 'Schweiz', 'Schweiz', 'Schweiz', 'Liechtenstein', 'Frankreich', 'Schweiz', 'Schweiz', 'Liechtenstein', 'Schweiz', 'Schweiz', 'Deutschland', 'Schweiz', 'Deutschland', 'Liechtenstein', 'Deutschland', 'Deutschland', 'Schweiz', 'Italien', 'Italien']
}
df = pd.DataFrame(data)

df['Latitude'], df['Longitude'] = zip(*df['City'].apply(lambda city: CityCoordinates(city).get_city_coordinates()))

print(df)
