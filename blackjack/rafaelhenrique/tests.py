# -*- coding: utf-8 -*-
import unittest


class TestBlackjack(unittest.TestCase):
    def setUp(self):
        print("Execute setUp")

    def test_error(self):
        self.assertEqual(True, False)

    def test_success(self):
        self.assertEqual(True, True)

    def tearDown(self):
        print("Execute tearDown")

if __name__ == '__main__':
    unittest.main()
