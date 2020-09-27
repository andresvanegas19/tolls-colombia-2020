#!/usr/bin/env python3

import pandas as pd
import unidecode

def clean_data_ani(file):
    result = {
        'TARIFAS 2020 EN LAS ESTACIONES DE PEAJES BAJO SUPERVISIÓN DE LA ANI': 'NOMBRE DEL PROYECTO VIAL',
        'Unnamed: 2': 'NOMBRE DEL CONCESIONARIO',
        'Unnamed: 3': 'DEPARTAMENTO',
        'Unnamed: 4': 'MUNICIPIO',
        'Unnamed: 5': 'FECHA ACTUAL',
        'Unnamed: 6': 'ESTACION DE PEAJE'
    }
    data = pd.read_excel(file)
    values = data.iloc[3].values[7:-1]

    for i in range(len(values)):
        result['Unnamed: ' + str(i + 7)] = values[i]

    return data.drop(['Unnamed: 0', 'Unnamed: 32'], axis=1)[4:105] \
        .rename(columns=result) \
        .fillna(method='ffill') \
        .reset_index() \
        .drop(['index'], axis=1)


def clean_data_hermes(file):
    data = pd.read_csv(file)
    new_data = data[[
        'X',
        "Y",
        'territoria',
        'administra',
        'nombre',
        'sentido',
        'cat_1',
        'cat_2',
        'cat_3',
        'cat_4',
        'cat_5',
        'cat_6',
        'cat_7',
        'cat_8',
        'cat_9',
        'cat_ie_10',
        'cat_iee',
        'cat_ieee',
        'cat_iia',
        'cat_eae',
        'cat_ec',
        'cat_e',
        'cat_ie',
        'cat_iie',
        'cat_iiie',
        'cat_ive',
        'cat_ve',
        'cat_vie',
        'cat_viie',
        'eje_adicional',
        'eje_adicional_r'
    ]].fillna(0)

    return new_data.rename(columns={
        'territoria': 'DEPARTAMENTO',
        'cat_1': 'I',
        'cat_2': 'II',
        'cat_3': "III",
        'cat_4': "IV",
        'cat_5': "V",
        'cat_6': "VI",
        'cat_7': "VII",
        'cat_8': "VIII",
        'cat_9': "IX",
        'cat_ie_10': "IE-10",
        'cat_iee': "IEE",
        'cat_ieee': "IEEE",
        'cat_iia': "IIA",
        'cat_eae': "EAE",
        'cat_ec': "EC",
        'cat_e': "E",
        'cat_ie': "IE",
        'cat_iie': "IIE",
        'cat_iiie': "IIIE",
        'cat_ive': "IVE",
        'cat_ve': "VE",
        'cat_vie': "VIE",
        'cat_viie': "VIIE",
        'eje_adicional': 'E.A.',
        'eje_adicional_r': 'E.A.R.'
    })


def remove_accents(a):
    if (type(a) == int):
        a = ''
    return unidecode.unidecode(a)

def clean_accents(data, columns):
    for column in columns:
        data[column] = data[column].apply(remove_accents)
    return data

file_hermes = "hermes-2020.csv"
file_ani = 'ani-peajes-2020.xlsx'

clean_accents(
    clean_data_ani(file_ani), [
    'NOMBRE DEL CONCESIONARIO',
    'DEPARTAMENTO',
    'MUNICIPIO',
    'ESTACION DE PEAJE'

]).to_json('ani.json')


clean_accents(
    clean_data_hermes(file_hermes),
    [
        'nombre',
        'sentido',
        'DEPARTAMENTO'
    ]
).to_json('hermes.json')
