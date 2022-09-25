# implement Linked List

class LinkedList(object):
    def __init__(self):
        self.head = None

class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

def printLinkedList(linkedlist):
    node = linkedlist

    while node:
        print(node.val)
        node = node.next

def printLinkedListHEAD(linkedlist):
    node = linkedlist.head

    while node:
        print(node.val)
        node = node.next