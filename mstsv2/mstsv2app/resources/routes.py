from flask import Blueprint
from flask_restful import Api
from resources import ResourceList, ResourceUpdate
from resources import CategoryList, CategoryUpdate
from views import list_resources


resources_blueprint = Blueprint('resources',__name__)

resource_api = Api(resources_blueprint)


# REST API Component
resource_api.add_resource(ResourceList,'')
resource_api.add_resource(ResourceUpdate,'/<int:id>')
resource_api.add_resource(CategoryList,'/categories')
resource_api.add_resource(CategoryUpdate,'/categories/<int:id>')


# Template Views
resources_blueprint.add_url_rule('/list/',view_func=list_resources)
