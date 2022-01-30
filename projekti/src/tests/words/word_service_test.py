import unittest
from words.word_service import WordService

class WordServiceTest(unittest.TestCase):
    def setUp(self):
        self.word_service = WordService()
        self.word_service.read_words_to_trie()

    def test_word_service_exist(self):
        self.assertIsNotNone(self.word_service)

    def test_seach_words(self):
        aamu_words = self.word_service.search_words('aamu')
        self.assertEqual(len(aamu_words), 52)