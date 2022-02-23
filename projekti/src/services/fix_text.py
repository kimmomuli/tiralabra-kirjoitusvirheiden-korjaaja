import string
from words.word_service import WordService
from services.damerau_levenshtein import damerau_levenshtein

class FixText:
    def __init__(self):
        self.service = WordService()
        self.service.read_words_to_trie()

    def calculate_new_word(self, word:str) -> str:
        result = ''
        smallest = damerau_levenshtein(word, self.service.all_words[0])

        for comparative_word in self.service.all_words:
            if smallest > damerau_levenshtein(word, comparative_word):
                smallest = damerau_levenshtein(word, comparative_word)
                result = comparative_word

        return f'{result} '


    def fix_text(self, txt:str) -> str:
        if len(txt) == 0:
            return ''

        words = txt.split(' ')
        result = ''

        for word in words:
            word = word.lower()
            #word is exist
            if self.service.is_word_exist(word):
                result += f'{word} '
                continue

            # word is not exist --> fix
            result += self.calculate_new_word(word)

        return result[:-1]

    def fast_calculate(self, word:str) -> str:
        if word[0] not in string.ascii_lowercase:
            return ''

        words = self.service.search_words(word[0])
        result = ''
        smallest = damerau_levenshtein(word, words[0])

        for comparative_word in words:
            if smallest > damerau_levenshtein(word, comparative_word):
                smallest = damerau_levenshtein(word, comparative_word)
                result = comparative_word

        return f'{result} '

    def fix_text_fast(self, txt: str) -> str:
        if len(txt) == 0:
            return ''

        words = txt.split(' ')
        result = ''

        for word in words:
            word = word.lower()
            if self.service.is_word_exist(word):
                result += f'{word} '
                continue

            result += self.fast_calculate(word)

        return result[:-1]
