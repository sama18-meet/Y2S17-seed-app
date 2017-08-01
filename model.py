from sqlalchemy import Column, DateTime, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
	__tablename__= 'user'
	id = Column(Integer, primary_key= True)
	full_name= Column(String)
	username= Column(String)
	password = Column(String)
	museum_choice = Column(String)
	post = relationship("Post")
    # ADD YOUR FIELD BELOW ID

class Piece(Base):
	__tablename__= 'Piece'
	id = Column(Integer, primary_key=True)
	title = Column(String)
	museum_Music = Column(Boolean)
	museum_Photography = Column(Boolean)
	museum_Painting = Column(Boolean)
	description = Column(String)
	pic_url = Column(String)
	likes = Column(Integer)
	user_id = Column(Integer, ForeignKey('user.id'))




# IF YOU NEED TO CREATE OTHER TABLE 
# FOLLOW THE SAME STRUCTURE AS YourModel