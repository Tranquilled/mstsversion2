from db import db
from flask import Flask
import os.path

# Uses Blueprints to import different modules
from blogs.routes import blogs_blueprint
from main.routes import main_blueprint
from resources.routes import resources_blueprint

def create_app():
    app = Flask(__name__)
    app = Flask(__name__)
    app.config.from_object('settings')
    db.init_app(app)

    app.register_blueprint(main_blueprint,url_prefix='/')
    app.register_blueprint(blogs_blueprint,url_prefix='/blogs')
    app.register_blueprint(resources_blueprint,url_prefix='/resources')
    return app

def db_setup(app):
    with app.app_context():
        db.create_all()

app = create_app()

db_setup(app)
