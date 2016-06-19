from werkzeug.security import generate_password_hash, check_password_hash
from mstsv2app.db import db
from mstsv2app.login import login_manager
from flask_login import UserMixin
from sqlalchemy_utils import ChoiceType


TYPES = [
    ('User','User'),
    ('Admin','Admin'),
    ('SuperAdmin','SuperAdmin')
]


class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key=True)
    email = db.Column(db.String(150),unique=True,nullable=False)
    verified = db.Column(db.Boolean,nullable=False)
    verification_code = db.Column(db.String(150),unique=True)
    first_name = db.Column(db.String(150),nullable=True)
    last_name = db.Column(db.String(150),nullable=True)
    password_hash = db.Column(db.String(150),nullable=False)
    role = db.Column(ChoiceType(choices=TYPES))

    # the property decorator gives you a bunch of methods like
    # a setter, getter and deleter decorator.
    @property
    def password(self):
        raise AttributeError('cannot read the password')

    # will create the password hash when the password field is created
    # Default Values are:
    #    method = pbkdf2:sha1
    #    salt_length = 8

    @password.setter
    def password(self,password):
        self.password_hash = generate_password_hash(password)


    def verify_password(self,password):
        return check_password_hash(self.password_hash, password)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
