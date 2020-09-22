import mongoengine


class Product(mongoengine.Document):
    name = mongoengine.StringField(required=True, unique=True)
    price = mongoengine.FloatField(required=True)
    quantity = mongoengine.IntField(required=True)

    meta = {
        'db_alias': 'core',
        'collection': 'products'
    }
