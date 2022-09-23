def printLinkedList(linkedList):
    node = linkedList.head

    while node:
        print(node.val)
        node = node.next