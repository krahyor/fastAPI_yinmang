import mongoengine as me 
import datetime 

class Students(me.Document):
    first_name = me.StringField(required=True)
    last_name = me.StringField(required=True)
    weight = me.IntField(required=True)
    height = me.IntField(required=True)
    create_date = me.DateField(
        required=True , default=datetime.datetime.now,auto_now=True
    )
    update_date = me.DateField(required=True , default=datetime.datetime.now, auto_now=True)
    meta = {"collection":"Students"}