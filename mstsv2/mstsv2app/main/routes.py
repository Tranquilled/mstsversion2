from flask import Blueprint, render_template

main_blueprint = Blueprint("main",__name__)

@main_blueprint.route('')
def homepage():
	return render_template('index.html')

@main_blueprint.route('mission')
def mission_statement():
	return render_template('mission_statement.html')
