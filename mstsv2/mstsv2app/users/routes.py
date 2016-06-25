from flask import Blueprint
from flask_restful import Api
from resources import UserList, UserUpdate, UserVerify

from views import login, logout, register, verify_account, account_settings
from views import reauthenticate, delete_account, forgot_password


users_blueprint = Blueprint('users',__name__)


# Flask Restful API
users_api = Api(users_blueprint)




# REST API Component
users_api.add_resource(UserList,'')
users_api.add_resource(UserUpdate,'/<int:id>')
users_api.add_resource(UserVerify,'/verify')


# Views import

# Login and Logout
users_blueprint.add_url_rule('/login',view_func=login,methods=['POST','GET'])
users_blueprint.add_url_rule('/logout',view_func=logout,methods=['POST','GET'])
users_blueprint.add_url_rule('/reauthenticate',view_func=reauthenticate,methods=['POST','GET'])

# Registration
users_blueprint.add_url_rule('/register',view_func=register,methods=['POST','GET'])
users_blueprint.add_url_rule('/register/verify/<verification_code>',view_func=verify_account,methods=['GET'])

# Account Views
users_blueprint.add_url_rule('/account/settings',view_func=account_settings,methods=['GET','POST'])
users_blueprint.add_url_rule('/account/settings/delete',view_func=delete_account,methods=['POST'])
users_blueprint.add_url_rule('/acccount/password/recover',view_func=forgot_password,methods=['POST','GET'])
