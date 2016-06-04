from flask import Flask
from flask_restful import Api
from db import db

# importing blueprint objects




# Starts flask application
app = Flask(__name__)
app.config.from_object('settings')


# Initializes Flask SQLAlchemy
db.init_app(app)
db.app = app
db.create_all()


# Uses Blueprint to import different modules
