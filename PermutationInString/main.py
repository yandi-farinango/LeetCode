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

        s1Map = [0] * 26
        s2Map = [0] * 26

        # We'll map s1 first
        # since charCounts will not change
        # like a sliding window charCount
        for i in range(len(s1)):
            s1Map[ord(s1[i]) - ord("a")] += 1
            s2Map[ord(s2[i]) - ord("a")] += 1

        matches = 0

        # now we'll traverse both arrays and update matches
        for i in range(26):
            if s1Map[i] == s2Map[i]:
                matches += 1

        # now sliding window

        left = 0

        for right in range(len(s1), len(s2)):
            if matches == 26:
                return True

            # bc we are using the loop above to
            # iterate through string s2
            # we'll need to get the charMap index
            # of the letter our right pointer is on
            index = ord(s2[right]) - ord("a")

            # and we'll need to increment
            # s2map at the respective index
            s2Map[index] += 1

            # update matches s1Map[index] == s2Map[index]
            if s2Map[index] == s1Map[index]:
                matches += 1
            # if after incrementing s2Map[index]
            # above, in line 64
            # our s2Map[index] == s1Map[index] + 1
            # we've incremented s2
            # too much
            elif s2Map[index] == s1Map[index] + 1:
                # update matches
                matches -= 1

                # left pointer adjustment
            index = ord(s2[left]) - ord("a")

            # we decrease s2Map at index
            # bc we will be shifting our left pointer
            s2Map[index] -= 1

            if s2Map[index] == s1Map[index]:
                matches += 1

            # if, by decreasing our our s2Map[index] charCount
            # in line 90
            # we are now == to s1Map[index] - 1
            # we've decreased too much
            # update matches
            if s2Map[index] == s1Map[index] - 1:
                matches -= 1

            # update left pointer
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
