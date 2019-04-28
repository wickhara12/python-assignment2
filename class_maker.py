from view import view


class ClassMaker:
    def file_name(self, new_file_name):
        return self.name_to_lower(new_file_name)

    @staticmethod
    def class_maker(new_class_name):
        return 'class ' + new_class_name + ':' + view.View.newline()

    def attribute_maker(self, new_attributes):
        attributes = ''
        if len(new_attributes) > 0:
            attributes = view.View.tab() + 'def __init__(self'
            arg_attributes = ''
            self_attributes = ''
            for attribute in new_attributes:
                temp = self.name_to_lower(attribute)
                arg_attributes += ', ' + 'new_' + temp
                self_attributes += view.View.tab() + view.View.tab() + 'self.' + temp + ' = new_' + temp + view.View.newline()
            attributes += arg_attributes + '):' + view.View.newline() + self_attributes
        return attributes + view.View.newline()

    @staticmethod
    def method_maker(new_methods):
        methods = ''
        for method in new_methods:
            methods += view.View.tab() + 'def ' + method + '(self):' + view.View.newline()
            methods += view.View.tab() + view.View.tab() + 'pass' + view.View.newline() + view.View.newline()
        return methods

    def class_designer(self, new_dict):
        file_name = self.file_name(new_dict['class'])
        class_name = self.class_maker(new_dict['class'])
        methods = self.method_maker(new_dict['method'])
        attributes = self.attribute_maker(new_dict['attribute'])
        temp_dict = {'file_name': file_name, 'file_content': class_name + attributes + methods}
        return temp_dict

    @staticmethod
    def name_to_lower(new_name):
        name = ''
        for i, char in enumerate(new_name):
            if char.isupper():
                x = ''
                if i != 0:
                    x = '_'
                char = x + char.lower()
            name += char
        return name
