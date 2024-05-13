import pandas as pd
import os

data = {
    'Country': ['Italien', 'Deutschland', 'Spanien', 'Frankreich', 'England', 'Österreich', 'Holand', 'Belgien', 'Brüssel'],
    'Website': ['https://www.trenitalia.com/de.html', 'https://www.bahn.de/', 'https://www.thetrainline.com/de/bahnunternehmen/renfe', 'https://www.sncf-connect.com/de-de/ter', 'https://www.nationalrail.co.uk/', 'https://fahrplan.oebb.at/webapp/#!P|TP!H|683087', 'https://www.ns.nl/en/', 'https://www.belgiantrain.be/de', 'https://www.belgiantrain.be/de']
}

df = pd.DataFrame(data)
current_dir = os.getcwd()
filename = os.path.join(current_dir, 'countrytrainmapping.csv')
df.to_csv(filename, index=False, encoding='utf-8')



