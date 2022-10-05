from LinkedList import *

"""
We are given two linked lists 
representing numbers written in reverse order 
    Ex: number: 123
        list: 3->2->1
        
Add the two numbers 
and return the ans in the same format 
"""

"""
We can add both numbers quite easily if we 
write them out in elementary fashion 
             1
    Ex:     123
          + 569
          ------
            692
            
We see that we actually start our addition at the ones-place

Lucky for us, 
We are given the lists in reverse! ie. starting at the ones-place
We can get these vals pretty easily l1.val, l2.val 
and perform the addition 

We also see that we're going to have to deal with carrying the tens place 

We can have a variable carry, 
that will get updated with the tens-place value that we carry in the event of an addition where ans > 10


We'll initialize a dummy node at the start
where we will be appending the val at dummy.next 
the val we want to append is the ones-place 
we can get this by val = val % 10 
and we set dummy.next = val 

we can traverse while list1 or list 1 or carry 

"""


class Solution(object):
    def addTwoNumbers(self, l1,l2):
        # initialize dummy node
        dummy = ListNode()

        """
        Traverse
        """
        # pointer to dummy
        current = dummy
        # initialize carry at 0
        carry = 0

        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            # addition
            total = v1 + v2 + carry

            # get tens, ones places
            carry = total // 10
            val = total % 10

            # connect to dummy
            current.next = ListNode(val)

            # shift pointers
            current = current.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next


if __name__ == "__main__":
    l1 = LinkedList()
    l1.head = ListNode(2, ListNode(4, ListNode(3)))

    l2 = LinkedList()
    l2.head = ListNode(5, ListNode(6, ListNode(4)))

    l3 = LinkedList()
    l3.head = ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9)))))))

    l4 = LinkedList()
    l4.head = ListNode(9, ListNode(9, ListNode(9, ListNode(9))))

    # Should print 708
    ans = Solution().addTwoNumbers(l1.head, l2.head)
    printLinkedList_head(ans)

    print('-------')

    # Should print 89990001
    ans2 = Solution().addTwoNumbers(l3.head, l4.head)
    printLinkedList_head(ans2)