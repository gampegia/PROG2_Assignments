import pandas as pd
import os

data = {
    'Country': ['italy', 'germany', 'spain', 'france', 'england', 'austria', 'niederland', 'belgien', 'brüssel'],
    'Website': ['https://www.trenitalia.com/de.html', 'https://www.bahn.de/', 'https://www.renfe.com/es/en', 'https://www.sncf-connect.com/de-de/ter', 'https://www.nationalrail.co.uk/', 'https://fahrplan.oebb.at/webapp/#!P|TP!H|683087', 'https://www.ns.nl/en/', 'https://www.belgiantrain.be/de', 'https://www.belgiantrain.be/de']
}

df = pd.DataFrame(data)
current_dir = os.getcwd()
filename = os.path.join(current_dir, 'countrytrainmapping.csv')
df.to_csv(filename, index=False, encoding='utf-8')



