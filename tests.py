import unittest
from mainmenuTests import *



class StartMenuTests1(unittest.TestCase):
    def setUp(self):
        self.start = MainMenu()
        self.interpreter = UmlInterpreter()

    def test_one(self):
        self.assertEqual(start(), self.start.start_menu(1))

    def test_two(self):
        self.assertEqual(data_entry(), self.start.start_menu(2))

    def test_three(self):
        self.assertEqual(read_from_db(), self.start.start_menu(3))

    def test_four(self):
        self.assertEqual(create_table(), self.start.start_menu(4))

    def test_five(self):
        self.assertEqual(graph_data(), self.start.start_menu(5))

    def test_six(self):
        self.assertEqual(graphs(), self.start.start_menu(6))

    def test_seven(self):
        self.assertEqual('goodbye', self.start.start_menu("55"))

    def test_eight(self):
        self.assertEqual(commandHelp, self.start.start_menu(7))

    def test_nine(self):
        self.assertEqual([], self.interpreter.uml_decoder(uml_content='@startuml'))

    def test_ten(self):
        self.assertEqual([], self.interpreter.uml_decoder(uml_content='@startuml\n'))

    def test_eleven(self):
        self.assertEqual([], self.interpreter.uml_decoder(uml_content='class ClassName'))

    def test_twelve(self):
        self.assertEqual([], self.interpreter.uml_decoder(uml_content='@enduml'))

    def test_thirteen(self):
        self.assertNotEquals([''], self.interpreter.uml_method(remove_list=''))

    def test_fourteen(self):
        self.assertNotEquals(['(', ')'], self.interpreter.uml_method(remove_list=['(', ')']))

    def tearDown(self):
        print("This test case is done!")


unittest.main(verbosity=2)
# runner = unittest.TextTestRunner(descriptions=True, verbosity=2)
