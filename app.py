# flask imports
from flask import Flask, render_template, request, redirect, url_for

# SQLAlchemy
from model import Base, User
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# setup
app = Flask(__name__)
engine = create_engine('sqlite:///project.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

@app.route('/')
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
	