from marshmallow_jsonapi import Schema, fields

class AcademicResourceSchema(Schema):
	id = fields.Integer(dump_only=True)
	category = fields.Integer()
	title = fields.Str()
	url = fields.Url(relative=False)
	class Meta:
		type_="resource"
		strict = True

class ResourceCategorySchema(Schema):
	id = fields.Integer(dump_only= True)
	name = fields.Str()

	class Meta:
		type_="resource"
		strict = True
