import pandas as pd
from CityCoordinates import CityCoordinates

# Define your data
data = {
    "City": ['Altach', 'Altstaetten', 'Arbon', 'Au', 'Balzers', 'Basel', 'Bregenz', 'Buchs', 'Diepoldsau', 'Dornbirn', 'Eichberg', 'Feldkirch', 'Friedrichshafen', 'Gams', 'Haag', 'Heerbrugg', 'Koblach', 'Konstanz', 'Kreuzlingen', 'Kriessern', 'Kuessaberg', 'Lindau', 'Loerrach', 'Lustenau', 'Maeder', 'Montlingen', 'Mulhouse', 'Oberriet', 'Rankweil', 'Rheinfelden', 'Romanshorn', 'Rorschach', 'Rueti', 'Sankt-Ludwig', 'Sankt-Gallen', 'Sargans', 'Schaan', 'Schaffhausen', 'Sevelen', 'Singen', 'St.Margrethen', 'Ueberlingen', 'Vaduz', 'Waldshut-Tiengen', 'Weil-am-Rhein', 'Widnau', 'Mailand', 'Como', 'Pontarlier', 'Morteau'],
    "Country": ['Oesterreich', 'Schweiz', 'Schweiz', 'Schweiz', 'Liechtenstein', 'Schweiz', 'Oesterreich', 'Schweiz', 'Schweiz', 'Oesterreich', 'Schweiz', 'Oesterreich', 'Deutschland', 'Schweiz', 'Schweiz', 'Schweiz', 'Oesterreich', 'Deutschland', 'Schweiz', 'Schweiz', 'Deutschland', 'Deutschland', 'Deutschland', 'Oesterreich', 'Oesterreich', 'Schweiz', 'Frankreich', 'Schweiz', 'Oesterreich', 'Schweiz', 'Schweiz', 'Schweiz', 'Schweiz', 'Frankreich', 'Schweiz', 'Schweiz', 'Liechtenstein', 'Schweiz', 'Schweiz', 'Deutschland', 'Schweiz', 'Deutschland', 'Liechtenstein', 'Deutschland', 'Deutschland', 'Schweiz', 'Italien', 'Italien', 'Frankreich', 'Frankreich']
}
df = pd.DataFrame(data)

# Initialize columns for latitude and longitude
df['Latitude'] = None
df['Longitude'] = None

# Populate latitude and longitude using CityCoordinates class
for index, row in df.iterrows():
    city = row['City']
    country = row['Country']
    city_country = f"{city},{country}"
    coordinates = CityCoordinates(city_country).get_city_coordinates()
    if coordinates:
        df.loc[index, 'Latitude'] = coordinates[0]
        df.loc[index, 'Longitude'] = coordinates[1]

print(df)

