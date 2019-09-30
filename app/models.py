from datetime import datetime
from random import random, choice
from app.extensions import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


follower = db.Table(
    'follower',
    db.Column('id', db.Integer, db.ForeignKey('user.id')),
    db.Column('followed_id', db.Integer, db.ForeignKey('user.id'))
)


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), index=True, unique=True)
    password = db.Column(db.String(128))
    salt = db.Column(db.String(10))
    email = db.Column(db.String(128), index=True, unique=True)
    # relationships
    posts = db.relationship('Post', backref='author', lazy='dynamic')
    injuries = db.relationship('Injury', backref='author', lazy='dynamic')
    likes = db.relationship('Like', backref='author', lazy='dynamic')
    runs = db.relationship('Run', backref='author', lazy='dynamic')
    followed = db.relationship(
        'User', secondary=follower,
        primaryjoin=(follower.c.id == id),
        secondaryjoin=(follower.c.followed_id == id),
        backref=db.backref('followers', lazy='dynamic'), lazy='dynamic')

    def set_password(self, password):
        abc = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
        self.salt = ''.join([choice(abc) for _ in range(10)])
        self.password = generate_password_hash(password+self.salt)
      
    def check_password(self, password):
        return check_password_hash(self.password, password+self.salt)
    
    def is_following(self, user):
        return self.followed.filter(follower.c.followed_id == user.id).count() > 0
    
    def follow(self, user):
        if not self.is_following(user):
            self.followed.append(user)
     
        
class Post(db.Model):
    post_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    run_id = db.Column(db.Integer, db.ForeignKey('run.run_id'))
    text = db.Column(db.String(512))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    # relationships
    likes = db.relationship('Like', backref='post', lazy='dynamic')
    
    
class Injury(db.Model):
    injury_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    text = db.Column(db.String(40))
    description = db.Column(db.String(512))
    timestamp = db.Column(db.DateTime, index=True)
    

class Run(db.Model):
    run_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    distances = db.Column(db.String(100))
    times = db.Column(db.String(256))
    timestamp = db.Column(db.DateTime, index=True)
    

class Like(db.Model):
    like_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    post_id = db.Column(db.Integer, db.ForeignKey('post.post_id'))
