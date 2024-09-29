def print_menu(options):
    # Bu funksiya menu-lar ucundur
    for id, option in enumerate(options, 1):
        print(f"{id}. {option}")

def get_user_choice(max_choice):
    while True:
        try:
            choice = int(input("Enter menu: "))
            if 0 <= choice <= max_choice:
                return choice
            else:
                print(f'Enter menu between 1 and {max_choice}')
        except:
            print("Please enter valid menu!!!")


def get_user_input(data: str):
    return input(data)

def print_cars(cars):
    for i, car in enumerate(cars, 1):
        print(f"{i}. id: {car[0]}, name: {car[1]}, color: {car[2]}, rental price: {car[3]}")