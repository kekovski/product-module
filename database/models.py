from .db import db
from flask_bcrypt import generate_password_hash, check_password_hash

class Product(db.Document):
    name = db.StringField(required=True, unique=True)
    price = db.FloatField(required=True)
    quantity = db.IntField(required=True)
    added_by = db.ReferenceField('User')

    meta = {
        'collection': 'products'
    }

class User(db.Document):
    email = db.EmailField(required=True, unique=True)
    password = db.StringField(required=True, min_length=8)
    products = db.ListField(db.ReferenceField('Product', reverse_delete_rule=db.PULL))

    meta = {
        'collection': 'users'
    }

    def hash_password(self):
        self.password = generate_password_hash(self.password).decode('utf8')

    def check_password(self, password):
        return check_password_hash(self.password, password)

User.register_delete_rule(Product, 'added_by', db.CASCADE)