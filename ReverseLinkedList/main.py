from LinkedList import *
from printLinkedList import *

"""
Given the head of a linked list, 
reverse the list
and return the reversed list 
"""

def reverseList(head):
    prev = None

    while head:
        temp = head.next
        head.next = prev
        prev = head
        head = temp

    return prev



# Press the green button in the gutter to run the script.
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

    printLinkedList(ll.head)

    # Reversed
    reversed = reverseList(ll.head)
    print('--Reversed--')
    printLinkedList(reversed)





