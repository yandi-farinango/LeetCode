"""
Given two strings s1, s2

return True
if s2 contains
a permutation of s1

    Ex: s1 = "ab"
        s2 = "eidbaooo"
        output = True

        s2 contains one permutation of s1 ("ba")

            * s1 may be rearranged
            * return True if substring s1 in s2
"""


"""
We can use an arrayMap 
to map letters a-z at indicies 0-26
Where value corresponds to the charCount 

We can then use a sliding window 
of the same size as s1
which will be formed using two pointers 

left pointer at 0 
right pointer will be used to traverse s2 

we'll also have a variable, matches, 
that will count the number of "matches"
in our two charMaps 

So, we'll need to 
    update our charCount as we shift our window 
    and update matches as our charCount changes 

    i.e if we shift our window and our charCount increases, 
    and our matches are no longer the same, 
    we'll need to decrement matches 
    similarly, if we shift our window 
    and our charCount now = charCount s1 
    we'll need to increment our matches

    We'll return True if matches == 26 
"""


class Solution(object):
    def checkInclusion(self, s1, s2) -> bool:
        # edge case
        if len(s1) > len(s2):
            return False

        s1map = [0] * 26
        s2map = [0] * 26

        for i in range(len(s1)):
            # map s1
            s1map[ord(s1[i]) - ord('a')] += 1
            # map s2
            s2map[ord(s2[i]) - ord('a')] += 1

        matches = 0

        # we traverse both arrays
        # update matches if charCounts are equal
        for i in range(26):
            if s1map[i] == s2map[i]:
                matches += 1

        # now we use a sliding window
        # and update matches

        left = 0

        # we start at len(s1) b/c our window needs to be min len(s1)
        for right in range(len(s1), len(s2)):
            if matches == 26:
                return True

            index = ord(s2[right]) - ord('a')

            # increment s2map at the respective index
            s2map[index] += 1

            # update matches
            if s2map[index] == s1map[index]:
                matches += 1

            # NOTE s1map charCount should never change!!
            # if after incrementing s2map[index]
            # s2map[index] == s1map[index] + 1
            elif s2map[index] == s1map[index] + 1:
                matches -= 1

                # shift left pointer
            index = ord(s2[left]) - ord('a')

            # decrease charCount
            s2map[index] -= 1

            if s2map[index] == s1map[index]:
                matches += 1

            # same as above but we put statment here
            # bc we are reducing a charCount
            # by shifting left pointer!!
            elif s2map[index] == s1map[index] - 1:
                matches -= 1

            # update left
            left += 1

        return matches == 26


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    s1_a = "ab"
    s2_a = "eidbaooo"

    s1_b = "ab"
    s2_b = "eidboaoo"

    print(Solution().checkInclusion(s1_a, s2_a))
    print(Solution().checkInclusion(s1_b, s2_b))
