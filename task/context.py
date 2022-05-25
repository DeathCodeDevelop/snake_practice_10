import sqlite3
from books_initialize import books_initialize
from logger import Log

class Context:
    def __init__(self, path_to_connect : str):
        self.__connection = sqlite3.connect(path_to_connect)
        self.__cursor = self.__connection.cursor()
        if self.table_exist('books') == False:
            self.__cursor.execute('CREATE TABLE IF NOT EXISTS books (id INTEGER PRIMARY KEY AUTOINCREMENT, name text, author text, publisher text, genre text, year text);')
            self.__commit()
            self.insert_books(books_initialize)
            self.__commit()
            
    def __commit(self):
        self.__connection.commit()
    
    def table_exist(self, table_name : str) -> bool:
        self.__cursor.execute("SELECT count(name) FROM sqlite_master WHERE type='table' AND name='"+table_name+"'")
        if  self.__cursor.fetchone()[0] == 1:
            return True
        return False

    @staticmethod
    def get_data_from_books(books : list[dict[str, str]]) -> list:
        list = []
        for book in books:
            list.append(Context.get_data_from_book(book))
        return list

    @staticmethod
    def get_data_from_book(book : dict[str, str]):
        return book['name'], book['author'], book['publisher'], book['genre'], book['year']

    def insert_book(self, book : dict[str, str]):
        try:
            self.__cursor.execute('INSERT INTO books VALUES(NULL,?,?,?,?,?)', Context.get_data_from_book(book))
            self.__connection.commit()
            Log.success("The book with name : " + book['name'] + " was added")
        except:
            Log.error("The book doesn't match the table in the database")

    def insert_books(self, books : list[dict[str,str]]):
        try:
            self.__cursor.executemany('INSERT INTO books VALUES(NULL,?,?,?,?,?)', Context.get_data_from_books(books))
            self.__connection.commit()
            Log.success("Books were added")
        except:
            Log.error("Books don't match the table in the database")

    def get_all_books(self):
        self.__cursor.execute("SELECT * FROM books")
        return Context.to_books_from_data(self.__cursor.fetchall())

    def get_books_by_parameter(self, parameter_name : str, parameter : str):
        try:
            self.__cursor.execute("SELECT * FROM books WHERE " + parameter_name + " LIKE '%" + parameter + "%'")
            return Context.to_books_from_data(self.__cursor.fetchall())
        except:
            Log.error("The book table doesn't have parameter with name " + parameter_name)
            return None

    def get_book_by_parameter(self, parameter_name : str, parameter : str):
        try:
            self.__cursor.execute("SELECT * FROM books WHERE " + parameter_name + " LIKE '%" + parameter + "%'")
            return Context.to_book_from_data(self.__cursor.fetchone())
        except:
            Log.error("The book table doesn't have parameter with name " + parameter_name)
            return None

    def get_books_by_parameters(self, parameters : dict[str, str]):
        try:
            sql = "SELECT * FROM books WHERE "
            list = []
            for key in parameters.keys():
                list.append(key + " LIKE '%" + parameters[key] + "%'")
            sql += str(' AND '.join(list))
            self.__cursor.execute(sql)
            return Context.to_books_from_data(self.__cursor.fetchall())
        except:
            Log.error("The book table doesn't have such parameters")
            return None

    def get_book_by_id(self, id : int):
        try:
            self.__cursor.execute("SELECT * FROM books WHERE id = " + str(id))
            return Context.to_book_from_data(self.__cursor.fetchone())
        except:
            return None

    def remove_book(self, id : int):
        if self.get_book_by_id(id) == None:
            Log.info("The book with id = " + str(id) + " doesn't exist")
            return None

        self.__cursor.execute("DELETE FROM books WHERE id = " + str(id))
        self.__commit()
        if self.get_book_by_id(id) == None:
            Log.success("The book was deleted")

    @staticmethod
    def to_books_from_data(data : list[list[str]]) -> list[dict[str, str]]:
        list = []
        for i in data:
            list.append(Context.to_book_from_data(i))
        return list


    @staticmethod
    def to_book_from_data(data : list[str]) -> dict[str, str]:
        if data == None:
            return
        book = {
                'id' : 0,
                'name' : '',
                'author' : '',
                'publisher' : '',
                'genre' : '',
                'year' : ''
               }
        iterator = 0
        for key in book:
            book[key] = data[iterator]
            iterator += 1
        return book

    def __del__(self):
        self.__connection.close()
