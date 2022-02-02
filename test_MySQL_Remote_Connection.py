import sqlalchemy
import pymysql
import sshtunnel
from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey
from sqlalchemy import inspect
from sqlalchemy.sql import text

print (sqlalchemy.__version__)

tunnel = sshtunnel.SSHTunnelForwarder(
    ('server153.web-hosting.com',21098),
    ssh_username='fruni',
    ssh_password='cljgifjao63',
    remote_bind_address=('127.0.0.1',3306))


#     remote_bind_address=('68.65.123.205',3306)

tunnel.start()
tunnel.check_tunnels()
print(tunnel.tunnel_is_up, flush=True)
print(tunnel.local_bind_port)
local_port = str(tunnel.local_bind_port)
print(local_port)

engine=create_engine('mysql+pymysql://fruni_javier:Clay2836@127.0.0.1:'+local_port+'/fruni_sensor')
engine.connect()
print(engine)
print('ok')

metadata = MetaData()
books = Table('book', metadata,
  Column('id', Integer, primary_key=True),
  Column('title', String(16)),
)

metadata.create_all(engine)

#inspector = inspect(engine)
#inspector.get_columns('book')
with engine.connect() as con:

    data = ( { "id": 1, "title": "The Hobbit" },
             { "id": 2, "title": "The Silmarillion" },
    )

    statement = text("""INSERT INTO book(id, title) VALUES(:id, :title)""")

    for line in data:
        con.execute(statement, **line)

with engine.connect() as con:

    rs = con.execute('SELECT * FROM book')

    for row in rs:
        print (row)

# DEFINE THE DATABASE CREDENTIALS
user = 'fruni_javier'
password = 'Clay2836'
host = '127.0.0.1'
port = 3306
database = 'fruni_sensor'

tunnel.stop()

# PYTHON FUNCTION TO CONNECT TO THE MYSQL DATABASE AND
# RETURN THE SQLACHEMY ENGINE OBJECT
#def get_connection():
#    return create_engine(
#        url="mysql://{0}:{1}@{2}:{3}/{4}".format(
#            user, password, host, port, database
#        )
#    )

#if __name__ == '__main__':

#    try:

        # GET THE CONNECTION OBJECT (ENGINE) FOR THE DATABASE
#        engine = get_connection()
#        print(
#            f"Connection to the {host} for user {user} created successfully.")
#    except Exception as ex:
#        print("Connection could not be made due to the following error: \n", ex)
