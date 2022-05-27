from colorama import Fore
import os

class Console:
    @staticmethod
    def error(text : str):
        print(Fore.RED + "Error : " + text)

    @staticmethod
    def info(text : str):
        print(Fore.BLUE + text)

    @staticmethod
    def success(text : str):
        print(Fore.GREEN + "Success : " + text)

    @staticmethod
    def print(text : str):
        print(Fore.WHITE + text)

    @staticmethod
    def pause():
        os.system('pause')

    @staticmethod
    def clear():
        os.system('cls')

    @staticmethod
    def get_space(quantity : int) -> str:
        if quantity <= 0:
            return ''
        text = ''
        for i in range(quantity):
            text += ' '
        return text

    @staticmethod
    def input(text : str) -> str:
        return input(Fore.WHITE + text)
