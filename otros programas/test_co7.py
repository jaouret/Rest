from datetime import datetime
from config import db, ma


#db = SQLAlchemy()

class Data2(db.Model):
    __tablename__ = 'data2'
    id = db.Column(db.Integer,primary_key=True)
    co2 = db.Column(db.Float)
    temp = db.Column(db.Float)
    hum = db.Column(db.Float)    
    timestamp = db.Column(db.DateTime, 
                          default=datetime.utcnow, 
                          onupdate=datetime.utcnow)

class Data3Schema(ma.SQLAlchemyAutoSchema):
      class Meta:
            model = Data2
            load_instance = True

class Data2Schema(ma.ModelSchema):
    class Meta:
        model = Data2
        sqla_session = db.session


