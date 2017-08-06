import sys
from login import *

# flask imports
from flask import Flask, Response, render_template, request, redirect, url_for
# flask setup
app = Flask(__name__)
app.config["SECRET_KEY"] = "ITSASECRET"

# flask-login imports
from flask_login import login_required, current_user
from login import login_manager, login_handler, logout_handler, sign_up_handler
login_manager.init_app(app)

# SQLAlchemy
from model import Base, User, Piece
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
engine = create_engine('sqlite:///project.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()


@app.route('/my_feed', methods=["GET", "POST"])
def my_feed():
	pieces = session.query(Piece).all()
	# favorites_pieces = []
	# if user.museum_literature == True:
	# 	favorites_pieces.append(museum_literature)
	# if user.museum_photography == True:
	# 	favorites_pieces.append(museum_photography)
	# if user.museum_painting == True:
	# 	favorites_pieces.append(museum_painting)		
	# pieces = session.query(Piece).filter_by(favorites_pieces)
	return render_template('my_feed.html',pieces=pieces)

@app.route('/profile')
@login_required
def profile():
	my_pieces = session.query(Piece).filter_by(id = current_user.id)
	return render_template ('profile.html')

@app.route('/about_us')
def about_us():
	return render_template ('about_us.html')

@app.route('/discover')
def discover():
	return render_template('discover.html')

@app.route('/post', methods=['GET', 'POST'])
def post():
	if request.method == 'GET':
		return render_template('/post.html')
	else:
		pic_url=request.form.get('pic_url')
		title = request.form.get('title')
		description = request.form.get('description')
		piece=Piece(title = title, pic_url = pic_url, description = description, )
		session.add(piece)
		session.commit()
		return redirect(url_for('my_feed'))



########### LOGIN USER / SIGN UP #################

@app.route('/login', methods=['GET', 'POST'])
def login():
	if request.method == 'GET':
		return render_template('login.html')
	else:
		return login_handler(request)	



@app.route('/', methods=["GET", "POST"])
def sign_up():
    if request.method == 'GET':
        return render_template('sign_in.html')
    else:
    	return sign_up_handler(request)


@app.route('/logout')
def logout():
	return logout_handler()    	











