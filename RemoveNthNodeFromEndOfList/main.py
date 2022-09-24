from LinkedList import *
from PrintLinkedList import *


class Solution(object):
    def removeNthFromEnd(self, head, n):
        # initialize dummy node
        dummy = ListNode(0, head)
        slow = dummy

        fast = head

        # get fast in the correct position
        while n > 0 and fast:
            fast = fast.next
            n -= 1

        # shift pointers
        while fast:
            slow = slow.next
            fast = fast.next

        # delete the node
        slow.next = slow.next.next

        return dummy.next


class Solution2(object):
    def removeNthFromEnd(self, head, n):
        slow, fast = head, head

        # get fast pointer in correct position
        i = 0
        while i < n:
            fast = fast.next
            i += 1

        # shift pointers
        while fast and fast.next:
            slow = slow.next
            fast = fast.next

        # remove nth node
        slow.next = slow.next.next

        return head


if __name__ == '__main__':
    ll = LinkedList()
    ll.head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    n = 2

    ans = Solution().removeNthFromEnd(ll.head, n)
    printLinkedList(ans)

    # Solution 2
    ll2 = LinkedList()
    ll2.head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    n = 2

    ans2 = Solution2().removeNthFromEnd(ll2.head, n)
    print("--Solution 2--")
    printLinkedList(ans2)
