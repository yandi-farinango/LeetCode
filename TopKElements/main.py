"""
Given an integer array nums and an integer k,
return the k most frequent elements.

You may return the answer in any order.
"""


"""
To solve this problem we can:

Start by mapping numbers:frequency
We can do this using a dictionary 
update frequency as we traverse through the array 

We can then use a BUCKET array 
to sort frequencies 
where frequency corresponds to
BUCKET array indices 

Finally, we'll need to return our ans 
in a result array 

We will be adding numbers
to our result array 
as we traverse BUCKET in reverse 

if length(result) == k
we'll return result 
"""


class Solution(object):
    def topKFrequent(self, nums, k):

        freqMap = {}
        bucket = [[] for i in range(len(nums) + 1)]

        for n in nums:
            freqMap[n] = 1 + freqMap.get(n, 0)

        for number, count in freqMap.items():
            bucket[count].append(number)

        res = []

        for index in range(len(bucket) - 1, -1, -1):
            for numbers in bucket[index]:
                res.append(numbers)
                if len(res) == k:
                    print(res)


if __name__ == "__main__":
    nums = [1, 1, 1, 2, 2, 3, 3, 3, 3]
    k = 2

    print(Solution().topKFrequent(nums, k))
