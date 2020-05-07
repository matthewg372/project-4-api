from peewee import *

from flask_login import UserMixin
import datetime


DATABASE = SqliteDatabase('profiles.sqlite')

class User(UserMixin, Model):
	username=CharField(unique=True)
	email=CharField(unique=True)
	password=CharField()
	class Meta:
		database = DATABASE

class Profile(Model):
	user=ForeignKeyField(User, backref='profiles')
	images=TextField()
	first_name=CharField()
	last_name=CharField()
	days_sober=IntegerField()
	date_of_birth=IntegerField()
	sponsor=BooleanField()
	date=DateTimeField(default=datetime.datetime.now)
	class Meta:
		database = DATABASE

class ToDoItem(Model):
	user=ForeignKeyField(User, backref='ToDoItem')
	item=CharField()
	class Meta:
		database = DATABASE

class Friendship(Model):
	user1=ForeignKeyField(User, backref='friends')
	user2=ForeignKeyField(User, backref='friends')
	class Meta:
		database = DATABASE

class Post(Model):
	user=ForeignKeyField(User, backref='posts')
	bio=CharField()
	date=DateTimeField(default=datetime.datetime.now)
	class Meta:
		database = DATABASE

class Comment(Model):
	user=ForeignKeyField(User, backref='comments')
	post=ForeignKeyField(Post, backref='comments')
	bio=CharField()
	class Meta:
		database = DATABASE

def initialize():
	DATABASE.connect()
	DATABASE.create_tables([User, Profile, ToDoItem, Friendship, Post, Comment], safe=True)
	print('connected to models and tables')
	DATABASE.close()