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
        searches wordDictionary, return true if word in wordDictionary

        will be a recursive function
        start by writing out the iterative, if c not '.'

        """

        def dfs(j, root):
            current = root

            # we for i in range j, len(word) bc we are getting this from recursive
            for i in range(j, len(word)):
                c = word[i]

                if c == '.':
                    # a dot can represent any of current.children.values()
                    for child in current.children.values():
                        # we'll actually be doing this recursively
                        # we're passing in the index of the remaining chars
                        # ie the chars after the dot, we'll call it j
                        # our j will be i + 1
                        # because we are at index
                        # for i in range len(word)
                        # and we'll pass in the node, child,
                        if dfs(i + 1, child):
                            return True

                    return False

                else:
                    if c not in current.children:
                        return False

                    else:
                        # shift pointer
                        current = current.children[c]

            return current.endOfWord

        # call to dfs
        return dfs(0, self.root)


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


