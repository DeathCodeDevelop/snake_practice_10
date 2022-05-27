from context import Context
from console import Console
from colorama import Fore

class HomeLibrary:
    def __init__(self, path_to_connect : str):
        self.__context = Context(path_to_connect)

    def show_books(self):
        '''Prints library books'''
        Console.info('Books in library : ')
        HomeLibrary.show_books_from_list(self.__context.get_all_books())

    @staticmethod
    def show_books_from_list(books : list[dict[str, str]]):
        '''Prints all books from list'''
        if books == None or len(books) == 0:
            Console.info('List is empty')
            return None
        for i in books:
            HomeLibrary.show_book(i)
        Console.print('_______________________________')

    @staticmethod
    def show_book(book : dict[str, str]):
        '''Prints book, takes book'''
        if book == None:
            Console.info("Empty")
            return None
        print()
        
        max_key_lenght = 0
        for i in book.keys():
            if max_key_lenght < i.__len__():
                max_key_lenght = i.__len__() 

        for i in book.keys():
            print(Console.get_space(max_key_lenght - i.__len__()) + Fore.YELLOW + i, ':', Fore.WHITE + str(book[i]))

    def add_book(self):
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
    
        Console.clear()
        print(Fore.WHITE + 'Your book:')
        HomeLibrary.show_book(book)

        self.__context.insert_book(book)

    def remove_book(self):
        id = int(Console.input('enter book id => '))
        book = self.__context.get_book_by_id(id)
    
        if book != None:
            HomeLibrary.show_book(book)
            yes = Console.input("Are you sure to delete this (yes) => ")
            if yes == 'yes':
                self.__context.remove_book(id)
        else:
            Console.info("The book with id = " + str(id) + " doesn't exist")
    
    def show_book_by_id(self, id : int):
        '''Prints book by id, takes index of book'''
        HomeLibrary.show_book(self.__context.get_book_by_id(id))

    def find_book_by_parameter(self):
        parameter_name = input('enter parameter name => ')
        parameter = input('enter parameter => ')
    
        Console.info("Find result : ")
        book = self.__context.get_book_by_parameter(parameter_name, parameter)
        HomeLibrary.show_book(book)

    def find_books_by_parameter(self):
        parameter_name = input('enter parameter name => ')
        parameter = input('enter parameter => ')
    
        Console.info("Find result : ")
        books = self.__context.get_books_by_parameter(parameter_name, parameter)
        HomeLibrary.show_books_from_list(books)

    @staticmethod
    def parameter_enter(enter):
        try:
            list = enter.split('=')
            if len(list) != 2:
                return None
            if list[0].isspace() or list[1].isspace():
                return None
            return list
        except:
            return None

    def find_books(self):
        parameters : dict[str, str] = {}
        enter = ''
    
        while enter != 'stop':
            enter = Console.input('enter parameter_name = parameter or stop => ')
            if enter != 'stop':
                result = HomeLibrary.parameter_enter(enter)
                if result != None:
                    parameters[result[0]] = result[1]
                    Console.info('parameter (' + result[0] + ' = ' + result[1] + ') was added')
                else:
                    Console.error('enter error')
    
        Console.clear()
        HomeLibrary.show_book(parameters)
        Console.info('For this parameters result : ')
        HomeLibrary.show_books_from_list(self.__context.get_books_by_parameters(parameters))
