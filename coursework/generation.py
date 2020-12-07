from sqlalchemy import exc
import psycopg2
from sqlalchemy.dialects.postgresql import psycopg2
from tables import Film
from model import Model
from bs4 import BeautifulSoup
import requests


class Generation(Model):
    def __init__(self):
        super().__init__()
        self.max_page = 698
    def generator_films(self, pages):
        q = self.get(Film).all()
        length = len(q)
        i = int(length/36)
        to_page = i + pages
        if pages > (self.max_page - i):
            return False
        else:
            while (i <= to_page):
                req = requests.get('https://rezka.ag/films/page/' + str(i) + '/')
                bs = BeautifulSoup(req.text, 'html.parser')
                a = bs.select('div.b-content__inline_item-link > a')
                div = bs.select('div.b-content__inline_item-link > div')
                titles = []
                years = []
                countries = []
                geners = []
                for k in a:
                    for j in k:
                        titles.append(j)
                for w in div:
                    for j in w:
                        x = j.split(',')
                        years.append(x[0])
                        countries.append(x[1])
                        geners.append(x[2])
                for m in range(0, len(titles)):
                    req = "INSERT INTO films (title, genre, country, year, released) " \
                          "VALUES (%s, %s, %s, %s, RANDOM()::INT::BOOLEAN)"
                    self.cur.execute(req, (titles[m], geners[m], countries[m], years[m]))
                    self.db.commit()
                i = i + 1
            return True

    def generator_users(self, num):
        try:
            req = "insert into users (login, fullname, password_hash)"\
                  "select random_string(8), random_string(14), encode(digest(random_string(10), 'md5'),'hex')"\
                  "from generate_series(1,:param);"
            self.sess.execute(req, {'param': num})
            self.sess.commit()
        except(Exception, exc.DatabaseError, exc.InvalidRequestError) as error:
            print(error)
            self.sess.rollback()
        return True
    def generator_halls(self, num):
        try:
            req = "insert into halls (name, amount_of_seats, type_of_hall)"\
                  "select random_name_of_hall(), random()*(50-120+1)+120, random_type_of_hall() "\
                  "from generate_series(1,:param);"
            self.sess.execute(req, {'param': num})
            self.sess.commit()
        except(Exception, exc.DatabaseError, exc.InvalidRequestError) as error:
            print(error)
            self.sess.rollback()
        return True

    def generator_ratings(self, num):
        try:
            req = "insert into ratings (film_id, user_id, evaluation)"\
                  "select random_films_id(), random_users_id(), random()*(1-10+1)+10"\
                  "from generate_series(1,:param);"
            self.sess.execute(req, {'param': num})
            self.sess.commit()
        except(Exception, exc.DatabaseError, exc.InvalidRequestError) as error:
            print(error)
            self.sess.rollback()
        return True
    def generator_tickets(self, num):
        try:
            req = "insert into tickets (user_id, film_id, hall_id, row_number, seat_number, date_time, price)"\
                  "select random_users_id(), random_films_id(), random_halls_id(), random()*(7-20+1)+20," \
                  "random()*(1-30+1)+30, timestamp '2020-12-01 23:00:00' + random() * (timestamp '2020-10-01 10:00:00' - timestamp '2020-12-01 23:00:00')," \
                  "random()*(70-120+1)+120 from generate_series(1,:param);"
            self.sess.execute(req, {'param': num})
            self.sess.commit()
        except(Exception, exc.DatabaseError, exc.InvalidRequestError) as error:
            print(error)
            self.sess.rollback()
        return True
