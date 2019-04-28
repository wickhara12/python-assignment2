""" the file handling and exception code was create by Rebecca Wickham"""

from model.file_handler import Filehandler, file_reader
from model.class_maker import ClassMaker
from model.uml_interpreter import UmlInterpreter



def start():
    try:
        file_content = file_reader('data.pickle')
        interpreter = UmlInterpreter()
        uml_list = interpreter.uml_decoder(file_content)
        class_maker = ClassMaker()
        all_my_classes = []
        for item in uml_list:
            all_my_classes.append(class_maker.class_designer(item))
        for item in all_my_classes:
            Filehandler.writing_to_python_file(item['file_name'], item['file_content'])
    except FileNotFoundError:
        print("Error - File not found")
    except FileExistsError:
        print("Error")
    except Exception as e:
        print(e)


if __name__ == '__main__':
     start()