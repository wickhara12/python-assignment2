"""this is Simon England's code for task five"""

class UmlInterpreter:
    def __init__(self):
        self.uml_content = ['@startuml\n', '\n', 'class ClassName {\n', '}\n', '@enduml']

    def uml_decoder(self, uml_content: object) -> object:
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

    def uml_class(self, new_line):
        remove_list = ['class', ' ', '{', '\n']
        return self.char_remover(new_line, remove_list)

    def uml_method(self, new_line):
        remove_list = ['\n', '\t', '(', ')', ' ']
        return self.char_remover(new_line, remove_list)

    def uml_attribute(self, new_line):
        remove_list = ['\n', '\t', '(', ')', ' ']
        return self.char_remover(new_line, remove_list)

    def char_remover(self, string_input, remove_list):
        for item in remove_list:
            string_input = string_input.replace(item, '')
        return string_input


# file_content = {'class': 'TestClass', 'attribute': ['attribute', 'attribute1'], 'methods': ['method1()', 'method2()']}
# file_content = ['@startuml\n', '\n', 'class dummy {\n', '}\n', '@enduml']
# test = UmlInterpreter()
# output = test.uml_decoder(file_content)
# print(output)
