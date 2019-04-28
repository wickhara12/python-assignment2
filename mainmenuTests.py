from model.converter import start
from Command_Help import commandHelp
from model.Database import *
from model.printPrettyWithDB import *
from model.printPrettywithoutDB import *


class MainMenu(object):

    def __init__(self, info=None):
        self.info = info

    def start_menu(self, user_input):

        if user_input == 1:
            return start()

        if user_input == 2:
            return data_entry()

        if user_input == 3:
            return read_from_db()

        if user_input == 4:

            return create_table()

        if user_input == 5:
            return graph_data()

        if user_input == 6:
            return graphs()
        if user_input == 7:
            quitter = commandHelp()
            quitter.cmdloop()
            return commandHelp
        else:
            return "goodbye"


class UmlInterpreter(object):
    def __init__(self):
        self.uml_content = ['@startuml\n', '\n', 'class ClassName {\n', '}\n', '@enduml']

    def uml_decoder(self, uml_content):
        uml_list = []
        class_dict = {}
        attr_list = []
        method_list = []
        for line in uml_content:
            if 'class' in line:
                class_dict['class'] = self.uml_class(line)
            elif '(' in line and ')' in line:
                method_list.append(self.uml_method(line))
            elif '}' in line:
                class_dict['attribute'] = attr_list
                class_dict['method'] = method_list
                temp_dict = class_dict.copy()
                uml_list.append(temp_dict)
                class_dict.clear()
                method_list = []
                attr_list = []
            elif '(' not in line and ')' not in line and '@' not in line and len(line) > 1:
                attr_list.append(self.uml_attribute(line))
        return uml_list

    def uml_method(self, remove_list):
        remove_list = ['\n', '\t', '(', ')', ' ']
       # return char_remover(new_line, remove_list)

    def uml_attribute(self, remove_list):
        remove_list = ['\n', '\t', '(', ')', ' ']
      #  return self.char_remover(new_line, remove_list)