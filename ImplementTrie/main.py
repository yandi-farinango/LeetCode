"""
A trie aka prefix tree
is a tree data structure
used to efficiently store
and retrieve keys
in a dataset of strings

Implement the trie class

"""

"""
To implement a Trie 
we're going to create a tree-like structure 
instead of having a next pointer, 
each node will have a dictionary 
mapping letter : node 

In this way, we can store letters
one after the other and have nodes as placeholders 

    Ex:     root 
            / 
        {a: node}
              /
           {p: node}
                /
             {p: node}
                 /
               {l: node}
                  /
                {e: node}


We insert values in this order 

This allows us to perform search 
and starts with operations 
efficiently 

When we insert new words, 
words will be inserted according to their pre-fix 

We will insert:

        for char in word:
            if char not in current.children:
                current.children[char] = TrieNode()

            # shift current pointer 
            current = current.children[char]

In this way, 
if a word has a similar prefix 
it will be connected to the longer word 

We also want to have each node contain a 
'endOfWord' boolean 
the end of word boolean 
lets us know when we've finished with a word 
this allows for searching for words within our trie 

"""

"""
Implement TrieNode
"""


class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False


class Trie(object):
    def __init__(self):
        """
        initializes the trie object

        To initialize a trie object,
        we'll want start by initializing the trie root
        """

        self.root = TrieNode()

    def insert(self, word):
        """
        inserts word in the trie

        to insert words into the trie
        we'll need to traverse chars in word
        and create new trie nodes representing each char

        we'll also need to mark endOfWord
        """

        # pointer
        current = self.root

        for char in word:
            if char not in current.children:
                current.children[char] = TrieNode()

            # shift pointer
            current = current.children[char]

        # mark endOfWord
        current.endOfWord = True

    def search(self, word):
        """
        checks trie and searches
        if word in trie, return True

        In order to check if a word is in our trie,
        we'll need to
        - get a pointer to the root
        - traverse each letter
        - if char not in current.children; return False
            * if all chars in our trie, we'll never execute return False

        But, we also check if endOfWord
        return current.endOfWord
        ie previously marked as True if endOfWord
        """

        # pointer
        current = self.root

        for char in word:
            if char not in current.children:
                return False

            # shift pointer
            current = current.children[char]

        return current.endOfWord

    def startsWith(self, prefix):
        """
        Checks trie, if there is a word
        that starts with the given prefix, return True

        This is similar to the search
        except that we do not need to check for endOfWord
        """

        # pointer
        current = self.root

        for char in prefix:
            if char not in current.children:
                return False

            # shift pointer
            current = current.children[char]

        # return True
        return True


if __name__ == '__main__':
    trie = Trie()
    trie.insert('apple')

    # returns True
    print(trie.search('apple'))
    # returns False
    print(trie.search('app'))
    # returns True
    print(trie.startsWith('app'))

    trie.insert('app')
    # returns True
    print(trie.search('app'))
