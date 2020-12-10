from controller import Controller
import hashlib
from datetime import datetime
from datetime import time

controller = Controller()
while True:
    print("Enter 1 if you want to work with films")
    print("Enter 2 if you want to work with users")
    print("Enter 3 if you want to work with halls")
    print("Enter 4 if you want to work with ratings")
    print("Enter 5 if you want to work with tickets")
    print("Enter 6 if you want to work with requests")
    print("Enter 7 if you want to look graph")
    print("Enter 0 if you want to exit")
    inp = input()
    if inp == '1':
        while True:
            print("Enter 1 if you want to get films")
            print("Enter 2 if you want to get film by id")
            print("Enter 3 if you want to add film")
            print("Enter 4 if you want to update film")
            print("Enter 5 if you want to delete film by id")
            print("Enter 6 if you want to generate films")
            print("Enter 0 if you want to go to menu")
            inp = input()
            if inp == '1':
                controller.print_films()
            elif inp == '2':
                while True:
                    try:
                        id = int(input("Enter id of film: "))
                        break
                    except ValueError:
                        print("Error! Try again: ")
                controller.print_film(int(id))
            elif inp == '3':
                print("Enter title of film:")
                title = input()
                print("Enter genre of film:")
                genre = input()
                print("Enter country of film:")
                country = input()
                while True:
                    try:
                        year = int(input("Enter year of film: "))
                        if 1895 > year or year > 2020:
                            print('Wrong year')
                            continue
                        else:
                            break
                    except ValueError:
                        print("Error! Try again: ")
                while True:
                    try:
                        released = bool(input("Enter released of film: "))
                        break
                    except ValueError:
                        print("Error! Try again: ")
                controller.add_film(title, genre, country, year, released)
            elif inp == '4':
                while True:
                    try:
                        id = int(input("Enter id of film: "))
                        break
                    except ValueError:
                        print("Error! Try again: ")
                print("Enter title of film:")
                title = input()
                print("Enter genre of film:")
                genre = input()
                print("Enter country of film:")
                country = input()
                while True:
                    try:
                        year = int(input("Enter year of film: "))
                        if 1895 > year or year > 2020:
                            print('Wrong year')
                            continue
                        else:
                            break
                    except ValueError:
                        print("Error! Try again: ")
                while True:
                    try:
                        released = bool(input("Enter released of film: "))
                        break
                    except ValueError:
                        print("Error! Try again: ")
                controller.update_film(id, title, genre, country, year, released)
            elif inp == '5':
                while True:
                    try:
                        id = int(input("Enter id of film: "))
                        break
                    except ValueError:
                        print("Error! Try again: ")
                controller.delete_film(int(id))
            elif inp == '0':
                break
            elif inp == '6':
                while True:
                    try:
                        num = int(input("Enter amount of pages data: "))
                        break
                    except ValueError:
                        print("Error! Try again: ")
                controller.generation_films(num)
            else:
                print("Incorrect number")
    elif inp == '2':
        while True:
            print("Enter 1 if you want to get users")
            print("Enter 2 if you want to get user by id")
            print("Enter 3 if you want to add user")
            print("Enter 4 if you want to update user")
            print("Enter 5 if you want to delete user by id")
            print("Enter 6 if you want to generate users")
            print("Enter 0 if you want to go to menu")
            inp = input()
            if inp == '1':
                controller.print_users()
            elif inp == '2':
                while True:
                    try:
                        id = int(input("Enter id of user: "))
                        break
                    except ValueError:
                        print("Error! Try again: ")
                controller.print_user(int(id))
            elif inp == '3':
                print("Enter login of user:")
                login = input()
                print("Enter fullname of user:")
                fullname = input()
                print("Enter password of user:")
                password = input()
                password_hash = hashlib.md5(password.encode())
                controller.add_user(login, fullname, password_hash.hexdigest())
            elif inp == '4':
                while True:
                    try:
                        id = int(input("Enter id of user: "))
                        break
                    except ValueError:
                        print("Error! Try again: ")
                print("Enter login of user:")
                login = input()
                print("Enter fullname of user:")
                fullname = input()
                print("Enter password of user:")
                password = input()
                password_hash = hashlib.md5(password.encode())
                controller.update_user(id, login, fullname, password_hash.hexdigest())
            elif inp == '5':
                while True:
                    try:
                        id = int(input("Enter id of user: "))
                        break
                    except ValueError:
                        print("Error! Try again: ")
                controller.delete_user(int(id))
            elif inp == '0':
                break
            elif inp == '6':
                while True:
                    try:
                        num = int(input("Enter amount of random data: "))
                        break
                    except ValueError:
                        print("Error! Try again: ")
                controller.generation_users(int(num))
            else:
                print("Incorrect number")

    elif inp == '3':
        while True:
            print("Enter 1 if you want to get halls")
            print("Enter 2 if you want to get hall by id")
            print("Enter 3 if you want to add hall")
            print("Enter 4 if you want to update hall")
            print("Enter 5 if you want to delete hall by id")
            print("Enter 6 if you want to add random data")
            print("Enter 0 if you want to go to menu")
            inp = input()
            if inp == '1':
                controller.print_halls()
            elif inp == '2':
                while True:
                    try:
                        id = int(input("Enter id of hall: "))
                        break
                    except ValueError:
                        print("Error! Try again: ")
                controller.print_hall(int(id))
            elif inp == '3':
                print("Enter name of hall:")
                name = input()
                print(name)
                while True:
                    try:
                        amount_of_seats = int(input("Enter amount_of_seats of hall: "))
                        break
                    except ValueError:
                        print("Error! Try again: ")
                print("Enter type_of_hall of hall:")
                type_of_hall = input()
                controller.add_hall(name, amount_of_seats, type_of_hall)
            elif inp == '4':
                while True:
                    try:
                        id = int(input("Enter id of hall: "))
                        break
                    except ValueError:
                        print("Error! Try again: ")
                print("Enter name of hall:")
                name = input()
                while True:
                    try:
                        amount_of_seats = int(input("Enter amount_of_seats of hall: "))
                        break
                    except ValueError:
                        print("Error! Try again: ")
                print("Enter type_of_hall of hall:")
                type_of_hall = input()
                controller.update_hall(int(id), name, amount_of_seats, type_of_hall)
            elif inp == '5':
                while True:
                    try:
                        id = int(input("Enter id of hall: "))
                        break
                    except ValueError:
                        print("Error! Try again: ")
                controller.delete_hall(int(id))
            elif inp == '0':
                break
            elif inp == '6':
                while True:
                    try:
                        num = int(input("Enter amount of random data: "))
                        break
                    except ValueError:
                        print("Error! Try again: ")
                controller.generation_halls(num)
            else:
                print("Incorrect number")

    elif inp == '4':
        while True:
            print("Enter 1 if you want to get ratings")
            print("Enter 2 if you want to get rating by id")
            print("Enter 3 if you want to add rating")
            print("Enter 4 if you want to update rating")
            print("Enter 5 if you want to delete rating by id")
            print("Enter 6 if you want to add random data")
            print("Enter 0 if you want to go to menu")
            inp = input()
            if inp == '1':
                controller.print_ratings()
            elif inp == '2':
                while True:
                    try:
                        id = int(input("Enter id of rating: "))
                        break
                    except ValueError:
                        print("Error! Try again: ")
                controller.print_rating(id)
            elif inp == '3':
                while True:
                    try:
                        film_id = int(input("Enter film_id of rating: "))
                        break
                    except ValueError:
                        print("Error! Try again: ")
                while True:
                    try:
                        user_id = int(input("Enter user_id of rating: "))
                        break
                    except ValueError:
                        print("Error! Try again: ")
                while True:
                    try:
                        evaluation = int(input("Enter evaluation(1-10) of rating: "))
                        if 0 < evaluation < 11:
                            break
                    except ValueError:
                        print("Error! Try again: ")
                controller.add_rating(film_id, user_id, evaluation)
            elif inp == '4':
                while True:
                    try:
                        id = int(input("Enter id of hall: "))
                        break
                    except ValueError:
                        print("Error! Try again: ")
                while True:
                    try:
                        film_id = int(input("Enter film_id of rating: "))
                        break
                    except ValueError:
                        print("Error! Try again: ")
                while True:
                    try:
                        user_id = int(input("Enter user_id of rating: "))
                        break
                    except ValueError:
                        print("Error! Try again: ")
                while True:
                    try:
                        evaluation = int(input("Enter evaluation(1-10) of rating: "))
                        if 0 < evaluation < 11:
                            break
                    except ValueError:
                        print("Error! Try again: ")
                controller.update_rating(int(id), film_id, user_id, evaluation)
            elif inp == '5':
                while True:
                    try:
                        id = int(input("Enter id of rating: "))
                        break
                    except ValueError:
                        print("Error! Try again: ")
                controller.delete_rating(int(id))
            elif inp == '0':
                break
            elif inp == '6':
                while True:
                    try:
                        num = int(input("Enter amount of random data: "))
                        break
                    except ValueError:
                        print("Error! Try again: ")
                controller.generation_ratings(num)
            else:
                print("Incorrect number")

    elif inp == '5':
        while True:
            print("Enter 1 if you want to get tickets")
            print("Enter 2 if you want to get ticket by id")
            print("Enter 3 if you want to add ticket")
            print("Enter 4 if you want to update ticket")
            print("Enter 5 if you want to delete ticket by id")
            print("Enter 6 if you want to add random data")
            print("Enter 0 if you want to go to menu")
            inp = input()
            if inp == '1':
                controller.print_tickets()
            elif inp == '2':
                while True:
                    try:
                        id = int(input("Enter id of ticket: "))
                        break
                    except ValueError:
                        print("Error! Try again: ")
                controller.print_ticket(id)
            elif inp == '3':
                while True:
                    try:
                        user_id = int(input("Enter user_id of ticket: "))
                        break
                    except ValueError:
                        print("Error! Try again: ")
                while True:
                    try:
                        film_id = int(input("Enter film_id of ticket: "))
                        break
                    except ValueError:
                        print("Error! Try again: ")
                while True:
                    try:
                        hall_id = int(input("Enter hall_id of ticket: "))
                        break
                    except ValueError:
                        print("Error! Try again: ")
                while True:
                    try:
                        row_number = int(input("Enter row_number of ticket: "))
                        break
                    except ValueError:
                        print("Error! Try again: ")
                while True:
                    try:
                        seat_number = int(input("Enter seat_number of ticket: "))
                        break
                    except ValueError:
                        print("Error! Try again: ")
                while True:
                    time = input('Enter date_time (Y-m-d hh:mm:ss): ')
                    try:
                        date_time = datetime.strptime(time, '%Y-%m-%d %H:%M:%S')
                        break
                    except ValueError:
                        print('Invalid time!')
                while True:
                    try:
                        price = int(input("Enter price of ticket: "))
                        break
                    except ValueError:
                        print("Error! Try again: ")
                controller.add_ticket(user_id, film_id, hall_id, row_number, seat_number, date_time, price)
            elif inp == '4':
                while True:
                    try:
                        id = int(input("Enter id of ticket: "))
                        break
                    except ValueError:
                        print("Error! Try again: ")
                while True:
                    try:
                        user_id = int(input("Enter user_id of ticket: "))
                        break
                    except ValueError:
                        print("Error! Try again: ")
                while True:
                    try:
                        film_id = int(input("Enter film_id of ticket: "))
                        break
                    except ValueError:
                        print("Error! Try again: ")
                while True:
                    try:
                        hall_id = int(input("Enter hall_id of ticket: "))
                        break
                    except ValueError:
                        print("Error! Try again: ")
                while True:
                    try:
                        row_number = int(input("Enter row_number of ticket: "))
                        break
                    except ValueError:
                        print("Error! Try again: ")
                while True:
                    try:
                        seat_number = int(input("Enter seat_number of ticket: "))
                        break
                    except ValueError:
                        print("Error! Try again: ")
                while True:
                    time = input('Enter date_time (Y-m-d hh:mm:ss): ')
                    try:
                        date_time = datetime.strptime(time, '%Y-%m-%d %H:%M:%S')
                        break
                    except ValueError:
                        print('Invalid time!')
                while True:
                    try:
                        price = int(input("Enter price of ticket: "))
                        break
                    except ValueError:
                        print("Error! Try again: ")
                controller.update_ticket(id, user_id, film_id, hall_id, row_number, seat_number, date_time, price)
            elif inp == '5':
                while True:
                    try:
                        id = int(input("Enter id of ticket: "))
                        break
                    except ValueError:
                        print("Error! Try again: ")
                controller.delete_ticket(id)
            elif inp == '0':
                break
            elif inp == '6':
                while True:
                    try:
                        num = int(input("Enter amount of random data: "))
                        break
                    except ValueError:
                        print("Error! Try again: ")
                controller.generation_tickets(num)
            else:
                print("Incorrect number")
    elif inp == '0':
        break
    elif inp == '6':
        while True:
            print("Enter 1 to look best films of genre")
            print("Enter 2 to look best films of year")
            print("Enter 3 to choose film for user")
            print("Enter 0 if you want to go to menu")
            inp = input()
            if inp == '1':
                genre = input("Enter genre: ")
                controller.best_films_in_genre(genre)
            elif inp == '2':
                while True:
                    try:
                        year = int(input("Enter year: "))
                        if 1895 > year or year > 2020:
                            print('Wrong year')
                            continue
                        else:
                            break

                    except ValueError:
                        print("Error! Try again: ")

                controller.best_films_in_years(year)
            elif inp == '3':
                while True:
                    try:
                        id = int(input("Enter id of user: "))
                        break
                    except ValueError:
                        print("Error! Try again: ")
                controller.choose_films(id)
            elif inp == '0':
                break
            else:
                print("Incorrect number")
    elif inp == '7':
        while True:
            print("Enter 1 to look statistics on genres(site)")
            print("Enter 2 to look statistics on years(site)")
            print("Enter 3 to look statistics on halls(cinema)")
            print("Enter 4 to look statistics on genres(cinema)")
            print("Enter 0 if you want to go to menu")
            inp = input()
            if inp == '1':
                controller.graph_genre()
            elif inp == '2':
                controller.graph_years()
            elif inp == '3':
                controller.graph_hall()
            elif inp == '4':
                controller.graph_ticket_genre()
            elif inp == '0':
                break
            else:
                print("Incorrect number")
    else:
        print("Incorrect number")
