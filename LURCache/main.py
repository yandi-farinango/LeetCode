"""
Design a data structure that
follows the constraints of
Least Recently Used (LRU) Cache

Implement the LRU Cache class

LRUCache(int capacity) initializes the LRU cache with POSITIVE size capacity

int get(int key) return the value of the KEY if key exists else return -1

void put(int key, int value) update the value of the key if the key exists
                                else add the key-value pair to the cache

                            If the number of keys exceeds the capacity,
                            evict the least recently used key

The functions get and put must run in O(1) time complexity

"""

"""
For this problem
We'll be initialize our cache as a dictionary - allowing us to return vals in O(1)
self.cache = {}
we'll be mapping self.cache = key: node(key,val) 
and returning self.cache[key].val

We'll want to keep track of our least recently/most recently used keys
we'll do this using doubly linked list

We'll use pointers 
Left, Right 
Where our LRU will always be to the right of our left ie left.next 
and our most recent will always be inserted to the left of right ie right.prev

"""

"""
Node class
"""
class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val

        # initialize prev, next pointers
        self.prev = None
        self.next = None


class LRUCache(object):

    def __init__(self, capacity):
        """
        Initializes
        - capacity
        - cache dictionary
        - left, right pointers

        We want to initially connect left and right pointers
        as we will be inserting nodes in between left -> ___ -> right
        """
        self.capacity = abs(capacity)
        self.cache = {}

        # initialize pointers
        self.left, self.right = Node(0, 0), Node(0, 0)

        # connect pointers
        self.left.next = self.right
        self.right.prev = self.left

    def get(self, key):
        """
        If key in cache
        returns the respective val
            since we are performing a "get" operation on a given key
            we want to remove the node from our list
            and re-insert it at the right-most position

        If key not in cache
        return -1
        """
        if key in self.cache:
            # TODO create remove/insert helper functions
            self.remove(self.cache[key])
            self.insert(self.cache[key])

            # return node val
            return self.cache[key].val
        return -1

    def put(self, key, value):
        """
        Inserts key, val into our cache
        Our cache is mapping key: node(key, val)

        If a node already exists for the respective key,
        we'll want to
        - remove that node from our list
        - update cache mapping key: new Node
        - insert new Node into list

        Check capacity
        if len(cache) > capacity
        - remove the left most node from our list
        - delete the removed node's key from our cache
        """

        # remove node from list
        if key in self.cache:
            self.remove(self.cache[key])

        # update cache w new node
        self.cache[key] = Node(key, value)

        # insert new node
        self.insert(self.cache[key])

        # capacity
        if len(self.cache) > self.capacity:
            lru = self.left.next
            # remove LRU ie left-most node from list
            self.remove(lru)
            # delete respective node's key from cache
            del self.cache[lru.key]

    """
    Helper Functions
    """
    def remove(self, node):
        """
        Removes nodes from our list

        To remove a node from our list
        We want to
        - get a reference to the prev node;     prev = node.prev
        - get a reference to the next node;     nxt = node.next
        - skip over node ie set prev.next = nxt

        """

        # get references
        prev = node.prev
        nxt = node.next

        # remove
        prev.next = nxt
        nxt.prev = prev

    def insert(self, node):
        """
        Inserts a node at the right-most position

        To insert a node at the right most position we need to
        - get reference to right.prev
        - get a reference to the right node

        Update the pointers
        - connecting right.prev to our node
        - connecting prev.next to our node

        Update node's pointers
        - connect node.next to right reference
        - connect node.prev to prev reference
        """

        # get references
        prev = self.right.prev
        nxt = self.right

        # update pointers
        prev.next = node
        nxt.prev = node

        # connect node's pointers
        node.next = nxt
        node.prev = prev


if __name__ == '__main__':
    object = LRUCache(2)

    object.put(1, 1)

    object.put(2, 2)

    # return 1
    print(object.get(1))

    object.put(3, 3)

    # return -1 object not found
    print(object.get(2))

    object.put(4, 4)

    # return -1 object not found
    print(object.get(1))

    # return 3
    print(object.get(3))

    # return 4
    print(object.get(4))
