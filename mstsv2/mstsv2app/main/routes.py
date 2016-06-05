from flask import Blueprint, render_template
main_blueprint = Blueprint("main",__name__)


@main_blueprint.route('/')
def homepage():
	return render_template('index.html')

@main_blueprint.route('/missionstatement')
def mission_statement():
	return render_template('mission_statement.html',mission_statement=mission_statement)


@main_blueprint.route('/resources')
def resources():
	return render_template('resources.html')
