from flask import Blueprint
from flask_restful import Api
from resources import ResourceList, ResourceUpdate
from resources import CategoryList, CategoryUpdate
from views import list_resources, add_resource, add_category, delete_resource
from views import delete_category

# Blueprint aids in creating a modular application. This blueprint can be
# imported and added to our main app so all of the resources and url rules
# listed in here can be used in the entire application.
# This allows for a modular design.
resources_blueprint = Blueprint('resources',__name__)

resource_api = Api(resources_blueprint)


# REST API Component
resource_api.add_resource(ResourceList,'/api')
resource_api.add_resource(ResourceUpdate,'/api/<int:id>')
resource_api.add_resource(CategoryList,'/api/categories')
resource_api.add_resource(CategoryUpdate,'/api/categories/<int:id>')

# Resource Template Views
resources_blueprint.add_url_rule('',view_func=list_resources)
resources_blueprint.add_url_rule('/add',view_func=add_resource,methods=['POST','GET'])
resources_blueprint.add_url_rule('/delete/<id>',view_func=delete_resource,methods=['POST','GET'])

# Category Template Views
resources_blueprint.add_url_rule('/category/add',view_func=add_category,methods=['POST','GET'])
resources_blueprint.add_url_rule('/category/delete/<id>',view_func=delete_category,methods=['POST','GET'])
