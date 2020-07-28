# A Semi-Custom Password generator

import random
import string 

# constants that hold all the letters, digits and punctuation characters, respectively
LETTER = string.ascii_letters
DIGITS = string.digits
PUNCTUATION = string.punctuation

def get_password_length():

  # Promts the user to provide the required length of the password

  length = int(input('How long would you like the password to be? \n'))
  return length


def password_generator(cbl, length=8):

  '''
    cbl -> this parameter holds a list that has the choice constraints for the password
    length = 8 -> this parameter will default to 8. It stores the desired password length

    The purpose of the function is to create a shuffled string that matches our constraints
  '''

  # create alphanumerical from string constants
  printable = fetch_string_constant(cbl)

  # convert printable into a list and shuffle
  printable = list(printable)
  random.shuffle(printable)

  # generate the password to the desired length and then convert it to a string
  random_password = random.choices(printable, k=length)
  random_password = ''.join(random_password)

  return random_password

# function that asks the user for what values they want: it returns a list of size

def password_combination_choice():

  '''
    This function will ask the user if they want certain types of characters and
    will then validate their input and return it as a list.

    The default is a fully True list
  '''

  # retrieve the users password character combination choice
  want_digits = input('Want digits ? (True or False) : ')
  want_letters = input('Want letters ? (True or False): ')
  want_puncts = input('Want punctuation ? (True or False): ')

  # convert those choices from string to boolean
  try:
    want_digits = eval(want_digits.title())
    want_letters = eval(want_letters.title())
    want_puncts = eval(want_puncts.title())
    return [want_digits, want_letters, want_puncts]

  except:
    print('Invalid value. Use either True or False')
    print('Invalidity returns a default, try again to regenerate')

  return [True, True, True]

def fetch_string_constant(choice_list):

  # choice_list -> list holding boolean values that determine how our password is built

  string_constant = ''
  string_constant += DIGITS if choice_list[0] else ''
  string_constant += LETTER if choice_list[1] else ''
  string_constant += PUNCTUATION if choice_list[2] else ''
  return string_constant

# main entry
if __name__ == "__main__":
    length = get_password_length()
    choice_list = password_combination_choice()
    password = password_generator(choice_list, length)
    print('\nYour new password is: ' + password)

