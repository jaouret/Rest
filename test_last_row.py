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

inspector = inspect(engine)
inspector.get_columns('data2')

#stmt=text("""SELECT id FROM data2 ORDER BY id DESC LIMIT 1""")
stmt=text("""SELECT id FROM data2 WHERE id = (SELECT MAX(id) FROM data2)""")
result=engine.execute(stmt)
last_id = result.fetchone()
for lastID in last_id:
    print(lastID)
    _id=lastID
result.close()
print(_id)