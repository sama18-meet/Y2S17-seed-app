from sqlalchemy import Column, DateTime, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from flask_login import UserMixin
from sqlalchemy.ext.declarative import declarative_base
from werkzeug.security import generate_password_hash, check_password_hash
Base = declarative_base()


class User(UserMixin, Base):
    __tablename__ = 'user'
    id            = Column(Integer, primary_key=True)
    username      = Column(String)
    full_name     = Column(String)
    pw_hash       = Column(String)
    authenticated     = Column(Boolean, default=False)
    museum_literature = Column(Boolean)
    museum_photography = Column(Boolean)
    museum_painting = Column(Boolean)
    piece = relationship("Piece")

    def __repr__(self):
        return "<User: %s, password: %s>" % (
            self.username, self.pw_hash)

    def set_password(self, password):
        self.pw_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.pw_hash, password)


class Piece(Base):
    __tablename__= 'Piece'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    ##story = Column(String)
    ## museum_literature = Column(Boolean)
    ## museum_photography = Column(Boolean)
    ## museum_painting = Column(Boolean)
    description = Column(String)
    pic_url = Column(String)
    ##likes = Column(Integer)
    user_id = Column(Integer, ForeignKey('user.id'))





# IF YOU NEED TO CREATE OTHER TABLE 
# FOLLOW THE SAME STRUCTURE AS YourModel