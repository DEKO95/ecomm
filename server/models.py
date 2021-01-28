import datetime
import os

from werkzeug.security import generate_password_hash, check_password_hash
from flask import url_for

from server import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(128), unique=True)
    hash_password = db.Column(db.String(256), nullable=False)
    orders = db.relationship('Order', backref=db.backref('user', lazy='joined'), lazy='dynamic')
    reviews = db.relationship('Review', backref=db.backref('user', lazy='joined'), lazy='dynamic')
    
    def set_password(self, password):
        self.hash_password = generate_password_hash(password + os.environ['PASSWORD_SALT'])

    def check_password(self, password):
        return check_password_hash(self.hash_password, password)

    

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(128), unique=True)
    price = db.Column(db.Numeric(precision=4, asdecimal=False, decimal_return_scale=None))
    description = db.Column(db.Text)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)
    is_available = db.Column(db.Boolean, default=True)
    # main_picture = db.Column(db.Integer, db.ForeignKey('item_picture.id'), nullable=True)
    pictures = db.relationship('ItemPicture', backref=db.backref('item', lazy='joined'), lazy='dynamic')
    
    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "price": self.price,
            "description": self.description,
            "is_available": self.is_available,
            "category_id": self.category_id, # or send category title?
            "pictures": [
                url_for('api.picture_endpoint', id=pic.id) for pic in self.pictures.all()
            ]
        }

# should we make many-to-many instead?
class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(128), unique=True)
    description = db.Column(db.Text)
    items = db.relationship('Item', backref=db.backref('category', lazy='joined'), lazy='dynamic')


class ItemPicture(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    item_id = db.Column(db.Integer, db.ForeignKey('item.id'), nullable=False)
    filename = db.Column(db.String(128), unique=True)
    file = db.Column(db.LargeBinary, nullable=False)


class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    item_id = db.Column(db.Integer, db.ForeignKey('item.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    parent_id = db.Column(db.Integer, db.ForeignKey('review.id'), nullable=True)
    rating = db.Column(db.Float, nullable=True)
    # (?) оценка отзыва другими пользователями


# table for many-to-many connections
order_items = db.Table('order_items',
    db.Column('order_id', db.Integer, db.ForeignKey('order.id'), nullable=False),
    db.Column('item_id' ,db.Integer, db.ForeignKey('item.id'), nullable=False),
    db.Column('price', db.Numeric(precision=4, asdecimal=False, decimal_return_scale=None)),
    db.Column('quantity' ,db.Integer, nullable=False, default=1),
    db.Column('parameters' ,db.LargeBinary, nullable=True) # json like {'size':'L','color':'red'}
)


class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    status = db.Column(db.Integer)
    # TODO: use actual timezone instead of UTC
    date = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    items = db.relationship('Item', secondary=order_items,
        backref=db.backref('orders', lazy='dynamic'))