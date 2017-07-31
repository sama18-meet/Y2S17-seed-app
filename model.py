from sqlalchemy import Column, DateTime, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


User(Base):
	__tablename__= 'user'
	id = Column(Integer, primary_key= True)
	full_name= Column(String)
	username= Column(String)
	password = Column(String)
	museum_choice = Column(String)
    # ADD YOUR FIELD BELOW ID

# IF YOU NEED TO CREATE OTHER TABLE 
# FOLLOW THE SAME STRUCTURE AS YourModel