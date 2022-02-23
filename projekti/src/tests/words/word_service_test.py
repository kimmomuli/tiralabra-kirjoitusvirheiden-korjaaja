import unittest
from words.word_service import WordService

class WordServiceTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.word_service = WordService()
        cls.word_service.read_words_to_trie()
    
    @classmethod
    def tearDownClass(cls):
        cls.word_service = None

    def test_word_service_exist(self):
        self.assertIsNotNone(self.word_service)

    def test_seach_words(self):
        aamu_words = self.word_service.search_words('aamu')
        self.assertEqual(len(aamu_words), 52)

    #Test is_word_exist and word_exist
    def test_word_exist_empty_string(self):
        self.assertEqual(self.word_service.is_word_exist(''), False)

    def test_word_exist_by_exist_string(self):
        self.assertEqual(self.word_service.is_word_exist('kissa'), True)
        self.assertEqual(self.word_service.is_word_exist('koira'), True)

    def test_word_exixt_by_right_begining_characters(self):
        self.assertEqual(self.word_service.is_word_exist('a'), False)
        self.assertEqual(self.word_service.is_word_exist('k'), False)

    def test_word_exist_by_wrong_word(self):
        self.assertEqual(self.word_service.is_word_exist('tämäsanaonväärin'), False)
        self.assertEqual(self.word_service.is_word_exist('aapina'), False)
