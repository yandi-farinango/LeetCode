# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.
#
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')
#



class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

class Solution(object):
    def hasCycle(self, head):
        fast, slow = head, head

        while head.next:
            slow = head.next
            fast = head.next.next

            if slow.val != fast.val:
                return False
            else:
                return True

ll = LinkedList()

ll.head = ListNode(3)
l2 = ListNode(2)
l3 = ListNode(0)
l4 = ListNode(-4)

ll.head.next = l2
l2.next = l3
l3.next = l4
l4.next = l2

print(Solution.hasCycle(ll.head))


