import re

from enums.user_characteristics_enum import HEIGHT, WEIGHT, AGE, PHYSICAL_ACTIVITY, MALE, FEMALE


def name_validator():
    isValid = False

    while not isValid:
        name = input("Enter name: ")
        for letter in name.lower():
            if letter not in "qwertyuiopasdfghjklzxcvbnm":
                print("Name not valid.")
                isValid = False
            elif len(name) <= 1 or len(name) > 20:
                print("Name not valid(min: 2, max: 20).")
                isValid = False
            else:
                isValid = True
    return name.title()


def password_validator():
    isValid = False

    while not isValid:
        password = input("Enter password: ")

        if re.match(r"^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%_*#?&])[A-Za-z\d@$!%_*#?&]{4,}$", password):
            return password
        else:
            print("Password not valid. Minimum 4 characters, at least 1 letter, 1 number and 1 special character.")


def float_validator(characteristic):
    isValid = False

    while not isValid:
        data = input(f"Enter {characteristic}: ")
        try:
            data = float(data)
        except ValueError:
            print(f"{characteristic} not valid.")
            isValid = False
        else:
            if characteristic == WEIGHT and data <= 14 or data > 200:
                print(f"{characteristic} not valid(min: 20 kg, max: 200).")
            elif characteristic == HEIGHT and data <= 67 or data > 251:
                print(f"{characteristic} not valid(min: 100 sm, max: 250 sm).")
            else:
                return float(data)


def int_validator(characteristic):
    isValid = False

    while not isValid:
        data = input(f"Enter {characteristic}: ")

        if characteristic == AGE:
            if not data.isdigit():
                print(f"{characteristic} not valid(only int, min: 1, max: 120).")
                continue
            elif 1 <= int(data) <= 120:
                return int(data)
            else:
                print(f"{characteristic} not valid(only int, min: 1, max: 120).")
        if characteristic == PHYSICAL_ACTIVITY:
            if not data.isdigit():
                print(f"{characteristic} not valid(only int, min: 1, max: 4).")
                continue
            elif 1 <= int(data) <= 4:
                return int(data)
            else:
                print(f"{characteristic} not valid(only int, min: 1, max: 4).")


def gender_validator():
    isValid = False

    while not isValid:
        gender = input("Enter gender: ").lower()

        if gender == MALE or gender == FEMALE:
            return gender.lower()
        else:
            print("gender invalid(male or female).")