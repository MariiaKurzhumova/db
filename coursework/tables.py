from sqlalchemy import TIMESTAMP, Column, Integer, ForeignKey, String, Boolean, Text
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()
class Film(Base):
    __tablename__ = 'films'
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    genre = Column(String, nullable=False)
    country = Column(String, nullable=False)
    year = Column(Integer, nullable=False)
    released = Column(Boolean, nullable=True)
    # relation = relationship(secondary='ratings')
    # relation1 = relationship(secondary='tickets')

    def __init__(self, title, genre, country, year, released):
        self.title = title
        self.genre = genre
        self.country = country
        self.year = year
        self.released = released
class Hall(Base):
    __tablename__ = 'halls'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    amount_of_seats = Column(Integer, nullable=False)
    type_of_hall = Column(Text, nullable=False)
    # relation1 = relationship(secondary='tickets')

    def __init__(self, name, amount_of_seats, type_of_hall):
        self.name = name
        self.amount_of_seats = amount_of_seats
        self.type_of_hall = type_of_hall

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    login = Column(String, nullable=False)
    fullname = Column(String, nullable=False)
    password_hash = Column(String, nullable=False)
    # relation = relationship(secondary='ratings')
    # relation1 = relationship(secondary='tickets')

    def __init__(self, login, fullname, password_hash):
        self.login = login
        self.fullname = fullname
        self.password_hash = password_hash

class Rating(Base):
    __tablename__ = 'ratings'
    id = Column(Integer, primary_key=True)
    film_id = Column(Integer, ForeignKey('films.id'), nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    evaluation = Column(Integer, nullable=False)

    def __init__(self, film_id, user_id, evaluation):
        self.film_id = film_id
        self.user_id = user_id
        self.evaluation = evaluation

class Ticket(Base):
    __tablename__ = 'tickets'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    film_id = Column(Integer, ForeignKey('films.id'), nullable=False)
    hall_id = Column(Integer, ForeignKey('halls.id'), nullable=False)
    row_number = Column(Integer, nullable=False)
    seat_number = Column(Integer, nullable=False)
    date_time = Column(TIMESTAMP, nullable=False)
    price = Column(Integer, nullable=False)

    def __init__(self, user_id, film_id, hall_id, row_number, seat_number, date_time, price):
        self.user_id = user_id
        self.film_id = film_id
        self.hall_id = hall_id
        self.row_number = row_number
        self.seat_number = seat_number
        self.date_time = date_time
        self.price = price
