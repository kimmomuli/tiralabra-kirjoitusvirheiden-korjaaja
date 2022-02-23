class Node:
    """ Node of Trie.
        Node contains information:
            - Is node, end of some word
            - children of node
            - node value (character)
    """

    def __init__(self, character: str):
        self.value = character
        self.is_last_character = False
        self.children = {}

class Trie:
    """
        Trie is a data structure of words.
        Trie contains methods:
            - insert
            - search
            - word_exist
    """

    def __init__(self):
        """
            Root node which is an empty string.
        """
        self.root_node = Node("")

    def insert(self, word: str):
        """

        Let's go through the characters of the word one by one.
        Let's compare to character to node value.

        Args:
            word (str): word which going to add into trie
        """
        node = self.root_node

        for char in word:
            if char in node.children:
                #character is already into Trie
                node = node.children[char]
            else:
                #character was not into Trie so add let's add new node
                new_node = Node(char)
                node.children[char] = new_node
                node = new_node
        node.is_last_character = True

    def __recursion(self, result: list, node: Node, words_part: str):
        """

        Let's find out all possible words which start with variable words_part.

        Args:
            result (list): result words
            node (Node): node at the moment
            words_part (str): part of a word at the moment
        """
        if node.is_last_character:
            result.append(words_part + node.value)

        for child in node.children.values():
            self.__recursion(result, child, (words_part + node.value))


    def search(self, words_part: str) -> list:
        """

        Search start with go through Words_part character by character.
        After that, we figure out all possibles word by recursion (__recursion).

        Args:
            words_part (str): words of search start with this variable

        Returns:
            list: List of words that start with word_part
        """
        result = []
        node = self.root_node

        for char in words_part:
            if char in node.children:
                node = node.children[char]
            else:
                return result #no results so return empty list

        self.__recursion(result, node, words_part[:-1])
        return result

    def word_exist(self, word:str) -> bool:
        """ Find out, if Trie contains a word

        Args:
            word (str): Word, what we looking for.

        Returns:
            bool:
                found --> True
                not found --> False
        """
        node = self.root_node

        for char in word:
            if char in node.children:
                node = node.children[char]
            else:
                return False

        return node.is_last_character
