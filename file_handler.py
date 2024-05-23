from pathlib import Path
from functools import wraps
from address_book import AddressBook
import pickle

filename = Path('addressbook.pkl')

# Decorator to add a logic for Exceptions which can appear while reading the file (file does not exist)
def file_error(func):
    @wraps(func)
    def inner(*args, **kwargs):
        try: 
            return func(*args, **kwargs)
        except FileNotFoundError:
            book = AddressBook()
            return book
    return inner

# Function to save data in a file before closing the app
def save_data(book, filename=filename):
    with open(filename, 'wb') as file:
        pickle.dump(book, file)

# Function to load data from a file when opening the app     
@file_error
def load_data(filename=filename):
    with open(filename, 'rb') as file:
        return pickle.load(file)

