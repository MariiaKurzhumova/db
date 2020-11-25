import psycopg2
import time
from sqlalchemy import exc, Column, Integer, ForeignKey, String, Time, Date, create_engine, Text
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Film(Base):
    __tablename__ = 'films'
    id = Column(Integer, primary_key=True)
    duration = Column(Time, nullable=False)
    year = Column(Integer, nullable=False)
    title = Column(String, nullable=False)
    description = Column(String, nullable=False)
    rating = Column(String, nullable=False)
    director = Column(String, nullable=False)
    # children = relationship("Session", secondary="film_session")

    def __init__(self, duration='', year="", title="", description="", rating="", director=""):
        self.duration = duration
        self.year = year
        self.title = title
        self.description = description
        self.rating = rating
        self.director = director

class Session(Base):
    __tablename__ = 'sessions'
    id = Column(Integer, primary_key=True)
    start_time = Column(Time, nullable=False)
    end_time = Column(Time, nullable=False)
    price = Column(Integer, nullable=False)
    hall_id = Column(Integer, ForeignKey('hall.id'))
    data = Column(Date, nullable=False)
    children = relationship("Film", secondary="film_session")

    def __init__(self, start_time='', end_time='', price='', hall_id='', data=''):
        self.start_time = start_time
        self.end_time = end_time
        self.price = price
        self.hall_id = hall_id
        self.data = data

class Connection(Base):
    __tablename__ = "film_session"
    id = Column(Integer, primary_key=True)
    id_film = Column(Integer, ForeignKey('films.id'), nullable=False)
    id_session = Column(Integer, ForeignKey('sessions.id'), nullable=False)

    def __init__(self, id_film, id_session):
        self.id_film = id_film
        self.id_session = id_session

class Hall(Base):
    __tablename__ = 'hall'
    id = Column(Integer, primary_key=True)
    number = Column(Integer, nullable=False)
    amount_of_seats = Column(Integer, nullable=False)
    seats_rows_id = Column(Integer, ForeignKey('seats_rows.id'))
    type_of_hall = Column(Text, nullable=False)
    children = relationship("Session")

    def __init__(self, number='', amount_of_seats='', seats_rows_id='', type_of_hall=''):
        self.number = number
        self.amount_of_seats = amount_of_seats
        self.seats_rows_id = seats_rows_id
        self.type_of_hall = type_of_hall


class Seat_row(Base):
    __tablename__ = 'seats_rows'
    id = Column(Integer, primary_key=True)
    row_number = Column(Integer, nullable=False)
    seat_number = Column(Integer, nullable=False)
    type_of_seat = Column(Text, nullable=False)
    children = relationship("Hall")

    def __init__(self, row_number='', seat_number='', type_of_seat=''):
        self.row_number = row_number
        self.seat_number = seat_number
        self.type_of_seat = type_of_seat


class Model(object):
    def __init__(self):
        self.engine = create_engine("postgres://postgres:Nuva2002@localhost/cinema")

        Session = sessionmaker(bind=self.engine)
        self.sess = Session()
        self.db = psycopg2.connect(database="cinema",
                                   user="postgres",
                                   password="Nuva2002",
                                   host="127.0.0.1",
                                   port="5432")
        self.cur = self.db.cursor()

    def close(self):
        self.db.close()

    def get_films(self):
        try:
            q = self.sess.query(Film)
            return q
        except(Exception, exc.DatabaseError, exc.InvalidRequestError) as error:
            print(error)
            self.sess.rollback()

    def get_film_by_id(self, id):
        try:
            q = self.sess.query(Film).get(id)
            return q
        except(Exception, exc.DatabaseError, exc.InvalidRequestError) as error:
            print(error)
            self.sess.rollback()

    def add_film(self, duration, year, title, description, rating, director):
        try:
            film = Film(duration, year, title, description, rating, director)
            self.sess.add(film)
            self.sess.commit()
            return True
        except(Exception, exc.DatabaseError, exc.InvalidRequestError) as error:
            print(error)
            self.sess.rollback()

    def update_film(self, film):
        try:
            self.sess.add(film)
            self.sess.commit()
            return True
        except(Exception, exc.DatabaseError, exc.InvalidRequestError) as error:
            print(error)
            self.sess.rollback()

    def delete_film(self, id):
        try:
            self.sess.query(Connection).filter_by(id_film=id).delete()
            film = self.get_film_by_id(id)
            self.sess.delete(film)
            self.sess.commit()
            return True
        except(Exception, exc.DatabaseError, exc.InvalidRequestError) as error:
            print(error)
            self.sess.rollback()

    def random_films(self, num):
        try:
            req = "INSERT INTO films (duration, year, title, description, rating, director) " \
                  "SELECT time '01:00:00' + random()*(time '03:00:00' - " \
                  "time '01:00:00'),random()*(2020-2000+1)+2000 ,md5(random()::text), " \
                  "md5(random()::text),random_rating(), md5(random()::text) " \
                  "FROM generate_series(1,%s)"
            self.cur.execute(req, (num,))
            self.db.commit()
            return True
        except(Exception, psycopg2.DatabaseError) as error:
            print(error)

    def select_films(self, year):
        list1 = list()
        try:
            req = "select films.rating, count(films.rating) AS Amount, films.year, " \
                  "hall.type_of_hall from films join film_session " \
                  "on film_session.id_film = films.id join sessions " \
                  "on film_session.id_session = sessions.id join hall " \
                  "on hall.id = sessions.hall_id " \
                  "where films.year > %s " \
                  "group by films.year, " \
                  "hall.type_of_hall, films.rating"
            current_time = time.time()
            self.cur.execute(req, (year,))
            query_time = time.time()
            print("Time of query: ")
            print(query_time - current_time)
            arr = self.cur.fetchall()
            for a in arr:
                list1.append(a)
            return list1
        except(Exception, psycopg2.DatabaseError) as error:
            print(error)

    ##################
    def get_sessions(self):
        try:
            q = self.sess.query(Session)
            return q
        except(Exception, exc.DatabaseError, exc.InvalidRequestError) as error:
            print(error)
            self.sess.rollback()

    def get_session_by_id(self, id):
        try:
            q = self.sess.query(Session).get(id)
            return q
        except(Exception, exc.DatabaseError, exc.InvalidRequestError) as error:
            print(error)
            self.sess.rollback()

    def add_session(self, start_time, end_time, price, hall_id, data):
        try:
            session = Session(start_time, end_time, price, hall_id, data)
            self.sess.add(session)
            self.sess.commit()
            return True
        except(Exception, exc.DatabaseError, exc.InvalidRequestError) as error:
            print(error)
            self.sess.rollback()

    def update_session(self, session):
        try:
            self.sess.add(session)
            self.sess.commit()
            return True
        except(Exception, exc.DatabaseError, exc.InvalidRequestError) as error:
            print(error)
            self.sess.rollback()

    def delete_session(self, id):
        try:
            self.sess.query(Connection).filter_by(id_session=id).delete()
            session = self.get_session_by_id(id)
            self.sess.delete(session)
            self.sess.commit()
            return True
        except(Exception, exc.DatabaseError, exc.InvalidRequestError) as error:
            print(error)
            self.sess.rollback()

    def random_sessions(self, num):
        try:
            req = "INSERT INTO sessions (start_time, end_time, price, hall_id, data) " \
                  "SELECT random()*(time '23:00:00' - time '10:00:00'), " \
                  "random()*(time '23:00:00' - time '10:00:00')," \
                  "random()*(200-50+1)::float8::numeric::money, " \
                  "random_halls_id(),timestamp  '2020-10-01' +" \
                  "random()*(timestamp  '2020-11-30' - timestamp  '2020-10-01') " \
                  "FROM generate_series(1,%s)"

            self.cur.execute(req, (num,))
            self.db.commit()
            return True
        except(Exception, psycopg2.DatabaseError) as error:
            print(error)

    def select_sessions(self, start_time, price):
        list1 = list()
        try:
            req = "select films.title, films.year, films.rating, " \
                  "sessions.data, sessions.start_time, sessions.price from films join film_session " \
                  "on film_session.id_film = films.id join sessions " \
                  "on film_session.id_session = sessions.id " \
                  "where sessions.start_time >= %s " \
                  "and sessions.price < %s::money"
            current_time = time.time()
            self.cur.execute(req, (start_time, price))
            query_time = time.time()
            print("Time of query: ")
            print(query_time - current_time)
            arr = self.cur.fetchall()
            i = 0
            for a in arr:
                list1.append(a)
        except(Exception, psycopg2.DatabaseError) as error:
            print(error)
        return list1

    ####################
    def get_film_session(self):
        try:
            q = self.sess.query(Connection)
            return q
        except(Exception, exc.DatabaseError, exc.InvalidRequestError) as error:
            print(error)
            self.sess.rollback()

    def add_film_session(self, film_id, session_id):
        try:
            film_session = Connection(film_id, session_id)
            self.sess.add(film_session)
            self.sess.commit()
            return True
        except(Exception, exc.DatabaseError, exc.InvalidRequestError) as error:
            print(error)
            self.sess.rollback()

    def delete_film_session(self, id):
        try:
            c = self.sess.query(Connection).get(id)
            self.sess.delete(c)
            self.sess.commit()
            return True
        except(Exception, exc.DatabaseError, exc.InvalidRequestError) as error:
            print(error)
            self.sess.rollback()

    def random_film_session(self, num):
        try:
            req = "INSERT INTO film_session (id_film, id_session) " \
                  "SELECT random_films_id(), random_sessions_id() " \
                  "FROM generate_series(1,%s)"
            self.cur.execute(req, (num,))
            self.db.commit()
            return True
        except(Exception, psycopg2.DatabaseError) as error:
            print(error)

    ####################
    def get_halls(self):
        try:
            q = self.sess.query(Hall)
            return q
        except(Exception, exc.DatabaseError, exc.InvalidRequestError) as error:
            print(error)
            self.sess.rollback()

    def get_hall_by_id(self, id):
        try:
            q = self.sess.query(Hall).get(id)
            return q
        except(Exception, exc.DatabaseError, exc.InvalidRequestError) as error:
            print(error)
            self.sess.rollback()

    def add_hall(self, number, amount_of_seats, seats_rows_id, type_of_hall):
        try:
            hall = Hall(number, amount_of_seats, seats_rows_id, type_of_hall)
            self.sess.add(hall)
            self.sess.commit()
            return True
        except(Exception, exc.DatabaseError, exc.InvalidRequestError) as error:
            print(error)
            self.sess.rollback()

    def update_hall(self, hall):
        try:
            self.sess.add(hall)
            self.sess.commit()
            return True
        except(Exception, exc.DatabaseError, exc.InvalidRequestError) as error:
            print(error)
            self.sess.rollback()

    def delete_hall(self, id):
        try:
            self.sess.query(Session).filter_by(hall_id=id).delete()
            hall = self.get_hall_by_id(id)
            self.sess.delete(hall)
            self.sess.commit()
            return True
        except(Exception, exc.DatabaseError, exc.InvalidRequestError) as error:
            print(error)
            self.sess.rollback()

    def random_halls(self, num):
        try:
            req = "INSERT INTO hall (number, amount_of_seats, seats_rows_id, type_of_hall) " \
                  "SELECT random()*(15-5+1)+5, random()*(200-50+1)+50, random_seats_rows_id(), random_type_of_hall() " \
                  "FROM generate_series(1,%s)"
            self.cur.execute(req, (num,))
            self.db.commit()
            return True
        except(Exception, psycopg2.DatabaseError) as error:
            print(error)
            self.sess.rollback()

    ######################
    def get_seats_rows(self):
        try:
            q = self.sess.query(Seat_row)
            return q
        except(Exception, exc.DatabaseError, exc.InvalidRequestError) as error:
            print(error)
            self.sess.rollback()

    def get_seat_row_by_id(self, id):
        try:
            q = self.sess.query(Seat_row).get(id)
            return q
        except(Exception, exc.DatabaseError, exc.InvalidRequestError) as error:
            print(error)
            self.sess.rollback()

    def add_seat_row(self, row_number, seat_number, type_of_seat):
        try:
            seat_row = Seat_row(row_number, seat_number, type_of_seat)
            self.sess.add(seat_row)
            self.sess.commit()
            return True
        except(Exception, exc.DatabaseError, exc.InvalidRequestError) as error:
            print(error)
            self.sess.rollback()

    def update_seat_row(self, seat_row):
        try:
            self.sess.add(seat_row)
            self.sess.commit()
            return True
        except(Exception, exc.DatabaseError, exc.InvalidRequestError) as error:
            print(error)
            self.sess.rollback()

    def delete_seat_row(self, id):
        try:
            self.sess.query(Seat_row).filter_by(seats_rows_id = id).delete()
            seat_row = self.get_seat_row_by_id(id)
            self.sess.delete(seat_row)
            self.sess.commit()
            return True
        except(Exception, exc.DatabaseError, exc.InvalidRequestError) as error:
            print(error)
            self.sess.rollback()

    def random_seats_rows(self, num):
        try:
            req = "INSERT INTO seats_rows (row_number, seat_number, type_of_seat) " \
                  "SELECT random()*(15-5+1)+5, random()*(20-10+1)+10, random_type_of_seat() " \
                  "FROM generate_series(1,%s)"
            self.cur.execute(req, (num,))
            self.db.commit()
            return True
        except(Exception, psycopg2.DatabaseError) as error:
            print(error)

    def select_seats_rows(self, row_number):
        list1 = list()
        try:
            req = "select seats_rows.row_number, " \
                  "seats_rows.type_of_seat, hall.type_of_hall, films.rating " \
                  "from seats_rows join hall " \
                  "on seats_rows.id = hall.seats_rows_id join sessions " \
                  "on sessions.hall_id = hall.id join film_session " \
                  "on film_session.id_session = sessions.id join films " \
                  "on films.id = film_session.id_film " \
                  "where seats_rows.row_number > %s"
            current_time = time.time()
            self.cur.execute(req, (row_number,))
            query_time = time.time()
            print("Time of query: ")
            print(query_time - current_time)
            arr = self.cur.fetchall()
            for a in arr:
                list1.append(a)
            return list1
        except(Exception, psycopg2.DatabaseError) as error:
            print(error)