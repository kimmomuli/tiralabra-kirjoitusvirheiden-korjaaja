import unittest
from services.damerau_levenshtein import damerau_levenshtein

class TestDamerauLevenshtein(unittest.TestCase):
    def setUp(self):
        pass

    def test_with_empty_string(self):
        result = damerau_levenshtein('','')
        self.assertEqual(0, result)

    def test_with_same_string(self):
        result = damerau_levenshtein('apina','apina')
        self.assertEqual(0, result)

    def test_with_LIONS_AND_MOON(self):
        #  | LIONS
        # --------
        #  |012345
        # M|112345
        # O|222234
        # O|333234
        # N|444323 <---- Answer

        result = damerau_levenshtein('LIONS','MOON')
        self.assertEqual(3, result)

    def test_with_LAHYQQKPGKA_AND_YHCQPGK(self):
        result = damerau_levenshtein('LAHYQQKPGKA','YHCQPGK')
        self.assertEqual(6, result)