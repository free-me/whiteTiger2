import mongoengine #导入包

class users(mongoengine.Document):
    userName = mongoengine.StringField(required=True,max_length=200)
    userID = mongoengine.IntField(default=1000)
    email = mongoengine.StringField(required=True,max_length=200)
    passWord = mongoengine.StringField(max_length=200)
    date = mongoengine.DateField()
