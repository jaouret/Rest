import sys
import sqlalchemy
import pymysql
import sshtunnel
from sqlalchemy import create_engine
from sqlalchemy import MetaData, Table, Column, Integer, Float, String, DateTime, ForeignKey
from sqlalchemy import inspect
from sqlalchemy.sql import text
from sqlalchemy import text
from datetime import datetime

print (sqlalchemy.__version__)

# DEFINE THE DATABASE CREDENTIALS
user = 'fruni_javier'
password = 'Clay2836'
host = '127.0.0.1'
port = 3306
database = 'fruni_sensor'
print('FIN')

tunnel = sshtunnel.SSHTunnelForwarder(
    ('server153.web-hosting.com',21098),
    ssh_username='fruni',
    ssh_password='cljgifjao63',
    remote_bind_address=('127.0.0.1',3306))

trace_logger = sshtunnel.create_logger(loglevel="TRACE")


#     remote_bind_address=('68.65.123.205',3306)
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

data1 = Table('data1', metadata, autoload=True)

#inspector = inspect(engine)
#inspector.get_columns('book')
print("Columnas de la Tabla data1 %s" %(data1.columns.keys()))
print(engine)


with engine.connect() as connection:
    result = connection.execute(text("SELECT * FROM data1"))
    for row in result:
        print (row)

#use session
#result = session.execute(sqlalchemy.text("SELECT * FROM ..."))
#session.execute(sqlalchemy.text("SELECT * FROM a_table WHERE a_column = :val"),{'val': 5})
# https: // docs.sqlalchemy.org / en / latest / core / connections.html
# connectionless-execution-implicit-execution

connection = engine.connect()

# recommended
ident = '5'
cmd = 'select * from data1 where id > :group'
resultado = connection.execute(text(cmd), group=ident)
for row in resultado:
    print(row)

# or - wee more difficult to interpret the command
resultado = connection.execute( text('select * from data1 where id = :group'),
                                group=ident)
for row in resultado:
    print(row)

# or - notice the requirement to quote '5'
resultado = connection.execute(text("select * from data1 where id = '5'"))
for row in resultado:
    print(row)



engine.dispose()
tunnel.stop()
print('FIN')
sys.exit()

