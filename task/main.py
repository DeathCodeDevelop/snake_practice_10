from home_library import HomeLibrary
from colorama import init, Fore
from logger import Log
import os

os.system('cls')

def main():
    path_to_connect = 'library_db.db'
    lib = HomeLibrary(path_to_connect)

    instuctions = {
        '1' : lambda : lib.show_books(),
        '2' : lambda : lib.add_book(),
        '3' : lambda : lib.remove_book(),
        '4' : lambda : lib.find_book_by_parameter(),
        '5' : lambda : lib.find_books_by_parameter(),
        '6' : lambda : lib.find_books()
    }

    choice : str = ''
    while choice != 'exit':
        os.system('cls')
        show_menu()
        choice = input('enter your choice : ')
        os.system('cls')
        if choice != 'exit':
            if choice in instuctions.keys():
                instuctions[choice]()
                os.system('pause')

def show_menu():
    print(Fore.WHITE + "1. Show all books")
    print("2. Add book")
    print("3. Remove book")
    print("4. Find book by parametr")
    print("5. Find books by parametr")
    print("6. Find books by parametrs")
    print("exit to exit")

if __name__ == '__main__' : main()
