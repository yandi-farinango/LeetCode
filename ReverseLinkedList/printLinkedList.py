# Implement print Linked List

def printLinkedList(linkedlist):
    node = linkedlist

    while node:
        print(node.val)
        node = node.next


