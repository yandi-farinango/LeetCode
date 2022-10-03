"""
Given an array of ints

containing n+1 integers
where each integer is in
the range [1,n] inclusive

in which there is one repeated number

find and return the repeated number

must solve without modifying the array
and using constant extra space

"""

"""
Although we are given an array, 

We can think of this as a linked list 

where the val in array[i]
is a reference to the ith node

    Ex: [1,3,4,2,2]
        val at array[0]
        is pointing to val at position array[1]
        
        val at array[1]
        is pointing to val at position array[3]
        
If we connect all the pointers, 
we'll see that our linked list actually has a cycle! 

The duplicate val 
will be the node
which has multiple nodes pointing towards it 

We'll apply Floyd's algo 
to determine which is our duplicate val

For Floyd's algo, 
we need two pointers 
slow, fast = head, head 

We'll shift
slow = slow.next 
fast = fast.next.next 

We want to get the first position
where our pointers will intersect at 

When we've found the first intersection, 
We want to introduce another slow pointer 
slow_2 = head

We'll continue to shift all our pointers 
slow = slow.next 
slow_2 = slow_2.next 

"""


class Solution(object):
    def findDuplicate(self, nums):
        # initialize pointers
        slow, fast = 0, 0

        while True:
            slow = nums[slow]
            # nums[nums[fast]] shifts the pointer twice
            fast = nums[nums[fast]]

            # we've found our first intersection
            if slow == fast:
                break

        # initialize slow_2
        slow_2 = 0

        # shift both slow pointers until they intersect
        while True:
            slow = nums[slow]
            slow_2 = nums[slow_2]

            # second intersection
            if slow == slow_2:
                return slow  # we can return either slow or slow_2


if __name__ == '__main__':
    nums = [3, 1, 3, 4, 2]

    print(Solution().findDuplicate(nums))
