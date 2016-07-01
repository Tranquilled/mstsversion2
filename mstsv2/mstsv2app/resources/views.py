from models import Resource, Category, db
from flask import render_template, jsonify, redirect,url_for, request, flash
from flask_login import current_user, login_required
from forms import ResourceForm, CategoryForm
import requests

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
                'id':academic_resource.id,
                "title":academic_resource.title,
                "url":academic_resource.url,
                "description":academic_resource.description
            })
    return render_template('resources/resource_list.html',resources_by_category=categories_display)

@login_required
def add_resource():
    # if not (current_user.is_admin() or current_user.is_superadmin()):
    #     return redirect(url_for('main.homepage'))

    form = ResourceForm(request.form)

    # Categories
    categories = Category.query.all()
    cat_choices = [ (category.id,category.name) for category in categories]
    form.category.choices = cat_choices

    if form.validate_on_submit():
        new_resource = Resource(title=form.title.data,
                                category=form.category.data,
                                description=form.description.data,
                                url=form.url.data)
        db.session.add(new_resource)
        db.session.commit()
        flash('Resource was successfully added.','alert-success')

    return render_template('resources/add_resource.html',form=form)

@login_required
def modify_resource(id):
    pass


@login_required
def delete_resource(id):
    # if not (current_user.is_admin() or current_user.is_superadmin()):
    #     return redirect(url_for('main.homepage'))
    try:
        resource = Resource.query.get_or_404(id)
        db.session.delete(resource)
        db.session.commit()
        flash('Resource successfully deleted','alert-success')
    except SQLAlchemyError as e:
        flash('Resource was not successfully deleted','alert-danger')
    return redirect(url_for('list_resources'))


@login_required
def add_category():
    # if not (current_user.is_admin() or current_user.is_superadmin()):
    #     return redirect(url_for('main.homepage'))

    form = CategoryForm(request.form)
    if form.validate_on_submit():
        new_category = Category(name=form.name.data)
        db.session.add(new_category)
        db.session.commit()
        flash('Category was successfully added','alert-success')

    return render_template('resources/add_category.html',form=form)

@login_required
def modify_category(id):
    # if not (current_user.is_admin() or current_user.is_superadmin()):
    #     return redirect(url_for('main.homepage'))
    pass
@login_required
def delete_category(id):
    # if not (current_user.is_admin() or current_user.is_superadmin()):
    #     return redirect(url_for('main.homepage'))

    try:
        category = Category.query.get_or_404(id)
        db.session.delete(category)
        db.session.commit()
        flash('Category Successfully deleted','alert-success')
    except SQLAlchemyError as e:
        flash('Category unsuccessfully deleted','alert-danger')
    return redirect(url_for('list_resources'))
