"""
Given two strings
s and t
return True if t is an anagram of s

An anagram is a word formed by rearranging the letters of a different word
ie all the letters appear exactly the same amount of times

"""

"""
To solve this problem, 

we know that an anagram is where two words have exactly the same letter count 

We'll need to get a charCount for s and t 

we can get a charCount using a dictionary 

we'll have a dictionary for s
and a dictionary for t 

we'll get a charCount for each 

sCount should be == tCount 

return sCount == tCount
        
"""

class Solution():
    def isAnagram(self, s, t):
        # edge case
        if len(s) != len(t):
            return False

        sCount, tCount = {}, {}

        for i in range(len(s)):
            sCount[s[i]] = 1 + sCount.get(s[i], 0)
            tCount[t[i]] = 1 + tCount.get(t[i], 0)

        return sCount == tCount

if __name__ == '__main__':
    s = 'anagram'
    t = "nagaram"

    s1 = 'rat'
    t1 = 'car'

    print(Solution().isAnagram(s, t))
    print(Solution().isAnagram(s1, t1))
