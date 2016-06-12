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
