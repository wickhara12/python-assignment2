"""this is Rebecca's code for tasks 2 & 3"""
from cmd import Cmd
class commandHelp(Cmd):

    def __init__(self):
        Cmd.__init__(self)
        self.prompt = ">>> "
    # commands
    def help_main_menu(self):
        """the main will run the program' """
    def help_pickle(self):
        print('pickle opens the file when it was last save')
    def help_main(self):
        print('opens a file and shows the file location of the file '
              'and evaluates and checks for classes, attributes and methods '
              'and also has file handling/exceptions')
    def help_database(self):
        print('the database will save and read data that is hard coded, '
              'the data is based on the PlantUML.txr file and also includes date of class creation '
              'the select statement is showing all of the data that is in the database.')
    def help_printPrettyWithoutDB(self):
        print('this is hard coded, and when u run the program, it will display a bar chart of how many information'
              'is in each class')
    def help_printPrettyWithDB(self):
        print('this is a part of the database file which allows data to be display in a graph ')
    def help_docTests(self):
        print('there are tests that examines the file "plantUML.txt" and checks if the class information is correct '
              'it is different from unitTests, so some people can be confused. however, both tests programs'
              ' ran the same way by going to run on the menu bar and clicking on run... ')
    def help_unitTexts(self):
        print('unit testing examines if the information or data is correct in your program '
              'it is different from DocTests, so some people can be confused. however, both tests programs'
              ' ran the same way by going to run on the menu bar and clicking on run... ')
    # quit
    def do_quit(self, line):
        print("Quitting ......")
        return True
    def help_quit(self):
        print("\n".join(['Quit from my CMD', ':return: True']))
    do_q = do_quit
if __name__ == "__main__":
    quitter = commandHelp()
    quitter.cmdloop()
