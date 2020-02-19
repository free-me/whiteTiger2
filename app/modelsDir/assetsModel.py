import mongoengine

class zichan(mongoengine.Document):
    AssetsName = mongoengine.StringField(max_length=600)
    AssetsIP = mongoengine.StringField(max_length=16)
    NetMask = mongoengine.StringField(max_length=64)
    Gateway = mongoengine.StringField(max_length=64)
    OsVersion = mongoengine.StringField(max_length=64)
    DeveType = mongoengine.StringField(max_length=64)
    appName = mongoengine.StringField(max_length=64)
    ManageUser = mongoengine.StringField(max_length=64)
    Person = mongoengine.StringField(max_length=64)
    DateTime = mongoengine.StringField(max_length=10)
