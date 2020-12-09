import psycopg2
from sqlalchemy import exc, create_engine
from sqlalchemy.orm import Session
from tables import Film
from tables import User
from tables import Rating
from tables import Hall
from tables import Ticket

class Model():
    def __init__(self):
        self.engine = create_engine("postgres://postgres:Nuva2002@localhost/coursework")

        self.sess = Session(bind=self.engine)
        self.db = psycopg2.connect(database="coursework",
                                   user="postgres",
                                   password="Nuva2002",
                                   host="127.0.0.1",
                                   port="5432")
        self.cur = self.db.cursor()

    def get(self, type_entity):
        try:
            q = []
            q = self.sess.query(type_entity)

        except(Exception, exc.DatabaseError, exc.InvalidRequestError) as error:
            print(error)
            self.sess.rollback()
        return q


    def get_by_id(self,id, type_entity):
        try:
            q = []
            q = self.sess.query(type_entity).get(id)

        except(Exception, exc.DatabaseError, exc.InvalidRequestError) as error:
            print(error)
            self.sess.rollback()
        return q


    def add(self, entity):
        try:
            self.sess.add(entity)
            self.sess.commit()
        except(Exception, exc.DatabaseError, exc.InvalidRequestError) as error:
            print(error)
            self.sess.rollback()
            return False
        return True

    def update(self, update_entity):
        try:
            self.sess.add(update_entity)
            self.sess.commit()
        except(Exception, exc.DatabaseError, exc.InvalidRequestError) as error:
            print(error)
            self.sess.rollback()
            return False
        return True

    def delete(self, id, type_entity):
        try:
            entity = self.get_by_id(id, type_entity)
            self.sess.delete(entity)
            self.sess.commit()
        except(Exception, exc.DatabaseError, exc.InvalidRequestError) as error:
            print(error)
            self.sess.rollback()
            return False
        return True
