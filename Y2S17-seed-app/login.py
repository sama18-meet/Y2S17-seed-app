from flask import redirect, url_for, render_template
from flask_login import LoginManager, login_user, logout_user

import sys

from model import Base, User
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
engine = create_engine('sqlite:///project.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

login_manager = LoginManager()


@login_manager.user_loader
def load_user(user_id):
    current_user = session.query(User).filter_by(id=user_id)
    if user.count() == 0:
        return
    return user.first()


@login_manager.unauthorized_handler
def unauthorized_handler():
    return 'Unauthorized'


def login_handler(request):
    if request.method == 'GET':
        return render_template('login.html')

    username = request.form.get('username')
    pw    = request.form.get('pw')
    current_user  = session.query(User).filter_by(username=username).first()
    if user.count() == 1:
        user = user.first()
        if user.check_password(pw):
            login_user(user)
            return 'Login Accepted'
        return 'Wrong Password'
    return 'Bad login'


def logout_handler():
    logout_user()
    return redirect('/')


def sign_up_handler(request):
    new_full_name = request.form.get('full_name')
    new_username  = request.form.get('username')
    new_pw        = request.form.get('password')
    museum_music  = request.form.get('museum_music_choice')
    museum_photography = request.form.get('museum_photography_choice')
    museum_painting    = request.form.get('museum_painting_choice')
    user = User(
        full_name=new_full_name, 
        username=new_username
    )
    user.set_password(new_pw)
    session.add(user)
    session.commit()
    login_user(current_user)
    return redirect(url_for('my_feed'))    