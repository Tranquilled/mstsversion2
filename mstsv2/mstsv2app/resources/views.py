from models import Resource, Category
from flask import render_template, jsonify

def list_resources():


    # getting all of the categories
    categories = Category.query.all()

    # organizing the categories into a dictionary with the category name and
    # a list of the resources for that particular category

    categories_display = { category.id:{"category":category.name,"resources":[]}
                         for category in categories}


    # getting all of the academic resources and sorting them into a dictionary
    # so the attributes can be easily presented in the Jinja template. 
    academic_resources = Resource.query.all()

    for academic_resource in academic_resources:
        categories_display[academic_resource.category]["resources"].append(
            {
                "title":academic_resource.title,
                "url":academic_resource.url,
                "description":academic_resource.description
            })


    return render_template('resources/resource_list.html',resources_by_category=categories_display)
