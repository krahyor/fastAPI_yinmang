import mongoengine as me 
import datetime 

class Employers(me.Document):
    first_name = me.StringField(required=True)
    last_name = me.StringField(required=True)
    width = me.IntField(required=True)
    height = me.IntField(required=True)
    birth_place = me.StringField(required=True)
    birth_date = me.DateField(default=datetime.datetime.now)
    create_date = me.DateField(
        required=True , default=datetime.datetime.now,auto_now=True
    )
    update_date = me.DateField(required=True , default=datetime.datetime.now, auto_now=True)
    meta = {"collection":"emplyers"}