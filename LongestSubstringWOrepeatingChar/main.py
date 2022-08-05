"""
Given a string, s,
find the length
of the longest substring
w/o repeating characters
"""

"""
We can use a start checking 
len of substrings 
starting at pos 0
until we get to a duplicate
if we reach a duplicate, 
we'll remove from the left
of our sliding window

Sliding window will be formed
using two pointers 

"""

"""
We'll form a sliding window using two pointers
And well use a set to check for duplicates

To create our window,
we'll use two pointers
leftPointer will be initialized at 0

rightPointer will loop through string s
as we loop through,

we can say that...
while s[rightPointer] is already in charSet, i.e DUPLICATE
    we'll remove s[leftPointer] from our charSet
    AND we'll need to update our leftPointer += 1

as there are no duplicates,
we can add s[rightPointer] to our charSet


*** b/c this algo will continuously remove/add
    to our charSet as it iterates through the entire string
    we'll need a res variable
    that will hold the max len of our char set

    len of charSet is calculated by
    rightPointer - leftPointer + 1

return res variable
"""




class Solution(object):
    def lengthOfLongestSubstring(self, s):

        charSet = set()
        res = 0

        leftPointer = 0

        for rightPointer in range(len(s)):
            # duplicate check
            while s[rightPointer] in charSet:
                charSet.remove(s[leftPointer])
                leftPointer += 1

            charSet.add(s[rightPointer])

            # max Length
            res = max(res, rightPointer - leftPointer + 1)

        return res



if __name__ == '__main__':
    s1 = "abcabcbb"
    s2 = "pwwkew"

    print(Solution().lengthOfLongestSubstring(s1))
    print(Solution().lengthOfLongestSubstring(s2))
