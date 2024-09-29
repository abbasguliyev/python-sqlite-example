from services import register_user, authenticate_user, get_all_cars, add_car, update_car, delete_car
from utils import print_menu, get_user_choice, get_user_input, print_cars

def main_menu():
    while True:
        options = ['Login', 'Register,', 'Exit']
        print_menu(options)
        choice = get_user_choice(len(options))

        if choice == 1:
            login()
        elif choice == 2:
            register()
        elif choice == 0:
            print('By By :((')
            break

def login():
    username = get_user_input('Enter username: ')
    password = get_user_input('Enter password: ')
    if authenticate_user(username, password):
        print("Welcome")
        car_menu()
    else:
        print("Enter valid username and password")



def register():
    first_name = get_user_input('First Name: ')
    last_name = get_user_input('Last Name: ')
    username = get_user_input('Username: ')
    password = get_user_input('Password: ')

    register_user(first_name, last_name, username, password)
    print('Register successfuly')


def car_menu():
    while True:
        print("*****Car Menu*****")
        options = ["Show all car", "Add Car", "Update Car", "Delete Car", "Exit"]
        print_menu(options)
        choice = get_user_choice(len(options))

        if choice == 1:
            show_all_cars()
        elif choice == 2:
            add_new_car()
        elif choice == 3:
            update_car_info()
        elif choice == 4:
            delete_car_info()
        elif choice == 0:
            print('By By :((')
            break
        
def show_all_cars():
    cars = get_all_cars()
    if cars:
        print_cars(cars)
    else:
        print("You have not any car...")

def add_new_car():
    name = get_user_input("Name: ")
    color = get_user_input("Color: ")
    rental_price = get_user_input("Rental Price: ")
    add_car(name, color, rental_price)
    print("Car successfully added!!!")

def update_car_info():
    show_all_cars()
    car_id = int(get_user_input("Enter the car id: "))
    name = get_user_input("Name: ")
    color = get_user_input("Color: ")
    rental_price = get_user_input("Rental Price: ")
    update_car(car_id, name, color, rental_price)
    print("Car successfully updated!!!")

def delete_car_info():
    show_all_cars()
    car_id = int(get_user_input("Enter the car id: "))
    delete_car(car_id)
    print("Car successfully deleted!!!")

if __name__ == "__main__":
    main_menu()