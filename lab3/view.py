from controller import Controller
from datetime import datetime
from datetime import time
controller = Controller()
while True:
    print("Enter 1 if you want to work with films")
    print("Enter 2 if you want to work with sessions")
    print("Enter 12 if you want to work with film_sessions")
    print("Enter 3 if you want to work with halls")
    print("Enter 4 if you want to work with seats_rows")
    print("Enter 0 if you want to exit")
    inp = input()
    if inp == '1':
        while True:
            print("Enter 1 if you want to get films")
            print("Enter 2 if you want to get film by id")
            print("Enter 3 if you want to add film")
            print("Enter 4 if you want to update film")
            print("Enter 5 if you want to delete film by id")
            print("Enter 6 if you want to add random data")
            print("Enter 7 if you want to request")
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
                while True:
                    time = input('Enter duration (hh:mm:ss): ')
                    try:
                        duration = datetime.strptime(time, '%H:%M:%S')
                        break
                    except ValueError:
                        print('Invalid time!')
                while True:
                    try:
                        year = int(input("Enter year of film: "))
                        break
                    except ValueError:
                        print("Error! Try again: ")
                print("Enter title of film:")
                title = input()
                print("Enter description of film:")
                description = input()
                print("Enter rating of film:")
                rating = input()
                print("Enter director of film:")
                director = input()
                controller.init_add_film(duration, year, title, description, rating, director)
            elif inp == '4':
                while True:
                    try:
                        id = int(input("Enter id of film: "))
                        break
                    except ValueError:
                        print("Error! Try again: ")
                while True:
                    time = input('Enter duration (hh:mm:ss): ')
                    try:
                        duration = datetime.strptime(time, '%I:%M:%S')
                        break
                    except ValueError:
                        print('Invalid time!')
                while True:
                    try:
                        year = int(input("Enter year of film: "))
                        break
                    except ValueError:
                        print("Error! Try again: ")
                print("Enter title of film:")
                title = input()
                print("Enter description of film:")
                description = input()
                print("Enter rating of film:")
                rating = input()
                print("Enter director of film:")
                director = input()
                controller.init_update_film(id, duration, year, title, description, rating, director)
            elif inp == '5':
                while True:
                    try:
                        id = int(input("Enter id of film: "))
                        break
                    except ValueError:
                        print("Error! Try again: ")
                controller.print_delete_film(int(id))
            elif inp == '0':
                break
            elif inp == '6':
                while True:
                    try:
                        num = int(input("Enter amount of random data: "))
                        break
                    except ValueError:
                        print("Error! Try again: ")
                controller.init_random_films(int(num))
            elif inp == '7':
                while True:
                    try:
                        year = int(input("Enter year of film: "))
                        break
                    except ValueError:
                        print("Error! Try again: ")
                controller.request_films(year)
            else:
                print("Incorrect number")
    elif inp == '2':
        while True:
            print("Enter 1 if you want to get sessions")
            print("Enter 2 if you want to get session by id")
            print("Enter 3 if you want to add session")
            print("Enter 4 if you want to update session")
            print("Enter 5 if you want to delete session by id")
            print("Enter 6 if you want to add random data")
            print("Enter 7 if you want to request")
            print("Enter 0 if you want to go to menu")
            inp = input()
            if inp == '1':
                controller.print_sessions()
            elif inp == '2':
                while True:
                    try:
                        id = int(input("Enter id of session: "))
                        break
                    except ValueError:
                        print("Error! Try again: ")
                controller.print_session(int(id))
            elif inp == '3':
                while True:
                    time = input('Enter start_time (hh:mm:ss): ')
                    try:
                        start_time = datetime.strptime(time, '%H:%M:%S')
                        break
                    except ValueError:
                        print('Invalid time!')
                while True:
                    t = input('Enter end_time (hh:mm:ss): ')
                    try:
                        end_time = datetime.strptime(t, '%H:%M:%S')
                        break
                    except ValueError:
                        print('Invalid time!')
                while True:
                    try:
                        price = int(input("Enter price of session: "))
                        break
                    except ValueError:
                        print("Error! Try again: ")
                while True:
                    try:
                        hall_id = int(input("Enter hall id: "))
                        break
                    except ValueError:
                        print("Error! Try again: ")
                while True:
                    time = input('Date (yyyy-mm-dd): ')
                    try:
                        data = datetime.strptime(time, '%Y-%m-%d')
                        break
                    except ValueError:
                        print('Invalid date!')
                controller.init_add_session(start_time, end_time, price, int(hall_id), data)
            elif inp == '4':
                while True:
                    try:
                        id = int(input("Enter id of session: "))
                        break
                    except ValueError:
                        print("Error! Try again: ")
                while True:
                    time = input('Enter start_time (hh:mm:ss): ')
                    try:
                        start_time = datetime.strptime(time, '%H:%M:%S')
                        break
                    except ValueError:
                        print('Invalid time!')
                while True:
                    time = input('Enter end_time (hh:mm:ss): ')
                    try:
                        end_time = datetime.strptime(time, '%H:%M:%S')
                        break
                    except ValueError:
                        print('Invalid time!')
                while True:
                    try:
                        price = int(input("Enter price of session: "))
                        break
                    except ValueError:
                        print("Error! Try again: ")
                while True:
                    try:
                        hall_id = int(input("Enter hall id: "))
                        break
                    except ValueError:
                        print("Error! Try again: ")
                while True:
                    time = input('Date (yyyy-mm-dd): ')
                    try:
                        data = datetime.strptime(time, '%Y-%m-%d')
                        break
                    except ValueError:
                        print('Invalid date!')
                controller.init_update_session(int(id), start_time, end_time, price, hall_id, data)
            elif inp == '5':
                while True:
                    try:
                        id = int(input("Enter id of session: "))
                        break
                    except ValueError:
                        print("Error! Try again: ")
                controller.print_delete_session(int(id))
            elif inp == '0':
                break
            elif inp == '6':
                while True:
                    try:
                        num = int(input("Enter amount of random data: "))
                        break
                    except ValueError:
                        print("Error! Try again: ")
                controller.init_random_sessions(int(num))
            elif inp == '7':
                start_time = input('Enter start_time (hh:mm:ss):')
                while True:
                    try:
                        price = int(input("Enter price of session: "))
                        break
                    except ValueError:
                        print("Error! Try again: ")
                controller.request_sessions(start_time, price)
            else:
                print("Incorrect number")
    elif inp == '12':
        while True:
            print("Enter 1 if you want to get films_sessions")
            print("Enter 2 if you want to add films_sessions")
            print("Enter 3 if you want to delete films_sessions by id")
            print("Enter 4 if you want to add random data")
            print("Enter 0 if you want to go to menu")
            inp = input()
            if inp == '1':
                controller.print_film_sessions()
            elif inp == '2':
                while True:
                    try:
                        film_id = int(input("Enter film id: "))
                        break
                    except ValueError:
                        print("Error! Try again: ")
                while True:
                    try:
                        session_id = int(input("Enter session id: "))
                        break
                    except ValueError:
                        print("Error! Try again: ")
                controller.init_add_film_session(int(film_id), int(session_id))
            elif inp == '3':
                while True:
                    try:
                        id = int(input("Enter id of film_session: "))
                        break
                    except ValueError:
                        print("Error! Try again: ")
                controller.print_delete_film_session(int(id))
            elif inp == '0':
                break
            elif inp == '4':
                while True:
                    try:
                        num = int(input("Enter amount of random data: "))
                        break
                    except ValueError:
                        print("Error! Try again: ")
                controller.init_random_film_session(int(num))
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
                while True:
                    try:
                        number = int(input("Enter number of hall: "))
                        break
                    except ValueError:
                        print("Error! Try again: ")
                while True:
                    try:
                        amount_of_seats = int(input("Enter amount_of_seats of hall: "))
                        break
                    except ValueError:
                        print("Error! Try again: ")
                while True:
                    try:
                        seats_rows_id = int(input("Enter seats_rows_id of hall: "))
                        break
                    except ValueError:
                        print("Error! Try again: ")
                print("Enter type_of_hall of hall:")
                type_of_hall = input()
                controller.init_add_hall(number, amount_of_seats, int(seats_rows_id), type_of_hall)
            elif inp == '4':
                while True:
                    try:
                        id = int(input("Enter id of hall: "))
                        break
                    except ValueError:
                        print("Error! Try again: ")
                while True:
                    try:
                        number = int(input("Enter number of hall: "))
                        break
                    except ValueError:
                        print("Error! Try again: ")
                while True:
                    try:
                        amount_of_seats = int(input("Enter amount_of_seats of hall: "))
                        break
                    except ValueError:
                        print("Error! Try again: ")
                while True:
                    try:
                        seats_rows_id = int(input("Enter seats_rows_id of hall: "))
                        break
                    except ValueError:
                        print("Error! Try again: ")
                print("Enter type_of_hall of hall:")
                type_of_hall = input()
                controller.init_update_hall(int(id), number, amount_of_seats, seats_rows_id, type_of_hall)
            elif inp == '5':
                while True:
                    try:
                        id = int(input("Enter id of hall: "))
                        break
                    except ValueError:
                        print("Error! Try again: ")
                controller.print_delete_hall(int(id))
            elif inp == '0':
                break
            elif inp == '6':
                while True:
                    try:
                        num = int(input("Enter amount of random data: "))
                        break
                    except ValueError:
                        print("Error! Try again: ")
                controller.init_random_halls(int(num))
            else:
                print("Incorrect number")
    elif inp == '4':
        while True:
            print("Enter 1 if you want to get seats_rows")
            print("Enter 2 if you want to get seat_row by id")
            print("Enter 3 if you want to add seat_row")
            print("Enter 4 if you want to update seat_row")
            print("Enter 5 if you want to delete seat_row by id")
            print("Enter 6 if you want to add random data")
            print("Enter 7 if you want to request")
            print("Enter 0 if you want to go to menu")
            inp = input()
            if inp == '1':
                controller.print_seats_rows()
            elif inp == '2':
                while True:
                    try:
                        id = int(input("Enter id of seat_row: "))
                        break
                    except ValueError:
                        print("Error! Try again: ")
                controller.print_seat_row(int(id))
            elif inp == '3':
                while True:
                    try:
                        row_number = int(input("Enter row_number of seat_row: "))
                        break
                    except ValueError:
                        print("Error! Try again: ")
                while True:
                    try:
                        seat_number = int(input("Enter seat_number of seat_row: "))
                        break
                    except ValueError:
                        print("Error! Try again: ")
                type_of_seat = input("Enter type_of_seat of seat_row: ")
                controller.init_add_seat_row(row_number, seat_number, type_of_seat)
            elif inp == '4':
                while True:
                    try:
                        id = int(input("Enter id of seat_row: "))
                        break
                    except ValueError:
                        print("Error! Try again: ")
                while True:
                    try:
                        row_number = int(input("Enter row_number of seat_row: "))
                        break
                    except ValueError:
                        print("Error! Try again: ")
                while True:
                    try:
                        seat_number = int(input("Enter seat_number of seat_row: "))
                        break
                    except ValueError:
                        print("Error! Try again: ")
                print("Enter type_of_seat of seat_row:")
                type_of_seat = input()
                controller.init_update_seat_row(int(id), int(row_number), int(seat_number), type_of_seat)
            elif inp == '5':
                while True:
                    try:
                        id = int(input("Enter id of seat_row: "))
                        break
                    except ValueError:
                        print("Error! Try again: ")
                controller.print_delete_seat_row(int(id))
            elif inp == '0':
                break
            elif inp == '6':
                while True:
                    try:
                        num = int(input("Enter amount of random data: "))
                        break
                    except ValueError:
                        print("Error! Try again: ")
                controller.init_random_seats_rows(int(num))
            elif inp == '7':
                while True:
                    try:
                        row_number = int(input("Enter row_number of seat_row: "))
                        break
                    except ValueError:
                        print("Error! Try again: ")
                controller.request_seats_rows(row_number)
            else:
                print("Incorrect number")
    elif inp == '0':
        print("Exit")
        break
    else:
        print("Incorrect number")