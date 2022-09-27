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
        # initialize hashmap that will be used to map oldnode:newnode
        nodeMap = {None: None}

        # first pass - cloning the nodes
        #            - mapping oldNodes:copyNodes
        current = head

        while current:
            # create a new node
            # that is a copy of the current node
            copy = Node(current.val)

            # map the current node:copy node
            nodeMap[current] = copy
            current = current.next

            # second pass -
        current = head
        while current:
            # returns copy node
            # that is mapped at nodeMap[current]
            copy = nodeMap[current]

            # set copy.next
            # to the copied     returned copy of current.next node  example above!
            copy.next = nodeMap[current.next]
            copy.random = nodeMap[current.random]
            current = current.next

        return nodeMap[head]

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
