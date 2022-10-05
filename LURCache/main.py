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
we'll be using a hashmap to return items in O(1) time complexity 
and we can use a doubly linked list to keep track of most recent/least recent used items 

We'll be using a hashmap to map keys: node

When we create a new key-val pair 
or we "get" the val for a respective key
we want to update the cache ie set respective key to most recent 

We're going to be keeping track of most recent/least recent 
using a doubly linked list 

We'll use pointers 
Left, Right 
Where our LRU will always be to the right of our left ie left.next 
and our most recent will always be inserted to the left of right ie right.prev

"""

"""
Initialize a Node class
"""
class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val

        self.prev = None
        self.next = None


class LRUCache(object):

    def __init__(self, capacity):
        """
        Initializes:
        - hashmap for mapping keys: node
        - left, right pointers

        left, right pointers shall initially be connected to one another
        we are going to be inserting nodes in between left -> ___ -> right

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
        Returns the val for the respective key
        bc we are mapping key: nodes
        our val is at cache[key].val

        Updates node position on our doubly linked list
        we want to remove the respective node
        and re-insert it at the right-most position ie most recently used

        If the key not in self.cache
        return -1
        """
        if key in self.cache:
            # TODO create remove/insert helper functions
            self.remove(self.cache[key])
            self.insert(self.cache[key])

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

        We also want to check our capacity,
        if we're over capacity,
        remove the left most node from our list
        and delete the node from our cache
        """

        # remove node from our list
        if key in self.cache:
            self.remove(self.cache[key])

        # update cache to map key: new Node
        self.cache[key] = Node(key, value)

        # insert new node into our list
        self.insert(self.cache[key])

        # if len self.cache > capacity
        if len(self.cache) > self.capacity:
            lru = self.left.next
            # remove LRU ie left-most node from our list
            self.remove(lru)
            # and delete node from our cache
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

        # get reference points
        prev = node.prev
        nxt = node.next

        # remove
        prev.next = nxt
        nxt.prev = prev

    def insert(self, node):
        """
        Inserts nodes at the right most position

        To insert a node at right
        We want to
        # update right's pointers
        - get a reference to the right most position;   prev = self.right.prev
        - get a reference to our right node;    nxt = self.right
            * used to set node.next = nxt

        - insert node at prev's next;           prev.next = node
        - update nxt node's, aka right node's, prev pointer = node

        # connect node's pointers
        - set node.next = nxt
        - set node.prev = prev
        """

        # get references to right
        prev = self.right.prev
        nxt = self.right

        # update right's pointers
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
