#!/usr/bin/env python3
import json
import unidecode
import requests

with open('hermes.json') as hermes:
    hermes_file = json.load(hermes)

with open('service.json') as scrape:
    scrape_file = json.load(scrape)

scrape_file = scrape_file['data']['tolls']
name_wrong = {
    '(Guarne) Copacabana*': 'GUARNE',
    'Vt. de Palmas':'VARIANTE LAS PALMAS',
    'Primavera':'VERSALLES (PRIMAVERA)',
    'Manga':'BAZURTO  (MANGA)',
    'Pavas - Trinidad I':'PAVAS (TRINIDAD I)',
    'San Bernardo - Trinidad II':'SAN BERNARDO (TRINIDAD ll)',
    'Villa Rica':'VILLARICA',
    'Los Garzones I':'LOS GARZONES 1',
    'Los Garzones II':'LOS GARZONES 2',
    'El Purgatorio':'PURGATORIO',
    'Boquerón II':'PUESTO DE CONTROL BOQUERON II',
    'Boquerón I':'EL BOQUERON I',
    'Caiquero':'CAIQUEROS',
    'Las Brisas':'BRISAS',
    'Naranjal':'PUENTE QUETAME (NARANJAL)',
    'Puente Laureano Gómez':'LAUREANO GOMEZ',
    'Puente Amarillo (Puesto de Control)':'PUENTE AMARILLO',
    'Daza (Solo cobro a Camiones)':'DAZA',
    'Cerritos 2':'CERRITOS II',
    'El Picacho':'PICACHO',
    'Curos':'LOS CUROS',
    'Rio Negro':'RIONEGRO',
    'Curití':'SAN GIL - CURITI',
    'La Caimanera':'CAIMANERA',
    'Cerrito':'EL CERRITO',
    'Toro':'EL TORO',
    'Araguaney': 'ARANGUANEY',
    'Neguanje': 'NENGUANJE',
    'Santágueda': 'SANT\'AGUEDA',
    'Ramal a Soacha':'RAMAL',
    'Gataquí': 'GUATAQUI'
}


def remove_accents(a):
    if (type(a) == int):
        a = ''
    return unidecode.unidecode(a)

def union(scrape_file):
    result={}
    for toll in scrape_file:
        result[str(toll['_id'])] = {}
        for number, hermes_tolls in hermes_file["nombre"].items():
            toll_service = remove_accents(toll['name']).replace('*', '').replace('?', '').lower()
            if toll_service == hermes_tolls.lower():
                result[toll['_id']]['name'] = toll_service
                result[toll['_id']]['direction'] = hermes_file['sentido'][number]
                result[toll['_id']]['department'] = hermes_file['DEPARTAMENTO'][number]
                result[toll['_id']]['toll_cost'] = {
                    "I": hermes_file['I'][number],
                    "II": hermes_file['II'][number],
                    "III": hermes_file['III'][number],
                    "IV": hermes_file['IV'][number],
                    "V": hermes_file['V'][number],
                    "VI": hermes_file['VI'][number],
                    "VII": hermes_file['VII'][number],
                    "VIII": hermes_file['VIII'][number],
                    "IX": hermes_file['IX'][number],
#                    "E": hermes_file['E'][number],
#                    "IE": hermes_file['IE'][number],
#                    "IIE": hermes_file['IIE'][number],
#                    "IIIE": hermes_file['IIIE'][number],
#                    "IVE": hermes_file['IVE'][number],
#                    "VE": hermes_file['VE'][number],
#                    "VIE": hermes_file['VIE'][number],
#                    "VIIE": hermes_file['VIIE'][number],
#                    "IEE": hermes_file['IEE'][number],
#                    "IEEE": hermes_file['IEEE'][number],
#                    "IIA": hermes_file['IIA'][number],
#                    "EAE": hermes_file['EAE'][number],
#                    "EC": hermes_file['EC'][number],
#                    "E.A.R.": hermes_file["E.A.R."][number],
#                    "E.A.": hermes_file["E.A."][number],
#                    "IE-10": hermes_file['IE-10'][number],
                }
    return result




for dictionary in scrape_file:
    if dictionary['name'] in name_wrong:
        dictionary['name'] = name_wrong[dictionary['name']]

for dictionary in scrape_file:
    if dictionary['name'] in name_wrong:
        dictionary['name'] = name_wrong[dictionary['name']]

for key, data in union(scrape_file).items():
    if data:
        url = 'https://api-tolls.herokuapp.com/tolls/{}'
        r = requests.patch(url.format(key), json=data)
        if r.status_code != 200:
            print(r.status_code)
        else:
            print(r.status_code)