def printLinkedList(linkedList):
    node = linkedList

    while node:
        print(node.val)
        node = node.next
