import psycopg2
import time

class Film(object):
    def __init__(self, id = "", duration = '', year = "", title = "", description = "", rating = "", director = ""):
        self.id = id
        self.duration = duration
        self.year = year
        self.title = title
        self.description = description
        self.rating = rating
        self.director = director


class Session(object):
    def __init__(self, id = '', start_time = '', end_time = '', price = '', hall_id = '', data = ''):
        self.id = id
        self.start_time = start_time
        self.end_time = end_time
        self.price = price
        self.hall_id = hall_id
        self.data = data


class Connection(object):
    def __init__(self, id = '', id_film = '', id_session = ''):
        self.id = id
        self.id_film = id_film
        self.id_session = id_session

class Hall(object):
    def __init__(self, id = '', number = '', amount_of_seats = '', seats_rows_id = '', type_of_hall = ''):
        self.id = id
        self.number = number
        self.amount_of_seats = amount_of_seats
        self.seats_rows_id = seats_rows_id
        self.type_of_hall = type_of_hall

class Seat_row(object):
    def __init__(self, id = '', row_number = '', seat_number = '', type_of_seat = ''):
        self.id = id
        self.row_number = row_number
        self.seat_number = seat_number
        self.type_of_seat = type_of_seat


class Model(object):
    def __init__(self):
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
            listoffilms = list()
            self.cur.execute("SELECT * FROM films")
            films = self.cur.fetchall()
            # i = 0
            for film in films:
                film1 = Film(film[0], film[1], film[2], film[3], film[4], film[5], film[6])
                # print(film1.duration, film1.year, film1.title, film1.description, film1.rating, film1.director)
                listoffilms.append(film1)
                # print(listoffilms[i].duration)
                # i = i + 1
            return listoffilms
        except(Exception, psycopg2.DatabaseError) as error:
            print(error)

    def get_film_by_id(self, id):
        films = self.get_films()
        check = False
        i = 0
        for film in films:
            if id == film.id:
                check = True
        if check == False:
            print("There is no record in db!")
            f = Film()
            return f
        try:
            self.cur.execute("SELECT * FROM FILMS WHERE ID = " + str(id))
            str_ = self.cur.fetchall()
            film = Film(str_[0][0], str_[0][1], str_[0][2], str_[0][3], str_[0][4], str_[0][5], str_[0][6])
            return film
        except(Exception, psycopg2.DatabaseError) as error:
            print(error)

    def add_film(self, duration, year, title, description, rating, director):
        films = self.get_films()
        check = False
        for film in films:
            if str(film.duration) == str(duration) and str(film.year) == str(
                    year) and film.title == title and film.description == description and film.rating == rating and film.director == director:
                check = True
        if check:
            print("Record already exists!")
            return False
        try:
            req = "INSERT INTO FILMS (duration, year, title, description, rating, director) VALUES (%s, %s, %s, %s, " \
                  "%s, %s) "
            self.cur.execute(req, (duration, year, title, description, rating, director))
            self.db.commit()
            return True
        except(Exception, psycopg2.DatabaseError) as error:
            print(error)

    def update_film(self, film):
        films = self.get_films()
        check = False
        for film_ in films:
            if film_.id == film.id:
                check = True
        if not check:
            print("There is no record in db!")
            return False
        try:
            req = "UPDATE FILMS SET duration = %s, year = %s, title = %s, description = %s, rating = %s, director = " \
                  "%s WHERE ID = " + str(film.id)
            self.cur.execute(req, (film.duration, film.year, film.title, film.description, film.rating, film.director))
            self.db.commit()
            return True
        except(Exception, psycopg2.DatabaseError) as error:
            print(error)

    def delete_film(self, id):
        films = self.get_films()
        check = False
        for film_ in films:
            if film_.id == id:
                check = True
        if not check:
            print("There is no record in db!")
            return False
        connections = self.get_film_session()
        for connection in connections:
            if id == connection.id_film:
                try:
                    self.cur.execute("DELETE FROM film_session WHERE id_film = " + str(connection.id_film))
                    self.db.commit()
                except(Exception, psycopg2.DatabaseError) as error:
                    print(error)
        try:
            self.cur.execute("DELETE FROM FILMS WHERE ID = " + str(id))
            self.db.commit()
            return True
        except(Exception, psycopg2.DatabaseError) as error:
            print(error)

    def random_films(self, num):
        try:
            req = "INSERT INTO films (duration, year, title, description, rating, director) " \
                  "SELECT time '01:00:00' + random()*(time '03:00:00' - "\
                  "time '01:00:00'),random()*(2020-2000+1)+2000 ,md5(random()::text), " \
                  "md5(random()::text),random_rating(), md5(random()::text) "\
                  "FROM generate_series(1,%s)"
            self.cur.execute(req, (num,))
            self.db.commit()
            return True
        except(Exception, psycopg2.DatabaseError) as error:
            print(error)
    def select_films(self, year):
        list1 = list()
        try:
            req = "select films.rating, count(films.rating) AS Amount, films.year, "\
                    "hall.type_of_hall from films join film_session "\
                    "on film_session.id_film = films.id join sessions "\
                    "on film_session.id_session = sessions.id join hall "\
                    "on hall.id = sessions.hall_id "\
                    "where films.year > %s "\
                    "group by films.year, "\
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
            listofsessions = list()
            self.cur.execute("SELECT * FROM sessions")
            sessions = self.cur.fetchall()
            # i = 0
            for session in sessions:
                sess = Session(session[0], session[1], session[2], session[3], session[4], session[5])
                # print(film1.duration, film1.year, film1.title, film1.description, film1.rating, film1.director)
                listofsessions.append(sess)
                # print(listofsessions[i].start_time, listofsessions[i].end_time,listofsessions[i].price, listofsessions[i].hall_id, listofsessions[i].data )
                # i = i + 1
            return listofsessions
        except(Exception, psycopg2.DatabaseError) as error:
            print(error)

    def get_session_by_id(self, id):
        sessions = self.get_sessions()
        check = False
        for session in sessions:
            if id == session.id:
                check = True
        if not check:
            print("There is no record in db!")
            s = Session()
            return s
        try:
            self.cur.execute("SELECT * FROM sessions WHERE ID = " + str(id))
            str_ = self.cur.fetchall()
            session = Session(str_[0][0], str_[0][1], str_[0][2], str_[0][3], str_[0][4], str_[0][5])
            # print(session.id, session.start_time)
            return session
        except(Exception, psycopg2.DatabaseError) as error:
            print(error)

    def add_session(self, start_time, end_time, price, hall_id, data):
        halls = self.get_halls()
        check = False
        for hall in halls:
            if hall.id == hall_id:
                check = True
        if not check:
            print("There is no such hall!")
            return False
        sessions = self.get_sessions()
        check = False
        for session in sessions:
            if str(session.start_time) == str(start_time) and str(session.end_time) == str(end_time) \
                    and str(session.price) == str(price) and str(session.hall_id) == str(hall_id) and str(
                session.data) == str(data):
                check = True
        if check:
            print("Record already exists!")
            return False
        try:
            req = "INSERT INTO sessions (start_time, end_time, price, hall_id, data) VALUES (%s, %s, %s, %s, " \
                  "%s) "
            self.cur.execute(req, (start_time, end_time, price, hall_id, data))
            self.db.commit()
            return True
        except(Exception, psycopg2.DatabaseError) as error:
            print(error)

    def update_session(self, session):
        sessions = self.get_sessions()
        check = False
        for session_ in sessions:
            if session_.id == session.id:
                check = True
        if not check:
            print("There is no record in db!")
            return False
        try:
            req = "UPDATE sessions SET start_time = %s, end_time = %s, price = %s, hall_id = %s, data = %s WHERE ID = " + str(
                session.id)
            self.cur.execute(req, (session.start_time, session.end_time, session.price, session.hall_id, session.data))
            self.db.commit()
            return True
        except(Exception, psycopg2.DatabaseError) as error:
            print(error)

    def delete_session(self, id):
        sessions = self.get_sessions()
        check = False
        for session in sessions:
            if id == session.id:
                check = True
        if not check:
            print("There is no record in db!")
            return False
        connections = self.get_film_session()
        for connection in connections:
            if id == connection.id_session:
                try:
                    self.cur.execute("DELETE FROM film_session WHERE id_session = " + str(connection.id_session))
                    self.db.commit()
                except(Exception, psycopg2.DatabaseError) as error:
                    print(error)
        try:
            self.cur.execute("DELETE FROM sessions WHERE ID = " + str(id))
            self.db.commit()
            return True
        except(Exception, psycopg2.DatabaseError) as error:
            print(error)

    def random_sessions(self, num):
        try:
            req = "INSERT INTO sessions (start_time, end_time, price, hall_id, data) " \
                  "SELECT random()*(time '23:00:00' - time '10:00:00'), " \
                  "random()*(time '23:00:00' - time '10:00:00')," \
                  "random()*(200-50+1)::float8::numeric::money, " \
                  "random_halls_id(),timestamp  '2020-10-01' +"\
                  "random()*(timestamp  '2020-11-30' - timestamp  '2020-10-01') "\
                  "FROM generate_series(1,%s)"

            self.cur.execute(req, (num,))
            self.db.commit()
            return True
        except(Exception, psycopg2.DatabaseError) as error:
            print(error)
    def select_sessions(self, start_time, price):
        list1 = list()
        try:
            req = "select films.title, films.year, films.rating, "\
                    "sessions.data, sessions.start_time, sessions.price from films join film_session "\
                    "on film_session.id_film = films.id join sessions "\
                    "on film_session.id_session = sessions.id "\
                    "where sessions.start_time >= %s "\
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
            list1 = list()
            self.cur.execute("SELECT * FROM film_session")
            connections = self.cur.fetchall()
            for connection in connections:
                con = Connection(connection[0], connection[1], connection[2])
                list1.append(con)
            return list1
        except(Exception, psycopg2.DatabaseError) as error:
            print(error)

    def add_film_session(self, film_id, session_id):
        sessions = self.get_sessions()
        check = False
        for session in sessions:
            if session_id == session.id:
                check = True
        if not check:
            print("There is no record in db!")
            return False
        films = self.get_films()
        check = False
        for film_ in films:
            if film_.id == film_id:
                check = True
        if not check:
            print("There is no record in db!")
            return False
        connections = self.get_film_session()
        check = False
        for connection in connections:
            if film_id == connection.id_film and session_id == connection.id_session:
                check = True
        if check:
            print("Record already exists!")
            return False
        try:
            req = "INSERT INTO film_session (id_film, id_session) VALUES (%s, %s)"
            self.cur.execute(req, (film_id, session_id))
            self.db.commit()
            return True
        except(Exception, psycopg2.DatabaseError) as error:
            print(error)

    def delete_film_session(self, id):
        connections = self.get_film_session()
        check = False
        for connection in connections:
            if id == connection.id:
                check = True
        if not check:
            print("There is no record in db!")
            return False
        try:
            self.cur.execute("DELETE FROM film_session WHERE ID = " + str(id))
            self.db.commit()
            return True
        except(Exception, psycopg2.DatabaseError) as error:
            print(error)

    def random_film_session(self, num):
        try:
            req = "INSERT INTO film_session (id_film, id_session) " \
                  "SELECT random_films_id(), random_sessions_id() "\
                  "FROM generate_series(1,%s)"
            self.cur.execute(req, (num,))
            self.db.commit()
            return True
        except(Exception, psycopg2.DatabaseError) as error:
            print(error)
    ####################
    def get_halls(self):
        try:
            list1 = list()
            self.cur.execute("SELECT * FROM hall")
            halls = self.cur.fetchall()
            for hall in halls:
                h = Hall(hall[0], hall[1], hall[2], hall[3], hall[4])
                list1.append(h)
            return list1
        except(Exception, psycopg2.DatabaseError) as error:
            print(error)

    def get_hall_by_id(self, id):
        halls = self.get_halls()
        check = False
        for hall in halls:
            if id == hall.id:
                check = True
        if not check:
            print("There is no record in db!")
            h = Hall()
            return h
        try:
            self.cur.execute("SELECT * FROM hall WHERE ID = " + str(id))
            str_ = self.cur.fetchall()
            hall = Hall(str_[0][0], str_[0][1], str_[0][2], str_[0][3], str_[0][4])
            return hall
        except(Exception, psycopg2.DatabaseError) as error:
            print(error)

    def add_hall(self, number, amount_of_seats, seats_rows_id, type_of_hall):
        seats_rows = self.get_seats_rows()
        check = False
        for seat_row in seats_rows:
            if seat_row.id == seats_rows_id:
                check = True
        if not check:
            print("There is no such seat_row!")
            return False
        halls = self.get_halls()
        check = False
        for hall in halls:
            if str(hall.number) == str(number) and str(hall.amount_of_seats) == str(amount_of_seats) and \
                    str(hall.seats_rows_id) == str(seats_rows_id) and str(hall.type_of_hall) == str(type_of_hall):
                check = True
        if check:
            print("Record already exists!")
            return False
        try:
            req = "INSERT INTO hall (number, amount_of_seats, seats_rows_id, type_of_hall) VALUES (%s, %s, %s, %s)"
            self.cur.execute(req, (number, amount_of_seats, seats_rows_id, type_of_hall))
            self.db.commit()
            return True
        except(Exception, psycopg2.DatabaseError) as error:
            print(error)

    def update_hall(self, hall):
        halls = self.get_halls()
        check = False
        for hall_ in halls:
            if hall_.id == hall.id:
                check = True
        if not check:
            print("There is no record in db!")
            return False
        try:
            req = "UPDATE hall SET number = %s, amount_of_seats = %s, seats_rows_id = %s, type_of_hall = %s WHERE ID = " + str(hall.id)
            self.cur.execute(req, (hall.number, hall.amount_of_seats, hall.seats_rows_id, hall.type_of_hall))
            self.db.commit()
            return True
        except(Exception, psycopg2.DatabaseError) as error:
            print(error)

    def delete_hall(self, id):
        halls = self.get_halls()
        check = False
        for hall in halls:
            if id == hall.id:
                check = True
        if not check:
            print("There is no record in db!")
            return False
        sessions = self.get_sessions()
        for session in sessions:
            if session.hall_id == id:
                self.delete_session(session.id)
        try:
            self.cur.execute("DELETE FROM hall WHERE ID = " + str(id))
            self.db.commit()
            return True
        except(Exception, psycopg2.DatabaseError) as error:
            print(error)

    def random_halls(self, num):
        try:
            req = "INSERT INTO hall (number, amount_of_seats, seats_rows_id, type_of_hall) " \
                  "SELECT random()*(15-5+1)+5, random()*(200-50+1)+50, random_seats_rows_id(), random_type_of_hall() "\
                  "FROM generate_series(1,%s)"
            self.cur.execute(req, (num,))
            self.db.commit()
            return True
        except(Exception, psycopg2.DatabaseError) as error:
            print(error)

    ######################
    def get_seats_rows(self):
        try:
            list1 = list()
            self.cur.execute("SELECT * FROM seats_rows")
            seats_rows = self.cur.fetchall()
            for seat_row in seats_rows:
                sr = Seat_row(seat_row[0], seat_row[1], seat_row[2], seat_row[3])
                list1.append(sr)
            return list1
        except(Exception, psycopg2.DatabaseError) as error:
            print(error)

    def get_seat_row_by_id(self, id):
        seats_rows = self.get_seats_rows()
        check = False
        for seat_row in seats_rows:
            if id == seat_row.id:
                check = True
        if not check:
            print("There is no record in db!")
            sr = Seat_row()
            return sr
        try:
            self.cur.execute("SELECT * FROM seats_rows WHERE ID = " + str(id))
            str_ = self.cur.fetchall()
            seat_row = Seat_row(str_[0][0], str_[0][1], str_[0][2], str_[0][3])
            return seat_row
        except(Exception, psycopg2.DatabaseError) as error:
            print(error)

    def add_seat_row(self, row_number, seat_number, type_of_seat):
        seats_rows = self.get_seats_rows()
        check = False
        for seat_row in seats_rows:
            if str(seat_row.row_number) == str(row_number) and str(seat_row.seat_number) == str(seat_number) and \
                    str(seat_row.type_of_seat) == str(type_of_seat) :
                check = True
        if check:
            print("Record already exists!")
            return False
        try:
            req = "INSERT INTO seats_rows (row_number, seat_number, type_of_seat) VALUES (%s, %s, %s)"
            self.cur.execute(req, (row_number, seat_number, type_of_seat))
            self.db.commit()
            return True
        except(Exception, psycopg2.DatabaseError) as error:
            print(error)

    def update_seat_row(self, seat_row):
        seats_rows = self.get_seats_rows()
        check = False
        for seat_row_ in seats_rows:
            if seat_row_.id == seat_row.id:
                check = True
        if not check:
            print("There is no record in db!")
            return False
        try:
            req = "UPDATE seats_rows SET row_number = %s, seat_number = %s, type_of_seat = %s WHERE ID = " + str(seat_row.id)
            self.cur.execute(req, (seat_row.row_number, seat_row.seat_number, seat_row.type_of_seat))
            self.db.commit()
            return True
        except(Exception, psycopg2.DatabaseError) as error:
            print(error)

    def delete_seat_row(self, id):
        seats_rows = self.get_seats_rows()
        check = False
        for seat_row in seats_rows:
            if seat_row.id == id:
                check = True
        if not check:
            print("There is no record in db!")
            return False
        halls = self.get_halls()
        for hall in halls:
            if hall.seats_rows_id == id:
                self.delete_session(hall.id)
        try:
            self.cur.execute("DELETE FROM seats_rows WHERE ID = " + str(id))
            self.db.commit()
            return True
        except(Exception, psycopg2.DatabaseError) as error:
            print(error)

    def random_seats_rows(self, num):
        try:
            req = "INSERT INTO seats_rows (row_number, seat_number, type_of_seat) " \
                  "SELECT random()*(15-5+1)+5, random()*(20-10+1)+10, random_type_of_seat() "\
                  "FROM generate_series(1,%s)"
            self.cur.execute(req, (num,))
            self.db.commit()
            return True
        except(Exception, psycopg2.DatabaseError) as error:
            print(error)
    def select_seats_rows(self, row_number):
        list1 = list()
        try:
            req = "select seats_rows.row_number, "\
                "seats_rows.type_of_seat, hall.type_of_hall, films.rating "\
                "from seats_rows join hall "\
                "on seats_rows.id = hall.seats_rows_id join sessions "\
                "on sessions.hall_id = hall.id join film_session "\
                "on film_session.id_session = sessions.id join films "\
                "on films.id = film_session.id_film "\
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

# create function random_type_of_seat() RETURNS SETOF text AS
# $BODY$
# DECLARE
# 	r integer = floor(random()*(100+50+1))-50;
# BEGIN
# 	IF r > 0 THEN
# 		return next 'Звичайне';
# 	ELSE
# 		return next 'Комфорт';
# 		END IF;
# END
# $BODY$
# LANGUAGE plpgsql;
# insert into seats_rows (row_number, seat_number, type_of_seat)
# values (1, 4, random_type_of_seat());

# select films.rating, count(*) AS Amount, films.title, films.year,
# sessions.price, hall.type_of_hall, count(*) AS Amount from films join film_session
# on film_session.id_film = films.id join sessions
# on film_session.id_session = sessions.id join hall
# on hall.id = sessions.hall_id
# where films.year >2000
# and sessions.price < 100::money group by films.rating, films.title, films.year,
# hall.type_of_hall, sessions.price;