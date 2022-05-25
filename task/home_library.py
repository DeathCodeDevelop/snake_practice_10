from colorama import init, Fore
from context import Context

class HomeLibrary:
    def __init__(self, path_to_connect : str):
        self.__context = Context(path_to_connect)

    def show_books(self):
        '''Prints library books'''
        print(Fore.GREEN + 'Books in library : ')
        HomeLibrary.show_books_from_list(self.__context.get_all_books())

    @staticmethod
    def show_books_from_list(books : list[dict[str, str]]):
        '''Prints all books from list'''
        if books == None or len(books) == 0:
            print(Fore.GREEN + 'List is empty')
            return None
        for i in books:
            HomeLibrary.show_book(i)

    @staticmethod
    def show_book(book : dict[str, str]):
        '''Prints book, takes book'''
        if book == None:
            print("Empty")
            return None
        print()
        for i in book.keys():
            print(Fore.YELLOW + i, ' : ', Fore.WHITE + str(book[i]))

    def add_book(self, book : dict[str, str]):
        '''Adds book to library, takes book'''
        self.__context.insert_book(book)

    def remove_book(self, id : int):
        '''Removes book to library, takes book index'''
        self.__context.remove_book(id)

    def get_book_by_id(self, id : int):
        '''Gets book by id, takes index of book, returns book'''
        return self.__context.get_book_by_id(id)
    
    def show_book_by_id(self, id : int):
        '''Prints book by id, takes index of book'''
        HomeLibrary.show_book(self.get_book_by_id(id))

    def find_books_by_parameter(self, parameter_name : str, parameter : str):
        return self.__context.get_books_by_parameter(parameter_name, parameter)

    def find_book_by_parameter(self, parameter_name : str, parameter : str):
        return self.__context.get_book_by_parameter(parameter_name, parameter)

    def find_books(self, parameters : dict[str, str]):
        '''Finds books by parameters, takes parameters, returns list of books'''
        return self.__context.get_books_by_parameters(parameters)
