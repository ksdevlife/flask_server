from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_required, login_user,logout_user, current_user

from root import db
from root.models import User
from root.users.forms import LoginForm, RegisterForm, UpdateForm

users = Blueprint('users', __name__)

@users.route('/register', methods=['GET', 'POST'])
def register_user():
    form = RegisterForm()
    if form.validate_on_submit():
        user = User(
            form.name.data,
            form.email.data,
            form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Thanks your registratioin!')
        return redirect(url_for('index'))
    return render_template('register_user.html', form=form)

@users.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        user.check_password(form.password.data)
        login_user(user) 
        flash('Logged In Successfully.')
        return redirect(url_for('index'))
    return render_template('login.html', form=form)

@users.route('/logout')
def logout():
    logout_user()
    flash('Logged Out Successfully.')
    return redirect(url_for('index'))
    
@users.route('/account', methods=['GET', 'POST'])
@login_required
def update_profile():
    form = UpdateForm()
    if form.validate_on_submit():
        flash(form.name.data)
        current_user.name = form.name.data
        current_user.email = form.email.data
        db.session.commit()
        flash('Updated User Profile')
        return redirect(url_for('index'))
    elif request.method == 'GET':
        form.name.data = current_user.name
        form.email.data = current_user.email
    return render_template('account.html', form=form)