from flask import Blueprint
from flask_restful import Api
from resources import UserList, UserUpdate, UserVerify
from views import login, logout, register


users_blueprint = Blueprint('users',__name__)


# Flask Restful API
users_api = Api(users_blueprint)




# REST API Component
users_api.add_resource(UserList,'')
users_api.add_resource(UserUpdate,'/<int:id>')
users_api.add_resource(UserVerify,'/verify')


# Views import
users_blueprint.add_url_rule('/login',view_func=login,methods=['POST','GET'])
users_blueprint.add_url_rule('/logout',view_func=logout,methods=['POST'])
users_blueprint.add_url_rule('/register',view_func=register,methods=['POST','GET'])
