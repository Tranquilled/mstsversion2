
from models import AcademicResource
from flask import render_template, jsonify

def list():
    academic_resources = AcademicResource.query.all()
    resources = [ {'title':academic_resource.title,'url':academic_resource.url } for academic_resource in academic_resources]
    return render_template('resources/resource_list.html',resources=resources)
