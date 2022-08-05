"""
Given a string, S
and int, K

We can choose any char
in string, S,
and change to any uppercase letter

We can only change K times

return the len of longest substring
containing the same letter

    Ex:
        s = "AABABBA"
        k = 1

        output = 4; AAAA
"""


"""
We're going to build a sliding window 
using two pointers 

We also want to use a charCount hashmap 
to map char:count

As we traverse through string S
using our rightPointer
We can increment a charCount 

    *** we also want to shift our left pointer 
        when number of chars to switch > k 

        * number of chars to switch = len(window) - max charCount

maxLen will be calculated
res = max(res, rightPointer - leftpointer + 1)

return res
"""



class Solution(object):
    def characterReplacement(self, s: str, k: int) -> int:

        charCount = {}
        res = 0

        leftPointer = 0

        # use rightPointer to iterate
        for rightPointer in range(len(s)):
            # increment charCount as we build our sliding window
            charCount[s[rightPointer]] = 1 + charCount.get(s[rightPointer], 0)

            # shift pointer when chars to switch > k
            # decrement respective charCount
            while ((rightPointer - leftPointer + 1) - max(charCount.values())) > k:
                charCount[s[leftPointer]] -= 1
                leftPointer += 1

            res = max(res, rightPointer - leftPointer + 1)

        return res


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    k1 = 1
    s1 = "AABABBA"

    k2 = 2
    s2 = "ABAB"

    print(Solution().characterReplacement(s1, k1))
    print(Solution().characterReplacement(s2, k2))
