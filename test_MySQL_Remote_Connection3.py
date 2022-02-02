import sys
import sqlalchemy
import pymysql
import sshtunnel
import time
from sqlalchemy import create_engine
from sqlalchemy import MetaData, Table, Column, Integer, Float, String, DateTime, ForeignKey
from sqlalchemy import inspect
from sqlalchemy.sql import text
from sqlalchemy import text
from datetime import datetime
#import board
#import adafruit_scd30

#i2c = board.I2C()   # uses board.SCL and board.SDA
#scd = adafruit_scd30.SCD30(i2c)

print (sqlalchemy.__version__)

# DEFINE THE DATABASE CREDENTIALS
user = 'fruni_javier'
password = 'Clay2836'
host = '127.0.0.1'
port = 3306
database = 'fruni_sensor'

tunnel = sshtunnel.SSHTunnelForwarder(
    ('server153.web-hosting.com',21098),
    ssh_username='fruni',
    ssh_password='cljgifjao63',
    remote_bind_address=('127.0.0.1',3306))

trace_logger = sshtunnel.create_logger(loglevel="TRACE")
tunnel.daemon_forward_servers = True
tunnel.start()
tunnel.check_tunnels()
print(tunnel.tunnel_is_up, flush=True)
print(tunnel.local_bind_port)
local_port = str(tunnel.local_bind_port)
print(local_port)

engine=create_engine('mysql+pymysql://fruni_javier:Clay2836@127.0.0.1:'+local_port+'/fruni_sensor')
connection=engine.connect()
print(engine)
print('ok')

metadata = MetaData(engine)

data2 = Table('data2', metadata, autoload=True)

print("Columnas de la Tabla data2 %s" %(data2.columns.keys()))
print(engine)

with engine.connect() as connection:
    result = connection.execute(text("SELECT * FROM data2"))
    for row in result:
        print(row)

inspector = inspect(engine)
inspector.get_columns('data2')

stmt=text("""SELECT id FROM data2 WHERE id = (SELECT MAX(id) FROM data2)""")
result=engine.execute(stmt)
last_id = result.fetchone()
for lastID in last_id:
    _id=lastID
result.close()
print(_id)

hay_datos = True

while True:
    # since the measurement interval is long (2+ seconds) we check for new data before reading
    # the values, to ensure current readings.
    if _id > 40:
        break
#    if scd.data_available:
    if hay_datos:
        print("Datos Disponibles...")
        _id = _id + 1
#        _co2 = scd.CO2
#        _temp = scd.temperature
#        _hum = scd.relative_humidity
        _co2 = 300.00
        _temp = 30.00
        _hum = 70.00
        _fecha = datetime.now()
        _datos=({"id":_id,"co2":300,"temp":30,"hum":70,"fecha":_fecha})
        print("Datos",_datos)
#        print("CO2:", scd.CO2, "PPM")
#        print("Temperatura:", scd.temperature, "grados C")
#        print("Humedad:", scd.relative_humidity, "%%Hr")
        print("Paso 1")
        print("Id",_id)
        print("CO2:", _co2, "PPM")
        print("Temperatura:", _temp, "grados C")
        print("Humedad:", _hum, "%%Hr")
        print("Fecha", _fecha)
        #ins=engine.execute("INSERT INTO 'fruni_sensor'.'data2' ('id','co2','temp','hum') VALUES ('1001','300','30','70')")
        #ins=engine.execute('INSERT INTO data2 (id,co2,temp,hum,fecha) VALUES (:id,:co2,:temp,:hum,:fecha)'\
        #                   , id=1001,co2=300,temp=30,hum=70,fecha=_fecha)
        #ins=engine.execute("INSERT INTO 'fruni_sensor'.'data2' ('id','co2','temp','hum') VALUES ('1001','300','30','70')")
        stmt = text("""INSERT INTO data2 (id,co2,temp,hum,fecha) VALUES (:id, :co2, :temp, :hum, :fecha)""")
        #ins = engine.execute("INSERT INTO data2 (id,co2,temp,hum,fecha) \
                     #VALUES (?,?,?,?,?);", (_id, _co2, _temp, _hum, _fecha))
        #id = my_conn.execute("INSERT INTO  `database_name`.`student` (`name` ,`class` ,`mark` ,`sex`) \
        #                  VALUES ('King1',  'Five',  '45',  'male')")
        print("Paso 2")
        print("str(stmt)")
        engine.execute(stmt,_datos)
#        print("params")
#        print(ins.compile().params)
#        ins.inserted_primary_key

    else:
        print("Esperando por datos del sensor...")
        print("Paso 3")

    time.sleep(2.5)

#print('Insertar fila')
#ins = data1.insert().values(
#    id="155",
#    co2="1090",
#    temp="15.66",
#    hum="77.89")
#print(str(ins))
#print(ins.compile().params)
#result = engine.execute(ins)
#result.inserted_primary_key
#print (data1.c.id)

#ejemplos
#connection = engine.connect()
# recommended
#ident = '5'
#cmd = 'select * from data1 where id > :group'
#resultado = connection.execute(text(cmd), group=ident)
#for row in resultado:
#    print(row)
# or - wee more difficult to interpret the command
#resultado = connection.execute( text('select * from data1 where id = :group'),
#                                group=ident)
#for row in resultado:
#    print(row)
# or - notice the requirement to quote '5'
#resultado = connection.execute(text("select * from data1 where id = '5'"))
#for row in resultado:
#    print(row)

# Adding engine.dispose() will close all hanging connections to database allowing the ssh tunnel to be closed.
engine.dispose()
tunnel.stop()
print('FIN')
sys.exit()

