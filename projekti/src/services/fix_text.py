import string
from words.word_service import WordService
from services.damerau_levenshtein import damerau_levenshtein

class FixText:
    """
        FixText is object which gets input string and fix it to output string.

        FixText uses word service and Damerau Levenshtein-algorithm to fix text.

        fix_text() --> compare every words
        fix_text_fast() --> compare words which start same letter.
    """

    def __init__(self):
        self.service = WordService()
        self.service.read_words_to_trie()

    def __calculate_new_word(self, word:str) -> str:
        """
            Compare parameter word to each word one by one.
            Then it calculate, which word is closest and return it.

        Args:
            word (str): Word which we want to fix.

        Returns:
            str: Fixed word.
        """
        result = ''
        smallest = damerau_levenshtein(word, self.service.all_words[0])

        for comparative_word in self.service.all_words:
            if smallest > damerau_levenshtein(word, comparative_word):
                smallest = damerau_levenshtein(word, comparative_word)
                result = comparative_word

        return f'{result} '


    def fix_text(self, txt:str) -> str:
        """
            Splits text into words.
            Check words one by one.
            If a word exists we don't do anything.
            If a word does not exist fix it using __calculate_new_word method.
            Add word every time to result.

        Args:
            txt (str): Text which we want to fix.

        Returns:
            str: Fixed text
        """
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
            result += self.__calculate_new_word(word)

        return result[:-1]

    def __fast_calculate(self, word:str) -> str:
        """
            Searchs which words start same letter and put them into list.
            Compare list of words to parameter word.
            Return closest word from list.

        Args:
            word (str): Word which we want to fix.

        Returns:
            str: Fixed word.
        """
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
        """
            Splits text into words.
            Check words one by one.
            If a word exists we don't do anything.
            If a word does not exist fix it using __fast_calculate method.
            Add word every time to result.

        Args:
            txt (str): Text which we want to fix.

        Returns:
            str: Fixed text
        """
        if len(txt) == 0:
            return ''

        words = txt.split(' ')
        result = ''

        for word in words:
            word = word.lower()
            if self.service.is_word_exist(word):
                result += f'{word} '
                continue

            result += self.__fast_calculate(word)

        return result[:-1]
