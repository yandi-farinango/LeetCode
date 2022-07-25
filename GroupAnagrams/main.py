"""
Given an array of strings, strs,
Group the anagrams together
Return ans in any order

    * Anagram *
    is a word or phrase
    formed by re-arranging letters
    of a different word or phrase
    using all the original letters exactly once

    Ex:
    [ATE, TEA, EAT]
"""
import collections

"""
First, we know an anagram is a word 
made by re-arranging the letters
of a different word 

BIG HINT: Anagrams are going to have 
the same letters & letter count! 

For each string in strings, 
we can create an array, COUNT,
in which indices correspond to
the 26 letters of the alphabet 
AND 
the values stored within each index
corresponds to the frequency
of the respective letter 

    - FOR MAPPING - 
    Once we've created array, COUNT, 
    for each string in strs
    we'll need to store character count 
    in the respective COUNT index
    
    For each character,
    We'll subtract ord(c) - ord("a")
    to access COUNT index 
    representing the respective letter 
    and increment 
    
We can use a hashmap, res,
to map COUNT:anagrams
Our key will be tuple(COUNT) 
and we will append strings 
with same tuple(COUNT)

Finally, we return 
res.values
    * we only want to return values
    not the COUNT array associated w 
    each group of strings
    
"""

class Solution(object):
    def groupAnagram(self, strs):
        res = collections.defaultdict(list)

        for s in strs:
            count = [0] * 26

            for c in s:
                count[ord(c) - ord("a")] += 1

            res[tuple(count)].append(s)

        return res.values()



if __name__ == '__main__':
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]

    print(Solution().groupAnagram(strs))
