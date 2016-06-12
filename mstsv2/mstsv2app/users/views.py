from flask import render_template
from flask_login import login_user,logout_user, login_required, current_user
from forms import LoginForm, RegistrationForm

def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user,form.remember_me.data)
            return redirect(request.args.get('next') or url_for('main.index'))

        flash('Invalid username or password.')
    return render_template('users/login.html',form=form)

@login_required
def logout():
    logout_user()
    flash('You have been logged out.')
    return redirect(url_for('main.homepage'))


def register():
    form = RegistrationForm()
    if current_user.is_authenticated:
        return redirect(url_for('homepage'))

    if form.validate_on_submit():
        user = User(email=form.email.data,password=form.password.data)
        db.session.add(user)
        flash('Successful registration. You may now login')
        return redirect(url_for('users.login'))
    return render_template('users/register.html',form=form)