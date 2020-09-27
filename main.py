"""A program that asks its user for a username and password.
If these credentials are valid, the user gets access.
If not, it asks the user again."""

import hashlib
import json


# Returns usernames and hashed passwords from config.
def jsonfiles():
    with open("config.json") as f:
        data = json.load(f)
    return data


# Generates and returns a sha3_256 hash from a string.
def genhash(pword):
    hashedpword = hashlib.sha3_256(str.encode(pword)).hexdigest()
    return(hashedpword)


def is_valid_credentials(usrname,pwd):
    users = jsonfiles()
    if usrname in users and users[usrname] == genhash(pwd):
        print(f"\nWelcome {usrname}\n")
    else:
        print("\nSorry, wrong username or password!\nPlease try again\n")


while __name__ == "__main__":
    #prints test username and pw
    print("Username:'User'\nPassword:'password'")

    is_valid_credentials(input("Input username > "), input("Input password > "))