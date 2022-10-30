from LinkedList import *

"""
Given the heads of two SORTED linked lists
merge the two lists into one sorted list

"""

"""
To do this, 
we'll have to initialize some pointers 
pointing to heads of list1, list2 

we'll also initialize a dummy node 
we're we'll be appending to dummy.next

we'll say while list1 or list2 

if list1.val < list2.val:
dummy.next =list1
we shift list1 = list1.next 

elif list2.val < list1.val 
dummy.next = list2
we shift list2 = list2.next 

"""

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        dummy = ListNode()
        current = dummy

        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                # shift list1
                list1 = list1.next
            else:
                current.next = list2
                # shift list2
                list2 = list2.next

            # shift current pointer
            current = current.next

        # append remaining list
        if list1:
            current.next = list1
        elif list2:
            current.next = list2

        return dummy.next

if __name__ == '__main__':
    list1 = LinkedList()
    list1.head = ListNode(1, ListNode(2, ListNode(4)))

    list2 = LinkedList()
    list2.head = ListNode(1, ListNode(3, ListNode(4)))

    ans = Solution().mergeTwoLists(list1.head, list2.head)

    printLinkedList_head(ans)











