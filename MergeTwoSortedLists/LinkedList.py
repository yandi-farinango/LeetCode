"""
Implement LinkedList
"""

class LinkedList(object):
    """
    LinkedList class
    """
    def __init__(self):
        self.head = None



class Node(object):
    """
    Node has pointers for next
    """
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next



class ListNode(object):
    """
    ListNode has pointers for next and random
    """
    def __init__(self, val=0, next=None, random=None):
        self.val = val
        self.next = next
        self.random = random


"""
Implementation for printing a LinkedList
"""


def printLinkedList(linkedlist):
    """
    Print a linkedlist
    if given linkedlist - not HEAD
    """
    node = linkedlist.head

    while node:
        print(node.val)
        node = node.next


def printLinkedList_head(linkedlist_head):
    """
    Print a LinkedList
    if given the HEAD of a LinkedList
    """
    node = linkedlist_head

    while node:
        print(node.val)
        node = node.next
