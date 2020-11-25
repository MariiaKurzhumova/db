from model import Model
from model import Film
from model import Session
from model import Connection
from model import Hall
from model import Seat_row

model = Model()
class Controller:
    def print_films(self):
        films = model.get_films()
        for film in films:
            print("Film: ")
            print(film.id, film.duration, film.year, film.title,film.rating, film.description, film.director)

    def print_film(self, id):
        film = model.get_film_by_id(id)
        print("Film: ")
        print( film.id, film.duration, film.year, film.title, film.description, film.director)

    def init_add_film(self, duration, year, title, description, rating, director):
        bl = model.add_film(duration, year, title, description, rating, director)
        if bl:
            print("New record was added in db")
        else:
            print("Error: New record wasn't added in db!")

    def init_update_film(self, id, duration, year, title, description, rating, director):
        film = model.get_film_by_id(id)
        film.duration = duration
        film.year = year
        film.title = title
        film.description = description
        film.rating = rating
        film.director = director
        bl = model.update_film(film)
        if bl:
            print("Record was updated")
        else:
            print("Error: Record wasn't updated!")

    def print_delete_film(self, id):
        bl = model.delete_film(id)
        if bl:
            print("Record was deleted")
        else:
            print("Error: Record wasn't deleted!")

    def print_sessions(self):
        sessions = model.get_sessions()
        for session in sessions:
            print("Session: ")
            print(session.id, session.start_time, session.end_time, session.price, session.hall_id, session.data)

    def print_session(self, id):
        session = model.get_session_by_id(id)
        print("Session: ")
        print( session.start_time, session.end_time, session.price, session.hall_id, session.data)

    def init_add_session(self, start_time, end_time, price, hall_id, data):
        bl = model.add_session(start_time, end_time, price, hall_id, data)
        if bl:
            print("New record was added in db")
        else:
            print("Error: New record wasn't added in db!")

    def init_update_session(self, id, start_time, end_time, price, hall_id, data):
        session = model.get_session_by_id(id)
        session.start_time = start_time
        session.end_time = end_time
        session.price = price
        session.hall_id = hall_id
        session.data = data
        bl = model.update_session(session)
        if bl:
            print("Record was updated")
        else:
            print("Error: Record wasn't updated!")

    def print_delete_session(self, id):
        bl = model.delete_session(id)
        if bl:
            print("Record was deleted")
        else:
            print("Error: Record wasn't deleted!")

    def print_film_sessions(self):
        connections = model.get_film_session()
        for connection in connections:
            print("Connections: ")
            print(connection.id, connection.id_film, connection.id_session)

    def init_add_film_session(self, film_id, session_id):
        bl = model.add_film_session(film_id, session_id)
        if bl:
            print("New record was added in db")
        else:
            print("Error: New record wasn't added in db!")

    def print_delete_film_session(self, id):
        bl = model.delete_film_session(id)
        if bl:
            print("Record was deleted")
        else:
            print("Error: Record wasn't deleted!")

    def print_halls(self):
        halls = model.get_halls()
        for hall in halls:
            print("Hall: ")
            print(hall.id, hall.number, hall.amount_of_seats, hall.seats_rows_id, hall.type_of_hall)

    def print_hall(self, id):
        hall = model.get_hall_by_id(id)
        print("Hall: ")
        print( hall.id, hall.number, hall.amount_of_seats, hall.seats_rows_id, hall.type_of_hall)

    def init_add_hall(self, number, amount_of_seats, seats_rows_id, type_of_hall):
        bl = model.add_hall(number, amount_of_seats, seats_rows_id, type_of_hall)
        if bl:
            print("New record was added in db")
        else:
            print("Error: New record wasn't added in db!")

    def init_update_hall(self, id, number, amount_of_seats, seats_rows_id, type_of_hall):
        hall = model.get_hall_by_id(id)
        hall.number = number
        hall.amount_of_seats = amount_of_seats
        hall.seats_rows_id = seats_rows_id
        hall.type_of_hall = type_of_hall
        bl = model.update_hall(hall)
        if bl:
            print("Record was updated")
        else:
            print("Error: Record wasn't updated!")

    def print_delete_hall(self, id):
        bl = model.delete_hall(id)
        if bl:
            print("Record was deleted")
        else:
            print("Error: Record wasn't deleted!")

    def print_seats_rows(self):
        seats_rows = model.get_seats_rows()
        for seat_row in seats_rows:
            print("Seat_row: ")
            print(seat_row.id, seat_row.row_number, seat_row.seat_number, seat_row.type_of_seat)

    def print_seat_row(self, id):
        seat_row = model.get_seat_row_by_id(id)
        print("Seat_row: ")
        print( seat_row.id, seat_row.row_number, seat_row.seat_number, seat_row.type_of_seat)

    def init_add_seat_row(self, row_number, seat_number, type_of_seat):
        bl = model.add_seat_row(row_number, seat_number, type_of_seat)
        if bl:
            print("New record was added in db")
        else:
            print("Error: New record wasn't added in db!")

    def init_update_seat_row(self, id, row_number, seat_number, type_of_seat):
        seat_row = model.get_seat_row_by_id(id)
        seat_row.row_number = row_number
        seat_row.seat_number = seat_number
        seat_row.type_of_seat = type_of_seat
        bl = model.update_seat_row(seat_row)
        if bl:
            print("Record was updated")
        else:
            print("Error: Record wasn't updated!")

    def print_delete_seat_row(self, id):
        bl = model.delete_seat_row(id)
        if bl:
            print("Record was deleted")
        else:
            print("Error: Record wasn't deleted!")
            
    def init_random_seats_rows(self, num):
        r = model.random_seats_rows(num)
        if r:
            print("Data added successfully")
        else:
            print("Data not added")
    def init_random_halls(self, num):
        r = model.random_halls(num)
        if r:
            print("Data added successfully")
        else:
            print("Data not added")
    def init_random_sessions(self, num):
        r = model.random_sessions(num)
        if r:
            print("Data added successfully")
        else:
            print("Data not added")
    def init_random_films(self, num):
        r = model.random_films(num)
        if r:
            print("Data added successfully")
        else:
            print("Data not added")
    def init_random_film_session(self, num):
        r = model.random_film_session(num)
        if r:
            print("Data added successfully")
        else:
            print("Data not added")
    def request_sessions(self, start_time, price):
        list = model.select_sessions(start_time, price)
        for l in list:
         print(l)
    def request_films(self, year):
        list = model.select_films(year)
        for l in list:
         print(l)
    def request_seats_rows(self, row_number):
        list = model.select_seats_rows(row_number)
        for l in list:
         print(l)