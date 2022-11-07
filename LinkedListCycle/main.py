from LinkedList import *

"""
Given the HEAD of a linked list,

Determine if the linkedList has a cycle

There is a cycle if,
some node in the list
can be reached repeatedly
by following the next pointer
"""

"""
To solve, 
we can use two pointers, 
fast, slow

We'll shift our fast pointer 
fast = fast.next.next 

and slow pointer 
slow = slow.next 

Since we'll be shifting our fast pointer 
fast = fast.next.next 

we can loop 
while fast and fast.next

If the two pointers ever meet 
ie fast == slow 
we know we have a cycle 
return TRUE 
"""


class Solution(object):
    def hasCycle(self, head):
        # initialize pointers
        fast, slow = head, head

        # loop
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

            if fast == slow:
                return True

        return False

if __name__ == '__main__':
    ll = LinkedList()

    ll.head = ListNode(3)
    l2 = ListNode(2)
    l3 = ListNode(0)
    l4 = ListNode(-4)

    ll.head.next = l2
    l2.next = l3
    l3.next = l4
    l4.next = l2

    print(Solution().hasCycle(ll.head))




