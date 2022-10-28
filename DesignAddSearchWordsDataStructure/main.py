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
Trie Node 
"""
class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False


"""
Word Search
"""

class WordDictionary(object):
    def __init__(self):
        """
        initialize root
        """

        self.root = TrieNode()

    def addWord(self, word):
        """
        Adds words to the Trie

        """

        # pointer
        current = self.root

        for char in word:
            if char not in current.children:
                current.children[char] = TrieNode()

            # shift pointer
            current = current.children[char]

        # end of word
        current.endOfWord = True


    def search(self, word):
        """
        Searches for a certain word in the Trie

        """

        def dfs(root, j):
            # pointer
            current = root

            for i in range(j, len(word)):
                c = word[i]

                # recursive section
                if c == '.':
                    for child in current.children.values():
                        if dfs(child, i + 1):
                            return True

                    return False

                else:
                    if c not in current.children:
                        return False

                    # shift pointer
                    else:
                        current = current.children[c]

            return current.endOfWord

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










