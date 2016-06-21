from db import db
from login import login_manager
from flask import Flask
from mail import mail
import os.path

# Uses Blueprints to import different modules
from blogs.routes import blogs_blueprint
from main.routes import main_blueprint
from resources.routes import resources_blueprint
from users.routes import users_blueprint

def create_app():
    app = Flask(__name__)
    app.config.from_object('settings')

    # Creating the mail object to manage emails in flask
    mail.init_app(app)



    # initializing the database lazily
    db.init_app(app)

    # registering the different modules in the application
    app.register_blueprint(blogs_blueprint,url_prefix='/blogs')
    app.register_blueprint(main_blueprint,url_prefix='/')
    app.register_blueprint(resources_blueprint,url_prefix='/resources')
    app.register_blueprint(users_blueprint,url_prefix='/users')

    # initializing the login manager lazily
    login_manager.init_app(app)

    return app

def db_setup(app):
    with app.app_context():
        db.create_all()

app = create_app()

# Flask Login
login_manager.init_app(app)

db_setup(app)
