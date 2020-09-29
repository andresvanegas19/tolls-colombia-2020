#!/usr/bin/env python3

import pandas as pd
import requests

r = requests.get('https://api-tolls.herokuapp.com/tolls')

data = {'name': [],
	'_id': [],
	'lat': [],
	'lng': [],
  'direction': []}

df_marks = pd.DataFrame(data)

for i in r.json()['data']['tolls']:
    new_row = {
        'name': i['name'],
	    '_id': i['_id'],
	    'lat': i['coordenates']['lat'],
	    'lng': i['coordenates']['lng'],
        'direction': i['direction']
    }
    df_marks = df_marks.append(new_row, ignore_index=True)

df_marks.to_csv('../finally/tolls-2020-colombia.xlsx')
