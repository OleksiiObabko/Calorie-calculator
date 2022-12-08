from enums.user_characteristics_enum import NAME, WEIGHT, HEIGHT, AGE, PHYSICAL_ACTIVITY, GENDER, PASSWORD
from services.db_service import read_db, write_db, write_login_user, read_login_user
from middlewares.user_middleware import isUserExists
from validators.auth_validator import name_validator, password_validator, float_validator, int_validator, \
    gender_validator


def register():
    db = read_db()

    name = name_validator()
    password = password_validator()
    weight = float_validator(WEIGHT)
    height = float_validator(HEIGHT)
    age = int_validator(AGE)
    gender = gender_validator()
    physical_activity = int_validator(PHYSICAL_ACTIVITY)

    new_user = {
        NAME: name,
        PASSWORD: password,
        WEIGHT: weight,
        HEIGHT: height,
        AGE: age,
        GENDER: gender,
        PHYSICAL_ACTIVITY: physical_activity
    }

    if not isUserExists(db, new_user[NAME]):
        db.append(new_user)

        write_db(db)

        print("New user has been created")
    else:
        print(f"user with name {new_user[NAME]} is already exist")


def login():
    user_name = input("Enter name: ").title()

    db = read_db()

    user = isUserExists(db, user_name)

    while not user:
        print(f"user with name {user_name} not found")
        user_name = input("Enter name again: ")
        user = isUserExists(db, user_name)

    user_password = input("Enter password: ")

    while user[PASSWORD] != user_password:
        print("wrong password")
        user_password = input("Enter password again: ")

    write_login_user(user)
    print(f"Welcome, {user_name}!")


def logout():
    login_user = read_login_user()

    write_login_user({})
    print(f"Goodbye {login_user[NAME]}")
