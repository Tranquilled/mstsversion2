from flask_restful import Resource
from flask import request, make_response, jsonify
from flask_login import login_required
from models import User
from schemas import UserSchema, UserVerifySchema
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm.exc import NoResultFound, MultipleResultsFound
from marshmallow import ValidationError
from marshmallow_jsonapi.exceptions import IncorrectTypeError
from mstsv2app.db import db



user_schema = UserSchema()
user_verify_schema = UserVerifySchema()

class UserList(Resource):
	@login_required
	def get(self):
		query = User.query.all()
		return user_schema.dump(query,many=True).data

	@login_required
	def post(self):
		request_dict = request.get_json(force=True)
		try:
			user_schema.validate(request_dict)
			attributes = request_dict['data']['attributes']

			user = User(
                        email = attributes['email'],
						verified = False,
						first_name = attributes['first_name'],
						last_name = attributes['last_name'],
						password_hash = attributes['password'],
						role_id = attributes['role_id']
						)

			db.session.add(user)
			db.session.commit()

			resource = User.query.get(user.id)
			result = user_schema.dump(user).data
			return result, 201

		except SQLAlchemyError as e:
			db.session.rollback()
			errors = {"error":str(e)}
			resp = make_response(jsonify(errors))
			resp.status_code = 400
			return resp

		except ValidationError as e:
			errors = {"error":str(e)}
			resp = make_response(jsonify(errors))
			resp.status_code = 400
			return resp

		except IncorrectTypeError as e:
			errors = {"error":str(e)}
			resp = make_response(jsonify(errors))
			resp.status_Code = 400
			return resp

class UserUpdate(Resource):

	@login_required
	def get(self,id):
		resource = User.query.get_or_404(id)
		return user_schema.dump(resource).data

	@login_required
	def put(self,id):
		request_dict = request.get_json(force=True)
		try:
			user_schema.validate(request_dict)
			attributes = request_dict['data']['attributes']
			user = User.query.get_or_404(id)
			for key,value in attributes.iteritems():
				setattr(user,key,value)

			db.session.add(user)
			db.session.commit()
			return user_schema.dump(user).data, 200

		except SQLAlchemyError as e:
			db.session.rollback()
			errors = {"error":str(e)}
			resp = make_response(jsonify(errors))
			resp.status_code = 400
			return resp

		except ValidationError as e:
			errors = {"error":str(e)}
			resp = make_response(jsonify(errors))
			resp.status_code = 400
			return resp

		except IncorrectTypeError as e:
			errors = {"error":str(e)}
			resp = make_response(jsonify(errors))
			resp.status_Code = 400
			return resp

	@login_required
	def delete(self,id):
		try:
			user = User.query.get_or_404(id)
			db.session.delete(user)
			db.session.commit()
			resp = make_response()
			resp.status_code = 204
			return resp

		except SQLAlchemyError as e:
			db.session.rollback()
			errors = {"error":str(e)}
			resp.status_code = 400
			return resp

class UserVerify(Resource):
	@login_required
	def post(self):
		request_dict = request.get_json(force=True)
		try:
			user_verify_schema.validate(request_dict)
			attributes = request_dict['data']['attributes']
			user = User.query.filter(email=attributes['email']).one()
			result = self.user.verify_password(attributes['password'])
			result = { 'data': {
                         'type': 'userverify',
                         'attributes': {
                                    'result':result
                                     }
                          }
                     }
			return user_verify_schema.dump(result).data , 200
		except NoResultFound as e:
			errors={"error":"User with that email does not exist"}
			resp = make_response(jsonify(errors))
			resp.status_code = 400
			return resp

		except MultipleResultsFound as e:
			errors={"error":"Multiple Users were returned"}
			resp = make_response(jsonify(errors))
			resp.status_code = 400
			return resp
		except SQLAlchemyError as e:
			db.session.rollback()
			errors = {"error":str(e)}
			resp = make_response(jsonify(errors))
			resp.status_code = 400
			return resp

		except ValidationError as e:
			errors = {"error":str(e)}
			resp = make_response(jsonify(errors))
			resp.status_code = 400
			return resp

		except IncorrectTypeError as e:
			errors = {"error":str(e)}
			resp = make_response(jsonify(errors))
			resp.status_Code = 400
			return resp
