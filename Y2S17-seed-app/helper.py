from model import Base, User, Piece
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
engine = create_engine('sqlite:///project.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()
new_user = User(username = "testuser", p)

new_piece = Piece(title="Test Title", description="Test Description", pic_url="http://www.louvre.fr/sites/default/files/imagecache/940x768/medias/medias_images/images/louvre-portrait-de-lisa-gherardini-epouse-de-francesco-del-giocondo-dite-monna-lisa-la-gioconda-ou-la-jocon.jpg")