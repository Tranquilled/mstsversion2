######### Introduction ###################

# Flask Tutorial for illustrating:
#	- Serving static files and templates
#	- Interacting with variables in a view function.
#	- Jinja Tutorial


############  Step 1: Installation ####################
# First step is to setup you virtual environment using pip and install Flask.
# The BASH commands for this are:
# 	pip install virtualenv
# 	virtualenv venv
# 	source venv/bin/activate
# 	pip install Flask

# Step 2: Initializing the Flask Application

# The second step is initializing a Flask App. This is done by
# creating an app.The next line here initializes your flask 
# web application

from flask import Flask
app = Flask(__name__)



# Step 3: Simple Hello World
# After this step you can run the code and go to
# http://127.0.0.1:5000
# and you should get a page returning the string
# below
@app.route('/')
def hello_world():
	return "Hello World!"

# Step 4: Rendering HTML Pages
# This step shows you how to render a html page. By default
# flask will search for the templates file which should be
# in the same folder as your app.py file.
# If you go to this page you should see an index file with some text
# in it. The index file can be found in templates, index.html
from flask import render_template

# Go to the page: http://127.0.0.1:5000/homepage
@app.route('/homepage')
def homepage():
	return render_template('index.html')
	
# Step 5: Rendering with Variables
# Sometimes you may want to render your template
# with some variables from the backend. This tutorial shows 
# you how to do that. Check out index_with_vars to see how to
# load the variable into a template
# go to the page: http://127.0.0.1:5000/homepagevars
@app.route('/homepagevars')
def homepagevars():
	bob = 'bob'

	return render_template('index_vars.html',bob=bob,my_name=my_name)

# Step 6: Referencing Static files (CSS and Javascript)
# Go to this file to see an example of loading static files (css, javascript and images) into a template)
@app.route('/static_files')
def static_files():
	return render_template('static_vars.html')


# Step 7: Jinja Tutorial
# This tutorial will show you the basics of jinja and give you a link for further learning :)
@app.route('/jinja_tutorial')
def jinja_tutorial():
	favorite_foods = ['spaghetti','tomatoes','celery','fries']
	
	jinja_doc_url = 'http://jinja.pocoo.org/docs/dev/templates/'
	
	flask_doc_url = 'http://flask.pocoo.org/docs/0.11/'

	tutorial = 'https://realpython.com/blog/python/primer-on-jinja-templating/'

	flask_is_fun = True

	montreal_is_warm = False


	return render_template('jinja_tutorial.html',favorite_foods = favorite_foods,
												 flask_fun = flask_is_fun, 
												 montreal_is_warm = montreal_is_warm, 
												 jinja_doc_url = jinja_doc_url, 
												 flask_doc_url=flask_doc_url,
												 tutorial=tutorial)







# NOTE: This will only run if you call python app.py. Otherwise it will not run and this file will skip starting the 
# actual flask application
if __name__ == '__main__':
	# if set to false you won't see the result of you errors
	app.run(debug=True)

