'''
Here you can store your WTForms classes which will be used in your views
to generate and validate form data.
'''
from flask_wtf import Form
from wtforms import StringField, SelectField, SubmitField
from wtforms.validators import Length, InputRequired, URL
from wtforms import ValidationError
from models import db, Category

class ResourceForm(Form):
    title = StringField('Title',validators=[Length(1,128),InputRequired()])
    category = SelectField('Category',validators=[InputRequired()],coerce=int)
    description = StringField('Description',validators=[Length(0,500)])
    url = StringField('URL',validators=[Length(0,500),URL()])
    submit = SubmitField('Save')
    def validate_url(self, field):
        '''
        Must be able to resolve the link (through ICMP protocol(ping))
        This prevents someone from giving a URL that doesn't resolve from the
        site. Be car
        '''
        pass

class CategoryForm(Form):
    name = StringField('Name',validators=[Length(1,80),InputRequired()])
    submit = SubmitField('Save')

    def validate_name(self,field):
        category_names = [category.name for category in db.session.query(Category).all()]
        if field.data in category_names:
            raise ValidationError('Category already exists')
