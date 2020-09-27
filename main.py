"""a program that asks its user for a username and password.
If these credentials are valid, the user gets access.
If not, it asks the user again."""

import hashlib
import json


# Generates and returns a sha3_256 hash from a string.
def genhash(pword):
    hashedpword = hashlib.sha3_256(str.encode(pword)).hexdigest()
    return(hashedpword)


def is_valid_credentials(usrname,pwd):

    if Usr.authenticate(usrname,pwd):
        print("\nWelcome\n")
    else:
        print("\nSorry, wrong username or password!\nPlease try again\n")



class UserData:
  def __init__( self ):
    with open("config.json") as f:
      self._data = json.load(f)
  def authenticate( self, username, password ):
      return username in self._data and self._data[ username ] == genhash(password)




while __name__ == "__main__":
    Usr = UserData()
    is_valid_credentials(input("Input username >"), input("Input password"))