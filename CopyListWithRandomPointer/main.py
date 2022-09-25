"""
We are given a linked list
where each node has an additional random pointer

the random pointer
can point to any node within the linked list
or null

We want to create a copy of the given linked list

"""

"""
The tricky part about this problem is 
copying the random pointer 
and the respective node which 
the random pointer is pointing at 

For some nodes, 
the random pointer may be pointing at a node 
that is further down the list 
ie hasn't been created yet 

bc of this, 
we're going to have to loop through our linked list 
in two-passes 

On the first pass 
we'll just be creating a copy of the nodes 
We also want to create a hashmap 
to map original node: new copied node 


On the second pass 
we'll be connecting the pointers 
to the next node 
and the random pointer 

We'll be able to use our hashmap 
to tel us where our nodes should be pointing at 

"""

from LinkedList import *

class Solution(object):
    def copyRandomList(self, head):

        # initializing hashmap
        # map null to null on initialization
        oldToCopy = {None:None}

        # first pass
        current = head

        while current:
            # copying node
            copy = Node(current.val)

            # mapping old node to our copy
            oldToCopy[current] = copy

            current = current.next

        # second pass
        current = head
        while current:
            # get our copy
            copy = oldToCopy[current]

            # connecting nodes
            copy.next = oldToCopy[current.next]
            copy.random = oldToCopy[current.random]

            current = current.next

        return oldToCopy[head]


if __name__ == '__main__':
    ll = LinkedList()

    ll.head = Node(7)
    l2 = Node(13)
    l3 = Node(11)
    l4 = Node(10)
    l5 = Node(1)

    ll.head.next = l2
    ll.head.random = None

    l2.next = l3
    l2.random = ll.head

    l3.next = l4
    l3.random = l5

    l4.next = l5
    l4.random = l3

    l5.next = None
    l5.random = ll.head

    copy = Solution().copyRandomList(ll.head)

    print(bool(ll.head.val == copy.val),
          bool(ll.head.next.val == copy.next.val),
          bool(ll.head.random == copy.random))
