import pandas as pd
from CityCoordinates import get_coordinates

def create_cities_dataframe():
    """
    Create a pandas DataFrame with cities and their corresponding countries, and populate the latitude and longitude columns using the get_coordinates function from the CityCoordinates module.

    Returns:
        pandas.DataFrame: A DataFrame containing columns for City, Country, Latitude, and Longitude.
    """
    # Define your data
    data = {
        "City": ['Altach', 'Altstätten', 'Arbon', 'Au', 'Balzers', 'Basel', 'Bregenz', 'Buchs', 'Diepoldsau', 'Dornbirn', 'Eichberg', 'Feldkirch', 'Friedrichshafen', 'Gams', 'Haag', 'Heerbrugg', 'Koblach', 'Konstanz', 'Kreuzlingen', 'Kriessern', 'Küssaberg', 'Lindau', 'Lörrach', 'Lustenau', 'Mäder', 'Montlingen', 'Mulhouse', 'Oberriet', 'Rankweil', 'Rheinfelden', 'Romanshorn', 'Rorschach', 'Rüthi', 'Sankt-Ludwig', 'Sankt-Gallen', 'Sargans', 'Schaan', 'Schaffhausen', 'Sevelen', 'Singen', 'St.Margrethen', 'Überlingen', 'Waldshut-Tiengen', 'Weil-am-Rhein', 'Widnau', 'Mailand', 'Como', 'Genf', 'Lausanne', 'Sion', 'Biel'],
        "Country": ['Österreich', 'Schweiz', 'Schweiz', 'Schweiz', 'Liechtenstein', 'Schweiz', 'Österreich', 'Schweiz', 'Schweiz', 'Österreich', 'Österreich', 'Österreich', 'Deutschland', 'Schweiz', 'Schweiz', 'Schweiz', 'Österreich', 'Deutschland', 'Schweiz', 'Schweiz', 'Deutschland', 'Deutschland', 'Deutschland', 'Österreich', 'Österreich', 'Schweiz', 'Frankreich', 'Schweiz', 'Österreich', 'Schweiz', 'Schweiz', 'Schweiz', 'Schweiz', 'Frankreich', 'Schweiz', 'Schweiz', 'Liechtenstein', 'Schweiz', 'Schweiz', 'Deutschland', 'Schweiz', 'Deutschland', 'Deutschland', 'Deutschland', 'Schweiz', 'Italien', 'Italien', 'Schweiz', 'Schweiz', 'Schweiz', 'Schweiz']
    }
    df = pd.DataFrame(data)

    # Initialize columns for latitude and longitude
    df['Latitude'] = None
    df['Longitude'] = None

    # Populate latitude and longitude using CityCoordinates class
    for index, row in df.iterrows():
        city = row['City']
        country = row['Country']
        coordinates = get_coordinates(city, country)
        print(coordinates)
        if coordinates:
            df.loc[index, 'Latitude'] = coordinates[0]
            df.loc[index, 'Longitude'] = coordinates[1]

    return df

if __name__ == "__main__":
    df = create_cities_dataframe()
    print(df)
    df.to_csv("cities.csv", sep=',', index=False, encoding='utf-8')