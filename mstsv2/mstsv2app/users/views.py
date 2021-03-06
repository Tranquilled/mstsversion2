from flask import render_template, flash, request,redirect, url_for
from flask_login import login_user,logout_user, login_required, current_user, fresh_login_required
from flask_mail import Message
from mstsv2app.mail import mail
from mstsv2app.tools.error_reporting import flash_errors
from sqlalchemy.orm.exc import NoResultFound, MultipleResultsFound
from models import User, TYPES, db
from forms import LoginForm, RegistrationForm, SettingsForm, ForgotPasswordForm
import random
import string
import socket

def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.homepage'))
    form = LoginForm(request.form)
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

def reauthenticate():
    form = LoginForm(request.form)
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
    if current_user.is_authenticated:
        return redirect(url_for('main.homepage'))
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

@login_required
@fresh_login_required
def account_settings():
    form = SettingsForm(request.form)
    if form.validate_on_submit():
        current_user.email = form.email.data
        if form.password.data:
            current_user.password = form.password.data

        flash("Settings Updated")

        db.session.add(current_user)
        db.session.commit()

    form.email.data = current_user.email

    flash_errors(form)
    return render_template('users/account_settings.html',form =form)

@login_required
@fresh_login_required
def delete_account():
    user_id = current_user.id
    user = User.query.get(user_id)
    logout_user()
    db.session.delete(user)
    db.session.commit()
    flash("Account Successfully deleted. We hope to see you again soon!")

    # may have to refactor and send an email when an account gets deleted

    return redirect(url_for("main.homepage"))


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

def forgot_password():
    form = ForgotPasswordForm(request.form)
    if form.validate_on_submit():
        # generating a random token to send to the user email
        user_email = form.email.data
        try:
            print("here")
            user = User.query.filter_by(email=user_email).one()
            verification_code = verification_code = ''.join([ random.choice(
                                    string.ascii_uppercase +
                                    string.ascii_lowercase +
                                    string.digits) for _ in range(1,48) ])


            msg = Message('MSTS Password Reset',
                              sender="from@example.com",
                              recipients=[user_email],
                              )
            msg.html = render_template('users/forgot_password_email.html',verification_code = verification_code)
            try:
                mail.send(msg)
            except socket.error as e:
                print("Message not successfully sent")

        except MultipleResultsFound as e:
            pass
        except NoResultFound as e:
            pass


        flash("If this email address has a registered account, we have sent an email with instructions on how to recover your account.","alert-success")
    print(form.errors)
    return render_template('users/forgot_password.html',form=form)
