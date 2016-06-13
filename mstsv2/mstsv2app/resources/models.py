'''
The models is the interface to the database using the flask-sqlalchemy package
Columns in the database are translated below as attributes of a class and then
translated into tables by the Object-Relational Mapper.

The particular example below is a Resource. A resource is some link to a URL
that may be useful for someone to know about. Resources are organized into
categories so we might be having resources in the category of books, movies
or podcasts.

'''
from mstsv2app.db import db
from sqlalchemy_utils.types import URLType


class Category(db.Model):
	__tablename__ = 'resourcecategory'
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String,nullable=False)


class Resource(db.Model):
	__tablename__ = 'academicresource'
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String,nullable=False)
	category = db.Column(db.Integer,db.ForeignKey('resourcecategory.id'),nullable=False)
	description = db.Column(db.String,nullable=True)
	url = db.Column(URLType)
