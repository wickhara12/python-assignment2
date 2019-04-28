from model.file_handler import Filehandler, file_reader
from model.class_maker import ClassMaker
from model.uml_interpreter import UmlInterpreter
from model.converter import start
import model.pickle_save
from Command_Help import *
from model.Database import *
from model.printPrettyWithDB import *
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
        create_table()
        data_entry()
        return start_menu()
    if user_input == "3":
        read_from_db()
        return start_menu()
    if user_input == "4":
        quitter = commandHelp()
        quitter.cmdloop()
        return start_menu()
    if user_input == "5":
        graph_data()
        cursor.close()
        connection.close()
        return start_menu()

    if user_input == "6":
        graphs()
        return start_menu()
    else:
        print("goodbye")


if __name__ == '__main__':
    model.pickle_save
    start_menu()
