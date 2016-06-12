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
