import sys

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


@app.route('/my_feed/')
def my_feed():
	pieces = session.query(Piece).all()
	# print ("my user %s" % current_user, file=sys.stderr)
	# favorites_pieces = []
	# if user.museum_literature == True:
	# 	favorites_pieces.append(museum_literature)
	# if user.museum_photography == True:
	# 	favorites_pieces.append(museum_photography)
	# if user.museum_painting == True:
	# 	favorites_pieces.append(museum_painting)		
	# pieces = session.query(Piece).filter_by(favorites_pieces)
	return render_template('my_feed.html',pieces=pieces)


@app.route('/profile/')
def profile():
	return render_template ('my_profile.html')

@app.route('/about-us/')
def about_us():
	return render_template ('my_profile.html')

@app.route('/discover/')
def discover():
	return render_template('discover.html')


########### LOGIN USER / SIGN UP #################

@app.route('/login', methods=['GET', 'POST'])
def login():
    return login_handler(request)


@app.route('/logout')
def logout():
  return logout_handler()


@app.route('/sign-up', methods=["GET", "POST"])
def sign_up():
    if request.method == 'GET':
        return render_template('sign_in.html')
    else:
    	return sign_up_handler(request)
