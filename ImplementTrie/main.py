"""
A trie aka prefix tree
is a tree data structure
used to efficiently store
and retrieve keys
in a dataset of strings

Implement the trie class

"""

"""
Implement TrieNode 
"""

class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

        # children['a'] = TrieNode()


class Trie(object):
    def __init__(self):
        """
        initializes the trie object

        initialize trie root
        """
        self.root = TrieNode()

    def insert(self, word):
        """
        inserts word,
        into trie

        We have to iterate through every character in the word
        and structure trie tree
        """

        current = self.root

        for char in word:
            # if the character is not in the trie's children,
            # it hasnt been inserted yet
            if char not in current.children:
                # This is how we insert new trie nodes
                current.children[char] = TrieNode()

            # move down the tries tree structure
            current = current.children[char]

        # we mark the last char as endOfWord
        current.endOfWord = True

    def search(self, word):
        """
        if word is in trie:
            return True

        return False
        """

        current = self.root

        for char in word:
            if char not in current.children:
                return False

            # update current pointer
            current = current.children[char]

        # current should be the last character of the word
        return current.endOfWord

    def startsWith(self, prefix):
        """
        if there is a previously inserted word
            that starts with the given prefix
            return True

        return False

        Should be the same as search
        except return current.endOfWord
        """

        current = self.root

        for char in prefix:
            if char not in current.children:
                return False

            current = current.children[char]

        return True


if __name__ == '__main__':
    trie = Trie()
    trie.insert('apple')

    # returns True
    print(trie.search('apple'))
    # returns False
    print(trie.search('app'))

    trie.insert('app')

    # return True
    print(trie.search('app'))
    # return True
    print(trie.startsWith('ap'))
