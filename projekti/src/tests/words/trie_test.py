import unittest
from words.trie import Trie

class TestTrie(unittest.TestCase):
    def setUp(self):
        self.trie = Trie()
        self.trie.insert('kissa')
        self.trie.insert('kirja')
        self.trie.insert('koira')
        self.trie.insert('kili')

    def test_create_trie(self):
        trie = Trie()
        root_node = trie.root_node
        self.assertEqual(root_node.value, "")
        self.assertEqual(len(root_node.children), 0)
        self.assertEqual(root_node.is_last_character, False)

    def test_search_empty_list(self):
        self.assertEqual(len(self.trie.search('apina')), 0)

    def test_search_word(self):
        self.assertEqual(len(self.trie.search('kissa')), 1)

    def test_search_many_words(self):
        self.assertEqual(len(self.trie.search('k')), 4)