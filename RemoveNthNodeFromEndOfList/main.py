from LinkedList import *
from PrintLinkedList import *

"""
Given the head of a linked list 
Remove the nth node 
from the end of the list 
Return its head 
"""

"""
We can do this using two pointers 
slow, fast 

We want to get the pointers n nodes apart 
and then shift them together 
when the fast pointer reaches the end, 
the slow pointer should be at the nth node from the end 

We can use a dummy node 
that will be one node behind the slow pointer 

when the slow pointer is at the nth node from the end 
We can delete the nth node 
by setting the dummy node = next.next 


To get the pointers in the respective position,
we'll first need to move the fast pointer by itself 

Once the fast pointer is in position 
we can shift all pointers 

To delete nth node 
we set dummy.next = dummy.next.next 

"""

class Solution(object):
    def removeNthFromEnd(self, head, n):
        # intialize nodes
        slow, fast = head, head

        dummy = ListNode(0, head)
        current = dummy

        # get Fast in position
        i = 0
        while i < n:
            fast = fast.next
            i += 1

        # shift pointers
        while fast:
            fast = fast.next
            slow = slow.next
            current = current.next

        # DELETE
        # skip over slow pointer
        current.next = current.next.next

        return dummy.next

if __name__ == '__main__':
    ll = LinkedList()
    ll.head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    n = 2

    printLinkedList(ll.head)

    print('--Removed--')
    ans = Solution().removeNthFromEnd(ll.head, n)
    printLinkedList(ans)

