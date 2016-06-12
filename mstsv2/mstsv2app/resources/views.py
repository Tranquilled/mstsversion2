from models import Resource, Category
from flask import render_template, jsonify

def list_resources():
    categories = Category.query.all()

    categories_display = { category.id:{"category":category.name,"resources":[]}
                         for category in categories}

    academic_resources = Resource.query.all()

    for academic_resource in academic_resources:
        categories_display[academic_resource.category]["resources"].append(
            {
                "title":academic_resource.title,
                "url":academic_resource.url,
                "description":academic_resource.description
            })


    return render_template('resources/resource_list.html',resources_by_category=categories_display)
