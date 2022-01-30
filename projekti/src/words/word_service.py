import os
from words.trie import Trie

class WordService:
    def __init__(self):
        self.trie = Trie()

    def read_words_to_trie(self):
        dirname = os.path.dirname(__file__)
        filename = os.path.join(dirname, './kaikkisanat.txt')
        with open(filename, 'r', encoding='utf8') as file:
            for row in file:
                row = row.replace('\n', '')
                self.trie.insert(row)

    def search_words(self, words_part: str) -> list:
        return self.trie.search(words_part)
