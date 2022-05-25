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
        '2' : lambda : add_book(lib),
        '3' : lambda : delete_book(lib),
        '4' : lambda : find_book_by_parameter(lib),
        '5' : lambda : find_books_by_parameter(lib),
        '6' : lambda : find_books_by_parameters(lib)
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
    print("3. Delete book")
    print("4. Find book by parametr")
    print("5. Find books by parametr")
    print("6. Find books by parametrs")
    print("exit to exit")

def add_book(lib : HomeLibrary):
    name = input('enter book name => ')
    author = input('enter book author => ')
    publisher = input('enter book publisher => ')
    genre = input('enter book genre => ')
    year = input('enter book year => ')
    
    book = {
        'name' : name,
        'author' : author,
        'publisher' : publisher,
        'genre' : genre,
        'year' : year
    }
    
    os.system('cls')
    print(Fore.WHITE + 'Your book:')
    HomeLibrary.show_book(book)
    
    lib.add_book(book)

def delete_book(lib : HomeLibrary):
    id = int(input('enter book id => '))
    book = lib.get_book_by_id(id)
    
    if book != None:
        HomeLibrary.show_book(book)
        yes = input("Are you sure to delete this (yes) => ")
        if yes == 'yes':
            lib.remove_book(id)
    else:
        Log.info("The book with id = " + str(id) + " doesn't exist")

def find_book_by_parameter(lib : HomeLibrary):
    parameter_name = input('enter parameter name => ')
    parameter = input('enter parameter => ')
    
    Log.info("Find result : ")
    book = lib.find_book_by_parameter(parameter_name, parameter)
    HomeLibrary.show_book(book)

def find_books_by_parameter(lib : HomeLibrary):
    parameter_name = input('enter parameter name => ')
    parameter = input('enter parameter => ')
    
    Log.info("Find result : ")
    books = lib.find_books_by_parameter(parameter_name, parameter)
    HomeLibrary.show_books_from_list(books)

def find_books_by_parameters(lib : HomeLibrary):
    parameters : dict[str, str] = {}
    enter = ''
    
    while enter != 'stop':
        enter = input('enter parameter_name = parameter or stop => ')
        if enter != 'stop':
            result = my_enter(enter)
            if result != None:
                parameters[result[0]] = result[1]
    
    os.system('cls')
    HomeLibrary.show_book(parameters)
    Log.info('For this parameters result : ')
    HomeLibrary.show_books_from_list(lib.find_books(parameters))
    
def my_enter(enter):
    try:
        list = enter.split('=')
        if len(list) != 2:
            return None
        if list[0].isspace() or list[1].isspace():
            return None
        return list
    except:
        return None

if __name__ == '__main__' : main()
