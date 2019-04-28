from model.converter import start
import model.pickle_save
from Command_Help import *
from model.printPrettywithoutDB import *


def start_menu():
    print("press one to convert file into framework")
    print("press two to save data into a database")
    print("press three to read from a database")
    print("press four to get the command help line")
    print("press five for graphs with DB "
          "or press six for graphs with DB")
    user_input = input("please enter your input")

    if user_input == "1":
        start()
        return start_menu()
    if user_input == "2":
        quitter = commandHelp()
        quitter.cmdloop()
        return start_menu()
    if user_input == "3":
        graphs()
        return start_menu()
    else:
        print("goodbye")


if __name__ == '__main__':
    model.pickle_save
    start_menu()
