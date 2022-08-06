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
We can take a sliding window approach 
where we look at every "window" 
that is size of s1 
and we'll use our window to iterate through s2

we can use two hashmaps to map s1 chars 

our second hashmap will be used to map chars
of the current window we are at 

we'll be mapping char count 
BUT also, having default val of 0 
for chars not existing in s1 or 
our sliding window 
i.e similar to one-hot encoding 

Well check if hashmaps are == 
as we traverse through s2 
using our window 

We'll use a variable, matches
that will be incremented
when we have matching charCount 

when matches add to 26, 
we'll know weve found a permutation 


    *** edge case
    if len(s1) > len(s2) 
    we return false 
"""



class Solution(object):
    def checkInclusion(self, s1, s2) -> bool:
        # edge case
        if len(s1) > len(s2):
            return False

        # declaring arrays for mapping
        s1map = [0] * 26
        s2map = [0] * 26

        # mapping s1
        for i in range(len(s1)):
            s1map[ord(s1[i]) - ord("a")] += 1
            s2map[ord(s2[i]) - ord("a")] += 1

        # matches variable
        matches = 0

        # iterating through maps
        for i in range(26):
            if s1map[i] == s2map[i]:
                matches += 1
            else:
                0

        # sliding window

        left = 0

        # we start at len(s1) b/c
        # we already iterated through first indices above
        # when mapping s1
        for right in range(len(s1), len(s2)):
            if matches == 26:
                return True

            # getting the index
            # where our right pointer at
            idx = ord(s2[right]) - ord("a")

            # incrementing s2map at idx
            s2map[idx] += 1

            # NOW...
            # Since we've incremented the count at idx
            # we check if it is matching the idx at s2map[idx]
            # and increment matches
            if s1map[idx] == s2map[idx]:
                matches += 1
                # if s1map[idx] + 1 == s2map[idx]
                # we've incremented our s2map   *line 95
                # too much
                # so we have to decrement matches
            elif s1map[idx] + 1 == s2map[idx]:
                matches -= 1

            # ***Left Pointer Adjustment***

            idx = ord(s2[left]) - ord("a")
            # we decrement count here b/c
            # we just removed this variable
            # as we're shifting our sliding window
            s2map[idx] -= 1

            if s1map[idx] == s2map[idx]:
                matches += 1
            # opposite of right
            elif s1map[idx] - 1 == s2map[idx]:
                matches -= 1
            # increment left pointer
            left += 1
        # we need to check again after we've done our shifting
        return matches == 26









# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    s1_a = "ab"
    s2_a = "eidbaooo"

    s1_b = "ab"
    s2_b = "eidboaoo"

    print(Solution().checkInclusion(s1_a, s2_a))
    print(Solution().checkInclusion(s1_b, s2_b))
