from LinkedList import *
from PrintLinkedList import *

"""
Given the head of a linked list 
Remove the nth node 
from the end of the list 
Return its head 
"""

"""
We can use two pointers, 
fast and slow

If we maintain n distance between the pointers, 
by the time the fast pointer reaches the end of the linked list 
the slow pointer should be on the nth node from the end 

We can remove that node 
"""

class Solution(object):
    def removeNthFromEnd(self, head, n):
        # initialize pointers
        dummy = ListNode(0, head)

        fast = head
        slow = dummy

        # get fast pointer in the correct position
        i = 0
        while i < n:
            fast = fast.next
            i += 1

        # shift pointers
        while fast:
            slow = slow.next
            fast = fast.next

            # remove node
        slow.next = slow.next.next

        return dummy.next

if __name__ == '__main__':
    ll = LinkedList()
    ll.head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    n = 2

    printLinkedList(ll.head)

    print('--Removed--')
    ans = Solution().removeNthFromEnd(ll.head, n)
    printLinkedList(ans)

