# flask imports
from flask import Flask, Response, render_template, request, redirect, url_for

# flask setup
app = Flask(__name__)
app.config["SECRET_KEY"] = "ITSASECRET"

# flask-login imports
from flask_login import login_required, current_user
from login import login_manager, login_handler, logout_handler
login_manager.init_app(app)

# SQLAlchemy
from model import Base, User
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
engine = create_engine('sqlite:///project.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

@app.route('/')
<<<<<<< HEAD
def sign_in():
	return render_template ('sign_in.html')

@app.route('/my_feed/<int:user_id>/') 
def my_feed():
	pieces = session.query(Piece).all()
	return render_template('my_feed.html',pieces=pieces)
@app.route('/profile/<int:user_id>/')
def profile():
	return render_template ('my_profile.html')

@app.route('/discover/<int:user_id>')
def discover():
	return render_template('discover.html')

if __name__ == '__main__':
	app.run(debug=True)
	
=======
def hello_world():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    return login_handler(request)


@app.route('/logout')
def logout():
  return logout_handler()


@app.route('/protected', methods=["GET"])
@login_required
def protected():
    return render_template('protected.html')
>>>>>>> f3b9e7cc5a0b9ef31b5e5397c3ee00a97c786cb7
