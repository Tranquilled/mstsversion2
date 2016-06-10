from mstsv2app.db import db
from sqlalchemy_utils.types import URLType

class AcademicResource(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String,nullable=False)
	url = db.Column(URLType)
