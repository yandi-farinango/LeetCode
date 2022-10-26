"""
Design a data structure
that supports adding new words
and
finding if a string matches
any previously added word

"""

"""
We will be implementing a Trie prefix-tree

To implement a trie, 
we'll need to define a function for TrieNode

for search function 
    the tricky thing about the search function is 
    dealing with the . 
    
    we're going to be doing the search function 
    recursively 
    
"""

"""
Implement TrieNode
"""


class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False


class WordDictionary(object):
    def __init__(self):
        """
        initializes WordDictionary object
        to initialize WordDictionary as a trie prefix tree
        we'll need to initialize a root node
        """

        self.root = TrieNode()

    def addWord(self, word):
        """
        adds a word to the dictionary

        for adding words to a dictionary,
        we'll go through each char
        if char not in current.dictionary,
        we can add it by mapping char: TrieNode()

        we'll also have to set endOfWord = True
        """

        # pointer
        current = self.root

        for char in word:
            if char not in current.children:
                # map char: TrieNode
                current.children[char] = TrieNode()

            # shift pointer
            current = current.children[char]

        # mark endOfWord
        current.endOfWord = True

    def search(self, word):
        """
        When searching for a word,
        we want to return true if a word exists in our trie

        we'll traverse the word
        for i in range(len(word))
        c = word[i]

        if
            char = '.', it can count towards any char,
            this will have to be done recursively


        else
            if c not in current.children
                return false

            else
                shift current pointer

        return end of word

        """

        def dfs(root, j):
            current = root

            for i in range(j, len(word)):
                c = word[i]

                if c == '.':
                    # '.' can count towards any char,
                    # we want to check all currents children braches
                    for child in current.children.values():

                        # recursive call, skipping over .
                        # by incrementing i
                        if dfs(child, i + 1):
                            # if word search ends in .
                            # we'll never execute below code,
                            # so we want to return True
                            return True

                    return False

                # non recursive
                else:
                    if c not in current.children:
                        return False

                    # shift pointer
                    else:
                        current = current.children[c]

            # return endOfWord
            return current.endOfWord

        # return recursive call
        return dfs(self.root, 0)


if __name__ == '__main__':
    wordDict = WordDictionary()

    wordDict.addWord('bad')
    wordDict.addWord('dad')
    wordDict.addWord('mad')

    # return false
    print(wordDict.search('pad'))
    # return True
    print(wordDict.search('dad'))

    # return True
    print(wordDict.search('.ad'))
    # return True
    print(wordDict.search('b..'))










