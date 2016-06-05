from flask import Blueprint, render_template

homepage_blueprint = Blueprint("homepage",templates='templates')


homepage_blueprint.route('/')
def homepage():
	return render_template('index.html') 
