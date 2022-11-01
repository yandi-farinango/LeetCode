"""
Given an integer array nums and an integer k,
return the k most frequent elements.

You may return the answer in any order.
"""


"""
To solve 

we'll need to initialize an ans variable
where well be appending the k most freq vals 

We'll need to use a freqMap to count the frequencies of the numbers 

We can then use a bucket array [[]] 
where indices correspond the the frequencies 
and values correspond to numbers with the matching frequency 

we'll need to initialize our bucket to have 
len nums + 1 buckets 
ie bucket = [[] for i in range (len(nums) + 1]

We'll need to traverse freqMap 
for number, count in freqMap.items()

bucket[count].append(number)

we can then traverse the bucket array in reverese 
ie starting with the most frequent bucket 

    we'll have to traverse for number in bucket 
    
    and append to ans 
    
    if len(res) == k
    
    return res
    
"""


class Solution(object):
    def topKFrequent(self, nums, k):

        # get freqCount
        freqMap = {}
        bucket = [[] for i in range(len(nums) + 1)]
        # bucket = [[]] * (len(nums) + 1)

        for n in nums:
            freqMap[n] = 1 + freqMap.get(n, 0)

        for number, count in freqMap.items():
            bucket[count].append(number)

        ans = []

        # traverse bucket in reverse
        for index in range(len(bucket) - 1, -1, -1):

            # traverse numbers in bucket
            for numbers in bucket[index]:
                ans.append(numbers)
                if len(ans) == k:
                    return ans


if __name__ == "__main__":
    nums = [1, 1, 1, 2, 2, 3, 3, 3, 3]
    k = 2

    print(Solution().topKFrequent(nums, k))
