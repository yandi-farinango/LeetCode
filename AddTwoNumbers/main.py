from LinkedList import *

"""
We are given two lists
each representing a number,
written in reverse order

    Ex: number =            123
        linkedList =        3 -> 2 -> 1

Add the two given numbers

and return the ans
as a linkedList
following the same format

    Ex:     number1 = 213
            number2 = 521

            ans = 734

            --GIVEN--
            list1 = 3->1->2
            list2 = 1->2->5

            ans = 4->3->7

"""

"""
We can actually sum this pretty straightforward! 

If we remember from elementary addition 
             1
    Ex:     125
          + 456
          ------
            581
            
We actually start adding from the ones place 
we carry the one - from the tens place 
etc. 

Bc our numbers are given in REVERSE order 
we can start adding vals at the head of the linked lists! 

We'll create a dummy node where well be appending/connecting 
our ans to 

We'll need a carry variable to hold tens-place vals 
in the event that we need to carry 

Well get the carry val by val//10 
well get the val by val % 10 

"""


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        # initialize dummy node
        dummy = ListNode()

        # pointer to dummy
        current = dummy

        # intialize carry at 0
        carry = 0

        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            # add vals
            total_sum = v1 + v2 + carry

            # get val to carry
            carry = total_sum // 10

            # get ones - place val
            val = total_sum % 10

            # connect pointer
            current.next = ListNode(val)

            # shift pointers
            current = current.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next


if __name__ == "__main__":
    list1 = LinkedList()

    list1.head = Node(2)
    l1 = Node(4)
    l2 = Node(3)

    list1.head.next = l1
    l1.next = l2

    list2 = LinkedList()

    list2.head = Node(5)
    l1_2 = Node(6)
    l2_2 = Node(4)

    list2.head.next = l1_2
    l1_2.next = l2_2

    # Printing lists
    printLinkedList(list1)
    print('----')
    printLinkedList(list2)

    print('--ANS--')
    ans = (Solution().addTwoNumbers(list1.head, list2.head))
    printLinkedList_head(ans)