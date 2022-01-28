import unittest
from index import hei


class TestIndex(unittest.TestCase):

    def test_hello_world(self):
        self.assertEqual(hei(), "test")
