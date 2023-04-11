from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base


engine = create_engine('sqlite:///films.db')

Base = declarative_base()

Session = sessionmaker(bind=engine)

session = Session()


class Films(Base):
    __tablename__ = 'films'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    director = Column(String)
    release_year = Column(Integer)


Base.metadata.create_all(engine)

film1 = Films(title='Back to the Future', director='Robert Lee Zemeckis', release_year=1989)
film2 = Films(title='Robocop', director='Paul Verhoeven', release_year=1987)
film3 = Films(title='Terminator', director='James Francis Cameron', release_year=1984)

session.add(film1)
session.add(film2)
session.add(film3)
session.commit()

session.query(Films).filter(Films.title == 'Robocop').update({Films.release_year: 2016})

films = session.query(Films).all()

for film in films:
    print(film.id, film.title, film.director, film.release_year)

session.query(Films).delete()
session.commit()
session.close()
