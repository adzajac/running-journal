from datetime import datetime
from random import random, choice
from app import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

follower = db.Table(
    'follower',
    db.Column('user_id', db.Integer, db.ForeignKey('user.user_id')),
    db.Column('followed_id', db.Integer, db.ForeignKey('user.user_id'))
)


class User(UserMixin, db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), index=True, unique=True)
    password = db.Column(db.String(128))
    salt = db.Column(db.String(10))
    email = db.Column(db.String(128), index=True, unique=True)
    # relationships
    posts = db.relationship('Post', backref='author', lazy='dynamic')
    likes = db.relationship('Like', backref='author', lazy='dynamic')
    runs = db.relationship('Run', backref='author', lazy='dynamic')
    followed = db.relationship(
        'User', secondary=follower,
        primaryjoin=(follower.c.user_id == user_id),
        secondaryjoin=(follower.c.followed_id == user_id),
        backref=db.backref('followers', lazy='dynamic'), lazy='dynamic')
    
    def __init__(self, **kwargs):
        abc = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
        self.salt = ''.join([choice(abc) for _ in range(10)])
    
    def set_password(self, password):
        self.password = generate_password_hash(password+self.salt)
      
    def check_password(self, password):
        return check_password_hash(self.password, password+self.salt)
    
        
class Post(db.Model):
    post_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'))
    run_id = db.Column(db.Integer, db.ForeignKey('run.run_id'))
    text = db.Column(db.String(512))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    # relationships
    likes = db.relationship('Like', backref='post', lazy='dynamic')
    
    

class Run(db.Model):
    run_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'))
    distances = db.Column(db.String(100))
    times = db.Column(db.String(256))
    timestamp = db.Column(db.DateTime, index=True)
    

class Like(db.Model):
    like_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'))
    post_id = db.Column(db.Integer, db.ForeignKey('post.post_id'))
