from peewee import * 
from datetime import datetime
from db import db 

class BaseModel(Model):
    
    class Meta:
        database = db

class User(BaseModel):
    id=PrimaryKeyField()
    username=CharField(unique=True)
    password_hash=CharField()
    caeates_at=DateTimeField(default=datetime.now)

    class Meta:
        table_name="users"

class Delivery(BaseModel):
    id=PrimaryKeyField()
    package_name=CharField()
    destination=CharField()
    weight=FloatField(constraints=[Check("weight>0")])
    status=CharField(default="waiting")
    owner=ForeignKeyField(User,backref="deliveries",column_name="owner_id")
    caeates_at=DateTimeField(default=datetime.now)
    class Meta:
        table_name="deliveries"


def creat_table():
    db.connect()
    db.create_tables([User,Delivery])
    db.close()

creat_table()