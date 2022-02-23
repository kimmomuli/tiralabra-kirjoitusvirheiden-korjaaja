import unittest
from services.fix_text import FixText

class TestFixTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.fixer = FixText()
    
    @classmethod
    def tearDownClass(cls):
        cls.fixer = None

    def test_read_words_to_trie(self):
        lenght = len(self.fixer.service.all_words)
        self.assertNotEqual(lenght, 0)
        self.assertEqual(lenght, 93086)

    #Test fix text (slower)
    def test_fix_text_by_empty_string(self):
        self.assertEqual(self.fixer.fix_text(''), '')

    def test_fix_text_uppercase_does_not_affect(self):
        self.assertEqual(self.fixer.fix_text('KISSA'), 'kissa')

    def test_fix_test_not_by_letters(self):
        self.assertEqual(self.fixer.fix_text('1¤%&'), 'aamu')

    def test_fix_test_search_from_all_words(self):
        self.assertEqual(self.fixer.fix_text('simerkki'), 'esimerkki')
        self.assertNotEqual(self.fixer.fix_text('simerkki'), 'savumerkki')

    def test_fix_test_by_valid_text(self):
        self.assertEqual(self.fixer.fix_text('abcdefg'), 'ahde')

    def test_fix_text_by_sentece(self):
        self.assertEqual(self.fixer.fix_text('apina kissa sika dsfdf'), 'apina kissa sika dandy')

    #Test fix text fast (faster)
    def test_fix_text_fast_by_empty_string(self):
        self.assertEqual(self.fixer.fix_text_fast(''), '')

    def test_fix_text_fast_uppercase_does_not_affect(self):
        self.assertEqual(self.fixer.fix_text_fast('KISSA'), 'kissa')

    def test_fix_text_fast_not_by_letter(self):
        self.assertEqual(self.fixer.fix_text_fast('1¤%&'), '')

    def test_fix_text_fast_return_word_if_start_by_letter(self):
        self.assertEqual(self.fixer.fix_text_fast('a¤%&'), 'aamu')

    def test_fix_text_fast_search_word_by_first_letter(self):
        self.assertEqual(self.fixer.fix_text_fast('simerkki'), 'savumerkki')
        self.assertNotEqual(self.fixer.fix_text_fast('simerkki'), 'esimerkki')

    def test_fix_text_fast_by_valid_text(self):
        self.assertEqual(self.fixer.fix_text_fast('abcdefg'), 'ahde')

    def test_fix_text_fast_by_sentece(self):
        self.assertEqual(self.fixer.fix_text('apina kissa sika dsfdf'), 'apina kissa sika dandy')
