import mongoengine

class appinfo(mongoengine.Document):
    appName = mongoengine.StringField(required=True, max_length=200)
    appAdd = mongoengine.StringField(required=True, max_length=200)
    portNum = mongoengine.IntField(default=80)
    path = mongoengine.StringField(required=True, max_length=500)
    passWord = mongoengine.StringField(max_length=200)
    date = mongoengine.DateField()
