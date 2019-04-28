from model.converter import start
from model.pickle_save import SavingPickle
from Command_Help import *
from model.printPrettywithoutDB import *


class Menu:
    @staticmethod
    def option_one():
        return start()

    @staticmethod
    def option_two():
        quitter = commandHelp()
        return quitter.cmdloop()

    @staticmethod
    def option_three():
        return Graphs.graphs()

    @staticmethod
    def user_input():
        user = int(input("press one to convert file into framework, \n"
                         " press two to get the command help line \n"
                         "or press three for graphs without DB \n"
                         "please enter your input: "))
        if user == 1:
            Menu.option_one()
        elif user == 2:
            Menu.option_two()
        elif user == 3:
            Menu.option_three()


if __name__ == '__main__':
    SavingPickle
    Menu.user_input()
