import os
from config import db
from models import Data2

print(os.path)

# Data to initialize database with

DATOS = [

    {'id': '3', 'co2': '1090', 'temp': '14.56', 'hum':'77.67'},

    {'id': '4', 'co2': '1090', 'temp': '14.56', 'hum':'77.67'}

]


# Delete database file if it exists currently

if os.path.exists('datos.db'):

    os.remove('datos.db')


# Create the database

db.create_all()


# Iterate over the DATOS structure and populate the database

for data2 in DATOS:

    p = Data2(id=data2['id'], co2=data2['co2'], temp=data2['temp'], hum=data2['hum'])

    db.session.add(p)


db.session.commit()