import pandas as pd
from CityCoordinates import CityCoordinates

# Define your data
data = {
    "City": ['Altach', 'Altstätten', 'Arbon', 'Au', 'Balzers', 'Basel', 'Bregenz', 'Buchs', 'Diepoldsau', 'Dornbirn', 'Eichberg', 'Feldkirch', 'Friedrichshafen', 'Gams', 'Haag', 'Heerbrugg', 'Koblach', 'Konstanz', 'Kreuzlingen', 'Kriessern', 'Küssaberg', 'Lindau', 'Lörrach', 'Lustenau', 'Mäder', 'Montlingen', 'Mulhouse', 'Oberriet', 'Rankweil', 'Rheinfelden', 'Romanshorn', 'Rorschach', 'Rüthi', 'Rüthi', 'Sankt-Ludwig', 'Sankt-Gallen', 'Sargans', 'Schaan', 'Schaffhausen', 'Sevelen', 'Singen', 'St.Margrethen', 'Überlingen', 'Vaduz', 'Waldshut-Tiengen', 'Weil-am-Rhein', 'Widnau', 'Mailand', 'Como'],
    "Country": ['Österreich', 'Schweiz', 'Schweiz', 'Schweiz', 'Liechtenstein', 'Schweiz', 'Österreich', 'Schweiz', 'Schweiz', 'Österreich', 'Schweiz', 'Österreich', 'Deutschland', 'Schweiz', 'Schweiz', 'Schweiz', 'Österreich', 'Deutschland', 'Schweiz', 'Schweiz', 'Deutschland', 'Deutschland', 'Deutschland', 'Österreich', 'Österreich', 'Schweiz', 'Frankreich', 'Schweiz', 'Österreich', 'Schweiz', 'Schweiz', 'Schweiz', 'Schweiz', 'Liechtenstein', 'Frankreich', 'Schweiz', 'Schweiz', 'Liechtenstein', 'Schweiz', 'Schweiz', 'Deutschland', 'Schweiz', 'Deutschland', 'Liechtenstein', 'Deutschland', 'Deutschland', 'Schweiz', 'Italien', 'Italien']
}
df = pd.DataFrame(data)

# Initialize columns for latitude and longitude
df['Latitude'] = None
df['Longitude'] = None

# Populate latitude and longitude using CityCoordinates class
for index, row in df.iterrows():
    city = row['City']
    country = row['Country']
    city_country = f"{city}-{country}"
    coordinates = CityCoordinates(city_country).get_city_coordinates()
    df.loc[index, 'Latitude'] = coordinates[0]
    df.loc[index, 'Longitude'] = coordinates[1]

print(df)
