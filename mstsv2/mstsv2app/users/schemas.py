from marshmallow_jsonapi import Schema, fields
from marshmallow.validate import Length



err_length_msg = "%s must be between 1 and 64 characters"



class UserSchema(Schema):
	id = fields.Integer(dump_only=True)

	email = fields.String(required=True,validate=[Length(min=1,max=64,
	error=err_length_msg%('Email'))])

	first_name = fields.String(required=True,validate=[Length(min=1,max=64,
	error=err_length_msg%('First name'))])

	last_name = fields.String(required=True, validate=[Length(min=1,max=64,
	error=err_length_msg%('Last Name'))])

	password = fields.String(load_only=True, validate=[Length(min=1,max=64,
	error=err_length_msg%('Password'))])

	role_id = fields.Integer(required=True)
	password_hash = fields.String(dump_only=True)

	class Meta:
		type_ = "user"
		strict = True


class UserVerifySchema(Schema):
	id = fields.Integer(required=False)
	email = fields.String(load_only=True)
	password = fields.String(load_only=True)
	result = fields.Bool(dump_only=True)
	class Meta:
		type_ = "userverify"
		strict = True
