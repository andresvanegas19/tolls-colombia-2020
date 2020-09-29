#!/usr/bin/env bash
curl https://www.ani.gov.co/sites/default/files/publicacion_23-03-2020.xlsx -o ani-peajes-2020.xlsx
curl https://api-tolls.herokuapp.com/tolls -o service.json
curl https://opendata.arcgis.com/datasets/659b88cc326a4251aca01b4f33a870c6_1.csv?outSR=%7B%22wkid%22%3A102100%2C%22latestWkid%22%3A3857%7D -o hermes-2020.csv

python3 clean-data.py

rm -f ani-peajes-2020.xlsx hermes-2020.csv

python3 upload-files.py
node change-direction.js

rm -f ani.json hermes.json service.json
