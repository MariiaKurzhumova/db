from model import Model
from tables import Film
from tables import User
from tables import Rating
from tables import Hall
from tables import Ticket
from generation import Generation

model = Model()
generator = Generation()
class Controller:
    def print_films(self):
        films = model.get(Film)
        if films is None:
            print('There is no such entities')
        else:
            for film in films:
                print("Film: ")
                print(film.id, film.title, film.genre, film.country, film.year, film.released)

    def print_film(self, id):
        film = model.get_by_id(id, Film)
        if film is None:
            print('There is no such entity')
        else:
            print("Film: ")
            print(film.id, film.title, film.genre, film.country, film.year, film.released)

    def add_film(self, title, genre, country, year, released):
        film = Film(title, genre, country, year, released)
        bl = model.add(film)
        if bl:
            print("New record was added in db")
        else:
            print("Error: New record wasn't added in db!")

    def update_film(self, id,  title, genre, country, year, released):
        film = model.get_by_id(id, Film)
        film.title = title
        film.genre = genre
        film.country = country
        film.year = year
        film.released = released
        bl = model.update(film)
        if bl:
            print("Record was updated")
        else:
            print("Error: Record wasn't updated!")

    def delete_film(self, id):
        bl = model.delete(id, Film)
        if bl:
            print("Record was deleted")
        else:
            print("Error: Record wasn't deleted!")
    def print_halls(self):
        halls = model.get(Hall)
        if halls is None:
            print('There is no such entities')
        else:
            for hall in halls:
                print("Hall: ")
                print(hall.id, hall.name, hall.amount_of_seats, hall.type_of_hall)

    def print_hall(self, id):
        hall = model.get_by_id(id, Hall)
        if hall is None:
            print('There is no such entities')
        else:
            print("Hall: ")
            print(hall.id, hall.name, hall.amount_of_seats, hall.type_of_hall)

    def add_hall(self, name, amount_of_seats, type_of_hall):
        hall = Hall(name, amount_of_seats, type_of_hall)
        bl = model.add(hall)
        if bl:
            print("New record was added in db")
        else:
            print("Error: New record wasn't added in db!")

    def update_hall(self, id,  name, amount_of_seats, type_of_hall):
        hall = model.get_by_id(id, Hall)
        hall.name = name
        hall.amount_of_seats = amount_of_seats
        hall.type_of_hall = type_of_hall
        bl = model.update(hall)
        if bl:
            print("Record was updated")
        else:
            print("Error: Record wasn't updated!")

    def delete_hall(self, id):
        bl = model.delete(id, Hall)
        if bl:
            print("Record was deleted")
        else:
            print("Error: Record wasn't deleted!")

    def print_users(self):
        users = model.get(User)
        if users is None:
            print('There is no such entities')
        else:
            for user in users:
                print("User: ")
                print(user.id, user.login, user.fullname, user.password_hash)

    def print_user(self, id):
        user = model.get_by_id(id, User)
        if user is None:
            print('There is no such entities')
        else:
            print("User: ")
            print(user.id, user.login, user.fullname, user.password_hash)


    def add_user(self, login, fullname, password_hash):
        user = User(login, fullname, password_hash)
        bl = model.add(user)
        if bl:
            print("New record was added in db")
        else:
            print("Error: New record wasn't added in db!")

    def update_user(self, id, login, fullname, password_hash):
        user = model.get_by_id(id, User)
        user.login = login
        user.fullname = fullname
        user.password_hash = password_hash
        bl = model.update(user)
        if bl:
            print("Record was updated")
        else:
            print("Error: Record wasn't updated!")

    def delete_user(self, id):
        bl = model.delete(id, User)
        if bl:
            print("Record was deleted")
        else:
            print("Error: Record wasn't deleted!")
    def print_ratings(self):
        ratings = model.get(Rating)
        if ratings is None:
            print('There is no such entities')
        else:
            for rating in ratings:
                print("Rating: ")
                print(rating.id, rating.film_id, rating.user_id, rating.evaluation)

    def print_rating(self, id):
        rating = model.get_by_id(id, Rating)
        if rating is None:
            print('There is no such entities')
        else:
            print("Rating: ")
            print(rating.film_id, rating.user_id, rating.evaluation)


    def add_rating(self, film_id, user_id, evaluation):
        rating = Rating(film_id, user_id, evaluation)
        bl = model.add(rating)
        if bl:
            print("New record was added in db")
        else:
            print("Error: New record wasn't added in db!")

    def update_rating(self, id, film_id, user_id, evaluation):
        rating = model.get_by_id(id, Rating)
        rating.film_id = film_id
        rating.user_id = user_id
        rating.evaluation = evaluation
        bl = model.update(rating)
        if bl:
            print("Record was updated")
        else:
            print("Error: Record wasn't updated!")

    def delete_rating(self, id):
        bl = model.delete(id, Rating)
        if bl:
            print("Record was deleted")
        else:
            print("Error: Record wasn't deleted!")
    def print_tickets(self):
        tickets = model.get(Ticket)
        if tickets is None:
            print('There is no such entities')
        else:
            for ticket in tickets:
                print("Tickets: ")
                print(ticket.id, ticket.user_id, ticket.film_id,
                      ticket.hall_id, ticket.row_number, ticket.seat_number, ticket.date_time, ticket.price)

    def print_ticket(self, id):
        ticket = model.get_by_id(id, Ticket)
        if ticket is None:
            print('There is no such entities')
        else:
            print("Ticket: ")
            print(ticket.id, ticket.user_id, ticket.film_id,
                  ticket.hall_id, ticket.row_number, ticket.seat_number, ticket.date_time, ticket.price)


    def add_ticket(self, user_id, film_id, hall_id, row_number, seat_number, date_time, price):
        ticket = Ticket(user_id, film_id, hall_id, row_number,
                        seat_number, date_time, price)
        bl = model.add(ticket)
        if bl:
            print("New record was added in db")
        else:
            print("Error: New record wasn't added in db!")

    def update_ticket(self, id, user_id, film_id, hall_id, row_number, seat_number, date_time, price):
        ticket = model.get_by_id(id, Ticket)
        ticket.user_id = user_id
        ticket.film_id = film_id
        ticket.hall_id = hall_id
        ticket.row_number = row_number
        ticket.seat_number = seat_number
        ticket.date_time = date_time
        ticket.price = price
        bl = model.update(ticket)
        if bl:
            print("Record was updated")
        else:
            print("Error: Record wasn't updated!")

    def delete_ticket(self, id):
        bl = model.delete(id, Ticket)
        if bl:
            print("Record was deleted")
        else:
            print("Error: Record wasn't deleted!")

    def generation_films(self, num):
        bl = generator.generator_films(num)
        if bl:
            print("Record was added")
        else:
            print("Error: Record wasn't added!")

    def generation_users(self, num):
        bl = generator.generator_users(num)
        if bl:
            print("Record was added")
        else:
            print("Error: Record wasn't added!")

    def generation_halls(self, num):
        bl = generator.generator_halls(num)
        if bl:
            print("Record was added")
        else:
            print("Error: Record wasn't added!")

    def generation_ratings(self, num):
        bl = generator.generator_ratings(num)
        if bl:
            print("Record was added")
        else:
            print("Error: Record wasn't added!")

    def generation_tickets(self, num):
        bl = generator.generator_tickets(num)
        if bl:
            print("Record was added")
        else:
            print("Error: Record wasn't added!")

    def best_films_in_genre(self, genre):
        q = generator.best_films_in_genre(genre)
        if q is None:
            print('There is no such films')
        else:
            for i in q:
                print(i)

    def best_films_in_years(self, year):
        q = generator.best_films_in_years(year)
        if q is None:
            print('There is no such films')
        else:
            for i in q:
                print(i)
    def choose_films(self, id):
        q = generator.choose_movie(id)
        if q is None:
            print('There is no such user')
        else:
            for i in q:
                print(i)

    def graph_genre(self):
        generator.graph_for_genres()

    def graph_years(self):
        generator.graph_for_years()

    def graph_hall(self):
        generator.graph_for_halls()

    def graph_ticket_genre(self):
        generator.graph_for_ticket()