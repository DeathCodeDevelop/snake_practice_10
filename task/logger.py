from colorama import Fore

class Log:
    @staticmethod
    def error(text : str):
        print(Fore.RED + "Error : " + text)

    @staticmethod
    def info(text : str):
        print(Fore.BLUE + text)

    @staticmethod
    def success(text : str):
        print(Fore.GREEN + "Success : " + text)
