from sqlalchemy import exc
from tables import Film
from model import Model
from bs4 import BeautifulSoup
import requests
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

PLOT_LABEL_FONT_SIZE = 14
PLOT_MEAKING_FONT_SIZE = 6

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
                for titles_ in a:
                    for title in titles_:
                        titles.append(title)
                for info in div:
                    for j in info:
                        x = j.split(',')
                        if len(x) < 3:
                            years.append(0)
                            countries.append("")
                            geners.append("")
                            continue

                        for s in x[0].split():
                            if s.isdigit():
                                year = int(s)
                        years.append(year)
                        countries.append(x[1])
                        geners.append(x[2])
                for m in range(0, len(titles)):
                    q = self.sess.query(Film).filter(Film.title == titles[m]).all()
                    if len(q) == 0:
                        req = "INSERT INTO films (title, genre, country, year, released) " \
                              "VALUES (:title, :genre, :country, :year, :released)"
                        released = True
                        if years[m] < 2020:
                            released = False
                        self.sess.execute(req, {'title': titles[m], 'genre': geners[m], 'country': countries[m],
                                                'year': years[m], 'released': released})
                        self.db.commit()
                    else:
                        continue
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

    def best_films_in_genre(self, genre):
        list = []
        try:
            genre = ' ' + genre
            req = "with select_all as (select title, avg(evaluation) from ratings "\
                    "join films on films.id = ratings.film_id "\
                    "where genre =  :param group by title) "\
                    "select * from select_all "\
                    "where avg = (select max(avg) from select_all)"
            q = self.sess.execute(req, {'param': genre})

            for i in q:
                list.append(i)
        except(Exception, exc.DatabaseError, exc.InvalidRequestError) as error:
            print(error)
            self.sess.rollback()
        return list

    def best_films_in_years(self, year):
        list = []
        try:
            req = "with select_all as (select title, avg(evaluation) from ratings "\
                    "join films on films.id = ratings.film_id "\
                    "where year =  :param group by title) "\
                    "select * from select_all "\
                    "where avg = (select max(avg) from select_all) "
            q = self.sess.execute(req, {'param': year})

            for i in q:
                list.append(i)
        except(Exception, exc.DatabaseError, exc.InvalidRequestError) as error:
            print(error)
            self.sess.rollback()
        return list

    def choose_movie(self, id):
        list = []
        try:
            reqs = "with select_genres as(select genre, count(genre) from films as f join ratings as r "\
                    "on f.id = r.film_id where r.user_id = :param group by genre) "\
                    "select genre from select_genres where count = (select max(count) from select_genres)"
            g = self.sess.execute(reqs, {'param': id}).fetchall()
            self.sess.commit()

            s = str(g)
            st = ''
            for i in range(3, len(s) - 4):
                st = st + s[i];
            print(st)
            genre = st
            if genre == '':
                return None
            for i in range(0, 9):
                req = "select title from films where " \
                      "id = (select random_films_for_user(:param))"
                q = self.sess.execute(req, {'param': genre})
                for j in q:
                    list.append(j)
        except(Exception, exc.DatabaseError, exc.InvalidRequestError) as error:
            print(error)
            self.sess.rollback()
        return list

    def getColors(self, n):
        COLORS = []
        cm = plt.cm.get_cmap('hsv', n)
        for i in np.arange(n):
            COLORS.append(cm(i))
        return COLORS
    def statistics(self):
        try:
            req = "select film_id, evaluation, genre, country," \
                  " year from ratings join films on films.id = ratings.film_id where year<>0"
            q = self.sess.execute(req).fetchall()
        except(Exception, exc.DatabaseError, exc.InvalidRequestError) as error:
            print(error)
            self.sess.rollback()
        return q

    def graph(self):
        q = self.statistics()
        df = pd.DataFrame(q, columns=["film_id", "evaluation", "genre", "country", "year"])
        select_data = df[["genre", "evaluation"]]
        group = select_data.groupby('genre')['evaluation'].mean(1).reset_index()
        group = group.sort_values(by=["evaluation"], ascending=False)
        plt.title('Середнє значення оцінок по жанрам')
        plt.bar(group["genre"], group["evaluation"], color=self.getColors(len(group["evaluation"])))
        plt.ylabel('Оцінки')
        plt.xlabel('Жанри')
        plt.xticks(rotation=90, fontsize=PLOT_MEAKING_FONT_SIZE)
        plt.show()
g = Generation()
g.graph()
# with select_all as (select title, avg(evaluation) from ratings
# inner join films on ratings.film_id = films.id
# group by title),
#
# select_max as (select * from select_all
# where avg = (select max(avg) from select_all)),
#
# all_years as (select select_max.avg, films.year, count(year)
# from select_max join films on select_max.title = films.title
# group by select_max.avg, films.year)
#
# select * from all_years
# where count = (select max(count) from all_years)

