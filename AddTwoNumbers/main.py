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
We can actually solve this problem
taking an elementary school approach 

    Ex: 123
      + 456
      ------
      
In solving the expression above, 
we're going to start adding at the ones place 

the lists are already given to us starting at the ones! 

the thing we'll have to take note of is what happens when 
we add values > 10 
and we have 

we can get the carried tens-place value by //10
and we can get the ones-place value by % 10 

We'll use initialize a dummy node 
and we'll append our vals to dummy.next 

return dummy.next 
"""


class Solution(object):
    def addTwoNumbers(self, list1, list2):
        # intialize dummy
        dummy = ListNode()

        # pointer
        current = dummy

        # initialize carry at 0
        carry = 0

        while list1 or list2 or carry:
            v1 = list1.val if list1 else 0
            v2 = list2.val if list2 else 0

            # add
            val = v1 + v2 + carry

            # get carried and val
            carry = val // 10
            val = val % 10

            # append
            current.next = ListNode(val)

            # shift pointers
            current = current.next
            list1 = list1.next if list1 else None
            list2 = list2.next if list2 else None

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