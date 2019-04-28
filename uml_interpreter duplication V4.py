class UmlInterpreter:
    def __init__(self):
        self.uml_content = ['@startuml\n', '\n', 'class ClassName {\n', '}\n', '@enduml']
        self.uml_list = []
        self.class_dict = {}
        self.attr_list = []
        self.method_list = []
        self.remove_list = ['\n', '\t', '(', ')', ' ', 'class', ' ', '{', '\n']

    def uml_decoder(self, uml_content: object) -> object:
        for line in uml_content:
            if 'class' in line:
                self.class_dict['class'] = self.uml_remover(line)
            elif '(' in line and ')' in line:
                self.method_list.append(self.uml_remover(line))
            elif '}' in line:
                UmlInterpreter.class_check(self)
            elif '(' not in line and ')' not in line and '@' not in line and len(line) > 1:
                self.attr_list.append(self.uml_remover(line))
        return self.uml_list

    def class_check(self):
        self.class_dict['attribute'] = self.attr_list
        self.class_dict['method'] = self.method_list
        temp_dict = self.class_dict.copy()
        self.uml_list.append(temp_dict)
        self.class_dict.clear()
        self.method_list = []
        self.attr_list = []

    def uml_remover(self, new_line):
        self.remove_list
        return self.char_remover(new_line, self.remove_list)


    def char_remover(self, string_input, remove_list: object) -> object:
        for item in remove_list:
            string_input = string_input.replace(item, '')
        return string_input




