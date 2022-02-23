import os
from words.trie import Trie


class WordService:
    def __init__(self):
        self.trie = Trie()
        self.all_words = []

    def read_words_to_trie(self):
        """kaikkisanat.txt ---> Trie
        """
        dirname = os.path.dirname(__file__)
        filename = os.path.join(dirname, './kaikkisanat.txt')
        with open(filename, 'r', encoding='utf8') as file:
            for row in file:
                row = row.replace('\n', '')
                self.trie.insert(row)
                self.all_words.append(row)

    def search_words(self, words_part: str) -> list:
        """Search words by starting part

        Args:
            words_part (str): starting part of word

        Returns:
            list: all words which start by starting word_part
        """
        return self.trie.search(words_part)

    def is_word_exist(self, word:str) -> bool:
        """

        word is exist -> True
        word is not exist -> False

        Args:
            word (str): word what we looking for

        Returns:
            bool: result is word exist
        """
        return self.trie.word_exist(word)
