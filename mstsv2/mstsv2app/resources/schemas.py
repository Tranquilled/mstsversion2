'''
Similar to your forms, your schemas validate data coming in. They also can be
used to validate outgoing data and are particularly useful in ensuring
that your REST API provides a consistent presentation of the data.

'''

from marshmallow_jsonapi import Schema, fields

class ResourceSchema(Schema):
	id = fields.Integer(dump_only=True)
	category = fields.Integer(required=True)
	title = fields.Str(required=True)
	url = fields.Url(relative=False, required=True)
	description = fields.Str(required=True)
	class Meta:
		type_="resource"
		strict = True

class CategorySchema(Schema):
	id = fields.Integer(dump_only= True)
	name = fields.Str()

	class Meta:
		type_="category"
		strict = True
