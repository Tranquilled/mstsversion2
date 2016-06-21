from flask import render_template, flash, request,redirect, url_for
from flask_login import login_user,logout_user, login_required, current_user
from flask_mail import Message
from mstsv2app.mail import mail
from sqlalchemy.orm.exc import NoResultFound, MultipleResultsFound
from models import User, TYPES, db
from forms import LoginForm, RegistrationForm
import random
import string
import socket

def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is not None and user.verify_password(form.password.data):
            if user.verified:
                login_user(user,remember=form.remember_me.data)
                return redirect(request.args.get('next') or url_for('main.homepage'))
            else:
                flash('Please verify your email address before logging in.','alert-danger')
        else:
            flash('Invalid username or password.','alert-danger')

    return render_template('users/login.html',form=form)

@login_required
def logout():
    logout_user()
    flash('You have been logged out.')
    return redirect(url_for('main.homepage'))


def register():
    form = RegistrationForm(request.form)
    if form.validate_on_submit():
        verification_code = ''.join([ random.choice(
                                string.ascii_uppercase +
                                string.ascii_lowercase +
                                string.digits) for _ in range(1,48) ])
        user = User(email=form.email.data,
                    verified=False,
                    verification_code = verification_code,
                    password=form.password.data,
                    role = TYPES[0][0]) # Get the User Type by Default
        db.session.add(user)
        db.session.commit()

        msg = Message('Welcome to MSTS',
                      sender="from@example.com",
                      recipients=[form.email.data],
                      )
        msg.html = render_template('users/registration_email.html',
                                    verification_code = verification_code)
        try:
            mail.send(msg)
        except socket.error as e:
            print("Message not successfully sent")

        flash('Successful registration. Please validate your email before logging in.')
        return redirect(url_for('users.login'))
    return render_template('users/register.html',form=form)


def verify_account(verification_code):
    try:
        user = User.query.filter_by(verification_code=verification_code).one()
        user.verified = True
        db.session.add(user)
        db.session.commit()

    except NoResultFound:
        return redirect(url_for('main.homepage'))

    except MultipleResultsFound:
        return redirect(url_for('main.homepage'))

    flash("Thank you for verifying your account, you may now login.")
    return redirect(url_for('users.login'))
