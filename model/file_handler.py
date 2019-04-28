"""this is Rebecca's code for task 8"""
class Filehandler:

    @staticmethod
    def writing_to_python_file(new_file_name, file_content):
        try:
            with open(new_file_name + '.py', 'w') as file:
                file.write(file_content)
        except Exception as e:
            print(e)


def file_reader(file_name):
    try:
        with open(file_name, 'r') as file:
            return file.readlines()
    except FileNotFoundError:
        print("Error - File not found")
    except FileExistsError:
        print("Error")
    except Exception as e:
        print(e)
