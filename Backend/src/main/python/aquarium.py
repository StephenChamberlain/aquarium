from peewee import *

database = MySQLDatabase('aquarium', **{'passwd': 'steve', 'charset': 'utf8', 'user': 'steve', 'use_unicode': True})

class UnknownField(object):
    def __init__(self, *_, **__): pass

class BaseModel(Model):
    class Meta:
        database = database

class Aquarium(BaseModel):
    capacity = IntegerField(null=True)
    description = CharField(null=True)

    class Meta:
        table_name = 'aquarium'

class Occupant(BaseModel):
    aquarium = ForeignKeyField(column_name='aquarium_id', field='id', model=Aquarium)
    name = CharField(null=True)
    species = CharField(null=True)

    class Meta:
        table_name = 'occupant'

class SensorReading(BaseModel):
    aquarium = ForeignKeyField(column_name='aquarium_id', field='id', model=Aquarium)
    reading = CharField(null=True)
    reading_units = CharField(null=True)
    sensor_type = CharField()
    timestamp = DateTimeField()

    class Meta:
        table_name = 'sensor_reading'

