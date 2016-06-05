from flask import Blueprint, render_template



blogs_blueprint = Blueprint('blogs',__name__)


@blogs_blueprint.route('')
def blogs():
    return render_template('blogs/blogs.html')
