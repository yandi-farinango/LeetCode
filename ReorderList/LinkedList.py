# Implement LinkedList

class ListNode(object):
    def __init__(self,x):
        self.val = x
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
