from sqlalchemy import create_engine
engine = create_engine('sqlite:///datos_sensor_02.db', echo = True)

from sqlalchemy import create_engine, MetaData, Table, Column, Integer, Float, String
engine = create_engine('sqlite:///datos_sensor_02.db', echo = True)
meta = MetaData()

