from home_library import HomeLibrary
from console import Console

Console.clear()

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
        Console.clear()
        show_menu()
        choice = Console.input('enter your choice : ')
        Console.clear()
        if choice != 'exit':
            if choice in instuctions.keys():
                instuctions[choice]()
                Console.pause()

def show_menu():
    Console.print("1. Show all books")
    Console.print("2. Add book")
    Console.print("3. Remove book")
    Console.print("4. Find book by parametr")
    Console.print("5. Find books by parametr")
    Console.print("6. Find books by parametrs")
    Console.print("exit to exit")

if __name__ == '__main__' : main()
