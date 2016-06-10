from marshmallow_jsonapi import Schema, fields

class AcademicResourceSchema(Schema):
	id = fields.Integer(dump_only=True)
	title = fields.Str()
	url = fields.Url(relative=False)

	class Meta:
		type_="resource"
		strict = True
