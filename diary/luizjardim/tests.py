import unittest
import calendar

class TestCalendar(unittest.TestCase):

    def setUp(self):
        self.file = calendar.create_tags()

    def test_tags_is_a_dict(self):
        self.assertIsInstance(self.file, dict)

if __name__ == '__main__':
    unittest.main(exit=False)

