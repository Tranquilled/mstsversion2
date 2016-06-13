'''
The following module implements a REST API for resources. This allows
us to manipulate our database using simple HTTP requests and without
having to go through a form. This may be useful in the future if we
are looking to have a mobile app or add an analytics application that is
separate from the main site.

The basic structure of the REST API for one particular table is as follows:

ResourcesList(self):
	- GET -> Get all Resources
	- POST - > Create a Resource
ResourcesUpdate
	- PUT -> Modify a Resource
	- DELETE -> Delete a Resource

There implementations are below. Schemas from the schema file are used
to filter data. Models are used to interact with the database.

'''



from flask_restful import Resource as RESTResource
from flask import request, make_response, jsonify
from models import Resource, Category
from schemas import ResourceSchema, CategorySchema
from sqlalchemy.exc import SQLAlchemyError
from marshmallow import ValidationError
from marshmallow_jsonapi.exceptions import IncorrectTypeError
from mstsv2app.db import db


# Initializing an instance of the schema to use for filtering incoming and outgoing
# data of the API
academic_resource_schema = ResourceSchema()
category_schema = CategorySchema()



class ResourceList(RESTResource):
	def get(self):
		query = Resource.query.all()
		return academic_resource_schema.dump(query,many=True).data

	def post(self):
		request_dict = request.get_json(force=True)
		try:
			# parsing JSON Request
			academic_resource_schema.validate(request_dict)
			attributes = request_dict['data']['attributes']


			# saving into database
			academic_resource = Resource(title = attributes['title'],
										 category = attributes['category'],
										 description = attributes['description'],
										 url = attributes['url'])

			db.session.add(academic_resource)
			db.session.commit()

			# getting the resource that was just saved and filtering it to ensure consistency
			resource = Resource.query.get(academic_resource.id)
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

class ResourceUpdate(RESTResource):
	def get(self,id):
		resource = Resource.query.get_or_404(id)
		return academic_resource_schema.dump(resource).data

	def put(self,id):
		request_dict = request.get_json(force=True)
		try:
			academic_resource_schema.validate(request_dict)
			attributes = request_dict['data']['attributes']
			academic_resource = Resource.query.get_or_404(id)
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
			academic_resource = Resource.query.get_or_404(id)
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


class CategoryList(RESTResource):
	def get(self):
		query = Category.query.all()
		return category_schema.dump(query,many=True).data

	def post(self):
		request_dict = request.get_json(force=True)
		try:
			category_schema.validate(request_dict)
			attributes = request_dict['data']['attributes']
			category = Category(name = attributes['name'])
			db.session.add(category)
			db.session.commit()
			category = Category.query.get(category.id)
			result = category_schema.dump(category).data
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

class CategoryUpdate(RESTResource):
	def get(self,id):
		resource = Category.query.get_or_404(id)
		return category_schema.dump(resource).data

	def put(self,id):
		request_dict = request.get_json(force=True)
		try:
			category_schema.validate(request_dict)
			attributes = request_dict['data']['attributes']
			category = Category.query.get_or_404(id)
			for key,value in attributes.iteritems():
				setattr(category,key,value)

			db.session.add(category)
			db.session.commit()
			return category_schema.dump(category).data, 200

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
			category = Category.query.get_or_404(id)
			db.session.delete(category)
			db.session.commit()
			resp = make_response()
			resp.status_code = 204
			return resp

		except SQLAlchemyError as e:
			db.session.rollback()
			errors = {"error":str(e)}
			resp.status_code = 400
			return resp
