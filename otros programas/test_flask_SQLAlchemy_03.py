from datetime import datetime
import time
import board
import adafruit_scd30

from sqlalchemy import create_engine
engine = create_engine('sqlite:///datos_sensor_01.db', echo = True)
connection=engine.connect()

from sqlalchemy import create_engine, insert, select, MetaData, Table, Column, Integer, Float, String, DateTime
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
#descending = Object.query.order_by(Object.id.desc())
#last_item = descending.first() 

i2c = board.I2C()   # uses board.SCL and board.SDA
scd = adafruit_scd30.SCD30(i2c)
#_id=177

_cont=0

print("Paso 0")
s = select([tabla03])
rp = connection.execute("SELECT max(id) from tabla03")
una_fila=rp.fetchone()
una_fila=una_fila[0]
_id=una_fila
print("una fila")
print(una_fila)

while _cont < 2:
    # since the measurement interval is long (2+ seconds) we check for new data before reading
    # the values, to ensure current readings.
    if scd.data_available:
        _id=_id+1
        _cont=_cont+1
        _co2=scd.CO2
        _temp=scd.temperature
        _hum=scd.relative_humidity
        
        print("Data Available!")
        print("CO2:", scd.CO2, "PPM")
        print("Temperature:", scd.temperature, "degrees C")
        print("Humidity:", scd.relative_humidity, "%%rH")
        print("")
        print("Waiting for new data...")
        print("")
        #ins = tabla03.insert().values(
            #id=_id,
            #co2=_co2,
            #temp=_temp,
            #hum=_hum)
        ins = insert(tabla03).values(
            id=_id,
            co2=_co2,
            temp=_temp,
            hum=_hum)
        _fecha=datetime.now
        _id=_id+1
        result2 = connection.execute("INSERT INTO tabla03 (id,co2,temp,hum,fecha) \
                 VALUES (?,?,?,?,?);",(_id,_co2,_temp,_hum,datetime.now()))
        print("Paso 1")
        print("str(ins)")
        print(str(ins))
        print("params")
        print(ins.compile().params)
        
        result = connection.execute(ins)
        result.inserted_primary_key

    time.sleep(0.5)
    
print("Paso2")
s = select([tabla03])
rp = connection.execute(s)
results = rp.fetchall()
print (results)
print(rp.lastrowid)
