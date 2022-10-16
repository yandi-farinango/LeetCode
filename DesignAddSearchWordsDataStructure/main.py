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

class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False


class WordDictionary(object):
    def __init__(self):
        """
        initializes the object

        to initialize a wordDictionary object
        we'll need to initialize a root
        """

        self.root = TrieNode()


    def addWord(self, word):
        """
        adds word to wordDictionary
        """

        # pointer
        current = self.root

        for char in word:
            if char not in current.children:
                # map char: TrieNode()
                current.children[char] = TrieNode()

            # shift pointer
            current = current.children[char]

        # mark endOfWord
        current.endOfWord = True

    def search(self, word):
        """
        returns True
        if there is any string in wordDictionary
        that matches word

        * word may contain dots,
        where dots can be matched with any letter
        """

        # pointer

        def dfs(j, root):
            current = root

            for i in range(j, len(word)):
                c = word[i]

                # dot
                # if we have a string '.ab'
                # we can traverse any node, ie . corresponds to any char
                if c == '.':
                    # getting each sub-tree ie any node corresponding to all chars
                    for child in current.children.values():
                        if dfs(i + 1, child):
                            return True

                    return False

                else:
                    if c not in current.children:
                        return False
                    # if char does exist, we want to shift our pointer down to search next chars
                    else:
                        current = current.children[c]
            return current.endOfWord
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


