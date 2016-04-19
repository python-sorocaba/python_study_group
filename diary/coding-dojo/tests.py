import diary
import json
import unittest


class TestDiary(unittest.TestCase):
    def setUp(self):
        self.structure = {"nome": None, "idade": None}
        self.dict_returned = diary.insert_arq(self.structure)

    def test_receive_field(self):
        structure = diary.receive_field("data")
        structure.update(diary.receive_field("nome"))
        expected_structure = {"data": None, "nome": None}
        self.assertEqual(expected_structure, structure)

    def test_insert_arq(self):
        with open("task.txt", 'r') as fp:
            dict_returned = json.loads(fp.read())
        self.assertEqual(dict_returned, self.structure)

    def test_import_arq_is_dict(self):
        imported_file = diary.import_arq()
        self.assertIsInstance(imported_file, dict)

    def test_import_arq(self):
        imported_file = diary.import_arq()
        self.assertEqual(self.structure, imported_file)

    def test_receive_multiple_fields(self):
        fieldlist = ["nome", "idade"]
        dict_fields = diary.receive_multiple_fields(fieldlist)
        self.assertEqual(self.structure, dict_fields)

    def tearDown(self):
        diary.new_dict = {}

if __name__ == '__main__':
    unittest.main()
