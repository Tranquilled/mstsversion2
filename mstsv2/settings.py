'''

Contains development settings for project

'''
from secret import SQLALCHEMY_DATABASE_URI 

DEBUG = True

HOST = '0.0.0.0'

PORT = 5000

SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_DATABASE_URI = SQLALCHEMY_DATABASE_URI

# change before production
WTF_CSRF_SECRET_KEY = 'aksdfasdfiqwpoerias;fialsdkfla;skdfl;askdlfasd'

SECRET_KEY = 'alskdfaskdfpaskdfl;aksdfopaksdfopawefaposdkfapsodkfasdf'



