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
We can actually solve this pretty straightforward 

Bc we are given the numbers in reverse,
we just add like we normally would in written math 
           1 1   
    Ex:     123
        +   789
        --------
           9 1 2 

When we add numbers as shown in the example above, 
we have to start adding from the ones place 

Our linked lists are given to us 
in reverse order
meaning, we can start adding from the heads of both lists!


"""


class Solution(object):
    def addTwoNumbers(self, list1, list2):

        # create a dummy node
        # we will be adding to dummy; returning dummy.next
        dummy = Node()

        # pointer
        current = dummy

        # initialize pointer at 0
        carry = 0

        # we do while list1 or list1 OR CARRY
        # bc carry might be 1 if we add two numbers and sum > 10
        # Ex: 5+6
        while list1 or list2 or carry:
            v1 = list1.val if list1 else 0
            v2 = list2.val if list2 else 0

            # add
            val = v1 + v2 + carry

            # set carry to val's tens place
            carry = val //10
            # set val to val's ones place
            val = val % 10

            current.next = Node(val)

            # update pointers
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