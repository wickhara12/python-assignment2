from model.converter import start
import model.pickle_save
from Command_Help import *
from model.printPrettywithoutDB import *


class Menu:
    @staticmethod
    def start_menu():

        user_input = input("press one to convert file into framework,"
                           " press two to get the command help line"
                           "or press three for graphs without DB"
                           "please enter your input")

        if user_input == "1":
            start()
            return Menu.start_menu()
        if user_input == "2":
            quitter = commandHelp()
            quitter.cmdloop()
            return Menu.start_menu()
        if user_input == "3":
            graphs()
            return Menu.start_menu()
        else:
            print("goodbye")


if __name__ == '__main__':
    model.pickle_save
    Menu.start_menu()
