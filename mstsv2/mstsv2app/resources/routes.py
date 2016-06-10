from flask import Blueprint
from flask_restful import Api
from resources import AcademicResourceList, AcademicResourceUpdate
from views import list


resources_blueprint = Blueprint('resources',__name__)

resource_api = Api(resources_blueprint)


# REST API Component
resource_api.add_resource(AcademicResourceList,'')
resource_api.add_resource(AcademicResourceUpdate,'/<int:id>')

# Template Views
resources_blueprint.add_url_rule('/list/',view_func=list)
