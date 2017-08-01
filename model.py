from flask_login import UserMixin

from sqlalchemy import Column, DateTime, Integer, String, Boolean, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import relationship

from werkzeug.security import generate_password_hash, check_password_hash
Base = declarative_base()


class User(UserMixin, Base):
    __tablename__ = 'user'
    id            = Column(Integer, primary_key=True)
    email         = Column(String)
    pw_hash       = Column(String)
    authenticated = Column(Boolean, default=False)
    museum_museum = Column(Boolean)
    museum_photography = Column(Boolean)
    museum_painting = Column(Boolean)
    post = relationship("Post")

    def __repr__(self):
      return "<User: %s, password: %s>" % (
        self.email, self.pw_hash)

    def set_password(self, password):
        self.pw_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.pw_hash, password)


class Post(Base):
	__tablename__= 'post'
	id = Column(Integer, primary_key=True)
	title = Column(String)
	museum_music = Column(Boolean)
	museum_photography = Column(Boolean)
	museum_painting = Column(Boolean)
	description = Column(String)
	pic_url = Column(String)
	likes = Column(Integer)
	user_id = Column(Integer, ForeignKey('user.id'))




# IF YOU NEED TO CREATE OTHER TABLE 
# FOLLOW THE SAME STRUCTURE AS YourModel