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
We're to form a sliding window 

We also want to calculate a charCount

The len(window) - most frequent charCount = number of letters to replace!!
                                            number of letters to replace <= k
if number of letters to replace > k 
we'll need to shift our leftPointer 
and b/c we shifted our pointer 
we need to decrement the count 
of the char we just moved past                                             
                                            

We'll be keeping track of the max len using a res variable

"""


class Solution(object):
    def characterReplacement(self, s: str, k: int) -> int:

        charCount = {}
        res = 0

        # leftPointer set at 0
        leftPointer = 0

        # rightPointer will iterate through s
        for rightPointer in range(len(s)):
            # mapping char:count
            charCount[s[rightPointer]] = 1 + charCount.get(s[rightPointer], 0)

            # number of letters to replace = len(window) - max(charCount)
            # if number of letters to replace > k
                # we want to shift leftPointer
                # and decrement count s[leftPointer]
            while ((rightPointer - leftPointer + 1) -
                   max(charCount.values())) > k:
                charCount[s[leftPointer]] -= 1
                leftPointer += 1

            # update res for max window length
            res = max(res, rightPointer - leftPointer + 1)
        return res


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    k = 1
    s = "AABABBA"
    print(Solution().characterReplacement(s, k))
