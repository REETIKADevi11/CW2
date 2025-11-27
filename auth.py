import bcrypt
import os
import re

USER_DATA_FILE ="users.txt"

# password hashing function
def hash_password(plain_text_password):
    password_byte = plain_text_password.encode('utf-8')
    salt = bcrypt.gensalt()
    password_hashed = bcrypt.hashpw(password_byte, salt)
    password_decode = password_hashed.decode('utf-8')
    return password_decode


# password verification function
def verify_password(plain_text_password, hashed_password):
    password_byte = plain_text_password.encode('utf-8')
    hashed_password_bytes = hashed_password.encode('utf-8')
    verification = bcrypt.checkpw(password_byte, hashed_password_bytes)
    return verification


# implementation of registration function
def register_user(username, password):
    if os.path.exists(USER_DATA_FILE):
        with open(USER_DATA_FILE, "r") as f:
            for line in f:
                username_exist = line.strip().split("|")[0]
                if username_exist == username:
                    return False
    hashed_password = hash_password(password)
    with open(USER_DATA_FILE, "a") as f:
        f.write(f"{username}|{hashed_password}\n")
    return True


# implementation of user existance check
def user_exists(username):
    if not os.path.exists(USER_DATA_FILE):
        return False
    with open(USER_DATA_FILE, "r") as f:
        for line in f:
            username_exist = line.strip().split("|")[0]
            if username_exist == username:
                return True
    return False


# implementation of user login
def login_user(username, password):
    if not user_exists(username):
        print("User not registered\n")
        print("You will have to register first\n")
        return False
    with open(USER_DATA_FILE, "r") as f:
        for line in f:
            user_exist, user_password = line.strip().split("|")
            if user_exist == username:
                if verify_password(password, user_password):
                    print("User found")
                    return True
                else:
                    print("Incorrect! Please re-enter password correctly.")
                    return False
    print("Username not found")
    return False


def validate_username(username):
    if re.search(r"\s", username):
        print("Username should not contain space.")
        return False
    else:
        return True


def validate_password(password):
    lowerCase = re.search("[a-z]", password)
    upperCase = re.search("[A-Z]", password)
    digit = re.search(r"\d", password)

    if all([lowerCase, upperCase, digit]):
        print("Strong password")
        return True
    else:
        print("password should contain: LowerCase,UpperCase and Digit.\n")
        return False


def display_menu():
    print("Welcome to MULTI_DOMAIN INTELLIGENCE PLATFORM (Secure authentication system)\n")
    print("Choose whether you want to:[1] Register" \
          "                                :[2] Login" \
          "                                :[3] Exit")


def main():
    print("This is week 7 authentication system\n")
    while True:
        display_menu()
        choice = input("\Please select an option(1-3): ").strip()

        if choice == '1':
            print("User Registration")
            username = input("Enter a username: ").strip()
            password = input("Enter a password: ").strip()

            valid_username = validate_username(username)
            if valid_username:
                print("Valid")
            else:
                print("Invalid")
                continue

            if not validate_password(password):
                print("Incorrect")
                continue
            password_confirm = input("Confirm password: ").strip()
            if password != password_confirm:
                print("Password does not match.")
                continue
            if register_user(username, password):
                print("User registered succesfully")
            else: 
                print("User already exist")

        elif choice == '2':
            print("\n")
            print("\n---User Login---")
            username = input("Enter your username: \n").strip()
            password = input("Enter your password: ").strip()

            if login_user(username, password):
                print("You have successfully logged in. ")
            else: 
                print("Enter correct user name and password.")

        elif choice == '3':
            print("Thank you for using the authentication system.")
            print("Existing")
            break
        else:
            print("Invalid option. please select 1, 2 or 3.")


if __name__ == "__main__":
    main()


