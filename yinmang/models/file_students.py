import mongoengine as me 
import datetime 

class Files(me.Document):
    file = me.FileField()
    file_name = me.StringField()
    status = me.StringField(default="failed")
    create_date = me.DateField(
        required=True , default=datetime.datetime.now,auto_now=True
    )
    update_date = me.DateField(required=True , default=datetime.datetime.now, auto_now=True)
    meta = {"collection":"File"}