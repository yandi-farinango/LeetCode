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




class Solution(object):
    def lengthOfLongestSubstring(self, s):

        # set for ensuring no duplicates
        charSet = set()

        res = 0

        leftPointer = 0

        for rightPointer in range(len(s)):
            # if we already have s[rightPointer], i.e DUPLICATE
            while s[rightPointer] in charSet:
                # we remove the left element
                charSet.remove(s[leftPointer])
                # and, increment leftPointer
                leftPointer += 1
            # once we've removed duplicates,
            # we can add right char to our set
            charSet.add(s[rightPointer])

            res = max(res, rightPointer - leftPointer + 1)

        return res



if __name__ == '__main__':
    s = "abcabcbb"

    print(Solution().lengthOfLongestSubstring(s))
