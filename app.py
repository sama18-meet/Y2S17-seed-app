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
def sign_up():
	if request.method == 'GET':
		return render_template ('sign_in.html')
	else:
		full_name = request.form.get('full_name')
		username = request.form.get('username')
		password = request.form.get('password')
		museum_music = request.form.get('museum_music_choice')
		museum_photography = request.form.get('museum_photography_choice')
		museum_painting = request.form.get('museum_painting_choice')
		user = User(full_name = full_name , username = username, pwd_hash= password, \
			authenticated= True, museum_music = museum_music  , museum_photography = museum_photography\
			,museum_painting= museum_painting)
		session.add(user)
		session.commit()
		return render_template ('my_feed.html')


@app.route('/my_feed/<int:user_id>/') 
def my_feed():
	favorites_pieces = []
	if user.museum_literature == True:
		favorites_pieces.append(museum_literature)
	if user.museum_photography == True:
		favorites_pieces.append(museum_photography)
	if user.museum_painting == True:
		favorites_pieces.append(museum_painting)		
	pieces = session.query(Piece).filter_by(favorites_pieces)
	return render_template('my_feed.html',pieces=pieces)
@app.route('/profile/<int:user_id>/')

def profile():
	user_pieces=session.query(Piece).filter_by(id=user_id)
	return render_template ('my_profile.html')

@app.route('/discover/<int:user_id>')
def discover():
	return render_template('discover.html')


	
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

if __name__ == '__main__':
	app.run(debug=True)
