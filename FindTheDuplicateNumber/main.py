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
to solve this problem, 
it helps if we think of our array as a linked list 

AND if we use our array as a linked list, 
we can then use Floyds slow, fast algo 
to find the duplciate val 

The given array 
may be thought of as a linked list 
where the indices 
represent the node 
which our .next would be pointing to 
in a linked list 

    Ex: [1, 3, 4, 2, 2]
    
        at array[0]: val = 1    meaning pointer connects to array[1]
        at array[1]: val = 3    meaning pointer connects to array[3]
        at array[2]: val = 4    meaning pointer connects to array[4]

If we consider our array to be a form of a linked list 
we can then use Floyds fast, slow pointer 
to find the duplicate val 

We will find the duplicate val by intializing 
slow, fast = 0, 0

while True
we'll shift our pointers
slow = nums[slow]
fast = nums[nums[fast]]

At the point where our fast == slow 
we want to break 

This is our first intersection 

Once we've found our first intersection point 
we'll want to introduce 
slow_2 = 0

while True
We'll move our slow pointers 
slow = nums[slow]
slow_2 = nums[slow_2]

At the point where slow == slow_2 
We've found our 2nd intersection 

THIS IS OUR DUPLICATE! 
We can return either slow or slow_2 

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
