from flask import render_template, flash, request,redirect, url_for
from flask_login import login_user,logout_user, login_required, current_user
from models import User, TYPES, db
from forms import LoginForm, RegistrationForm

def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user,form.remember_me.data)
            return redirect(request.args.get('next') or url_for('main.homepage'))

        flash('Invalid username or password.')
    return render_template('users/login.html',form=form)

@login_required
def logout():
    logout_user()
    flash('You have been logged out.')
    return redirect(url_for('main.homepage'))


def register():
    form = RegistrationForm(request.form)

    if form.validate_on_submit():
        user = User(email=form.email.data,
                    verified=False,
                    password=form.password.data,
                    role = TYPES[0][0]) # Get the User Type by Default
        db.session.add(user)
        db.session.commit()
        flash('Successful registration. Please validate your email before logging in.')
        return redirect(url_for('users.login'))

    return render_template('users/register.html',form=form)
