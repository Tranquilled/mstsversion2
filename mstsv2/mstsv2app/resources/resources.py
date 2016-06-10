from flask_restful import Resource
from flask import request, make_response, jsonify
from models import AcademicResource
from schemas import AcademicResourceSchema
from sqlalchemy.exc import SQLAlchemyError
from marshmallow import ValidationError
from marshmallow_jsonapi.exceptions import IncorrectTypeError
from mstsv2app.db import db



academic_resource_schema = AcademicResourceSchema()

class AcademicResourceList(Resource):
	def get(self):
		query = AcademicResource.query.all()
		return academic_resource_schema.dump(query,many=True).data

	def post(self):
		request_dict = request.get_json(force=True)
		try:
			academic_resource_schema.validate(request_dict)
			attributes = request_dict['data']['attributes']

			academic_resource = AcademicResource(title = attributes['title'],
												 category = attributes['category'],
												 description = attributes['description'],
												 url = attributes['url'])
			db.session.add(academic_resource)
			db.session.commit()

			resource = AcademicResource.query.get(academic_resource.id)
			print(resource)
			result = academic_resource_schema.dump(resource).data
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

class AcademicResourceUpdate(Resource):
	def get(self,id):
		resource = AcademicResource.query.get_or_404(id)
		return academic_resource_schema.dump(resource).data

	def put(self,id):
		request_dict = request.get_json(force=True)
		try:
			academic_resource_schema.validate(request_dict)
			attributes = request_dict['data']['attributes']
			academic_resource = AcademicResource.query.get_or_404(id)
			for key,value in attributes.iteritems():
				setattr(academic_resource,key,value)

			db.session.add(academic_resource)
			db.session.commit()
			return academic_resource_schema.dump(academic_resource).data, 200

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

	def delete(self,id):
		try:
			academic_resource = AcademicResource.query.get_or_404(id)
			db.session.delete(academic_resource)
			db.session.commit()
			resp = make_response()
			resp.status_code = 204
			return resp
			
		except SQLAlchemyError as e:
			db.session.rollback()
			errors = {"error":str(e)}
			resp.status_code = 400
			return resp
