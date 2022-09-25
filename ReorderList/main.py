"""
Given the head of a singly linked list,

Reorder the list as the following:

    Ex: [1,2,3,4,5]
        [1,5,2,4,3]

        In the ex above the list, of len 5
        The last element, 5,
        gets pushed between the first two elements 1,5,2
        then the 4th element gets pushed between the 2nd and 3rd elements 2,4,3

Basically, alternating between the beginning and the last elements in the list

"""
import LinkedList

"""
To do this, we can think of the list as having two halves 
Left:   1 -> 2 -> 3
Right:  4 -> 5

We can reverse the pointers in the Right portion 
Right:  5 -> 4

Then we can merge the two portions

Result: 1 -> 5 -> 2 -> 4 -> 3


First, we'll need to identify the halves 
We can do this by using fast, slow pointers 
    If we move the fast pointer .next.next 
    slow pointer .next 
    When the fast pointer reaches the end, 
    the slow pointer should be in the midway point

Once we've split the right portion from the linked list, 
we can proceed to reverse the right portion
"""

from LinkedList import *

class Solution(object):
    def reorderList(self, head):
        slow, fast = head, head.next

        # get pointers in the correct position
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # split portions
        second_half = slow.next
        slow.next = None

        # reverse second_half
        prev = None

        while second_half:
            temp = second_half.next
            second_half.next = prev
            prev = second_half
            second_half = temp

        # assign variables to the respective portions
        first_half, second_half = head, prev

        # merge the two lists
        while second_half:
            temp1, temp2 = first_half.next, second_half.next

            first_half.next = second_half
            second_half.next = temp1

            first_half = temp1
            second_half = temp2

        return head.next


if __name__ == '__main__':
    ll = LinkedList()

    ll.head = ListNode(1)
    l2 = ListNode(2)
    l3 = ListNode(3)
    l4 = ListNode(4)
    l5 = ListNode(5)

    ll.head.next = l2
    l2.next = l3
    l3.next = l4
    l4.next = l5

    printLinkedListHEAD(ll)

    Solution().reorderList(ll.head)

    print('--Reordered--')
    printLinkedListHEAD(ll)
