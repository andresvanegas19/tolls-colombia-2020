#!/usr/bin/env python3

import requests

# recursos
ani_tolls_2019 = 'https://www.invias.gov.co/index.php/archivo-y-documentos/cnsc/tarifa-peajes/8558-tarifas-de-peaje-a-cargo-del-invias-2019/file'
ani_tolls = 'https://www.ani.gov.co/sites/default/files/publicacion_23-03-2020.xlsx'
estadistics = 'https://opendata.arcgis.com/datasets/659b88cc326a4251aca01b4f33a870c6_1.csv?outSR=%7B%22wkid%22%3A102100%2C%22latestWkid%22%3A3857%7D'

def download_recurse(url, name):
    r = requests.get(url)
    with open(name, 'wb') as output:
        output.write(r.content)

# download_recurse(ani_tolls_2019, 'ani-peajes-2019.xls')
download_recurse(ani_tolls, 'ani-peajes-2020.xls')
download_recurse(estadistics, 'mapas-y-estadisticas-2020.csv')
