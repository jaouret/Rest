from datetime import datetime
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, Float, String, DateTime

engine = create_engine('sqlite:///datos_sensor_01.db', echo = True)
meta = MetaData()


tabla03 = Table(
   'tabla03', meta,
   Column('id', Integer, primary_key = True), 
   Column('co2', Float),
   Column('temp', Float),
   Column('hum', Float),
   Column('fecha', DateTime(), default=datetime.now)
)
meta.create_all(engine)
print("Columnas de la Tabla tabla03 %s" %(tabla03.columns.keys()))
print(engine)

ins = tabla03.insert().values(
    id="155",
    co2="1090",
    temp="15.66",
    hum="77.89")
print(str(ins))
print(ins.compile().params)

result = engine.execute(ins)
result.inserted_primary_key
print (tabla03.c.id)
